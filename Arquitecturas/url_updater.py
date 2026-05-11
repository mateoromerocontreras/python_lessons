"""
Módulo de utilidades para actualización y validación de URLs.

Contiene funciones especializadas en manipulación de URLs usando expresiones regulares,
extracción de enlaces de páginas web y verificación de disponibilidad de URLs.
"""

import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# ============================================================================
# PATRONES REGEX COMPILADOS
# ============================================================================

# Expresión regular para detectar paginación en URLs como page-2, p2, next-3 o c4.
PAGINATION_REGEX = re.compile(
    r'(?:(?:page|p|next|c)[-_/]?)(\d+)',
    re.IGNORECASE
)

# Patrón para detectar URLs que terminan con "-1" en el último segmento.
_ONE_SUFFIX_RE = re.compile(r'-1(?:/)?$')

# Patrón para detectar URLs que comienzan el último segmento con "1-".
_ONE_PREFIX_RE = re.compile(r'/1-([^/]+)(?:/)?$')

# ============================================================================
# FUNCIONES DE EXTRACCIÓN Y PARSING
# ============================================================================

def extract_urls(link, filter=None):
    """Extrae enlaces de una página y sigue la paginación cuando la detecta.

    Recorre una página web, extrae todos los enlaces encontrados y continúa
    navegando automáticamente a las siguientes páginas si detecta un patrón
    de paginación en las URLs.

    Parameters:
        link (str): URL inicial a analizar.
        filter (str | None): Texto opcional que debe aparecer en la URL final.

    Returns:
        list[str]: Lista con las URLs encontradas.
    """
    # all_urls: lista de strings con los enlaces encontrados.
    all_urls = []
    # visited_links: conjunto de strings para evitar bucles de navegación.
    visited_links = set()
    # current_page: string con la URL que se está procesando en este momento.
    current_page = link
    # page_number: entero que ayuda a detectar avance en páginas numeradas.
    page_number = 1

    # Bucle principal: sigue navegando mientras haya una página nueva por visitar.
    while current_page and current_page not in visited_links:
        try:
            visited_links.add(current_page)
            response = requests.get(current_page, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Recorremos todos los enlaces HTML <a> de la página.
            for a in soup.find_all('a', href=True):
                href = a['href']
                # urljoin convierte enlaces relativos en URLs absolutas.
                absolute_url = urljoin(current_page, href)
                if not filter or filter in absolute_url:
                    all_urls.append(absolute_url)

            # Intentamos encontrar el siguiente enlace de paginación.
            next_page_link = None
            for a in soup.find_all('a', href=True):
                href = a['href']
                # Si el enlace parece una página posterior, seguimos el recorrido.
                match = PAGINATION_REGEX.search(href)
                if match:
                    next_page_num = int(match.group(1))
                    if next_page_num > page_number:
                        next_page_link = urljoin(current_page, href)
                        page_number = next_page_num
                        break

            current_page = next_page_link

        except requests.exceptions.Timeout:
            print(f"Timeout al intentar acceder a la URL: {current_page}")
        except requests.exceptions.RequestException as e:
            print(f"Error de solicitud al acceder a la URL: {current_page} - {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    return all_urls

# ============================================================================
# FUNCIONES DE MANIPULACIÓN DE NÚMEROS EN URLs
# ============================================================================

def increment_url_number(url):
    """Incrementa el número encontrado al final o antes de un guion en la URL.

    Se usa como intento de navegación automática cuando una URL parece tener
    una versión siguiente basada en numeración. Intenta dos patrones:
    1. Números antes de un guion y palabra (ej: 1-khala-mite -> 2-khala-mite)
    2. Números al final o antes del cierre (ej: page/1 -> page/2)

    Parameters:
        url (str): URL a incrementar.

    Returns:
        str | None: URL incrementada o None si no se encontró ningún número.
    """
    # Primer intento: busca números antes de un guion seguido de caracteres de palabra.
    match = re.search(r'(\d+)(?=-\w+)', url)
    if match:
        start, end = match.span()
        number = int(match.group())
        incremented_url = url[:start] + str(number + 1) + url[end:]
        print(f"URL original: {url}, URL incrementada: {incremented_url}")
        return incremented_url

    # Segundo intento: busca números al final o antes de una barra diagonal.
    match = re.search(r'(\d+)(?=/|$)', url)
    if match:
        start, end = match.span()
        number = int(match.group())
        incremented_url = url[:start] + str(number + 1) + url[end:]
        print(f"URL original: {url}, URL incrementada: {incremented_url}")
        return incremented_url

    print(f"No se pudo incrementar la URL: {url}")
    return None

# ============================================================================
# FUNCIONES DE VALIDACIÓN DE URLs
# ============================================================================

def check_url_active(url):
    """Comprueba si una URL responde correctamente con estado HTTP 200.

    También detecta ciertas redirecciones hacia la raíz del dominio para evitar
    marcar como activas páginas que realmente redirigen a una home genérica.

    Parameters:
        url (str): URL a verificar.

    Returns:
        bool: True si la URL responde con código 200 y no redirige a la raíz,
              False en caso contrario.
    """
    try:
        response = requests.get(url, allow_redirects=True, timeout=10)
        # final_url es la URL a la que terminó respondiendo el servidor.
        final_url = response.url.rstrip('/')
        # original_url conserva la URL pedida, normalizada sin barra final.
        original_url = url.rstrip('/')

        print(f"Verificando URL: {url}, Redirige a: {final_url}, Código de estado: {response.status_code}")

        if final_url != original_url:
            # Si la redirección llega solo a la raíz del dominio, la tratamos como no activa.
            domain = re.findall(r'https?://(www\.)?([^/]+)', final_url)[0][1]
            if final_url == f'https://{domain}' or final_url == f'http://{domain}':
                return False

        return response.status_code == 200
    except requests.ConnectionError:
        return False
    except requests.Timeout:
        return False
    except requests.RequestException:
        return False

# ============================================================================
# FUNCIONES HELPER PARA DETECCIÓN Y ELIMINACIÓN DE SUFIJO "1"
# ============================================================================

def _has_terminal_one(url: str) -> bool:
    """Detecta si la URL termina con un patrón de "1" en el último segmento.

    Se usa para identificar casos como:
    - /khala-mite-1/  (sufijo -1)
    - /1-khala-mite/  (prefijo 1-)

    Parameters:
        url (str): URL a analizar.

    Returns:
        bool: True si la URL tiene el patrón de "1" terminal, False en caso contrario.
    """
    return bool(_ONE_SUFFIX_RE.search(url) or _ONE_PREFIX_RE.search(url))

def _remove_terminal_one(url: str) -> str:
    """Elimina sólo el "1" terminal del último segmento, conservando barra final si existía.

    Maneja dos casos:
    1. Sufijo -1: /khala-mite-1/  -> /khala-mite/
    2. Prefijo 1-: /1-khala-mite/  -> /khala-mite/

    Parameters:
        url (str): URL con potencial sufijo o prefijo "1".

    Returns:
        str: URL sin el patrón de "1" terminal, o la original si no se encontró.
    """
    # Sufijo -1 al final del segmento
    m = _ONE_SUFFIX_RE.search(url)
    if m:
        return _ONE_SUFFIX_RE.sub(lambda s: '/' if url.endswith('/') else '', url)

    # Prefijo 1- al comienzo del último segmento
    m = _ONE_PREFIX_RE.search(url)
    if m:
        return _ONE_PREFIX_RE.sub(lambda s: f"/{m.group(1)}" + ('/' if url.endswith('/') else ''), url)

    return url
