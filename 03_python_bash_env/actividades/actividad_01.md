# Actividad 1: Supervivencia en la Terminal (Windows / macOS / Linux) y Entornos Virtuales

**Objetivo:** Poner en práctica los conocimientos fundamentales sobre navegación de terminal, revisión de instalaciones globales (Git y Python), creación de entornos virtuales, y gestión de dependencias y ejecución de scripts.

---

### Ejercicio 1: Dominando la Terminal

Vamos a afianzar tu habilidad para moverte ágilmente a través de las carpetas usando tu consola. Utilizaremos los comandos adecuados según tu sistema operativo.

1. **Paso 1:** Abre tu terminal. Averigua dónde estás posicionado ahora mismo.
   - *Comando (macOS/Linux):* `pwd`
   - *Comando (Windows PowerShell):* `pwd`
   - *Comando (Windows CMD):* `cd` sin argumentos o `echo %cd%`
2. **Paso 2:** Navega hasta la raíz de tu disco principal, por ejemplo, al directorio central de `C:\` o al directorio *Home* `~`.
   - *Comando (macOS/Linux):* `cd ~` o `cd /`
   - *Comando (Windows):* `cd C:\`
3. **Paso 3:** Crea un directorio principal para tus desarrollos llamado `codigo`.
   - *Comando:* `mkdir codigo`
4. **Paso 4:** Entra al directorio que acabas de crear.
   - *Comando:* `cd codigo`
5. **Paso 5:** Crea otra carpeta directamente ahí adentro llamada `carpeta_temporal`.
   - *Comando:* `mkdir carpeta_temporal`
6. **Paso 6:** Lista el contenido actual del directorio para verificar que la carpeta existe.
   - *Comando:* `dir` (o `ls` en PowerShell)
7. **Paso 7:** Ahora procede a eliminar la carpeta `carpeta_temporal`.
   - *Comando (macOS/Linux):* `rm -r carpeta_temporal`
   - *Comando (Windows PowerShell):* `rm -r carpeta_temporal`
   - *Comando (Windows CMD):* `rmdir carpeta_temporal`
8. **Paso 8:** Crea una carpeta nueva que utilizarás para la lección de hoy, nombrada `leccion_01`.
   - *Comando:* `mkdir leccion_01`
9. **Paso 9:** Por último entra a tu nueva carpeta.
   - *Comando:* `cd leccion_01`

---

### Ejercicio 2: Verificación de Herramientas y Aislamiento de Proyecto

Antes de construir el entorno virtual, vamos a asegurarnos de que la computadora tiene lo que necesitamos para trabajar de manera adecuada.

1. **Paso 1:** Comprueba la versión de Python que tienes en tu máquina global.
   - *Comando (macOS/Linux):* `python3 --version`
   - *Comando (Windows):* `python --version`
   *(Deberías recibir un texto como 'Python 3.11.x' o similar).*
2. **Paso 2:** Verifica que la herramienta de control de versiones (Git) funciona y está instalada.
   - *Comando:* `git --version`
   *(Debería arrojar 'git version 2.x.x' o relacionado).*
3. **Paso 3:** Teniendo todo alineado, ahora crea tu entorno virtual local en esta carpeta y llámalo `.venv`. 
   - *Comando (macOS/Linux):* `python3 -m venv .venv`
   - *Comando (Windows):* `python -m venv .venv`
4. **Paso 4:** **Activa** tu entorno virtual recién creado usando la sintaxis particular de tu sistema operativo.
   - *Comando (macOS/Linux):* `source .venv/bin/activate`
   - *Comando (Windows PowerShell):* `.\.venv\Scripts\Activate.ps1`
   - *Comando (Windows CMD):* `.\.venv\Scripts\activate`
5. **Paso 5:** Verifica y asegúrate observando que, antes de la ruta en tu consola, ahora aparece el indicador visual del entorno activado `(.venv)`.
6. **Paso 6:** Corrobora que estás utilizando el Python aislado y no el global.
   - *Comando (macOS/Linux):* `which python3` o `which python`
   - *Comando (Windows):* `where python` 
   *(La ruta principal listada debería ser la de la carpeta local, como `.venv/bin/python` o `.venv\Scripts\python.exe`, y no otra principal de tu Sistema).*

---

### Ejercicio 3: Ejecución de Scripts y Dependencias

Veremos cómo generar y solucionar el error más común que experimentan los desarrolladores con los paquetes.

1. **Paso 1:** Crea un script nuevo de Python llamado `main.py` vacio inicialmente.
   - *Comando (macOS/Linux):* `touch main.py`
   - *Comando (Windows PowerShell):* `Ni main.py`
   - *Comando (Windows CMD):* `echo. > main.py`
2. **Paso 2:** Abre el archivo `main.py` usando tu editor preferido (VS Code, etc). Escribe el siguiente código y **guárdalo**:
   ```python
   import colorama
   
   print(colorama.Fore.GREEN + "¡Hola terminal! Mi entorno está configurado correctamente en mi sistema operativo.")
   print(colorama.Style.RESET_ALL)
   ```
3. **Paso 3:** De regreso en la terminal, ejecuta tu aplicación.
   - *Comando (macOS/Linux):* `python3 main.py` (o `python main.py`)
   - *Comando (Windows):* `python main.py`
4. **Paso 4:** Te encontrarás con un fallo, porque la librería de colores (`colorama`) no viene instalada en Python por defecto, y estamos en un entorno limpio. Aprende a leer el `ModuleNotFoundError: No module named 'colorama'`.
5. **Paso 5:** Haz la instalación correspondiente con pip para solventar el error.
   - *Comando (macOS/Linux):* `pip3 install colorama` (o `pip install colorama`)
   - *Comando (Windows):* `pip install colorama`
6. **Paso 6:** Inténtalo de nuevo, vuelve a ejecutar el código una vez finalice la descarga.
   - *Comando (macOS/Linux):* `python3 main.py` (o `python main.py`)
   - *Comando (Windows):* `python main.py`
   *(Se debería ver el texto con colores directamente sobre el terminal).*
7. **Paso 7:** Congela y comparte las dependencias para futuras referencias con el comando `pip freeze` redirigido a un archivo de texto.
   - *Comando (macOS/Linux):* `pip3 freeze > requirements.txt` (o `pip freeze > requirements.txt`)
   - *Comando (Windows):* `pip freeze > requirements.txt`
8. **Paso 8:** Visualiza la receta de ingredientes dentro de la misma terminal o lee sus líneas para comprobar.
   - *Comando (macOS/Linux):* `cat requirements.txt`
   - *Comando (Windows PowerShell):* `cat requirements.txt`
   - *Comando (Windows CMD):* `type requirements.txt`

---

### Ejercicio 4: Uso de Archivos de Configuración .env

La información sensible debe resguardarse cuidadosamente y nunca quedarse atada en bloque con resto del código generalizado.

1. **Paso 1:** En la interfaz de tu editor o consola crea un archivo oculto designado como `.env` dentro de `leccion_01`.
2. **Paso 2:** En él depositarás los secretos. Ábrelo y genera tu primera variable pero envuélvela como comentario para silenciarla utilizando de prefijo el comodín de comentario hashtag.
   ```env
   # GITHUB_TOKEN=este_es_un_secreto_que_no_se_sube_al_repo
   ```
   *Guarda el archivo.*
3. **Paso 3:** Imita ser la librería lectora en producción y quita el hashtag `#` a tu código para proceder al descomentado. El archivo lucirá limpio de la siguiente manera:
   ```env
   GITHUB_TOKEN=este_es_un_secreto_que_no_se_sube_al_repo
   ```
   *Guarda los cambios nuevamente.*

---

### Ejercicio 5: Limpieza General de Estación

El orden es fundamental antes de abandonar toda área de trabajo. 

1. **Paso 1:** Apaga este ambiente aislado de software desactivando para recuperar el Python de todo el esquema tradicional.
   - *Comando:* `deactivate`
2. **Paso 2:** Observa atentamente que el marcador `(.venv)` dejó de mostrarse al inicio.
3. **Paso 3:** Mueve tu ubicación retrocediendo una dimensión (un nivel de carpeta hacia arriba) en la consola y verifica.
   - *Comando:* `cd ..`

¡Felicidades! Haber interiorizado todos estos pasos es la meta perfecta para ser más productivo y un desarrollador más seguro cada día.
