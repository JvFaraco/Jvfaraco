"""Render a short, single-play terminal animation. Development dependency: Pillow.
Run: python tools/render_banner.py [--font-dir PATH]
"""
from pathlib import Path
import argparse
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--font-dir', type=Path, default=Path('C:/Windows/Fonts'))
args = parser.parse_args()


def font(size, bold=False, mono=False):
    name = 'consolab.ttf' if mono and bold else 'consola.ttf' if mono else 'segoeuib.ttf' if bold else 'segoeui.ttf'
    if (args.font_dir / name).is_file():
        return ImageFont.truetype(str(args.font_dir / name), size)
    return ImageFont.truetype('DejaVuSansMono.ttf' if mono else 'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf', size)


BG, PANEL, BORDER = '#0a0f1e', '#111a2d', '#29364d'
TEXT, MUTED, YELLOW = '#e2e8f0', '#a1aec5', '#ffc72c'
frames = []
lines = ['$ python rotina.py', '[ok] dados organizados', '[ok] tarefa automatizada']
for frame in range(64):
    img = Image.new('RGB', (1200, 320), BG)
    draw = ImageDraw.Draw(img)
    draw.line((0, 318, 1200, 318), fill=YELLOW, width=3)
    draw.text((48, 33), '</> JvFaraco', font=font(22, bold=True, mono=True), fill=YELLOW)
    draw.text((46, 91), 'João Victor', font=font(58, bold=True), fill=TEXT)
    draw.text((46, 159), 'Faraco', font=font(58, bold=True), fill=YELLOW)
    draw.text((48, 246), 'Python · Automação · Integrações', font=font(24), fill=TEXT)
    draw.text((48, 282), 'Analista de Sistemas / São José, SC', font=font(16, mono=True), fill=MUTED)
    draw.rounded_rectangle((651, 47, 1152, 277), radius=14, fill=PANEL, outline=BORDER, width=2)
    draw.line((651, 91, 1152, 91), fill=BORDER, width=1)
    for x, color in [(677, '#ed746c'), (698, '#ffc72c'), (719, '#83c6a2')]:
        draw.ellipse((x, 66, x+9, 75), fill=color)
    draw.text((750, 59), 'uma rotina a menos', font=font(17, mono=True), fill=MUTED)
    progress = max(0, frame-6) * 2
    for index, line in enumerate(lines):
        shown = line[:max(0, min(len(line), progress))]
        y = 113 + index*39
        draw.text((678, y), shown, font=font(23, mono=True), fill=YELLOW if index == 0 else '#a0d4b7')
        if progress < len(line):
            if frame < 43 and (frame//5) % 2 == 0:
                x = 679 + draw.textlength(shown, font=font(23, mono=True))
                draw.rectangle((x, y+5, x+10, y+28), fill=TEXT)
            break
        progress -= len(line)
    draw.text((678, 243), '// ilustração, sem execução real', font=font(15, mono=True), fill=MUTED)
    frames.append(img)

# One short playback, then a stable final frame. No loop extension.
palette = frames[-1].quantize(colors=96)
indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
asset = ROOT / 'assets/profile-banner.gif'
indexed[0].save(asset, save_all=True, append_images=indexed[1:], duration=70, disposal=1, optimize=True)
frames[-1].save(ROOT / 'assets/profile-banner.png', optimize=True)
print(f'{asset.name}: {asset.stat().st_size:,} bytes, 4.48s single playback')
