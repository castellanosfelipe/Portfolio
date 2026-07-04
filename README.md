<div align="center">
  <img src="avatar-felipe-memoji.png" alt="Memoji de Felipe Peña" width="160"/>

  <h1>Portfolio — Felipe Peña</h1>
  <p><strong>La marca personal de un Growth Product Manager: el crecimiento no se hackea, se compone.</strong></p>

  ![Status](https://img.shields.io/badge/status-en_producción-green)
  ![Deploy](https://img.shields.io/badge/deploy-GitHub_Pages-222222)
  ![Stack](https://img.shields.io/badge/stack-HTML_·_CSS_·_JS-blue)

  **[→ Ver el sitio en vivo](https://castellanosfelipe.github.io/Portfolio/)**

</div>

---

## 📋 Tabla de Contenidos

- [¿Qué es este portafolio?](#-qué-es-este-portafolio)
- [Demo en vivo](#-demo-en-vivo)
- [Características principales](#-características-principales)
- [Capturas de pantalla](#-capturas-de-pantalla)
- [Instalación rápida](#-instalación-rápida)
- [Cómo usar](#-cómo-usar)
- [Arquitectura](#-arquitectura)
- [Roadmap](#-roadmap)
- [Licencia y créditos](#-licencia-y-créditos)

---

## 🎯 ¿Qué es este portafolio?

Es el sitio de marca personal de **Felipe Peña**, Growth Product Manager en Bogotá, Colombia. En una sola página presenta quién es, cómo trabaja, qué ha construido y qué escribe — y lo hace practicando lo que predica: cada proyecto se presenta como un caso de producto (problema, solución, resultado), no como una lista de tecnologías.

### El problema que resuelve

Un CV estático dice qué cargos tuviste, pero no muestra **cómo piensas**. Quien evalúa a un Product Manager necesita ver su método, sus decisiones y sus productos funcionando — y normalmente eso está disperso entre LinkedIn, GitHub y documentos sueltos.

### La solución

Un portafolio navegable que concentra todo en un solo lugar: el método de trabajo paso a paso, seis proyectos con ficha completa y demo en vivo, cuatro ensayos de producto, y un chat integrado que responde las preguntas típicas de un reclutador en segundos.

### ¿Para quién es?

| Audiencia | Beneficio clave |
|-----------|----------------|
| Recruiters y hiring managers | Evalúan en minutos la trayectoria, el método y proyectos reales con demos funcionando |
| Comunidad de producto | Ensayos sobre experimentación, Product-Market Fit e IA aplicada al día a día de un PM |
| Clientes y colaboradores potenciales | Entienden cómo trabaja Felipe antes del primer contacto, y le escriben con un clic |

---

## 🎬 Demo en vivo

El sitio está publicado y funcionando en GitHub Pages:

[![Ver el sitio en vivo](https://img.shields.io/badge/▶_Ver_el_sitio-castellanosfelipe.github.io/Portfolio-5b4bd6?style=for-the-badge)](https://castellanosfelipe.github.io/Portfolio/)

<!-- TODO: agregar demo.gif del flujo principal (abrir el sitio → clic en "Ficha completa del proyecto" → abrir el chat y usar un chip). Guardarlo en docs/media/demo.gif y referenciarlo aquí. -->

---

## ✨ Características principales

| Feature | Descripción |
|---------|-------------|
| 🧭 **Narrativa de marca personal** | Hero con tagline, sección "Sobre mí" con foto, trayectoria en tres actos y método de trabajo en cuatro pasos con entregables concretos |
| 💬 **Chat asistente integrado** | Un chat flotante responde por Felipe: trayectoria, proyectos, skills, método y contacto. Enruta preguntas libres por palabras clave y funciona sin backend |
| 🗂️ **Fichas de proyecto en modal** | Seis proyectos con ficha completa (problema, solución, funcionalidades, stack y roadmap) tomada de los README reales de cada repositorio |
| ✍️ **Ensayos de producto** | Cuatro ensayos sobre experimentación, PMF e IA, con páginas propias enlazadas desde la portada |
| 🎨 **Diseño editorial** | Tipografía serif/mono, animaciones de entrada, cursor fluido interactivo y paleta consistente en todo el sitio |
| 🚀 **Publicación automática** | Cada push a `main` despliega el sitio en GitHub Pages, sin build step ni dependencias |

---

## 📸 Capturas de pantalla

<!-- TODO: agregar capturas reales del sitio en docs/screenshots/ y referenciarlas aquí. Tomas sugeridas, en este orden: -->
<!-- 1. hero.png — portada con el tagline "El crecimiento no se hackea. Se compone." y el memoji -->
<!-- 2. ficha-modal.png — modal de ficha completa de un proyecto (ej. AgileFlow) abierto -->
<!-- 3. chat.png — chat flotante abierto mostrando la respuesta de "Método" -->
<!-- 4. sobre-mi.png — sección Sobre mí con la foto y los tres principios -->

> 🖼️ **Capturas en camino.** Mientras tanto, el sitio completo puede verse en vivo en [castellanosfelipe.github.io/Portfolio](https://castellanosfelipe.github.io/Portfolio/).

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
open http://localhost:8000
```

✅ Si todo está correcto, verás la portada con el titular **"El crecimiento no se hackea. Se compone."** y el cursor fluido reaccionando al movimiento.

---

## 💡 Cómo usar

### Personalizar la identidad

El nombre y el correo se definen como propiedades al final de `index.html` y se propagan a todo el sitio (nav, hero, chat y footer):

```html
<script type="text/x-dc" data-dc-script data-props="{
  &quot;name&quot;:  { &quot;default&quot;: &quot;Felipe Peña&quot; },
  &quot;email&quot;: { &quot;default&quot;: &quot;correo@ejemplo.com&quot; },
  &quot;chatEnabled&quot;: { &quot;default&quot;: true }
}">
```

### Añadir un ensayo

```bash
# 1. Crear la página del ensayo (usar una existente como plantilla)
cp ensayos/pmf-sostener-y-expandir.html ensayos/mi-nuevo-ensayo.html

# 2. Enlazarlo en la sección "Ensayos" de index.html
#    (copiar uno de los bloques <a href="ensayos/..."> existentes)
```

### Añadir un proyecto con su ficha

1. Duplicar una tarjeta en la sección `<!-- PROYECTOS -->` de `index.html`.
2. Duplicar su panel en `<!-- FICHAS DE PROYECTO (MODAL) -->`.
3. Registrar el par botón/panel en `renderVals()` (`openFichaX` y `fichaX`).

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
| Componentes | `support.js` — plantillas declarativas con estado | Chat flotante, modales de ficha y reactividad de la UI |
| Efectos | `fluid-cursor.js` | Simulación de fluido que sigue al cursor en la portada |
| Contenido | `ensayos/*.html` | Páginas independientes por ensayo, con enlace de vuelta a la portada |
| Hosting | GitHub Pages + `.nojekyll` | Deploy automático en cada push a `main`, sirviendo los archivos tal cual |

---

## 🚧 Roadmap

### ✅ Completado
- [x] Portada de marca personal: hero, sobre mí con foto, método en 4 pasos y trayectoria
- [x] Seis proyectos con ficha completa en modal, basada en los README reales de cada repo
- [x] Chat asistente con chips guiados y enrutamiento de preguntas libres
- [x] Cuatro ensayos con páginas propias y URLs limpias
- [x] Despliegue automático en GitHub Pages

### 🔮 Próximamente
- [ ] Capturas de pantalla y GIF de demo para este README
- [ ] Metadatos SEO y Open Graph (título, descripción e imagen al compartir el enlace)
- [ ] Favicon propio
- [ ] Versión en inglés del sitio

---

## 📄 Licencia y créditos

El código de esta página puede usarse como referencia. Los textos, ensayos y fotografías son contenido personal — © 2026 Felipe Peña, todos los derechos reservados.

---

<div align="center">
  <p>Hecho con ❤️ por <a href="https://github.com/castellanosfelipe">castellanosfelipe</a></p>
</div>
