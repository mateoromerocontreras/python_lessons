# Actividad 3: Ramas, Pull Requests y Trabajo Colaborativo en Git

**Objetivo:** Introducirte profundamente en el flujo de trabajo moderno en Git para crear nuevas características y líneas de código de manera ágil sin romper el código que ya funciona. Aprenderás a transitar entre versiones locales y remates (la Nube).

---

### Conceptos Clave Básicos
Antes de iniciar los comandos, comprendamos las analogías detrás de ellos:
- **Commit:** Una "fotografía" fiel y permanente o punto de guardado en la historia de tu código en el tiempo.
- **Push:** "Empujar" o enviar todos tus commits desde tu computadora local directamente hacia el servidor en la nube (tu GitHub).
- **Pull:** "Halar", jalar o buscar y descargar todas las últimas actualizaciones y cambios desde la nube hacia tu computadora.
- **Rama (Branch):** Considera a una rama como un "universo paralelo". Tomas una fotocopia exacta de los archivos en ese instante, en ella puedes destruir y reparar a gusto trabajando de manera asilada y prudente, totalmente apartado del tronco principal seguro (normalmente la rama `main`).

**¿Es lo mismo aceptar una Pull Request que hacer un Merge?**
- **No son lo mismo.**
  - Un **Pull Request (PR)**: Representa el lado burocrático y formal en GitHub ("Oigan líder y equipo de proyecto, he diseñado estos cambios útiles en mi rama de código. ¿Creen que puedan hacerles una revisión por favor y considerar que pasen a formar parte del proyecto oficial?"). 
  - Un **Merge**: Es simplemente fusionar o juntar las dos líneas de carpetas a nivel técnico. Se puede originar un Merge local desde tu terminal sin jamás tener que abrir ninguna PR; aun así, al dar click definitivo en aceptar una Pull Request por la plataforma tu recompensa final es ser agraciado por ese famoso *Merge* entre ramas de parte de GitHub.

---

### Paso 1: Crear nuestra Primera Rama de Desarrollo Alterna

En la profesionalidad de uso constante no reescribimos nada directo desde `main`, debemos de ir a transitar sobre una rama hija.

1. Abre tu terminal e insértate dentro del proyecto de forma adecuada `codigo/leccion_01`. *(Recuerda que en Windows/Linux para pegar puedes usar Ctrl+Shift+V y en macOS Cmd+V)*.
2. Construye tu rama de la siguiente forma indicando creación y transporte unificado:
   - *Comando:* `git checkout -b modificando-archivos`
   **¿Qué hace esto?:** La palabra `checkout` indica traslados entre divisiones en tu git. Añadiendo el sufijo `-b` garantizas una orden de crear la rama obligatoriamente si es la primera vez que se visita ese nombre.

---

### Paso 2: Construir un Edificio Diferente en nuestro Mundo (Programación Python)

1. En tu terminal o en tu programa del visualizador local de sistema, pon en obra negra un nuevo archivo que vas a llamar de nombre como gustes, ejemplo: `saludos.py`.
   - *Comando (macOS/Linux):* `touch saludos.py`
   - *Comando (Windows PowerShell):* `Ni saludos.py`
   - *Comando (Windows CMD):* `echo. > saludos.py`
2. Entra en su panel por el editor y aliméntalo reescribiendo la siguiente función. No olvides apretar Ctrl+S (o Cmd+S en macOS) o buscar cómo "Guardar" ese progreso en tu software del editor.
   ```python
   def saludar_alumno(nombre):
       print(f"¡Hola {nombre}, este es tu mensaje viajando desde una nueva rama hija!")

   if __name__ == "__main__":
       saludar_alumno("Desarrollador Top")
   ```
3. *(Opcional)* Transfórmate el panorama y también entra al histórico archivo viejo para esta lección (`main.py`) que creaste en tu anterior actividad, edítalo e inclúyele un agregado fácil de línea a tu elección cómo: `print("Mi programa acaba de evolucionar en dos ramas")`. Guárdalo.

---

### Paso 3: Guardar el Código en Cápsulas (Añadir a Scene y Hacer Commit)

Debemos blindarlos por fotografía si vamos a querer empujarlos.

1. Averigua qué de nuevo capturó tu radar:
   - *Comando:* `git status`
   *(Verás ahora texto en rojo apuntando al archivo nuevo `saludos.py`, además de los cambios actualizados sobre `main.py`).*
2. Agrega esos cambios íntegros todos de golpe al Escenario *(Stage)* que lo subirá.
   - *Comando:* `git add .`
3. Formaliza la documentación que acabamos de meter al camión de carga.
   - *Comando:* `git commit -m "Se añade archivo modular saludos.py y pequeña modernización extra sobre main.py"`

---

### Paso 4: Transportar a la Nube (Un Push Hacia a Lo Desconocido)

Vamos a intentar trasladarlos hasta tu GitHub nube. Notarás un peculiar fenómeno porque en la red mundial aún no existen rumbos nombrados `modificando-archivos`.

1. Ensambla y eleva tú mismo tu primera línea de subida. Tendrás que decirle hacia a qué lugar mandarlo de manera muy técnica (Sólo es en esta primera vez particular al existir).
   - *Comando:* `git push -u origin modificando-archivos`
   **¿Qué significa -u?:** `Upstream`. Lo obligas a memorizar en la base de datos interna la conexión de modo de lograr usar sencillamente a futuro puro `git push`.

---

### Paso 5: Comprobar las Diferencias Universales (En la Máquina vs Por Internet)

Certifiquemos visualmente tu asilo y protección frente a roturas.

**A. Analizándolo dentro de tu Editor PC**
1. Realiza el salto y aterriza de regreso a posicionarte en el entorno general `main`.
   - *Comando:* `git checkout main`
2. Ve corriendo y abre rápido tu editor para escanear y visualizar el índice natural y explorador de los ficheros del panel. **¡Desapareció nuestro Python de saludos y las mejoras cayeron al pasado antiguo!**. Sin sustos; git ocultó tu historial ya que nunca fueron producidos jamás desde allá adentro de acuerdo con su bitácora.
3. Puedes regresar la historia tecleando nuevamente:
   - *Comando:* `git checkout modificando-archivos`

**B. Analizándolo desde un Navegador Web (Chrome/Safari/Edge)**
1. Ve a pasearte sobre el sitio de tu repositorio por internet de [GitHub.com](https://github.com/).
2. Apretando un botón gris sutil posicionado frente al marco arriba por el centro inferior rotulado indicándote claramente encontrarse situado en "`main`" en lista de opciones (tu selector manual de Ramas).
3. Selecciona pulsar encima de a la que nombraste `modificando-archivos`. Fíjate que al actualizarte los índices todos tus archivos extras si brotan mágicos en el instante.

---

### Paso 6: Elevar un Pull Request de Petición y Proceder con su Aceptación por Fusión (Merge)

1. Cámbiate a un panel más allá ingresando por **GitHub.com** sobre este mismo repositorio de nueva cuenta principal.
2. Si notas bien, en grande la Inteligencia automática de GitHub te desplega casi imperativo ahora arriba un recuadro un tanto verde de advertencias. Éste anuncia "**modificando-archivos had recent pushes...**" al unísono de empujar el encuadre final botonial con leyenda al ladito verde vivo que te dice **"Compare & pull request"**. *Písalo de inmediato.*
   - *(En caso de faltar esta leyenda visual ingresa a la pestaña "Pull requests" manualmente e incorpora pinchando en tu botón verde que figura la palabra: **"New pull request"**).*
3. Una hoja general y final emerge cargando todas tus discrepancias rojas o marcadas como ganancias verdes. Te deja firmar una leyenda como tú mismo el Creador Solicitando formal el pedimento en tu Título general del pedido. Haz rodar al fin oprimiendo tu recuadro de la solicitud final **"Create pull request"**.

*Se ha levantando frente ante tus oficinas un requerimiento digital muy serio.*

4. Aceptación tuya. (Ese papel "Juez" o "Tester Code Revisor" y "Supervisor de Garantía" será tuyo por estos días). Aclara tus pensamientos, sitúate en los zapatos de calidad. Haz un pequeño "Scroll" dirigiéndote allá en la zona inferior de tu pantalla de PRs abiertas hasta conseguir apuntalar fijamente tu flecha frente en al gran recuadro brillante en color césped o pasto marcado al final leyendo como: **"Merge pull request"**.
5. Finaliza en ese cuadro apretando por un rotundo **"Confirm merge"**.   

---

### Paso 7: La Cosecha (Halar el Crecimiento hacia Casa con un Pull)

Llegado al Merge oficial con victoria el avance germinó dentro del árbol general. ¡PERO ALERTA!, La memoria en físico real del equipo tuyo se encuentra aún varada muy vieja atrás del periodo con el Main original simple sin mutar.

1. Adéntrate por lo final asomándote a tu Consola.
2. Exígele tu relocalización obligada brincando hacia adentrarte de cuerpo en el terreno plano antiguo:
   - *Comando:* `git checkout main`
3. Arrastra las bonanzas o modificaciones ganadas usando la cuerda o la línea "haladora" (`pull`) extraídas puramente recién forzadas en GitHub.
   - *Comando:* `git pull`
4. Observa fijamente nuevamente en tu editor visual el área global. Tus creaciones que antes sólo lograste plasmar renegado afuera por medio de tu otra versión clonada local (Como ese `saludos.py`) se inocularon finalmente con un éxito apabullante dentro del corazón primario en el proyecto. 
Todo logró alinearse con la nube. Felicidades Señor, has sido graduado exitosamente de Git.
