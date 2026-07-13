"""Genera en/index.html a partir de index.html + scripts/strings_en.json.

index.html (ES) es la fuente canónica y se edita a mano, como siempre.
Este script se corre manualmente cuando cambia el copy (mismo espíritu que
capture.py); el sitio publicado sigue siendo 100% estático, sin build step
en el deploy.

    python3 scripts/build_en.py

Garantía: si un string ES del diccionario ya no existe en index.html
(porque el copy cambió), el build ABORTA listando los pares rotos —
nunca publica una mezcla de idiomas silenciosa.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "index.html")
OUT_DIR = os.path.join(ROOT, "en")
OUT = os.path.join(OUT_DIR, "index.html")
STRINGS = os.path.join(ROOT, "scripts", "strings_en.json")

html = open(SRC, encoding="utf-8").read()
data = json.load(open(STRINGS, encoding="utf-8"))

errors = []

# ---------- 1. Transformaciones estructurales ----------
struct = [
    # idioma del documento (no confundir con los atributos hreflang)
    ('<html lang="es">', '<html lang="en">', 1),
    # rutas relativas: /en/ está un nivel más abajo
    ('src="./support.js"', 'src="../support.js"', 1),
    ('from="./fluid-cursor.js"', 'from="../fluid-cursor.js"', 1),
    ('src="./avatar-felipe-memoji.png"', 'src="../avatar-felipe-memoji.png"', None),
    ('src="./foto-felipe.jpg"', 'src="../foto-felipe.jpg"', 1),
    ('href="ensayos/', 'href="../ensayos/', None),
    # toggle: el activo pasa a EN; ES navega con goSpanish
    ('<a href="/" aria-current="true" hreflang="es" lang="es">ES</a>',
     '<a href="/" hreflang="es" lang="es" onClick="{{ goSpanish }}">ES</a>', 2),
    ('<a href="/en/" hreflang="en" lang="en" onClick="{{ goEnglish }}">EN</a>',
     '<a href="/en/" aria-current="true" hreflang="en" lang="en">EN</a>', 2),
]
for old, new, expected in struct:
    n = html.count(old)
    if n == 0 or (expected is not None and n != expected):
        errors.append(f"[estructural] esperaba {expected or '>=1'}, encontré {n}: {old[:70]!r}")
        continue
    html = html.replace(old, new)

# ---------- 2. Quitar el banner de sugerencia (en /en/ no aplica) ----------
banner_re = re.compile(r"\n?[ \t]*<!-- lang-banner -->.*?<!-- /lang-banner -->\n?", re.S)
if not banner_re.search(html):
    errors.append("[banner] marcadores <!-- lang-banner --> no encontrados")
else:
    html = banner_re.sub("\n", html)

# ---------- 3. Diccionario de copy ----------
for section, pairs in data.items():
    if section.startswith("_"):
        continue
    replace_all = section == "global_replace_all"
    for es, en in pairs:
        n = html.count(es)
        if n == 0:
            errors.append(f"[{section}] no encontrado: {es[:70]!r}")
            continue
        if not replace_all and es != en and n > 1 and len(es) < 25:
            # aviso: string corto repetido — se reemplazan todas las apariciones
            print(f"  aviso [{section}]: {es!r} aparece {n} veces; se reemplazan todas")
        html = html.replace(es, en)

if errors:
    print("BUILD ABORTADO — el copy ES cambió y el diccionario quedó desfasado:")
    for e in errors:
        print("  ✗", e)
    sys.exit(1)

os.makedirs(OUT_DIR, exist_ok=True)
open(OUT, "w", encoding="utf-8").write(html)
print(f"OK → {OUT} ({len(html)//1024} KB)")
