"""Render the project previews used in the README. Development dependency: Pillow.
Run: python tools/render_previews.py PATH/TO/mapaderotas/docs/assets/overview.png
The map preview is a crop of the mapaderotas demo screenshot (fictional dataset).
The bot preview is an illustration: fictional offer, no real store, logo or username.
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / 'tools/fonts'
W, H = 800, 500


def font(size, weight=400, mono=False):
    f = ImageFont.truetype(str(FONTS / ('FiraCode.ttf' if mono else 'DMSans.ttf')), size)
    f.set_variation_by_axes([weight] if mono else [min(size, 40), weight])
    return f


def map_preview(source):
    img = Image.open(source).convert('RGB')
    img = img.crop((0, 0, 2400, 1500)).resize((W, H), Image.LANCZOS)
    img.save(ROOT / 'assets/preview-route-coverage.png', optimize=True)


def bot_preview():
    BG, BAR, BUBBLE, TEXT, MUTED, LINK, YELLOW = '#0e1621', '#17212b', '#182533', '#e2e8f0', '#8a9bb0', '#6ab3f3', '#ffc72c'
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, W, 64), fill=BAR)
    d.ellipse((24, 14, 60, 50), fill='#2b5278')
    d.text((42, 32), 'A', font=font(20, 700), fill=TEXT, anchor='mm')
    d.text((76, 14), 'Alertas de ofertas', font=font(20, 600), fill=TEXT)
    d.text((76, 38), 'bot', font=font(14), fill=MUTED)
    d.text((W-24, 32), 'ilustração', font=font(14, mono=True), fill=YELLOW, anchor='rm')

    def bubble(y, lines, time):
        h = 24 + sum(lh for _, _, _, lh in lines) + 22
        d.rounded_rectangle((24, y, 640, y+h), radius=14, fill=BUBBLE)
        cy = y + 16
        for text, f, color, lh in lines:
            d.text((44, cy), text, font=f, fill=color)
            cy += lh
        d.text((620, y+h-12), time, font=font(13), fill=MUTED, anchor='rb')
        return y + h + 16

    y = 88
    y = bubble(y, [
        ('[Notebook] Notebook Exemplo 15, 16 GB, 512 GB SSD', font(19, 700), TEXT, 30),
        ('R$ 2999.00 (32% off) — Loja Exemplo', font(18), TEXT, 28),
        ('Cupom: EXEMPLO10', font(17, mono=True), YELLOW, 28),
        ('https://example.com/oferta/notebook-exemplo-15', font(16), LINK, 24),
    ], '09:00')
    bubble(y, [
        ('[Fone] Fone Sem Fio Exemplo', font(19, 700), TEXT, 30),
        ('R$ 199.90 (45% off) — Loja Exemplo', font(18), TEXT, 28),
        ('https://example.com/oferta/fone-exemplo', font(16), LINK, 24),
    ], '15:00')
    d.text((W//2, H-22), 'oferta fictícia · formato real das mensagens do bot', font=font(14, mono=True), fill=MUTED, anchor='mm')
    img.quantize(colors=64, dither=Image.Dither.NONE).save(ROOT / 'assets/preview-bot-alertas.png', optimize=True)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        map_preview(sys.argv[1])
    bot_preview()
    for p in sorted((ROOT / 'assets').glob('preview-*.png')):
        print(f'{p.name}: {p.stat().st_size:,} bytes')
