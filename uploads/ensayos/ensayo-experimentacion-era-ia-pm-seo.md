---
layout: post
title: "La era de la IA exige otra forma de experimentar"
description: "Menos micro-optimizaciones, apuestas más grandes en monetización y tests más largos. Por qué el playbook de experimentación de 2022 quedó obsoleto y qué hacer distinto."
slug: experimentacion-producto-era-ia
canonical_url: https://TU-DOMINIO.com/blog/experimentacion-producto-era-ia
lang: es
keywords:
  - experimentación de producto
  - experimentación con IA
  - monetización de producto
  - A/B testing
  - product manager
  - estrategia de producto
image: /assets/img/experimentacion-era-ia.png
---

# La era de la IA exige otra forma de experimentar

La experimentación es de mis partes favoritas del trabajo en producto. Pero apostaría a que el playbook de experimentación que la mayoría de los equipos sigue usando quedó obsoleto. Y quizás no sea tan malo, porque la forma vieja de experimentar tenía límites que todos conocíamos y pocos admitían:

- Ajustes menores en vez de apuestas grandes.
- Optimizar superficies visibles en vez de la complejidad de fondo.
- Ni tocar la monetización ("son seis meses de aprobaciones y desarrollo, con suerte").
- Medir con antes/después en vez de A/B tests reales o feature flags.
- Perseguir victorias rápidas, todo medido a dos semanas.

Algo de eso tenía sentido cuando el desarrollo era lento y había tanta superficie que dar a conocer una feature ya era una victoria. Pero incluso entonces, muchos de esos experimentos apenas adelantaban ingresos que iban a llegar igual. Mejorabas un poco la experiencia, creabas algo de urgencia, y algo que habría pasado de todos modos pasaba antes. Por eso tantos experimentos suman al bottom line sin producir jamás un salto real.

Había margen de mejora hace rato. Ahora el terreno cambió por completo. Estos son los cuatro cambios de fondo y las tres cosas que haría distinto.

## Los 4 cambios que rompieron el playbook

### 1. Las superficies se están colapsando

Los flujos nuevos, sobre todo en productos de IA, son conversacionales y van por prompt. Hay menos superficies que necesiten "awareness". La UI dejó de ser la forma principal de interactuar con muchas features, así que optimizarla hasta el infinito ya no paga.

Piensa en una herramienta de transcripción de reuniones que usas a diario sin abrir casi nunca su interfaz. Se mete a tu reunión, genera la transcripción, y tú conversas con ese contenido por prompts desde otro producto. ¿Qué UI le vas a hacer A/B test ahí?

### 2. El desarrollo se aceleró

El impacto de un experimento exitoso dura menos, porque la superficie donde lo corriste cambia rapidísimo. Mejorar un embudo 1% suena absurdo cuando ese embudo se rediseña en dos meses. Peor si medir el cambio te toma dos o tres semanas. La mayoría de los equipos no tiene ni el tiempo ni el tráfico para sacar conclusiones a tiempo. Normalmente le faltan los dos.

### 3. La personalización dejó de ser necesaria

Buena parte de los micro-ajustes existía por la personalización: dar más contexto, usar lenguaje más relevante para cada segmento. Siempre fue doloroso. Limitabas la audiencia por defecto, lo que servía para un segmento no escalaba a otro, y todo había que hardcodearlo. Pura deuda de vida útil incierta.

La IA volvió casi todo eso irrelevante. Una conversación es personalizada por naturaleza. La necesidad de testear esos ajustes chicos simplemente desapareció.

### 4. Usar el producto ahora cuesta plata

Muchos productos consumen tokens de LLM para funcionar, así que el uso dejó de ser gratis. La monetización golpea antes en el embudo y cada acción del usuario cuesta más.

Por eso, no tocar la monetización en tus experimentos pasó de ser prudencia a ser el peor error disponible. Nadie tiene la monetización de IA resuelta. Hasta los laboratorios más grandes siguen cambiando sus modelos de precios cada rato. Tratar esa área como algo estático es regalar la palanca de crecimiento más potente que tienes.

## Las 3 cosas que haría distinto

### 1. Dejar de gastar ingeniería en micro-optimizaciones

Antes cada optimización pasaba por horas de ingeniería. Hoy un PM puede resolver tareas cada vez más complejas de punta a punta por su cuenta. Algunas las corres como A/B test de verdad. Otras honestamente no valen la pena. Pero hay algo que no haría jamás: quemar al equipo de ingeniería en retoques de interfaz. Ese recurso es demasiado escaso para gastarlo ahí.

Además estos ajustes pueden ser hasta entretenidos para un PM o un marketer, y son miserables para la mayoría de los ingenieros. Si los absorbes tú, liberas a ingeniería para los problemas difíciles. Todos crean más valor.

### 2. Apostar más grande, sobre todo en monetización

En algún momento estas transformaciones se van a asentar y volveremos a afinar plataformas estables. Hoy no. Hoy lo grande se mueve rápido y hay que jugar a ese nivel. Y sí, hablo de monetización: es la palanca más grande disponible para desbloquear engagement, cuidar margen y empujar expansión y retención.

Un principio contraintuitivo que vale oro: los mejores experimentos de monetización no buscan subir ingresos. Los experimentos neutrales en ingresos suelen ser los grandes ganadores, porque levantan engagement, y ese engagement se convierte en ingresos uno, dos o tres meses después. Mientras no empujen el negocio a territorio insostenible y suban el engagement, son victoria.

Cuando la mayoría piensa en ingresos va directo a conversión de gratis a pago o a renovaciones. Ese no es el punto ahora. Estamos en pleno ciclo de adopción de una tecnología nueva. Todo debería apuntar a tu North Star o a otra métrica de engagement, dentro de un margen aceptable.

### 3. Apuestas más grandes, tests más largos

Si tus cambios impactan al sistema completo, tienes que dejarlos correr mucho más tiempo. Esos resultados a dos semanas que tanto gustan en los comités son justo lo peor que puedes hacer ahora.

Si tienes tanta fruta al alcance de la mano que puedes mejorar el producto en dos semanas, adelante, arrégla todo eso. Pero en un producto maduro eso no debería estar pasando. El foco va en lo grande: dónde están tus límites de freemium, cómo funciona tu sistema de créditos, qué features van en cada plan, cómo cambia el uso cuando mueves una feature de plan.

Todo eso tiene impacto de sistema y efectos en cascada. Corre el split una o dos semanas, pero monitorea las cohortes uno o dos meses. No decidas apenas termina la primera fase.

Un ejemplo de cómo se ve esto en la práctica: pruebas dar 5 contra 10 créditos el primer día del plan gratis. De inmediato se ve horrible. ¿Por qué regalar más? Pero dos meses después, el efecto en engagement y retención alcanza al costo inicial y lo supera. Primeros 30 días, pésimo. Largo plazo, netamente positivo. Con experimentos de recargas pasa igual: horrible el primer mes, salvajemente positivo cuando las cohortes maduran, que puede tomar 45 días o más.

Enciende el experimento y dale tiempo. Y para que haya impacto que esperar, necesitas apuestas de verdad. Cambiar la página de precios de "$25/mes" a "$24.99/mes" no es una apuesta. Ese tipo de retoque, automatízalo con IA: las buenas prácticas aciertan el 80% de las veces.

## Quizás ni deberías testear eso

Mi opinión más polémica: no tienes que testear todo. En este mundo nuevo hay áreas donde puedes saltarte ese paso.

Ojo, todo debe medirse. Cada cambio anotado, cada clic e interacción trackeados, idealmente en el código, donde un agente puede recuperar qué cambió, dónde y cuándo. Eso no se negocia.

Pero con inteligencia promedio disponible a un prompt de distancia, partir de cero es absurdo. No necesitas a alguien testeando cada elemento para llegar a una página de precios optimizada. Pregúntale a la IA, implementa eso como baseline y listo. La IA acumuló toneladas de estándares de industria. A menos que seas un caso genuinamente atípico, arranca del default.

Un ejemplo. Un principio de producto que sostengo con fuerza: las features de los planes superiores deberían verse desde el plan inferior, con paywalls a nivel de feature que se expliquen solos. Si descubres que tu plan gratis esconde diez features de pago que ni se muestran, eso no es un experimento pendiente. Es prácticamente un bug. Implementar la versión con las features visibles y el disparador de upgrade toma poco tiempo y está validado por miles de empresas que ya pasaron por ahí. ¿A/B test? No. Usa lo que ya funciona y guarda la experimentación para lo que sí es incierto.

Antes, cuando implementar algo así requería coordinar a diez equipos de ingeniería, tenía sentido vetarlo primero. Hoy no.

## La experimentación no murió, cambió de forma

La UI que retocábamos está desapareciendo. Los cambios corren demasiado rápido para testearlos todos. La personalización es automática. Y el costo de usar el producto se disparó. La forma vieja de experimentar dejó de ser inteligente.

Pero si sueltas las micro-optimizaciones, apuestas más grande y dejas correr los tests más tiempo, tu sistema de experimentación va a importar más que nunca. Y si te llevas una sola cosa de todo esto, que sea esta: ve y experimenta con tu sistema de monetización. Ahí hay espacio para crecer, te lo aseguro.

> Nota: este ensayo trata sobre experimentación y monetización de producto en términos generales. No es asesoría financiera.

## Preguntas frecuentes

**¿Sigue teniendo sentido hacer A/B tests?**
Sí, pero para apuestas grandes con impacto de sistema: monetización, límites de freemium, sistemas de créditos. Los micro-retoques de interfaz conviene automatizarlos o saltarlos.

**¿Por qué experimentar con monetización si nadie la tiene resuelta?**
Justamente por eso. En pleno ciclo de adopción de la IA, la monetización es de las palancas más grandes y menos exploradas. Ignorarla es dejar valor sobre la mesa.

**¿Cuánto debe durar un experimento hoy?**
Corre el split una o dos semanas, pero monitorea las cohortes uno o dos meses. Muchos efectos positivos solo aparecen cuando las cohortes maduran, a veces pasados los 45 días.

**¿Hay cosas que no debería testear?**
Sí. Cuando algo es un estándar validado por miles de empresas, o directamente un bug, no lo testees desde cero. Adopta la mejor práctica como baseline y reserva los experimentos para lo incierto y de alto impacto.

---

*¿Trabajas en producto? Suscríbete a la newsletter o explora otros ensayos sobre [estrategia de producto](/blog/).*
