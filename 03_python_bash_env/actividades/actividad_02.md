# Actividad 2: Tu Primer Repositorio en GitHub (Paso a Paso)

**Objetivo:** Aprender el proceso exacto y minucioso para respaldar tu código local de la carpeta `leccion_01` en internet (GitHub) utilizando la terminal. No asumiremos ningún conocimiento previo de Git.

### Conceptos Clave (Glosario Rápido)
- **Git:** El programa en tu computadora que vigila tus archivos y toma "fotos" (respaldos) seguros de tu código.
- **GitHub:** La página web (nube) donde se guardan esas "fotos".
- **Repositorio (Repo):** Una carpeta que está siendo vigilada y controlada por Git.

---

### Paso 1: Preparar la Receta del Olvido (El archivo .gitignore)

Antes de hacer cualquier foto de nuestro código, debemos enseñarle a Git qué cosas debe ignorar. **NUNCA** debemos subir nuestro entorno virtual (`.venv`) ni nuestros secretos (`.env`) a internet, porque la carpeta `.venv` es muy pesada y un archivo `.env` tiene contraseñas sensibles.

1. Abre tu terminal (Windows, macOS o Linux) y navega a la carpeta de la lección que empezamos antes (`leccion_01`):
   - *Comando (macOS/Linux):* `cd ~/codigo/leccion_01` (o la ruta exacta).
   - *Comando (Windows):* `cd C:\codigo\leccion_01` (o la ruta exacta donde la hayas ensamblado).
2. Crea un archivo llamado `.gitignore` (nota el punto al inicio, es muy importante).
   - *Comando (macOS/Linux):* `touch .gitignore`
   - *Comando (Windows PowerShell):* `Ni .gitignore`
   - *Comando (Windows CMD):* `echo. > .gitignore`
3. Abre este archivo en tu editor de código y escribe adentro exactamente estas dos líneas separadas:
   ```text
   .venv/
   .env
   ```
   *Guarda el archivo y ciérralo.*
   **¿Qué hace esto?:** Le dice a Git: "Por favor, si ves una carpeta llamada .venv y/o un archivo llamado .env, finge que no existen".

---

### Paso 2: Inicializar (Crear) el Repositorio Local

Vamos a convertir nuestra carpeta aburrida en un "Repositorio" inteligente.

1. Asegúrate de seguir en la terminal dentro de `leccion_01`.
2. Ejecuta el comando mágico para despertar a Git:
   - *Comando:* `git init`
   **¿Qué hace esto?:** "Init" viene de inicializar. Este comando crea en secreto una carpeta oculta dentro de la tuya llamada `.git`. A partir de este segundo, Git empieza a monitorizar todos los cambios en este lugar.

---

### Paso 3: Preparar los Archivos en el Escenario (Add)

Git vigila, pero no guarda fotos automáticamente. Tenemos que decirle exactamente qué archivos entrarán en nuestra primera foto grupal. Esta etapa de selección se llama "Stage" (Escenario).

1. Para revisar qué es lo que Git ha notado hasta el momento, pregúntale:
   - *Comando:* `git status`
   **¿Qué hace esto?:** Verás texto de color rojo. Esto significa que hay archivos nuevos (como `main.py` y `requirements.txt`), pero Git te advierte que aún no están listos en el "escenario" de la foto.
2. Dile a Git que ponga TODOS los archivos actuales en el escenario de preparación:
   - *Comando:* `git add .`
   **¿Qué hace esto?:** `add` significa añadir. Y el punto `.` es un comodín de la terminal que significa "Absolutamente todo en esta ruta". Note el espacio entre add y el punto.
3. Vuelve a revisar qué te dice Git ahora:
   - *Comando:* `git status`
   **¿Qué hace esto?:** Ahora verás el texto y los nombres en verde. Esto indica éxito: los archivos están formados y listos para ser guardados en la versión.

---

### Paso 4: Tomar la Foto del Código (Commit)

Tenerlos en el escenario no los guarda. Ahora vamos a sellar la foto con un nombre que describa lo que hicimos hoy.

1. Ejecuta el comando para crear tu historial:
   - *Comando:* `git commit -m "Mi primer commit para la leccion 01"`
   **¿Qué hace esto?:** 
   - `commit` significa comprometer (guardar/efectuar el cambio).
   - `-m` le avisa al sistema que vas a dejar un "mensaje".
   - Todo lo que digite entre las comillas `""` será la descripción humana para leerla fácilmente a futuro.

---

### Paso 5: Renombrar tu "Rama" Principal

En Git, la línea de trabajo principal se llama "rama" (branch). Antes se llamaba 'master', hoy el estándar dictamina que debe llamarse 'main'. Modifiquémoslo de una vez por todas.

1. Ejecuta:
   - *Comando:* `git branch -M main`
   **¿Qué hace esto?:** `branch` maneja las ramas. El parámetro `-M` fuerza a renombrar la rama actual en la que te encuentras posicionado al nombre "main".

---

### Paso 6: Construir el Puente hacia la Nube (GitHub)

El trabajo local finalizó. Para enviar esto a GitHub necesitamos preparar una "caja" directamente en el sitio web de GitHub, y luego conectar tu computadora a esa "caja".

1. Abre el navegador de internet, entra a **[GitHub.com](https://github.com/)**, inicia sesión con tu usuario y contraseña.
2. Haz clic en el botón verde de la izquierda (o esquina superior) que dice **"New"** para montar un nuevo Repositorio remoto.
3. Lo único que llenarás será la sección *Repository name*. Ponle por ejemplo `mi_leccion_01`.
4.  No pulses ninguna otra casilla. Haz clic directamente hasta abajo en el botón verde de **"Create repository"**.
5. GitHub te abrirá una pantalla con código. Identifica la zona que te ofrece un Link o URL (se verá como `https://github.com/TuUsuario/mi_leccion_01.git`). **Copia esa URL**.
6. Retorna otra vez a la terminal donde veníamos trabajando. Vas a ejecutar lo siguiente, sustituyendo URL_COPIADA por tu enlace real:
   
   **NOTA IMPORTANTE: para copiar y pegar en la terminal de Windows/Linux usamos Ctrl + Shift + C y Ctrl + Shift + V. En macOS usamos Cmd + C y Cmd + V.** 
   - *Comando:* `git remote add origin URL_COPIADA`
   **¿Qué hace esto?:**
   - `remote` declara que configuraremos un servidor de internet remoto.
   - `add` suma la información a tus ajustes.
   - `origin` es un apodo. Git llama 'origin' (origen) a la URL de forma tradicional para que a ti no te toque escribir esa url mega larga nunca más en el futuro, sólo su apodo.

---

### Paso 7: Empujar tu Código Hacia Arriba (Push)

El puente existe, pero todavía no transitó nada hacia arriba. Hagamos que viajen los archivos.

1. Empuja tu código local hacia la internet con el siguiente comando final:
   - *Comando:* `git push -u origin main`
   **¿Qué hace esto?:**
   - `push` en inglés es empujar. Arroja lo propio al servidor en la nube.
   - `-u` significa de "upstream"; le ordenas a Git que recuerde eternamente que tú (la rama main), dependes de GitHub (origin), así en tu trabajo del día de mañana, usarás un comando corto.
   - `origin` al destino adonde vas a empujar todo de la nube.
   - `main` la rama local de tu PC que estás enviando.
2. *(Nota: Si es tu primera vez, el sistema va a abrir una miniventana en el navegador o terminal pidiendo que autorices la sesión en GitHub o pongas tus credenciales. Sigue los pasos y dale Aceptar/Login).*
3. ¡Ve a tu repositorio en el navegador de internet y recarga la pestaña! Todos los archivos de tu consola ahora deberían verse en la nube permanentemente protegidos.
