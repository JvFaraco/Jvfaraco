"""Render a short, single-play terminal animation. Development dependency: Pillow.
Run: python tools/render_banner.py
Fonts (OFL) live in tools/fonts/, so the output is reproducible on any OS.
"""
from functools import lru_cache
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / 'tools/fonts'


@lru_cache(maxsize=None)
def font(size, weight=400, mono=False):
    f = ImageFont.truetype(str(FONTS / ('FiraCode.ttf' if mono else 'DMSans.ttf')), size)
    f.set_variation_by_axes([weight] if mono else [min(size, 40), weight])
    return f


BG, PANEL, BORDER = '#0a0f1e', '#111a2d', '#29364d'
TEXT, MUTED, YELLOW = '#e2e8f0', '#a1aec5', '#ffc72c'
frames = []
lines = ['$ python rotina.py', '[ok] dados organizados', '[ok] tarefa automatizada']
for frame in range(64):
    img = Image.new('RGB', (1200, 360), BG)
    draw = ImageDraw.Draw(img)
    draw.line((0, 357, 1200, 357), fill=YELLOW, width=3)
    draw.text((48, 30), '// JvFaraco', font=font(26, 600, mono=True), fill=YELLOW)
    draw.text((44, 78), 'João Victor', font=font(80, 700), fill=TEXT)
    draw.text((44, 162), 'Faraco', font=font(80, 700), fill=YELLOW)
    draw.text((48, 266), 'Python · Automação · Integrações', font=font(34, 500), fill=TEXT)
    draw.text((48, 314), 'Analista de Sistemas / São José, SC', font=font(20, mono=True), fill=MUTED)
    draw.rounded_rectangle((690, 52, 1160, 300), radius=14, fill=PANEL, outline=BORDER, width=2)
    draw.line((690, 96, 1160, 96), fill=BORDER, width=1)
    for x, color in [(716, '#ed746c'), (737, '#ffc72c'), (758, '#83c6a2')]:
        draw.ellipse((x, 71, x+9, 80), fill=color)
    draw.text((789, 63), 'uma rotina a menos', font=font(18, mono=True), fill=MUTED)
    progress = max(0, frame-6) * 2
    for index, line in enumerate(lines):
        shown = line[:max(0, min(len(line), progress))]
        y = 118 + index*42
        draw.text((716, y), shown, font=font(24, mono=True), fill=YELLOW if index == 0 else '#a0d4b7')
        if progress < len(line):
            if frame < 43 and (frame//5) % 2 == 0:
                x = 717 + draw.textlength(shown, font=font(24, mono=True))
                draw.rectangle((x, y+5, x+11, y+30), fill=TEXT)
            break
        progress -= len(line)
    draw.text((716, 260), '// ilustração, sem execução real', font=font(16, mono=True), fill=MUTED)
    frames.append(img)

# One short playback, then a stable final frame. No loop extension.
palette = frames[-1].quantize(colors=96)
indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
asset = ROOT / 'assets/profile-banner.gif'
indexed[0].save(asset, save_all=True, append_images=indexed[1:], duration=70, disposal=1, optimize=True)
frames[-1].save(ROOT / 'assets/profile-banner.png', optimize=True)
print(f'{asset.name}: {asset.stat().st_size:,} bytes, 4.48s single playback')
