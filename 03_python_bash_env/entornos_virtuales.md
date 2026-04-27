# Entornos Virtuales en Python: Aislamiento y Gestión de Proyectos

## 1. El Proceso de Creación
El entorno virtual es, físicamente, una carpeta. El comando `venv` copia el ejecutable de Python a esa carpeta para que funcione de forma autónoma.

- **Comando base:** `python -m venv <nombre_del_entorno>`
- **Convención:** Casi todo el mundo lo llama `venv`, `.venv` o `env`.
- **Ejemplo:** 
  ```bash
  python -m venv .venv
  ```

## 2. Activación y Verificación
La activación le dice a tu terminal: *"Oye, a partir de ahora, cuando escriba `python`, no uses el del sistema global, usa el que está dentro de esta carpeta"*.

### Comandos de activación:
- **Windows (PowerShell):** `.\.venv\Scripts\Activate.ps1`
- **Windows (CMD):** `.\.venv\Scripts\activate`
- **macOS / Linux:** `source .venv/bin/activate`

### ¿Cómo verificar que está activo?
1. **El indicador visual:** Verás el nombre del entorno entre paréntesis al principio de tu línea de comandos, ejemplo: `(.venv) C:\Proyectos\MiApp> `.
2. **El comando de ruteo:**
   - En Windows: escribe `where python`
   - En Mac/Linux: escribe `which python`
   
   *Resultado esperado:* La ruta devuelta debe apuntar a la carpeta interna de tu proyecto, y nunca a lugares globales como `C:\Python312` o `/usr/bin/python`.

## 3. Desactivación (Salir del entorno)
Es el proceso más sencillo. No importa en qué carpeta estés parado, simplemente escribe la siguiente palabra y presiona Enter:

```bash
deactivate
```
Esto restaura las variables de entorno de tu terminal a su estado global original.

---

## 4. Gestión de Dependencias

### El rol de pip
`pip` es el instalador oficial de paquetes de Python. Su trabajo es conectarse a un repositorio público en internet llamado [PyPI](https://pypi.org/) (Python Package Index), descargar la librería que hayas pedido y guardarla directamente adentro de la carpeta reservada para tu entorno virtual.

### ¿Qué es requirements.txt?
Es la "receta de cocina" de tu proyecto. Es un archivo de texto simple que enumera todas las librerías externas y de qué versiones numéricas exactas depende tu código para lograr ejecutarse bien. Sin este archivo, otra persona (o tú mismo probándolo dentro de otro servidor) no sabría qué instalar.

- **Para crear el archivo automáticamente:** Una vez que tengas tus librerías instaladas bajo tu entorno virtual, ejecutas el siguiente comando que listará todo lo que tienes y lo arrojará hacia un archivo:
  ```bash
  pip freeze > requirements.txt
  ```
  *(Esto efectivamente "congela" tus versiones actuales en el documento).*

### Cómo instalar las dependencias del proyecto
Si recibes un proyecto externo que acabas de descargar (por ejemplo, bajado de tu colega o clonado de GitHub) y ves que trajo un archivo `requirements.txt`, no te pones a buscar o adivinar instalando las librerías una por una. Únicamente sigues estos pasos:

1. Creas tu entorno virtual.
2. Abres terminal y lo activas.
3. Ejecutas un comando para leer la receta de golpe:
   ```bash
   pip install -r requirements.txt
   ```
Este comando revisará cada renglón del archivo y lo descargará todo de un solo tirón.

> 💡 **Un consejo para el ecosistema Asset Management (y en la industria general)**
>
> En el mundo financiero, la reproducibilidad y estabilidad es ley. Si un algoritmo de predicción y cálculo de riesgo funciona bien en tus pruebas de hoy, debe funcionar exactamente con las mismas ecuaciones dentro de un año. Por eso es que en los archivos `requirements.txt` casi siempre verás **versiones fijadas** como `Django==5.0.4` en lugar de una palabra simple como solo `Django`. Esto se hace para evitar que una actualización del creador reescriba la lógica que altere los resultados a medias.
