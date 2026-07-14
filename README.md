<div align="center">
  <img src="avatar-felipe-memoji.webp" alt="Memoji de Felipe Peña" width="160"/>

  <h1>Portfolio · Felipe Peña</h1>
  <p><strong>La marca personal de un Growth Product Manager: el crecimiento no se hackea, se compone.</strong></p>

  ![Status](https://img.shields.io/badge/status-en_producción-green)
  ![Deploy](https://img.shields.io/badge/deploy-GitHub_Pages-222222)
  ![Stack](https://img.shields.io/badge/stack-HTML_·_CSS_·_JS-blue)
  ![Idiomas](https://img.shields.io/badge/idiomas-ES_·_EN-5b4bd6)
  ![Responsive](https://img.shields.io/badge/responsive-320px_→_1440px-8b7cf6)

  **[→ Ver el sitio en vivo](https://felipepena.co/)** · **[English version](https://felipepena.co/en/)**

</div>

---

## 📋 Tabla de Contenidos

- [¿Qué es este portafolio?](#-qué-es-este-portafolio)
- [Demo en vivo](#-demo-en-vivo)
- [Características principales](#-características-principales)
- [Capturas de pantalla](#-capturas-de-pantalla)
- [Métricas de éxito](#-métricas-de-éxito)
- [Instalación rápida](#-instalación-rápida)
- [Cómo usar](#-cómo-usar)
- [Arquitectura](#-arquitectura)
- [Roadmap](#-roadmap)
- [Licencia y créditos](#-licencia-y-créditos)

---

## 🎯 ¿Qué es este portafolio?

Es el sitio de marca personal de **Felipe Peña**, Growth Product Manager. Y está construido como pienso los productos: el visitante es un usuario con un job-to-be-done (evaluar en pocos minutos si vale la pena hablar conmigo) y cada sección existe para mover esa decisión, no para decorar.

### El problema que resuelve

Un CV estático dice qué cargos tuviste, pero no muestra **cómo piensas**. Quien evalúa a un Product Manager necesita ver su método, sus decisiones y sus productos funcionando, y normalmente eso está disperso entre LinkedIn, GitHub y documentos sueltos. Cada salto entre plataformas es fricción, y la fricción mata conversión.

### La solución

Un funnel de una sola página con una sola conversión: **que el visitante correcto escriba**. El recorrido reduce fricción en cada paso: método de trabajo con entregables concretos, ocho proyectos con ficha de caso de producto y demo funcionando, cuatro ensayos que muestran criterio, y un chat integrado que responde las preguntas típicas de un reclutador sin esperar respuesta de nadie.

Y como el visitante más frecuente llega desde el móvil (el link se comparte por LinkedIn y WhatsApp), el funnel completo funciona igual de bien a 320px que a 1440px, en español o en inglés, y con una tarjeta social que se defiende sola al compartir el enlace.

### ¿Para quién es?

| Audiencia | Job-to-be-done que resuelve |
|-----------|----------------------------|
| Recruiters y hiring managers | Evaluar trayectoria, método y evidencia real de producto en minutos, sin agendar una llamada, desde cualquier dispositivo e idioma |
| Comunidad de producto | Leer ensayos sobre experimentación, Product-Market Fit e IA aplicada al día a día de un PM |
| Clientes y colaboradores potenciales | Entender cómo trabajo antes del primer contacto, y escribirme con un clic |
| Buscadores y asistentes de IA | Indexar y citar el perfil y los ensayos: metadatos completos, JSON-LD, `llms.txt` y crawlers de IA permitidos explícitamente |

---

## 🎬 Demo en vivo

El sitio está publicado y funcionando en `felipepena.co` (GitHub Pages + dominio propio):

[![Ver el sitio en vivo](https://img.shields.io/badge/▶_Ver_el_sitio-felipepena.co-5b4bd6?style=for-the-badge)](https://felipepena.co/)

<div align="center">
  <img src="docs/media/demo-ficha-proyecto.gif" alt="Recorrido desde la portada hasta abrir la ficha completa de un proyecto en modal" width="800"/>
  <p><em>Flujo principal: del hero a la ficha de caso de producto, con problema, solución, funcionalidades y stack sin salir de la página.</em></p>
</div>

<div align="center">
  <img src="docs/media/demo-chat.gif" alt="El chat integrado respondiendo sobre trayectoria, método y proyectos" width="800"/>
  <p><em>El chat responde por mí: trayectoria, método y proyectos en segundos; cero fricción para el visitante que evalúa rápido.</em></p>
</div>

---

## ✨ Características principales

| Feature | Qué mueve en el funnel |
|---------|------------------------|
| 🧭 **Narrativa de marca personal** | Hero con posicionamiento claro, "Sobre mí" con foto, trayectoria en tres actos con logros concretos y método en cuatro pasos con entregables: el visitante entiende el valor en el primer scroll |
| 📱 **Responsive de 320px a 1440px** | Custom properties con media queries y nav móvil propio (hamburguesa + hoja de anclas): el recruiter que abre el link desde LinkedIn en el teléfono ve el mismo funnel, no una versión rota |
| 🌐 **Bilingüe ES / EN** | Portada completa en inglés en `/en/` con URLs reales e indexables, toggle que conserva la sección actual y banner discreto según el idioma del navegador (nunca redirección automática) |
| 💬 **Chat asistente integrado** | Responde trayectoria, proyectos, skills, método y contacto con chips guiados y enrutado de preguntas libres. Convierte curiosidad en información sin backend ni esperas |
| 🗂️ **Fichas de proyecto en modal** | Ocho proyectos presentados como casos de producto (problema → solución → funcionalidades → stack → roadmap), tomados de los README reales de cada repositorio. Evidencia, no adjetivos |
| ✍️ **Ensayos de producto** | Cuatro ensayos sobre experimentación, PMF e IA con páginas propias, fecha y autoría visibles: retención para el lector que quiere profundidad |
| 🔍 **SEO e indexabilidad para IA** | Metadatos completos (title, description, Open Graph, Twitter cards, canonical, hreflang), JSON-LD (Person, ProfilePage, Article), `robots.txt` con crawlers de IA permitidos, `sitemap.xml` y `llms.txt`: el sitio existe para Google y para los asistentes de IA |
| ⚡ **Carga ligera** | Primera visita móvil de ~0.9 MB: memoji en WebP de 18 KB con `fetchpriority` en el LCP, efecto WebGL solo en dispositivos con cursor |
| 🎨 **Diseño editorial** | Tipografía serif/mono, animaciones de entrada y cursor fluido: la primera impresión también comunica estándar de calidad |
| 🚀 **Publicación automática** | Cada push a `main` despliega en GitHub Pages sin build step; tiempo de fricción detectada a mejora publicada: minutos |

---

## 📸 Capturas de pantalla

### Portada: el posicionamiento en 5 segundos
<div align="center">
  <img src="docs/screenshots/hero.png" alt="Portada del sitio con el titular 'El crecimiento no se hackea. Se compone.' y el memoji de Felipe" width="800"/>
  <p><em>El primer pantallazo responde quién soy, qué hago y qué creo, y ofrece dos rutas: conocerme o preguntarle al chat.</em></p>
</div>

### Ficha de proyecto: evidencia en formato caso de producto
<div align="center">
  <img src="docs/screenshots/ficha-modal.png" alt="Modal con la ficha completa del proyecto AgileFlow: problema, solución, funcionalidades y stack" width="800"/>
  <p><em>Cada proyecto se defiende solo: problema, solución, funcionalidades y stack, con demo y código a un clic.</em></p>
</div>

### Chat: la conversación que un CV no puede tener
<div align="center">
  <img src="docs/screenshots/chat.png" alt="Chat flotante abierto respondiendo el método de trabajo en cuatro pasos" width="800"/>
  <p><em>El visitante pregunta, el sitio responde: aquí explicando el método de trabajo en cuatro pasos con entregables.</em></p>
</div>

### Método: cómo trabajo, con entregables y no promesas
<div align="center">
  <img src="docs/screenshots/metodo.png" alt="Sección del método: Escuchar, Medir, Experimentar y Componer, cada paso con su entregable" width="800"/>
  <p><em>Escuchar → Medir → Experimentar → Componer: cada paso termina en un entregable concreto, como debe ser.</em></p>
</div>

### Sobre mí: la persona detrás del funnel
<div align="center">
  <img src="docs/screenshots/sobre-mi.png" alt="Sección Sobre mí con la fotografía de Felipe y sus tres principios de trabajo" width="800"/>
  <p><em>Foto real, historia real y tres principios: datos antes que opiniones, experimentos que se acumulan, crecimiento que se compone.</em></p>
</div>

---

## 📈 Métricas de éxito

Este sitio tiene una sola conversión y la mido como cualquier producto:

| Señal | Qué valida |
|-------|-----------|
| **Mensajes recibidos** (mail / LinkedIn) | La conversión final: el visitante correcto decidió escribir |
| **Clics a demos y repositorios** | La evidencia interesa: los proyectos hacen su trabajo |
| **Interacciones con el chat** | El formato responde dudas reales antes del primer contacto |
| **Lecturas de ensayos** | El contenido retiene a la audiencia de producto |
| **Impresiones y clics en Google** (Search Console) | El sitio es visible donde el visitante busca, en español y en inglés |

> La instrumentación de analítica en la página está en el roadmap; hoy las fuentes de verdad son los mensajes que llegan y Search Console.

---

## 🚀 Instalación rápida

### Prerrequisitos

- Un navegador moderno. Nada más.
- (Opcional) Python 3 o Node.js para servirlo en local.

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/castellanosfelipe/Portfolio.git
cd Portfolio

# 2. Servir en local (no hay dependencias que instalar)
python3 -m http.server 8000

# 3. Abrir en el navegador
open http://localhost:8000        # portada en español
open http://localhost:8000/en/    # portada en inglés
```

✅ Si todo está correcto, verás la portada con el titular **"El crecimiento no se hackea. Se compone."** y el cursor fluido reaccionando al movimiento (solo en dispositivos con cursor: en táctil se desactiva a propósito).

---

## 💡 Cómo usar

### Personalizar la identidad

El nombre, las iniciales y el correo están escritos directamente en el HTML (nav, hero, footer y chat) para que sean legibles sin ejecutar JavaScript, que es como los leen los crawlers y las IAs. Si cambias alguno, búscalo y reemplázalo en `index.html`; el chat además toma sus valores por defecto de las propiedades al final del archivo:

```html
<script type="text/x-dc" data-dc-script data-props="{
  &quot;name&quot;:  { &quot;default&quot;: &quot;Felipe Peña&quot; },
  &quot;email&quot;: { &quot;default&quot;: &quot;correo@ejemplo.com&quot; },
  &quot;chatEnabled&quot;: { &quot;default&quot;: true }
}">
```

Después de cualquier cambio de copy en `index.html`, regenera la versión en inglés (ver más abajo).

### Añadir un ensayo

```bash
# 1. Crear la página del ensayo (usar una existente como plantilla)
cp ensayos/pmf-sostener-y-expandir.html ensayos/mi-nuevo-ensayo.html

# 2. Enlazarlo en la sección "Ensayos" de index.html
#    (copiar uno de los bloques <a href="ensayos/..."> existentes)
```

Los ensayos están encadenados: el botón "Siguiente ensayo" del footer de cada página apunta al `href` del siguiente archivo, y el último vuelve al primero. Al insertar uno nuevo, hay que reapuntar dos enlaces: el del ensayo anterior (para que apunte al nuevo) y el del nuevo (para que apunte al que antes era el siguiente).

Checklist SEO del ensayo nuevo (todo está en el `<head>` de cualquier ensayo existente como referencia):

1. `<title>` propio (≤60 caracteres) y `meta description` (150–160).
2. `canonical` con la URL definitiva y bloque Open Graph / Twitter.
3. JSON-LD `Article` con `headline`, `datePublished` y autoría.
4. Línea visible de categoría · tiempo de lectura · autor · fecha bajo el título.
5. Añadir la URL a `sitemap.xml` y el enlace anotado a `llms.txt`.

### Añadir un proyecto con su ficha

1. Duplicar una tarjeta en la sección `<!-- PROYECTOS -->` de `index.html`.
2. Duplicar su panel en `<!-- FICHAS DE PROYECTO (MODAL) -->`.
3. Registrar el par botón/panel en `renderVals()` (`openFichaX` y `fichaX`).
4. Añadir la descripción de la tarjeta al diccionario `scripts/strings_en.json` y regenerar `/en/` (si no, la tarjeta saldría en español en la versión en inglés).

### Actualizar la versión en inglés

`index.html` (español) es la fuente canónica y se edita a mano. La portada en inglés se regenera con un comando:

```bash
python3 scripts/build_en.py
```

El script aplica el diccionario `scripts/strings_en.json` (pares exactos ES → EN) y **aborta con la lista de pares rotos** si el copy en español cambió y el diccionario quedó desfasado: nunca publica una mezcla de idiomas en silencio. El sitio publicado sigue siendo 100% estático; esto no es un build step del deploy, es un generador que se corre cuando cambia el copy, igual que `capture.py`.

### Regenerar las capturas de este README

```bash
# Requisitos (solo la primera vez)
pip3 install --user playwright pillow
python3 -m playwright install chromium

# Servir el sitio y capturar
python3 -m http.server 8899 &
python3 scripts/capture.py
```

Genera los screenshots en `docs/screenshots/` y los GIFs en `docs/media/`.

### Publicar cambios

```bash
git add . && git commit -m "Descripción del cambio" && git push origin main
# GitHub Pages despliega automáticamente en 1-2 minutos
```

---

## 🧱 Arquitectura

Sitio 100% estático, sin build step, sin bundler y sin dependencias de npm.

| Capa | Tecnología | Propósito |
|------|-----------|-----------|
| Interfaz | HTML + estilos inline + Google Fonts (Newsreader, Hanken Grotesk, IBM Plex Mono) | Diseño editorial de una sola página |
| Responsive | Custom properties con fallback (el valor desktop vive como default de cada `var(--…)`) + media queries en el `<style>` del `<helmet>` | Un solo markup que colapsa a 1 columna en <768px y a 2 en tablet, con el desktop intacto por construcción; nav móvil con hamburguesa y toggle de idioma siempre visible |
| Idioma | `en/index.html` generado por `scripts/build_en.py` + diccionario `scripts/strings_en.json` | Portada en inglés con URLs reales e indexables (hreflang es/en/x-default), toggle ES/EN que conserva la sección y banner por `navigator.language` con persistencia en `localStorage` |
| Componentes | `support.js`: plantillas declarativas con estado (generado desde `dc-runtime/src`, no editar a mano) | Chat flotante, modales de ficha, menú móvil y reactividad de la UI |
| Efectos | `fluid-cursor.js`, importado solo con `pointer: fine` | Simulación de fluido que sigue al cursor en la portada; en táctil ni se carga |
| Contenido | `ensayos/*.html` | Páginas independientes por ensayo, con fecha y autoría visibles, encadenadas entre sí con un botón "Siguiente ensayo" y con enlace de vuelta a la portada en la barra superior |
| SEO / IA | Metas OG y Twitter, canonical, JSON-LD (`Person`, `ProfilePage`, `Article`), `robots.txt` (crawlers de IA permitidos), `sitemap.xml`, `llms.txt`, favicon, `og-image.png` 1200×630 y `404.html` | Visibilidad en buscadores y citabilidad por asistentes de IA; todo el contenido clave es legible en el HTML crudo, sin ejecutar JavaScript |
| Performance | Memoji en WebP (844 KB → 18 KB) con `fetchpriority="high"` en el LCP | Primera visita móvil de ~0.9 MB (antes 1.78 MB) |
| Documentación | `scripts/capture.py`: Playwright + Pillow | Screenshots y GIFs de este README, regenerables con un comando |
| Hosting | GitHub Pages + dominio propio (`felipepena.co` vía CNAME) + `.nojekyll` | Deploy automático en cada push a `main`, sirviendo los archivos tal cual |

### Estructura del repositorio

```
.
├── index.html               # Portada en español (fuente canónica del copy)
├── en/index.html            # Portada en inglés (generada: no editar a mano)
├── ensayos/                 # 4 ensayos con páginas propias + runtime
├── scripts/
│   ├── build_en.py          # Regenera /en/ desde index.html + diccionario
│   ├── strings_en.json      # Diccionario ES → EN (pares exactos)
│   └── capture.py           # Screenshots y GIFs de este README
├── support.js               # Runtime de componentes (generado, no editar)
├── fluid-cursor.js          # Efecto WebGL del cursor (solo pointer: fine)
├── robots.txt · sitemap.xml · llms.txt · 404.html
├── og-image.png             # Tarjeta social 1200×630
├── favicon.ico · favicon-192.png · apple-touch-icon.png
└── avatar-felipe-memoji.webp / .png · foto-felipe.jpg
```

---

## 🚧 Roadmap

### ✅ Completado
- [x] Portada de marca personal: hero, sobre mí con foto, método en 4 pasos y trayectoria con logros
- [x] Ocho proyectos con ficha de caso de producto en modal, basada en los README reales de cada repo
- [x] Chat asistente con chips guiados y enrutamiento de preguntas libres
- [x] Cuatro ensayos con páginas propias, URLs limpias, fecha y autoría visibles, y navegación encadenada ("Siguiente ensayo")
- [x] Responsive completo de 320px a 1440px con nav móvil propio, sin tocar el diseño desktop
- [x] Versión en inglés de la portada (`/en/`) con toggle, banner de idioma y hreflang
- [x] SEO completo: title, metas, Open Graph, Twitter cards, canonical y JSON-LD en todas las páginas
- [x] Indexabilidad para IA: `robots.txt` con crawlers de IA permitidos, `sitemap.xml` y `llms.txt`
- [x] Favicon propio y tarjeta social 1200×630 al compartir el enlace
- [x] Performance: memoji en WebP (−98%) y primera carga móvil a la mitad
- [x] Dominio propio `felipepena.co` y despliegue automático en GitHub Pages
- [x] Capturas y GIFs de demo generados con Playwright, regenerables con `scripts/capture.py`

### 🔮 Próximamente
- [ ] Instrumentar analítica de producto (la sección de métricas pide datos, no intuiciones)
- [ ] Fichas de proyecto y chat en inglés (hoy la portada EN enlaza los ensayos en español)
- [ ] Ensayos traducidos al inglés, según demanda de la audiencia
- [ ] Monitoreo de Core Web Vitals tras cada deploy

---

## 📄 Licencia y créditos

El código de esta página puede usarse como referencia. Los textos, ensayos y fotografías son contenido personal. © 2026 Felipe Peña, todos los derechos reservados.

---

<div align="center">
  <p>Hecho con ❤️ por <a href="https://github.com/castellanosfelipe">castellanosfelipe</a></p>
</div>
