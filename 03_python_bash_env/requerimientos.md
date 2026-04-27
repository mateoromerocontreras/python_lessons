# Requerimientos: Plan de Formación Práctica Urgente

Este plan se enfoca en las habilidades fundamentales que necesitas para dejar de bloquearte y dejar de perder tu tiempo en tareas básicas.
> ⏱️ **Prioridad:** Práctica inmediata directamente sobre conceptos reales.

---

## 1. Estructura y Gestión de Proyectos (Git Básico)
**Objetivo:** Claridad absoluta sobre cómo organizar tu código y tu trabajo de manera segura.

### Conceptos Prácticos
- Comprender qué es un repositorio (`repo`) y con qué propósito se crea.
- Interiorizar qué es una rama (`branch`) y cuál es su utilidad vitalicia.
- Aprender cómo y por qué **NO** se debe tener jamás múltiples copias de la misma carpeta del proyecto (ej: una en *Escritorio* y otra idéntica en *Programación*).
- Descubrir y aprender a identificar desde la terminal dónde ubicar la ruta de la "raíz" central del proyecto.

> **Enfoque:** Explicación lo más directa posible. Basado en una carpeta de un proyecto real, no utilizando pura teoría.

---

## 2. Terminal Esencial para Desarrolladores
**Objetivo:** Automatizar tus reflejos para utilizar la terminal. Moverte y ejecutar con agilidad los comandos evadiendo todos los errores.

### Comandos Vitales y Práctica Intensiva
- `pwd` (Saber con exactitud dónde estás parado en Mac/Linux/PowerShell).
- `ls` o `dir` (Imprimir o ver qué contenidos o carpetas existen en ese lugar).
- `cd` (Cambiar y saltar de un directorio hacia otro).
- Uso ágil de **flechas del teclado** para recuperar el historial de comandos pasados sin tener que reescribir.
- Autocompletado de oraciones pesadas utilizando la tecla **Tab**.
- Descubrir la técnica correcta al copiar y pegar direcciones de repositorios para evitar fallos.
- Asegurar previamente la ejecución de los comandos situándote desde el directorio raíz y correcto.

**⚠️ Advertencia:** Si no logramos convencerte de automatizar profundamente esta parte, seguirás perdiéndote habitualmente durante las videollamadas de seguimiento.

---

## 3. Entornos Virtuales y Dependencias (ALTA PRIORIDAD)
**Objetivo:** Entender la filosofía de por qué se debe aislar tus paquetes, crearlos y gobernarlos para destruir los conflictos de versión.

### Gestión del Entorno Virtual (venv)
- **Definición:** ¿Qué es un `venv` y por lo tanto, por qué es imprescindible hoy en día?
- Dominar el proceso de creación.
- Dominar el proceso de activación, y comprender cómo verificar su estatus visual o revisándolo en consola con las utilidades de comandos.
- Dominar cómo terminar el horario de trabajo con un proceso de desactivación rápido con la palabra `deactivate`.

### Gestión Inteligente de Dependencias
- ¿Cuál es el importante rol de `pip` en este mundo?
- Aprender sobre `requirements.txt`.
- Aprender el atajo oficial para instalar una tabla completa con todas las dependencias del ecosistema del proyecto con solo invocar un comando.

---

## 4. Variables de Entorno y Comentarios
**Objetivo:** Desarrollar el cuidado necesario para manipular tu configuración sensible con suma precaución por la sintaxis estándar de la industria.

### Uso Correcto del Archivo `.env`
- ¿Qué es y qué abarca un archivo resguardado con la etiqueta de `.env`?
- ¿A qué le llamamos una **variable de entorno** y cómo reacciona en tu servidor?
- Separar totalmente la barrera mental entre leer una *línea funcional (activa)* y ser ciego a un *comentario*.
- Aplicar correctamente la simbología con peso de comentario, como el *hashtag (`#`)*.
- Entender el concepto verbal de la acción llamada "descomentar".
- Darse la labor de analizar, por último, por qué el renglón `MODEL_ID=...` se acciona mientras que el engañoso renglón `# MODEL_ID=...` simplemente es ignorado.

> **Enfoque:** Esta es puramente una exploración práctica en un archivo real, partiendo de que este ha sido tu talón de Aquiles o punto constante de errores en sesiones pasadas recientes.

---

## 5. Ejecución de Scripts y Lectura de Errores
**Objetivo:** Estimular tus ojos para encontrar y desarmar anomalías e inconvenientes al tratar de correr un ejecutable Python de antemano.

### Proceso de Inicialización, Ejecución y Diagnóstico
1. Aprender a ir abriendo tu proyecto correctamente.
2. Hacer el acto protocolario de encender siempre primero el entorno temporal.
3. Llamar y ejecutar por nombre exacto tu archivo extendido en `.py`.
4. Culturizarse a no temerle a un temible y popular `ModuleNotFoundError`.
5. Ser rápido decidiendo si el actual incidente se centra en un defecto del creador (por ejemplo, por mala sintaxis de un código) o por otro lado meramente falta de nutrición al programa debiéndole una herramienta u paquete que te olvidaste añadir instalándolo.

> 💡 **Aclaración:** NO pongamos nuestra energía principal todavía sobre la forma pura de la sintaxis Python por ahora. Concéntrate solamente en desarrollar músculos lógicos enfocados a detectar el escenario de diagnóstico correcto.

---

## Resumen de la Sesión de Pair Programming

La sesión particular de programación conjunta (en pareja) se centró primordialmente en echarle vista previa y revisar la base de datos, repasar la arquitectura del lugar y erradicar depurando un cúmulo de obstáculos técnicos y fallas de software.

- **Base de Datos:** Se examinó en esta ventana toda la tabla y registro de `dev midnight lab link review`. A esto, se rectificó de todo corazón que existía un total en la hoja "link entity" de exactas 1,013 divisiones. Posteriormente fue asignado que cada eslabón y etiqueta provenientes de *scripts de scraping* deben ser registradas puntualmente con los campos *added type* dictados bajo `"from script"`. A sí mismo también sus *source type* deberán entrar bajo un estado de ser un `"submitted from admin panel"`. El último recado en este eslabón fue ordenarle a Javier Aparicio clausurar bajo advertencia de uso una computadora del tipo *Windows* muy añeja gracias a las inconsistencias y disrupciones.
- **Configuración del Entorno:** Todo el sector clonó los documentos oficiales a la nube perteneciendo a la rama que contiene `cartis airflow worker`, se ordenó acceder al archivo y panel `content creator at source worker` directamente montado en Visual Studio Code, y consiguientemente procedieron a instalar un bloque oculto y principal conocido como `.env` bajo los cimientos preestablecidos del folder para poder gestionar adecuadamente el entorno configurativo. Como hincapié clave, se destacó el apunte donde exigía borrar por mano un hashtag al margen a un lado que restringía al identificador oficial la activación correcta (model ID habilitado sin el `#`).
- **Problema Descubierto y Diagnóstico (Depuración):** Tristemente y por obvias razones a fallos tempranos en esta sesión, las rutinas se desplomaron. Falló rotundo con la alerta `ModuleNotFoundError`, obligando de manera obvia establecer en ese mismo minuto un escenario digital protegido para asilar módulos (entorno virtual de Python) garantizando la salvaguarda controlada para paquetes y herramientas variadas.
- **Próximos Pasos de Acción Inminentes:** Por disposición general de liderazgos (Jack Doyle) se estructuró a futuro el próximo chequeo del nivel de la tarea en exactamente una cita dictada a la una en la tarde para el día siguiente (`1:00 PM`). Finalmente se empoderó al Sr. Javier Aparicio dejándole bajo encargo urgente empaparse en toda clase de documentación que se le cruce explicando qué en el mundo es un Python Entorno Virtual (venv), cómo se acciona correctamente y cómo inyectar librerías mediante textos de control de masas en un archivo de formato `.txt` con exigencias (`requirements.txt`).

---

## Áreas de Mejora Priorizadas (Feedback a Javier)

Tomaremos todos aquellos errores con atención extra, ya que en la actualidad estas representan nuestra área de crecimiento mayor en ruta.

- [ ] Mejorar la familiaridad navegativa utilizando la Terminal o Consola.
- [ ] Optimizar la agilidad aprovechando fuertemente los atajos del teclado a favor.
- [ ] Incorporación natural e inconsciente en levantar los Entornos Virtuales.
- [ ] Comprendimiento exacto del mundo de los archivos ocultos y variables de Configuración.
- [ ] Flujo lógico al utilizar los servicios y comandos preestablecidos de versionamiento como `Git`.
- [ ] Reforzar la asimilación del espacio gráfico por default en las Interfaces y sus botones.
- [ ] Conocimiento base arquitectónico de Tablas informáticas en un ambiente de Base de datos.
- [ ] La capacidad principal para entrelazar las ideas por pedazos y construir un sistema final funcionando (es decir: Primero clono → Entiendo que sigo en un Entorno y lo aislo en Virtual → para al último de todo, mandar la sentencia de ejecución).
