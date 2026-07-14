# Auditoría felipepena.co — Responsive · Idioma ES/EN · SEO/IA

> **Estado 2026-07-13 (fase 2):** estrategias C/C aprobadas e **implementadas** en el working tree
> (sin commitear). Verificado post-implementación: overflow 0px y 0 errores JS en ES y EN a
> 320/390/768/1024/1440; desktop 1440 con diff de 0.04% localizado en el toggle del nav (esperado);
> toggle ES⇄EN conservando ancla; banner por `navigator.language` con persistencia; nav móvil
> funcional en ambos idiomas; fluid-cursor desactivado en táctil (canvas 0 en móvil, 1 en desktop).
> Evidencia: `final-{es,en}-{390,1440}.webp`, `final-en-390-menu.webp`, `nav-390-despues.webp`,
> `nav-390-abierto.webp`, `index-full-390-despues.webp`.
> Pendientes que requieren decisión/acción de Felipe: fechas de ensayos (omitidas a propósito),
> jerarquía h2/h3 (§6.3), memoji→WebP (#8), y las acciones manuales de §6.6.

**Fecha:** 2026-07-13 · **Método:** código + DOM renderizado (Playwright, Chromium) a 320/390/768/1024/1440px, métricas en [metrics.json](metrics.json), capturas en esta carpeta.
**Regla:** nada inventado — cada hallazgo cita captura y `archivo:línea`; lo no verificado está marcado ⚠️.

---

## 1 · Resumen ejecutivo

**El riesgo #1 es el recruiter móvil.** Un recruiter que abre felipepena.co desde el teléfono (el caso más común desde LinkedIn) recibe una página con **348px de desbordamiento horizontal a 390px** de ancho (418px a 320px): el nav aparece cortado a mitad de palabra («En…»), el retrato del hero queda **completamente fuera de pantalla**, y Método/Trayectoria/Proyectos se rompen en columnas de 81–137px con texto en torre de una palabra por línea y columnas enteras invisibles. La página además pesa **1.78 MB** en la primera visita móvil, con un solo PNG (el memoji) responsable del 47%. El mensaje del sitio es "datos y experimentos, no humo"; la experiencia móvil actual contradice ese mensaje ante la audiencia que más importa.

**El riesgo #2 es la invisibilidad total en buscadores e IA.** Ninguna de las 5 páginas tiene `<title>`, `lang`, meta description, Open Graph, canonical ni datos estructurados; no existen robots.txt, sitemap ni favicon. Al compartir el link en LinkedIn/WhatsApp no se genera ninguna tarjeta. Y para los crawlers de IA (que no ejecutan JS), el hero dice literalmente «Soy {{ name }}»: el nombre y el email viven solo en JavaScript. La buena noticia: el 95% del contenido (h1, secciones, ensayos completos) **sí** está en el HTML crudo, así que el arreglo es de metadatos, no de arquitectura.

Desktop (≥1024px) está impecable y no se toca: overflow 0px en 1024 y 1440 (evidencia: `index-full-1024.webp`, `index-full-1440.webp`, `nav-1440.webp`).

---

## 2 · Hallazgos responsive (evidencia medida)

Overflow horizontal del documento (medido, `metrics.json`):

| Página | 320px | 390px | 768px | 1024px | 1440px |
|---|---|---|---|---|---|
| index.html | **+418px** | **+348px** | 0 | 0 | 0 |
| ensayo (agencia) | +49px | 0 | 0 | 0 | 0 |

| # | Sección | Breakpoint | Problema | Severidad | Evidencia |
|---|---|---|---|---|---|
| R1 | Nav | ≤767px | Fila flex sin wrap ni menú móvil: «Ensayos» y «Hablemos» quedan fuera del viewport (medido: right=557px en viewport de 390). «Sobre mí» se parte en 2 líneas. No hay forma de navegar ni de ver el CTA. | **Crítico** | `nav-390.webp`, `nav-320.webp` · [index.html:41-52](../../index.html#L41-L52) |
| R2 | Hero | ≤767px | `display:flex` sin wrap + retrato fijo `width:290px`: la imagen queda 100% fuera de pantalla (medido: left=412, right=702 a 390px) y estira el documento +348px. Todo lo demás hereda este overflow. | **Crítico** | `hero-390.webp`, `index-full-390.webp`, metrics `[Hero] img w=290 left=412` · [index.html:58](../../index.html#L58), [index.html:79-80](../../index.html#L79-L80) |
| R3 | Método | ≤767px | `grid-template-columns:1fr 1fr 1fr 1fr` fijo: columnas computadas de **89/81/137/107px** a 390px. Texto de lectura de 14px en torres de una palabra; la col. 3 se corta en el borde y la col. 4 no se ve. | **Crítico** | `metodo-390.webp`, metrics `computedCols: 89px 80.8px…` · [index.html:115](../../index.html#L115) |
| R4 | Trayectoria | ≤767px | `grid-template-columns:1fr 1fr 1fr` fijo: columnas de **88/82/108px**. Los 3 «actos» de la historia profesional son ilegibles justo donde un recruiter los lee. | **Crítico** | `trayectoria-390.webp`, metrics · [index.html:149](../../index.html#L149) |
| R5 | Proyectos | ≤767px | Grid de 3 columnas fijo: tarjetas de 262/233/179px; la 2ª se corta a media pantalla y la 3ª casi no existe. Los CTAs «Demo/Código» de las columnas cortadas quedan inalcanzables sin scroll lateral. | **Crítico** | `proyectos-390.webp`, `chat-flotante-390.webp` (fondo) · [index.html:180](../../index.html#L180) |
| R6 | Global | ≤767px | Con overflow de +348px, el móvil real renderiza con zoom-out o doble scroll; los elementos `position:fixed` (modal, chat) se desplazan respecto al viewport visual (reproducido en emulación móvil de Chromium). | **Crítico** | `index-full-390.webp`, `index-full-320.webp`, metrics |
| R7 | Ficha de proyecto (modal) | ≤767px | El modal en sí está bien construido (`width:min(680px,100%)`), pero hereda el viewport desbordado: el texto de la ficha aparece cortado por el borde derecho en emulación móvil. Se arregla solo al eliminar R2–R5. | **Alto** | `ficha-modal-390.webp`, `ficha-modal-320.webp` · [index.html:328-330](../../index.html#L328-L330) |
| R8 | Carga móvil | todos | Primera visita: **1.78 MB**. `avatar-felipe-memoji.png` = **845 KB (47%)** para renderizarse a 290px; es además candidata a LCP. foto-felipe.jpg 164 KB, fuentes ~340 KB, React+ReactDOM (unpkg) 138 KB, index.html 102.5 KB sin minificar. | **Alto** | metrics `network-390` · [index.html:80](../../index.html#L80), [index.html:6](../../index.html#L6) |
| R9 | Sobre mí | ≤340px | `min-width:300px` en la columna de texto: a 320px (320−64 padding=256 disponibles) desborda +44px. A 390px no afecta. La foto usa `min(360px,80vw)` y sí se adapta. | **Medio** | metrics index-320 `[Sobre mí] div w=300` · [index.html:96](../../index.html#L96) |
| R10 | Fluid cursor | touch | Registra `touchstart/touchmove/touchend` sin detección de dispositivo táctil: el sim. WebGL corre y reacciona al dedo en móvil (CPU/GPU/batería). ⚠️ Verificado en código; impacto visual en dispositivo real no medido. | **Medio** | [fluid-cursor.js:1178-1202](../../fluid-cursor.js#L1178-L1202) |
| R11 | Ensayo (página) | 320px | Overflow +49px por la figura interna con `grid-template-columns:1fr 1fr`. El cuerpo del ensayo (max-width:700px, `clamp()` en h1) es el único layout genuinamente fluido del sitio. | **Bajo** | `ensayo-full-320.webp`, metrics · [ensayos/agencia-sobre-agentes.html:61](../../ensayos/agencia-sobre-agentes.html#L61) |
| R12 | Tipografía | todos | Hipótesis matizada con medición: los ~94 usos de 10–12px son labels overline/chips mono cortos (aceptable). **Cero** bloques de texto de lectura (>80 chars) computan <13px. El cuerpo va de 13.5 a 18.5px. Sin acción requerida. | **Bajo** | metrics `smallText: 0` |
| R13 | Chat flotante | ≤767px | **Funciona bien**: `min(410px, calc(100vw−48px))` adapta el panel, chips y input usables. Único componente ya mobile-ready junto con las páginas de ensayo. | OK ✅ | `chat-flotante-390.webp` · [index.html:641](../../index.html#L641) |
| R14 | Contenedores | ≤767px | `max-width:1140px` + `padding:…32px` da 32px laterales en móvil: correcto, no es causa de overflow (hipótesis 7 descartada como problema). | OK ✅ | metrics |

Transiciones: a **768px** el overflow ya es 0 y los grids caben (columnas ~145–220px, apretadas pero legibles); el punto de quiebre real está entre 767px y abajo. Los cortes recomendados: `@media (max-width:767px)` (colapso a 1 col + nav móvil) y `@media (min-width:768px) and (max-width:1023px)` (2 columnas en Método/Proyectos).

### Nota de accesibilidad (bonus, verificado en código)
Los botones del chat y fichas ya llevan `aria-label` (bien). El nav móvil nuevo deberá conservar foco visible y `aria-expanded` en la hamburguesa (incluido en el mockup).

---

## 3 · Diagnóstico por causa raíz

1. **Ausencia total de media queries.** Verificado: la única en todo el sitio es `@media print` dentro del runtime ([support.js:119](../../support.js#L119)). Todo lo demás es un único layout de escritorio servido a todos los anchos.
2. **Estilos inline como bloqueador estructural.** Con ~940 líneas de `style="…"`, no existe hoy ningún punto donde una media query pueda actuar: CSS en atributo `style` no puede ser condicionado por viewport, y ganarle requiere `!important` selector a selector. Es la causa por la que nunca se añadieron media queries, no un descuido puntual.
3. **Grids y anchos fijos pensados a 1140px.** `1fr 1fr 1fr (1fr)` reparte por igual cualquier ancho — a 390px eso son columnas de ~85px; `width:290px` (retrato) y `min-width:300px` (columna de texto) imponen mínimos que no caben en 320–390px. El overflow global (R6) es la suma de R2+R3+R4+R5.
4. **Nav sin patrón móvil.** 4 anclas + CTA en una fila `flex` sin `flex-wrap` ni menú alternativo (la hipótesis decía ~7 anclas; son 4 + CTA — el problema es idéntico).
5. **Assets sin variantes responsive.** Un solo PNG de 845 KB para un círculo de 290px; sin `srcset`, sin formato moderno, sin `fetchpriority`.

---

## 4 · Estrategia de remediación responsive — comparativa y recomendación

| Criterio | A · Migrar layout a clases en `<helmet><style>` | B · Inline + `!important` quirúrgico | C · Custom properties en `:root` consumidas desde inline |
|---|---|---|---|
| Diff sobre index.html | Enorme: reescribir cientos de atributos | Medio en `<style>`, cero en markup | **Pequeño y localizado**: solo los ~20 valores que cambian por breakpoint |
| Riesgo de regresión desktop | Alto (reconstruir todo el layout ≥1024px que hoy es perfecto) | Medio (guerras de especificidad, orden de carga) | **Mínimo**: el valor desktop queda como default de la var, byte a byte igual |
| Mantenibilidad | Alta a largo plazo | Baja (cada `!important` es deuda) | Alta: cada knob responsive tiene nombre (`--cols-metodo`) |
| Compatibilidad con runtime x-dc (`style-hover`, plantillas) | Hay que verificar interacciones | Frágil | **Intacta**: el runtime sigue viendo atributos `style` normales |
| Esfuerzo estimado | Días | Horas (pero crece mal) | **Horas, acotado** |

**Recomendación: C para lo existente + A solo para componentes nuevos.**

- **C:** en los ~20 puntos de layout críticos, el valor fijo se sustituye por `var(--x, valor-desktop-actual)` y las media queries viven en el `<style>` de `<helmet>` que ya existe. Ejemplo (Método, [index.html:115](../../index.html#L115)):

  ```html
  <!-- antes -->
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:36px;">
  <!-- después -->
  <div style="display:grid;grid-template-columns:var(--cols-metodo,1fr 1fr 1fr 1fr);gap:var(--gap-grid,36px);">
  ```
  ```css
  /* en el <style> de <helmet>, junto a las .ficha-* */
  @media (max-width:767px){
    :root{ --cols-metodo:1fr; --cols-3:1fr; --gap-grid:28px;
           --hero-dir:column; --hero-img:200px; --minw-col:0; }
  }
  @media (min-width:768px) and (max-width:1023px){
    :root{ --cols-metodo:1fr 1fr; --cols-3:1fr 1fr; }
  }
  ```
  En ≥1024px ninguna var está definida → se usa el fallback → **desktop no cambia ni un píxel** (restricción cumplida por construcción). Knobs identificados: `--cols-metodo` (L115), `--cols-3` (L149, L180), `--hero-dir/--hero-img` (L58, L79-80), `--minw-col` (L96), padding vertical de secciones, tamaño del h1 (o `clamp()` como ya hacen los ensayos), y el gigante decorativo `15rem` (L85).

- **A (solo nuevo):** el nav móvil (hamburguesa + hoja) y el toggle ES/EN son markup nuevo → nacen como clases en `<helmet><style>` con su media query, como ya hacen `.ficha-*`. No hay razón para escribirlos inline.

- **B descartada:** cada regla nueva pelearía contra 940 líneas de inline con `!important`; en 6 meses sería ilegible.

Complementos de la fase responsive (no-layout): `srcset`/WebP para el memoji (845→~40 KB), `fetchpriority="high"` en la imagen LCP, y guard táctil en el `x-import` del fluid-cursor (condicionar la importación a `matchMedia('(pointer:fine)')` **desde index.html**, sin tocar support.js ni fluid-cursor.js).

---

## 5 · Selector de idioma ES/EN (Frente 2)

### Decisión arquitectónica: **C · Híbrido (URLs reales `/en/` + toggle contextual)** ✅

| Opción | SEO/IA | Esfuerzo | Mantenimiento | Veredicto |
|---|---|---|---|---|
| A · Solo páginas separadas | ✅ hreflang, ambos idiomas indexables | Medio | Duplicación a mitigar | Base correcta, UX incompleta |
| B · Toggle client-side | ❌ Google/IAs solo ven ES; sin hreflang; URLs no compartibles por idioma | Bajo | Un archivo pero con dos copys entrelazados | **Descartada**: contradice tu objetivo declarado (EN indexable) |
| **C · A + toggle que enlaza la URL equivalente** | ✅ igual que A | Medio | Igual que A | **Recomendada** |

**Mitigación de la duplicación** (manteniendo el espíritu "sin build step"): `index.html` ES sigue siendo la fuente canónica y se edita a mano como hoy. Un script único `scripts/build_en.py` (mismo patrón que `capture.py`: se corre manualmente cuando cambia el copy) genera `/en/index.html` a partir de `index.html` + un diccionario `scripts/strings_en.json` (ES→EN de los textos visibles, ya redactados en borrador). El sitio publicado sigue siendo 100% estático; no hay build en el deploy. Si el diccionario pierde una clave, el script falla listando los strings sin traducir (nunca publica mezcla de idiomas).

### Decisión de UX: toggle textual «ES / EN» (pastilla)

- **Patrón:** texto, no banderas (bandera ≠ idioma: ¿Colombia o España?) ni globo+dropdown (2 idiomas no justifican un dropdown: un tap de más para dos opciones). Pastilla en IBM Plex Mono — la familia que el sitio ya usa para todo lo "meta" — con el activo en tinta `#17141c` y hover `#5b4bd6`.
- **Desktop:** entre «Ensayos» y el CTA «Hablemos». El toggle es utilidad, no destino: no debe competir con el CTA ni mezclarse con las anclas. Con 4 anclas + CTA hay espacio de sobra a ≥1024px (verificado en `nav-1440.webp`).
- **Móvil (diseñado junto con el nav del Frente 1):** el toggle queda **siempre visible en la barra**, al lado de la hamburguesa — quien no lee español no va a abrir un menú en español para buscarlo. La hamburguesa (`aria-expanded`) abre una hoja con las 4 anclas numeradas + CTA «Hablemos». Una sola propuesta coherente para ambos frentes: **mockup navegable en [mockups/nav-idioma.html](mockups/nav-idioma.html)** (desktop, móvil cerrado, móvil abierto y banner).
- **Comportamiento:** el toggle enlaza a la URL equivalente **conservando el ancla** (`/#proyectos` ⇄ `/en/#proyectos`; los ids no se traducen). Elección persistida en `localStorage`. Sugerencia pasiva vía `navigator.language`: banner discreto y descartable «This site is also available in English» — **nunca redirección automática** (rompe crawlers y es mala UX).
- **Alcance v1:** solo `index.html` (coincide con tu default). Los ensayos permanecen en ES; en `/en/` se listan con la nota «(in Spanish)» — apuntan a queries en español y traducirlos duplicaría el mantenimiento del contenido más largo. hreflang solo donde existe equivalente (index). **Borrador EN completo para tu revisión en [en-draft-index.md](en-draft-index.md) — nada se publica sin tu validación.** Pendiente de tu decisión: qué hacer con el chat en `/en/` (propuestas en el borrador).

---

## 6 · Plan SEO e indexabilidad IA (Frente 3)

### 6.0 Gap analysis (verificado a 2026-07-13)

| Elemento | index | 4 ensayos | Estado |
|---|---|---|---|
| `<title>` | ❌ | ❌ | 0 en todo el sitio |
| `lang` en `<html>` | ❌ | ❌ | `<html>` pelado ([index.html:2](../../index.html#L2)) |
| meta description / OG / Twitter / canonical / JSON-LD / hreflang | ❌ | ❌ | 0 de todo |
| robots.txt · sitemap.xml · llms.txt · favicon · 404.html | ❌ | — | **Creados en esta auditoría (sin commitear)**: [robots.txt](../../robots.txt), [sitemap.xml](../../sitemap.xml), [llms.txt](../../llms.txt), favicon.ico + favicon-192.png + apple-touch-icon.png (derivados del memoji). Falta 404.html (snippet abajo). |
| Jerarquía | 1 h1 + 3 h2 (Sobre mí, Método, Proyectos) para 9 secciones | h1 + h2 correctos ✅ | Trayectoria/Ensayos/Contacto sin heading |
| `alt` en imágenes | ✅ 3/3 | — | OK |

**HTML crudo vs DOM renderizado** (crítico para IAs, que no ejecutan JS — el sitio es estático, el HTML servido es idéntico al archivo):
- ✅ En crudo: h1, los 4 pasos del método, trayectoria completa, 8 tarjetas + fichas completas, títulos de ensayos, cuerpo íntegro de los 4 ensayos con FAQs.
- ❌ Solo post-JS: **el nombre** («Soy {{ name }}» en el hero [index.html:62](../../index.html#L62), marca del nav L44, © del footer L320) y **el email** ({{ email }} ×4) — viven en [index.html:881-882](../../index.html#L881-L882). Un crawler de IA ve mustaches literales donde va tu nombre. *(Mitiga: «Soy Felipe Peña, Growth Product Manager» sí aparece en texto plano en Sobre mí L99.)* → Recomendación fase 2: hornear nombre/email estáticos en esos 4 puntos; son constantes, no estado.
- ⚠️ Hallazgo colateral: el email por defecto del runtime es `ing.felipe55@outlook.com` (L882) pero los ensayos publican `hola@felipepena.co` — unificar hacia el del dominio.
- ❌ Ensayos sin fecha de publicación ni autor visibles en texto plano (solo «9 min de lectura» y «ENSAYO 3 DE 4») → añadir línea de meta visible + `datePublished`.

### 6.1 `<head>` de index.html — listo para pegar

```html
<html lang="es">
...
<title>Felipe Peña — Growth Product Manager · SaaS B2B/B2G</title>
<meta name="description" content="Growth Product Manager para SaaS B2B/B2G. Convierto fricción de usuario en retención e ingresos con datos y experimentos. Proyectos, método y ensayos.">
<link rel="canonical" href="https://felipepena.co/">

<meta property="og:type" content="profile">
<meta property="og:title" content="Felipe Peña — Growth Product Manager">
<meta property="og:description" content="El crecimiento no se hackea. Se compone. Datos, experimentos y producto SaaS B2B/B2G.">
<meta property="og:url" content="https://felipepena.co/">
<meta property="og:image" content="https://felipepena.co/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="es_CO">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Felipe Peña — Growth Product Manager">
<meta name="twitter:description" content="El crecimiento no se hackea. Se compone. Datos, experimentos y producto SaaS B2B/B2G.">
<meta name="twitter:image" content="https://felipepena.co/og-image.png">

<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">

<!-- hreflang: activar SOLO cuando exista /en/ (decisión Frente 2 = C) -->
<!-- <link rel="alternate" hreflang="es" href="https://felipepena.co/"> -->
<!-- <link rel="alternate" hreflang="en" href="https://felipepena.co/en/"> -->
<!-- <link rel="alternate" hreflang="x-default" href="https://felipepena.co/"> -->

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Person",
      "@id": "https://felipepena.co/#person",
      "name": "Felipe Peña",
      "alternateName": "Bairon Felipe Peña Castellanos",
      "jobTitle": "Growth Product Manager",
      "email": "mailto:hola@felipepena.co",
      "url": "https://felipepena.co/",
      "image": "https://felipepena.co/foto-felipe.jpg",
      "knowsLanguage": ["es", "en"],
      "sameAs": [
        "https://www.linkedin.com/in/bairon-felipe-peña-castellanos-ab18411b5/",
        "https://github.com/castellanosfelipe"
      ]
    },
    {
      "@type": "ProfilePage",
      "@id": "https://felipepena.co/#page",
      "url": "https://felipepena.co/",
      "name": "Felipe Peña — Growth Product Manager",
      "inLanguage": "es",
      "about": { "@id": "https://felipepena.co/#person" },
      "mainEntity": { "@id": "https://felipepena.co/#person" }
    }
  ]
}
</script>
```
La og-image de 1200×630 ya está generada y aprobable: [og-image-1200x630.webp](og-image-1200x630.webp) (plantilla editable en [mockups/og-image-template.html](mockups/og-image-template.html); al implementar, copiarla a la raíz como `og-image.png`).

### 6.2 `<head>` por ensayo — listos para pegar

Común a los 4: `<html lang="es">`, favicon links (como arriba con rutas absolutas `/favicon.ico`), y su bloque propio:

**como-elegir-el-experimento-correcto.html**
```html
<title>Cómo elegir el experimento correcto · Felipe Peña</title>
<meta name="description" content="Cuándo hacer A/B tests, cuándo innovar y cómo alinear tus experimentos con la etapa de tu producto. Un marco práctico de experimentación. 5 min de lectura.">
<link rel="canonical" href="https://felipepena.co/ensayos/como-elegir-el-experimento-correcto.html">
```

**pmf-sostener-y-expandir.html**
```html
<title>Product-Market Fit no es un destino · Felipe Peña</title>
<meta name="description" content="El product-market fit se erosiona si no lo trabajas: señales para detectarlo a tiempo, cómo sostenerlo y cuándo expandir mercado o producto. 7 min de lectura.">
<link rel="canonical" href="https://felipepena.co/ensayos/pmf-sostener-y-expandir.html">
```

**agencia-sobre-agentes.html**
```html
<title>Agencia sobre agentes: IA y confianza · Felipe Peña</title>
<meta name="description" content="Tu estrategia de IA no falla por herramientas sino por confianza: la velocidad depende de dar autonomía y contexto real a los equipos. 9 min de lectura.">
<link rel="canonical" href="https://felipepena.co/ensayos/agencia-sobre-agentes.html">
```

**experimentacion-en-la-era-de-la-ia.html**
```html
<title>La era de la IA exige otra forma de experimentar · Felipe Peña</title>
<meta name="description" content="Menos micro-optimizaciones y apuestas más grandes: por qué la era de la IA exige otra forma de experimentar en producto y monetización. 10 min de lectura.">
<link rel="canonical" href="https://felipepena.co/ensayos/experimentacion-en-la-era-de-la-ia.html">
```

Cada uno con OG análogo (`og:type` = `article`) y su JSON-LD `Article` — plantilla (rellenar `datePublished` real; el repo se publicó el 2026-07-10, **confírmame la fecha por ensayo**):
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Agencia sobre agentes: tu estrategia de IA tiene un problema de confianza, no de herramientas",
  "author": { "@id": "https://felipepena.co/#person" },
  "publisher": { "@id": "https://felipepena.co/#person" },
  "datePublished": "2026-07-10",
  "inLanguage": "es",
  "url": "https://felipepena.co/ensayos/agencia-sobre-agentes.html",
  "image": "https://felipepena.co/og-image.png"
}
</script>
```

### 6.3 Jerarquía semántica sin alterar estilos

Regla: el tag cambia, el atributo `style` se conserva idéntico añadiendo solo `margin:0` (o el margin actual) y `font-weight` explícito para neutralizar defaults del heading. Cero cambio visual.

| Ubicación | Hoy | Propuesto |
|---|---|---|
| Trayectoria, frase intro ([index.html:148](../../index.html#L148)) | `<p>` | `<h2>` (mismo style, ya tiene margin) |
| Contacto, titular ([index.html:304](../../index.html#L304)) | `<div>` | `<h2>` (añadir `margin:0` al style) |
| Ensayos, label de sección ([index.html:261](../../index.html#L261)) | `<div>` overline | `<h2>` (mismo style mono + `margin:0`) |
| Títulos de cada ensayo en la lista (L267, L275, L283, L291) | `<div>` | `<h3>` (+`margin:0;font-weight:300`) |
| Método, nombre de cada paso (L118, L124, L130, L136) | `<div>` | `<h3>` (+`margin:0;font-weight:400`) |
| Proyectos, nombre de tarjeta (L182 etc. ×8) | `<span>` | `<h3>` (+`margin:0;font-weight:400;font-size:22px` ya en style) |

Resultado: h1 único → h2 por sección → h3 por ítem. Los overlines de Hero/Sobre mí/Método/Proyectos siguen siendo `<div>` (ya hay h2 reales en esas secciones).

### 6.4 Indexabilidad IA

1. **robots.txt** ya creado con Allow explícito para GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, Claude-SearchBot, anthropic-ai, PerplexityBot, Perplexity-User, Google-Extended y CCBot + `Sitemap:` → [robots.txt](../../robots.txt).
2. **llms.txt** ya creado: quién eres, método, los 8 proyectos, los 4 ensayos anotados y perfiles → [llms.txt](../../llms.txt). (Al existir `/en/`, añadirle una línea "Also available in English".)
3. **Legibilidad en texto plano:** cuerpo de ensayos ✅ íntegro en crudo (incl. FAQs, muy citables por IAs). Títulos ✅. **Fechas y autoría ❌** → añadir en cada ensayo una línea visible bajo el overline, estilo del sitio: `<span>Por Felipe Peña · Julio 2026</span>` (mono 11px, como «9 MIN DE LECTURA») + JSON-LD 6.2. Y hornear nombre/email (ver 6.0).

### 6.5 404.html — listo para crear en la raíz

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>404 — Página no encontrada · Felipe Peña</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;1,6..72,300&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">
<style>
  body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#f6f5f3;color:#17141c;font-family:'Newsreader',Georgia,serif;text-align:center;padding:24px;}
  .overline{font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:0.18em;color:#5b4bd6;text-transform:uppercase;margin-bottom:18px;}
  h1{font-weight:300;font-size:clamp(40px,8vw,72px);margin:0;line-height:1.1;}
  h1 em{color:#5b4bd6;}
  a{display:inline-block;margin-top:28px;background:#17141c;color:#fff;text-decoration:none;font-family:'IBM Plex Mono',monospace;font-size:13px;padding:12px 24px;border-radius:999px;}
  a:hover{background:#5b4bd6;}
</style>
</head>
<body>
  <main>
    <div class="overline">Error 404</div>
    <h1>Esta página no existe.<br><em>Todavía.</em></h1>
    <a href="/">← Volver a la portada</a>
  </main>
</body>
</html>
```

### 6.6 Acciones manuales para ti

1. **Google Search Console** → añadir propiedad de dominio `felipepena.co` (verificación DNS TXT en tu registrador; GitHub Pages ya sirve el CNAME).
2. Enviar `https://felipepena.co/sitemap.xml` en GSC → Sitemaps.
3. En GSC → Inspección de URL: solicitar indexación de `/` y de los 4 ensayos (acelera el primer rastreo).
4. Validar la tarjeta social tras el deploy: [opengraph.xyz](https://www.opengraph.xyz) o el Post Inspector de LinkedIn.
5. Test de resultados enriquecidos: [search.google.com/test/rich-results](https://search.google.com/test/rich-results) sobre `/` y un ensayo.
6. Decidir y confirmarme: fechas reales de publicación de cada ensayo, y el email canónico (`hola@felipepena.co` vs `ing.felipe55@outlook.com`).

---

## 7 · Plan maestro priorizado (impacto ÷ esfuerzo, con dependencias)

| # | Ítem | Frente | Impacto | Esfuerzo | Riesgo | Depende de |
|---|---|---|---|---|---|---|
| 0 | Commitear los archivos ya creados: robots.txt, sitemap.xml, llms.txt, favicons | SEO/IA | Alto | 5 min | Cero | Tu aprobación |
| 1 | `lang="es"` + `<title>` + descriptions + canonical en las 5 páginas (§6.1–6.2) | SEO | **Muy alto** | 30 min | Cero | — |
| 2 | og-image.png a raíz + bloques OG/Twitter + JSON-LD Person/ProfilePage | SEO | Alto (tarjeta al compartir) | 30 min | Cero | Aprobar [og-image-1200x630.webp](og-image-1200x630.webp) |
| 3 | 404.html (§6.5) + fecha/autor visibles en ensayos + JSON-LD Article | SEO/IA | Medio | 45 min | Cero | Fechas confirmadas por ti |
| 4 | GSC + sitemap + solicitudes de indexación (§6.6) | SEO | Alto | 20 min | Cero | #0–1 desplegados |
| 5 | **Responsive core**: vars C + media queries (hero, 3 grids, min-width, decorativo 15rem) | Resp. | **Crítico** | 3–5 h | Bajo (fallbacks = desktop actual) | Aprobar estrategia C |
| 6 | **Nav móvil** (hamburguesa + hoja) con hueco para el toggle | Resp. | Crítico | 2–3 h | Bajo | #5; mockup aprobado |
| 7 | Hornear nombre/email estáticos + unificar email (§6.0) | SEO/IA | Medio | 20 min | Bajo | Email canónico decidido |
| 8 | Memoji → WebP con srcset (845→~40 KB) + `fetchpriority="high"` | Resp./CWV | Alto | 30 min | Bajo | — |
| 9 | Jerarquía h2/h3 (§6.3) | SEO | Medio | 45 min | Bajo (tags con mismo style) | — |
| 10 | Fluid-cursor solo en `pointer:fine` (guard en el x-import desde index.html) | Resp. | Medio | 20 min | Bajo | — |
| 11 | **/en/index.html** vía `build_en.py` + diccionario, tras validar [en-draft-index.md](en-draft-index.md) | Idioma | Alto | 4–6 h | Medio | Copy EN validado por ti; #6 (toggle vive en nav) |
| 12 | Toggle ES/EN + banner `navigator.language` + localStorage | Idioma | Alto | 1–2 h | Bajo | #6 y #11 |
| 13 | hreflang es/en/x-default + `/en/` en sitemap + nota en llms.txt | SEO | Medio | 15 min | Cero | **#11 (decisión C)** — no antes |
| 14 | Fix overflow 320px en figuras de ensayos (grid 1fr 1fr → var) | Resp. | Bajo | 20 min | Bajo | #5 (mismo patrón) |

Cadenas de dependencia clave: **hreflang (#13) ← /en/ (#11) ← copy validado**; **toggle móvil (#12) ← patrón nav (#6) ← estrategia C aprobada (#5)**. Todo lo de riesgo cero (#0–#4) es implementable hoy sin esperar ninguna decisión de los frentes 1–2.

## 8 · Quick wins (<30 min cada uno)

1. **Commit de robots.txt + sitemap.xml + llms.txt + favicons** (ya creados y verificados) — 5 min.
2. **`<title>` + `lang="es"` en las 5 páginas** — 15 min, el mayor salto de visibilidad por minuto invertido.
3. **Meta descriptions + canonical ×5** (§6.1–6.2, copy listo) — 15 min.
4. **Bloques OG/Twitter + subir og-image.png** — 20 min (la imagen ya está generada).
5. **JSON-LD Person/ProfilePage en index** — 10 min (snippet listo).
6. **404.html** — 10 min (código completo en §6.5).
7. **Alta en GSC + envío de sitemap** — 20 min.
8. **Memoji a WebP + srcset** — 25 min; −800 KB (−45%) en la primera carga móvil.
9. **Guard táctil del fluid-cursor** — 20 min.
10. **Línea «Por Felipe Peña · [mes año]» en los 4 ensayos** — 15 min (necesita tus fechas).

---

### Anexo · Inventario de evidencia

`index-full-{320,390,768,1024,1440}.png` · `ensayo-full-{...}.png` · `nav-{...}.png` · `hero-390.webp` · `sobre-mi-390.webp` · `metodo-390.webp` · `trayectoria-390.webp` · `proyectos-390.webp` · `ensayos-390.webp` · `contacto-390.webp` · `ficha-modal-{320,390}.png` · `chat-flotante-390.webp` · `og-image-1200x630.webp` · `metrics.json` (overflow, offenders con sección/px, columnas computadas de cada grid, texto <13px, pesos de red) · `mockups/nav-idioma.html` · `mockups/og-image-template.html` · `en-draft-index.md`.

*Peso de red medido en servidor local sin gzip; GitHub Pages comprime los textos (~102 KB de HTML → ~25 KB transferidos), las imágenes viajan igual. Los porcentajes citados usan el total sin compresión.*
