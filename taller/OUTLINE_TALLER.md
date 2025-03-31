Outline del taller

Título: "Construye tu propio ChatGPT con Python y Open Source"
Título alternativo:  "¡Haz tu propio ChatGPT! Taller de Python + IA para todos"
Público objetivo: Estudiantes de DUOC de 1er a 3er año, de cualquier carrera.
Descripción: En este taller se enseña las bases de que es LLMs & IA, y se construye un ChatGPT simple usando Python y streamlit.

Inspiración: 
El mago de Oz. Se ve impresionante, y le rinden pleitesía, pero no es magia. Detrás de la cortina "sólo" hay tecnología. IA & LLMs son lo mismo.

El computador & la ilusión de la continuidad.
bits, just bits. 
Imagen: bits + context/conventions -> representación

todo es discretos: numeros, colores, gráficos, sonidos, etc etc.
Alta fidelidad no es continuidad. Pero es una muy buena aproximación.
No necesitamos la realidad, necesitamos una buena aproximación. Suficiente para engañar a los sentidos.
Otro ejemplo: una película. Ojo humano es muy malo para detectar el frame rate. Una pelicula de 24 fps es suficiente para engañar al ojo humano.

¿Como representar una imagen?

¿Cómo representar una palabra?
Depende...
Si solo queremos transmitir texto (sin interpretar - semántica), basta con representar cada letra con una secuencia de bits, y almacenarla. Listo.
Si quieres poder interpretar el texto, necesitamos una mejor REPRESENTACIÓN.
texto -> tokens -> embeddings
(ejemplo)

¿LLM?
LLM = Large Language Model = Grandes Modelos de Lenguaje

Representación filtrada de OpenAI del funcionamiento de un LLM
(imagen de grommit poniendo tracks en el tren)

Predecir la próxima palabra a partir de las anteriores.
Mostrar imagen de cómo va avanzando la creación de la respuesta, palabra por palabra.
Ojo: no es que el LLM "piense" o "sabe" lo que está haciendo. Es sólo una representación.
Ojo 2: es estadística aplicada! 
Ojo 3: Se predice token a token. No hay paralelismo, no se puede predecir el siguiente token mientras los anteriores no se han predicho. Es super secuencial.
OJo 4: El LLM no tiene memoria. Siempre empieza a predecir desde el mismo estado inicial.
Comparar con una multiplicación de matrices. La matriz no recuerda que ya hizo multiplicaciones antes.

- Versión 1 del chat
- Probar el chatciit
- Hacer pruebas: Ejemplo Q1: ¿Qué animal da leche y dice mu? Q2: ¿Como se llama un animal castrado de esa especie?

Ya, y porqué recuerda lo que ya le dije?
Los inteligentes son los ingenieros que los programaron. Hay mil y 1 trucos que se están usando e inventando.
Pasemosle la historia de la conversación.
- Tecnica 1: Pasarle todo el texto.
- Tecnica 2: Pasarle un resumen de la conversación.

¿Que es la temperatura?
Rpa: Que tan aleatoria es la elección del siguiente token.

¿Cómo se entrena un LLM?
Corpus de texto y mucho dinero o muchas gpus.
¿Que se obtiene? Muchas grandes matrices! (depende de la arquitectura) - dar 1 ejemplo.

Esto significa que un LLM open source puede descargarse (son bits), y ejecutarse localmente - si tu hardware lo permite.
