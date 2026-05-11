# `import modulo` trae el módulo completo y se usa con su nombre completo.
# `from modulo import X` trae sólo símbolos concretos del módulo para usarlos directamente.
# Aquí se mezclan ambos estilos según convenga por legibilidad y por la cantidad de elementos que se necesitan.

'''
    Modularizar este codigo
    Separar en partes funcionales, donde cada una cumpla una tarea especifica
    En contraposicion a una arquitectura, donde un solo bloque cumple muchas tareas.
'''

import requests
import tkinter as tk
from tkinter import messagebox, Text, Scrollbar, Label, StringVar, OptionMenu
from collections import OrderedDict
import json
import os
import threading
from concurrent.futures import ThreadPoolExecutor  # <-- NUEVO

# Importar funciones que manipulan URLs con expresiones regulares
from url_updater import extract_urls, increment_url_number, check_url_active, _has_terminal_one, _remove_terminal_one

# Diccionario de páginas de inicio para la verificación de URLs.
# Clave: dominio del cliente.
# Valor: URL de inicio asociada.
homepage_dict = {
    # Ejemplo: "example.com": "https://example.com",
    # Añade aquí otros dominios y sus respectivas páginas de inicio
}

def load_client_libraries(json_path='client_libraries.json'):
    """Carga desde disco el archivo JSON con las URLs por cliente.

    Devuelve un diccionario Python donde cada clave es el nombre de un cliente
    y cada valor es una lista de URLs. Si el archivo no existe, devuelve un
    diccionario vacío para que el resto del flujo siga funcionando.
    """
    if not os.path.exists(json_path):
        return {}
    with open(json_path, 'r') as file:
        return json.load(file)







def update_client_urls(max_workers=8):  # <-- Acepta número de workers
    """Revisa las URLs guardadas por cliente y actualiza el JSON con las que siguen activas.

    max_workers controla cuántas comprobaciones se lanzan en paralelo.
    La función devuelve una lista con las URLs activas detectadas.
    """
    libraries = load_client_libraries()
    # updated_libraries: dict[str, list[str]] con el resultado final por cliente.
    updated_libraries = {}
    # active_urls: lista de strings con las URLs que han pasado la verificación.
    active_urls = []
    # lock: objeto threading.Lock para proteger escrituras concurrentes.
    lock = threading.Lock()

    # ------------------ FUNCIÓN AJUSTADA CON FALLBACK “1” ------------------
    def update_url(url, client_name):
        nonlocal active_urls

        # Primero probamos la URL tal cual viene del JSON.
        active = check_url_active(url)
        with lock:
            print(f"URL: {url}, Activa: {active}")
            if active:
                # Caso 1: la URL original funciona.
                updated_libraries[client_name].append(url)
                active_urls.append(url)
                return

        # Fuera del lock hacemos intentos alternativos para no bloquear el resto de hilos.
        incremented_url = increment_url_number(url)

        if incremented_url and check_url_active(incremented_url):
            with lock:
                # Caso 2: la versión incrementada funciona.
                updated_libraries[client_name].append(incremented_url)
                active_urls.append(incremented_url)
            return

        # Caso 3: fallback sin número, sólo si la URL tenía un “1” terminal.
        if _has_terminal_one(url):
            base_url = _remove_terminal_one(url)
            if base_url != url and check_url_active(base_url):
                with lock:
                    # Guardamos la original en el JSON, pero reportamos la versión sin número como activa.
                    updated_libraries[client_name].append(url)   # guarda la original con 1
                    active_urls.append(base_url)                 # reporta la sin número como activa
                return

        # Caso 4: ninguna variante respondió, así que conservamos la URL original.
        with lock:
            updated_libraries[client_name].append(url)
    # ----------------------------------------------------------------------

    # Ejecutamos las comprobaciones en paralelo con un número limitado de workers.
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for client_name, urls in libraries.items():
            updated_libraries[client_name] = []
            for url in urls:
                executor.submit(update_url, url, client_name)

    # Persistimos el resultado final en disco para que la siguiente ejecución use estos datos.
    with open('client_libraries.json', 'w') as file:
        json.dump(updated_libraries, file, indent=4)

    messagebox.showinfo("Información", "Todas las URLs de clientes han sido revisadas y actualizadas.")
    return active_urls  # Devolver la lista de URLs activos

def main():
    """Construye la interfaz gráfica y conecta los botones con las acciones principales."""
    # root: objeto Tk principal que actúa como ventana base de la aplicación.
    root = tk.Tk()
    root.title("Extractor de URLs")
    root.geometry("550x650")  # Ajuste de tamaño para acomodar todos los controles.

    # label: widget Label de Tkinter con el texto de instrucciones.
    label = tk.Label(root, text="Introduce las URLs (una por línea):")
    label.pack(pady=10)

    # input_text: widget Text donde el usuario pega una o varias URLs.
    input_text = Text(root, wrap=tk.WORD, height=10, width=55)
    input_text.pack(pady=10)

    # scrollbar: widget Scrollbar enlazado con el área de texto.
    scrollbar = Scrollbar(root, command=input_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    input_text.config(yscrollcommand=scrollbar.set)

    # popup_menu: menú contextual para copiar y pegar dentro del Text.
    popup_menu = tk.Menu(root, tearoff=0)
    popup_menu.add_command(label="Copiar", command=lambda: root.focus_get().event_generate('<<Copy>>'))
    popup_menu.add_command(label="Pegar", command=lambda: root.focus_get().event_generate('<<Paste>>'))

    def show_popup(event):
        """Muestra el menú contextual donde se hizo clic derecho."""
        try:
            popup_menu.tk_popup(event.x_root, event.y_root)
        finally:
            popup_menu.grab_release()

    input_text.bind("<Button-3>", show_popup)

    label_filter = tk.Label(root, text="Introduce el filtro para URLs (opcional):")
    label_filter.pack(pady=10)

    # input_filter: entrada de una sola línea para filtrar URLs por texto.
    input_filter = tk.Entry(root, width=55)
    input_filter.pack(pady=10)

    # remove_duplicates_var: variable de control de Tkinter asociada al Checkbutton.
    remove_duplicates_var = tk.IntVar(value=1)
    remove_duplicates_checkbox = tk.Checkbutton(root, text="Filtrar URLs repetidas", variable=remove_duplicates_var)
    remove_duplicates_checkbox.pack(pady=10)

    # Selector de workers para ajustar el nivel de concurrencia.
    workers_label = tk.Label(root, text="Workers (concurrencia):")
    workers_label.pack(pady=5)

    # workers_var: variable numérica vinculada al Spinbox.
    workers_var = tk.IntVar(value=8)  # valor por defecto
    workers_spin = tk.Spinbox(root, from_=1, to=64, textvariable=workers_var, width=6)
    workers_spin.pack(pady=5)

    def extract_and_save():
        """Lee las URLs introducidas, extrae enlaces y guarda el resultado en un TXT."""
        # Convertimos el contenido del widget Text en una lista de strings.
        urls = input_text.get("1.0", tk.END).strip().split("\n")
        filter_text = input_filter.get().strip()
        # all_extracted_urls: lista de resultados acumulados de todas las páginas.
        all_extracted_urls = []

        for url in urls:
            extracted_urls = extract_urls(url, filter=filter_text if filter_text else None)
            all_extracted_urls.extend(extracted_urls)

        if remove_duplicates_var.get():
            all_extracted_urls = list(OrderedDict.fromkeys(all_extracted_urls))

        with open("extracted_urls.txt", "w", encoding="utf-8") as file:
            for link in all_extracted_urls:
                file.write(link + "\n")

        messagebox.showinfo("Información", "URLs extraídas y guardadas en extracted_urls.txt.")

    extract_button = tk.Button(root, text="Extraer URLs", command=extract_and_save, bg='blue', fg='white', font=('Helvetica', 12), height=2, width=20)
    extract_button.pack(pady=20)

    # client_label: etiqueta para seleccionar un cliente existente en el JSON.
    client_label = Label(root, text="Selecciona un cliente para extraer URLs:")
    client_label.pack(pady=10)

    # client_var: StringVar que guarda la opción seleccionada en el menú desplegable.
    client_var = StringVar(root)
    client_var.set("Elige un cliente")
    client_option_menu = OptionMenu(root, client_var, *load_client_libraries().keys(),1)
    client_option_menu.pack(pady=10)

    def extract_client_urls():
        """Extrae URLs sólo del cliente seleccionado y las guarda en un TXT propio."""
        client_name = client_var.get()
        libraries = load_client_libraries()
        if client_name not in libraries:
            messagebox.showerror("Error", "El cliente seleccionado no es válido o no tiene URLs asociadas.")
            return

        # all_extracted_urls reúne todos los enlaces encontrados para ese cliente.
        all_extracted_urls = []
        for url in libraries[client_name]:
            extracted_urls = extract_urls(url, filter=url)
            all_extracted_urls.extend(extracted_urls)

        all_extracted_urls = list(OrderedDict.fromkeys(all_extracted_urls))

        with open(f"{client_name}_extracted_urls.txt", "w", encoding="utf-8") as file:
            for link in all_extracted_urls:
                file.write(link + "\n")

        messagebox.showinfo("Información", f"URLs del cliente '{client_name}' extraídas y guardadas en {client_name}_extracted_urls.txt.")

    extract_client_button = tk.Button(root, text="Extraer URLs del Cliente", command=extract_client_urls, bg='green', fg='white', font=('Helvetica', 12), height=2, width=20)
    extract_client_button.pack(pady=20)

    def show_active_urls_window(active_urls):
        """Abre una ventana secundaria para mostrar las URLs activas detectadas."""
        window = tk.Toplevel(root)
        window.title("URLs Activos")
        window.geometry("400x300")

        scrollbar = tk.Scrollbar(window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        url_list = tk.Text(window, yscrollcommand=scrollbar.set, wrap=tk.WORD, height=15, width=50)
        url_list.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=url_list.yview)

        for url in active_urls:
            url_list.insert(tk.END, url + "\n")

    def update_and_show_active_urls():
        """Actualiza las URLs de clientes y luego muestra el resultado en una ventana."""
        # workers_var.get() devuelve un entero desde el Spinbox.
        active_urls = update_client_urls(max_workers=workers_var.get())
        show_active_urls_window(active_urls)

    update_client_urls_button = tk.Button(root, text="Actualizar y Mostrar URLs Activos", command=update_and_show_active_urls, bg='orange', fg='white', font=('Helvetica', 12), height=2, width=25)
    update_client_urls_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()







