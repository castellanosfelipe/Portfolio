"""Regenera las capturas y GIFs del README.

Uso:
    python3 -m http.server 8899 &          # servir el sitio en local
    pip3 install --user playwright pillow  # solo la primera vez
    python3 -m playwright install chromium # solo la primera vez
    python3 scripts/capture.py
"""
import io
import os
from PIL import Image
from playwright.sync_api import sync_playwright

BASE = "http://localhost:8899/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = os.path.join(ROOT, "docs", "screenshots")
MEDIA = os.path.join(ROOT, "docs", "media")


def save_gif(frames, path, duration=650, width=880):
    imgs = []
    for f in frames:
        im = Image.open(io.BytesIO(f)).convert("RGB")
        im = im.resize((width, int(im.height * width / im.width)), Image.LANCZOS)
        imgs.append(im.quantize(colors=128, dither=Image.FLOYDSTEINBERG))
    imgs[0].save(path, save_all=True, append_images=imgs[1:], duration=duration, loop=0, optimize=True)
    print(f"gif -> {path} ({len(imgs)} frames)")


os.makedirs(SHOTS, exist_ok=True)
os.makedirs(MEDIA, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()

    # ---- Screenshots fijos (retina 2x) ----
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page = ctx.new_page()
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(3500)  # fuentes + animaciones de entrada

    page.screenshot(path=f"{SHOTS}/hero.png")
    print("hero OK")

    for sec, name in [("#sobre-mi", "sobre-mi"), ("#metodo", "metodo"), ("#proyectos", "proyectos"), ("#ensayos", "ensayos")]:
        el = page.locator(sec)
        el.scroll_into_view_if_needed()
        page.wait_for_timeout(800)
        el.screenshot(path=f"{SHOTS}/{name}.png")
        print(f"{name} OK")

    # Modal de ficha abierto
    page.locator("#proyectos").scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.get_by_text("Ficha completa del proyecto").first.click()
    page.wait_for_timeout(900)
    page.screenshot(path=f"{SHOTS}/ficha-modal.png")
    print("ficha-modal OK")
    page.keyboard.press("Escape")
    page.wait_for_timeout(400)

    # Chat abierto con respuesta de método
    page.get_by_text("Pregúntame lo que quieras").first.click()
    page.wait_for_timeout(700)
    page.get_by_role("button", name="Método", exact=True).click()
    page.wait_for_timeout(900)
    page.screenshot(path=f"{SHOTS}/chat.png")
    print("chat OK")
    ctx.close()

    # ---- GIF 1: recorrido -> ficha modal ----
    ctx = browser.new_context(viewport={"width": 1280, "height": 800}, device_scale_factor=1)
    page = ctx.new_page()
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(3000)
    frames = [page.screenshot()]
    page.locator("#proyectos").scroll_into_view_if_needed()
    page.wait_for_timeout(700)
    frames.append(page.screenshot())
    page.mouse.wheel(0, 260)
    page.wait_for_timeout(500)
    frames.append(page.screenshot())
    page.get_by_text("Ficha completa del proyecto").first.click()
    page.wait_for_timeout(800)
    frames.append(page.screenshot())
    for _ in range(3):
        page.mouse.wheel(0, 420)
        page.wait_for_timeout(450)
        frames.append(page.screenshot())
    save_gif(frames, f"{MEDIA}/demo-ficha-proyecto.gif", duration=900)
    ctx.close()

    # ---- GIF 2: chat en acción ----
    ctx = browser.new_context(viewport={"width": 1280, "height": 800}, device_scale_factor=1)
    page = ctx.new_page()
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(3000)
    frames = [page.screenshot()]
    page.get_by_text("Pregúntame lo que quieras").first.click()
    page.wait_for_timeout(700)
    frames.append(page.screenshot())
    for chip in ["Yo", "Método", "Proyectos"]:
        page.get_by_role("button", name=chip, exact=True).click()
        page.wait_for_timeout(900)
        frames.append(page.screenshot())
    save_gif(frames, f"{MEDIA}/demo-chat.gif", duration=1100)
    ctx.close()

    browser.close()
print("CAPTURA COMPLETA")
