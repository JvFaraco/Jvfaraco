"""Record the animated previews of the validator and binance-daytrade demos.

Writes, for each demo, assets/preview-<name>.gif (720x416, loops, under ~1.5 MB)
and assets/preview-<name>.png (a still from the same recording, shown to whoever
asked for reduced motion). Same 1.73:1 ratio as the other previews, so the
README rows stay level.

Same stop-motion approach as record_route_preview.py (and its Film class): a
drawn cursor advances one step per frame, and what the page animates by itself
is captured in real time.

- validator: the published os-validator-demo (fictional O.S., recorded AI
  answers). The cursor opens three O.S. that leave the pipeline at different
  stages: the note that tries to give orders to the system, the swapped sensor
  that goes back to the technician, and the note whose name and phone are
  masked before leaving the machine.
- binance: the published binance-daytrade panel (public market data, analysis
  only, no orders). The 10,000-replay sphere spins while the cursor changes the
  target and the stop of the simulated plan.

Development dependencies: Playwright (with Chromium) and Pillow; needs network.

Run: python tools/record_demo_previews.py [validator|binance ...]
"""
import io
import re
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from record_route_preview import CURSOR, Film, centre  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
WIDTH = 720           # the width of the quick-replies preview
FINAL_HOLD_MS = 1600


def open_page(p, url, viewport):
    browser = p.chromium.launch()
    context = browser.new_context(viewport=viewport, color_scheme='dark', reduced_motion='no-preference')
    page = context.new_page()
    page.goto(url, wait_until='networkidle')       # warms the cache
    page.add_init_script(f"addEventListener('DOMContentLoaded', () => {{ {CURSOR} }})")
    page.reload(wait_until='networkidle')
    return browser, page


def validator(p):
    browser, page = open_page(p, 'https://jvfaraco.github.io/os-validator-demo/', {'width': 1280, 'height': 740})
    page.wait_for_timeout(1200)
    # Scroll just enough to show the three O.S. cards the cursor will click, beside the pipeline.
    page.evaluate("""() => { const r = document.querySelector('button.destaque[data-os="OS-0029"]').getBoundingClientRect();
                              scrollTo(0, Math.max(0, scrollY + r.bottom - innerHeight + 12)); }""")
    page.wait_for_timeout(400)
    film = Film(page)
    page.mouse.move(*film.mouse)
    film.hold(1200)
    for os_id, hold in (('OS-0029', 2600), ('OS-0019', 2200), ('OS-0007', 2600)):
        card = page.locator(f'button.destaque[data-os="{os_id}"]')
        film.click(*centre(card.bounding_box()), 14)
        film.live(900)                              # the pipeline lights up to the stage the O.S. leaves at
        film.hold(hold)
        if os_id == 'OS-0029':
            film.mark('still')
    film.frames[-1][1] += FINAL_HOLD_MS
    browser.close()
    return film


def binance(p):
    browser, page = open_page(p, 'https://jvfaraco.github.io/binance-daytrade/?modo=pro', {'width': 1080, 'height': 624})
    page.wait_for_timeout(2500)
    film = Film(page)
    page.mouse.move(*film.mouse)
    film.live(1500)                                 # the sphere spins
    film.mark('still')
    for label in ('2R', 'fundo da faixa', '3R'):
        film.click(*centre(page.locator('button.seg__opt').filter(has_text=re.compile(f'^{re.escape(label)}$')).first.bounding_box()), 12)
        film.live(1500)
    film.frames[-1][1] += FINAL_HOLD_MS
    browser.close()
    return film


def assemble(name, film, colors):
    images = []
    for png, _ in film.frames:
        img = Image.open(io.BytesIO(png)).convert('RGB')
        images.append(img.resize((WIDTH, round(img.height * WIDTH / img.width)), Image.LANCZOS))
    durations = [max(20, d) for _, d in film.frames]
    # One palette for all frames, so unchanged pixels stay identical between frames.
    picks = images[:: max(1, len(images) // 12)] + [images[-1]]
    sample = Image.new('RGB', (WIDTH, images[0].height * len(picks)))
    for i, img in enumerate(picks):
        sample.paste(img, (0, i * img.height))
    palette = sample.quantize(colors=colors, method=Image.Quantize.FASTOCTREE)
    frames = [img.quantize(palette=palette, dither=Image.Dither.NONE) for img in images]
    gif = ROOT / f'assets/preview-{name}.gif'
    frames[0].save(gif, save_all=True, append_images=frames[1:], duration=durations, loop=0, optimize=True)
    png = ROOT / f'assets/preview-{name}.png'
    images[film.marks['still']].quantize(
        colors=256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.FLOYDSTEINBERG).save(png, optimize=True)
    print(f'{gif.name}: {gif.stat().st_size // 1024} KB, {len(images)} frames, {sum(durations) / 1000:.1f} s')
    print(f'{png.name}: {png.stat().st_size // 1024} KB')


DEMOS = {'validator': (validator, 96), 'binance': (binance, 128)}

if __name__ == '__main__':
    with sync_playwright() as p:
        for name in sys.argv[1:] or DEMOS:
            record, colors = DEMOS[name]
            assemble({'validator': 'os-validator'}.get(name, 'binance-daytrade'), record(p), colors)
