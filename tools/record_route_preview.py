"""Record the animated Route Coverage Map preview for the README.

Writes assets/preview-route-coverage.gif (640x370, loops, ~13 s, under 1 MB)
and assets/preview-route-coverage.png (a still from the same recording, shown
to whoever asked for reduced motion). Same proportions as the quick-replies
preview, so the two sit level in the README table.

Stop-motion rather than a screen recording: a screenshot takes ~140 ms, and
taking them in a loop while the mouse moves made every mouse step wait for one.
So the drawn cursor advances one step per frame, with a set duration; what
the page animates by itself (the opening, the flight to a route, the theme
fade) is captured in real time; pauses are a single frame held on screen.

The page is the published demo (fictional data). Screenshots do not show the
system pointer, so a drawn cursor follows the mouse. Development dependencies:
Playwright (with Chromium) and Pillow; needs network for the demo and its tiles.

Run: python tools/record_route_preview.py [--url URL]
"""
import argparse
import io
import time
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
DEMO = 'https://jvfaraco.github.io/mapaderotas/'
# Opens framed on the two southern states, where most of the demo lives.
VIEW = '#z=8&c=-27.20000,-49.35000'
VIEWPORT = {'width': 1080, 'height': 624}   # 1.73:1, the ratio of the quick-replies preview
WIDTH = 640                                  # same ratio, so the README row stays level; ~1.4x the cell's width
COLORS = 128                                 # per theme; the map tiles make every extra colour expensive
STEP_MS = 60                                 # one cursor step per frame
FINAL_HOLD_MS = 1800                         # the last frame stays before the loop restarts

CURSOR = """
(() => {
  const c = document.createElement('div');
  c.innerHTML = '<svg width="22" height="22" viewBox="0 0 24 24"><path d="M4 2l15 11-6.5 1.2L16 21l-3 1.4-3.4-6.6L4 20z" fill="#fff" stroke="#0b0f14" stroke-width="1.6" stroke-linejoin="round"/></svg>';
  Object.assign(c.style, { position: 'fixed', left: '0', top: '0', zIndex: 2147483647, pointerEvents: 'none',
    transform: 'translate(-100px,-100px)', filter: 'drop-shadow(0 2px 3px rgba(0,0,0,.45))' });
  const ring = document.createElement('div');
  Object.assign(ring.style, { position: 'fixed', width: '34px', height: '34px', margin: '-17px 0 0 -17px', borderRadius: '50%',
    border: '2px solid #26d7e8', zIndex: 2147483646, pointerEvents: 'none', opacity: '0', left: '0', top: '0' });
  document.body.append(ring, c);
  addEventListener('mousemove', (e) => { c.style.transform = `translate(${e.clientX - 3}px, ${e.clientY - 2}px)`; }, true);
  addEventListener('mousedown', (e) => {
    ring.style.left = e.clientX + 'px'; ring.style.top = e.clientY + 'px';
    ring.animate([{ opacity: .9, transform: 'scale(.4)' }, { opacity: 0, transform: 'scale(1.4)' }], { duration: 450, easing: 'ease-out' });
  }, true);
})();
"""

# A pixel inside an area of the route (real outline or approximation) that really hits its path.
FIND = """(want) => {
  const area = state.shown.find((a) => a.route === want.route && a.kind === 'district' && a.approx === want.approx);
  if (!area) return null;
  const path = area.layer.getLayers()[0].getElement();
  const b = path.getBoundingClientRect();
  for (let fy = .5; fy < .95; fy += .05) for (let fx = .5; fx < .95; fx += .05)
    for (const [gx, gy] of [[fx, fy], [1 - fx, 1 - fy]]) {
      const x = b.left + b.width * gx, y = b.top + b.height * gy;
      if (document.elementFromPoint(x, y) === path) return { x, y };
    }
  return null;
}"""


class Film:
    """Frames and how long each one stays on screen."""

    def __init__(self, page):
        self.page, self.frames, self.mouse = page, [], (VIEWPORT['width'] * .6, VIEWPORT['height'] * .55)
        self.marks = {}

    def shot(self, duration):
        self.frames.append([self.page.screenshot(), duration])

    def hold(self, ms):
        self.shot(ms)

    def live(self, ms):
        """Real time: the page animates by itself; each frame lasts until the next."""
        start = last = time.perf_counter()
        while (time.perf_counter() - start) * 1000 < ms:
            png = self.page.screenshot()
            now = time.perf_counter()
            if self.frames and self.frames[-1][1] is None:
                self.frames[-1][1] = round((now - last) * 1000)
            self.frames.append([png, None])
            last = now
        self.frames[-1][1] = round((time.perf_counter() - last) * 1000)

    def move(self, x, y, steps=12):
        x0, y0 = self.mouse
        for i in range(1, steps + 1):
            k = i / steps
            k = 4 * k ** 3 if k < .5 else 1 - (-2 * k + 2) ** 3 / 2   # ease in-out
            self.page.mouse.move(x0 + (x - x0) * k, y0 + (y - y0) * k)
            self.shot(STEP_MS)
        self.mouse = (x, y)

    def click(self, x, y, steps=12):
        self.move(x, y, steps)
        self.page.mouse.click(x, y)

    def mark(self, name):
        self.marks[name] = len(self.frames) - 1


def centre(box):
    return box['x'] + box['width'] / 2, box['y'] + box['height'] / 2


def record(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport=VIEWPORT, color_scheme='dark', reduced_motion='no-preference')
        page = context.new_page()
        # The first visit only warms the cache, so the tiles are there from the first frame.
        page.goto(url + VIEW, wait_until='networkidle')
        page.wait_for_function("document.body.classList.contains('ready')")
        page.wait_for_timeout(1500)

        page.add_init_script(f"addEventListener('DOMContentLoaded', () => {{ {CURSOR} }})")
        # A reload, not a second goto: the same address with a #hash would be a
        # same-document navigation, with no new page and no init script.
        page.reload(wait_until='domcontentloaded')
        film = Film(page)
        film.live(1100)                                             # boot fades, cards rise, sheen crosses
        page.mouse.move(*film.mouse)

        real = page.evaluate(FIND, {'route': 'ROUTE-SOUTH-02', 'approx': False})
        film.move(real['x'], real['y'], 14)
        film.hold(900)                                              # the hover tip
        page.mouse.click(real['x'], real['y'])
        film.live(900)                                              # the route lights up, its card opens
        film.hold(500)

        card = page.locator('#detail').bounding_box()               # scroll the card down to its buttons
        film.move(card['x'] + card['width'] * .5, card['y'] + card['height'] * .72, 12)
        page.mouse.wheel(0, 400)
        film.live(500)
        film.click(*centre(page.locator('#detail [data-act="zoom-route"]').bounding_box()), 8)
        film.live(1000)                                             # the app flies to the route

        approx = page.evaluate(FIND, {'route': 'ROUTE-SOUTH-02', 'approx': True})
        film.move(approx['x'], approx['y'], 14)
        film.hold(500)
        page.mouse.click(approx['x'], approx['y'])
        film.live(600)
        film.hold(1500)                                             # why this one is approximated
        film.mark('still')

        film.click(*centre(page.locator('#btnTheme').bounding_box()), 14)
        film.mark('theme')
        film.live(700)                                              # cross-fade to the light theme
        film.frames[-1][1] += FINAL_HOLD_MS
        browser.close()
        return film


def assemble(film):
    images = []
    for png, _ in film.frames:
        img = Image.open(io.BytesIO(png)).convert('RGB')
        images.append(img.resize((WIDTH, round(img.height * WIDTH / img.width)), Image.LANCZOS))
    durations = [max(20, duration) for _, duration in film.frames]

    # One palette per theme, shared by all its frames: with a shared palette the
    # pixels that did not move stay identical, and each frame stores only what
    # changed (a palette per frame made a 7 MB file). Octree keeps the few
    # saturated route colours that median cut merges into the map's browns.
    split = film.marks['theme'] + 1
    quantized = []
    for part in (images[:split], images[split:]):
        if not part:
            continue
        picks = part[:: max(1, len(part) // 10)] + [part[-1]]
        sample = Image.new('RGB', (WIDTH, part[0].height * len(picks)))
        for i, img in enumerate(picks):
            sample.paste(img, (0, i * img.height))
        palette = sample.quantize(colors=COLORS, method=Image.Quantize.FASTOCTREE)
        quantized += [img.quantize(palette=palette, dither=Image.Dither.NONE) for img in part]
    gif = ROOT / 'assets/preview-route-coverage.gif'
    quantized[0].save(gif, save_all=True, append_images=quantized[1:], duration=durations, loop=0, optimize=True)

    # The still: the approximated area explained, in the dark theme like the other previews.
    png = ROOT / 'assets/preview-route-coverage.png'
    images[film.marks['still']].quantize(
        colors=256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.FLOYDSTEINBERG).save(png, optimize=True)
    print(f'{gif.name}: {gif.stat().st_size // 1024} KB, {len(images)} frames, {sum(durations) / 1000:.1f} s')
    print(f'{png.name}: {png.stat().st_size // 1024} KB')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--url', default=DEMO)
    assemble(record(parser.parse_args().url))
