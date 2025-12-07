 #6 Aspect ratio de una imagen
"""
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
"""

# Necesitas instalar dependencias si no las tienes:
# pip install requests pillow

import requests                     # 1
from PIL import Image               # 2
from io import BytesIO              # 3
from math import gcd                # 4

def descargar_imagen(url, timeout=10):  # 5
    """
    Descarga el contenido de la URL y devuelve bytes.
    Lanza requests.exceptions.RequestException si falla.
    """
    resp = requests.get(url, timeout=timeout)  # 6
    resp.raise_for_status()                     # 7
    return resp.content                         # 8

def obtener_dimensiones_desde_bytes(image_bytes):  # 9
    """
    Abre la imagen desde bytes y devuelve (width, height).
    Lanza OSError si los bytes no forman una imagen válida.
    """
    with Image.open(BytesIO(image_bytes)) as img:  # 10
        return img.width, img.height               # 11

def aspect_ratio_simplificado(width, height):     # 12
    """
    Simplifica el ratio usando el máximo común divisor.
    Devuelve una tupla (w_simpl, h_simpl) y el string "w:h".
    """
    if width == 0 or height == 0:                  # 13
        raise ValueError("Ancho o alto inválido (0).") 
    divisor = gcd(width, height)                   # 14
    w_simpl = width // divisor                     # 15
    h_simpl = height // divisor                    # 16
    return (w_simpl, h_simpl), f"{w_simpl}:{h_simpl}"  # 17

def aspect_ratio_from_url(url):                    # 18
    """
    Función de alto nivel: recibe URL, devuelve (width, height), (w_simpl, h_simpl), "w:h".
    """
    imagen_bytes = descargar_imagen(url)           # 19
    width, height = obtener_dimensiones_desde_bytes(imagen_bytes)  # 20
    (w_s, h_s), ratio_str = aspect_ratio_simplificado(width, height) # 21
    return {
        "width": width,
        "height": height,
        "ratio_tuple": (w_s, h_s),
        "ratio_str": ratio_str
    }                                               # 22

if __name__ == "__main__":                         # 23
    url = "https://www.ociocaballo.com/wp-content/uploads/2020/05/articulo_055.jpg"  # 24
    try:
        info = aspect_ratio_from_url(url)          # 25
        print(f"Dimensiones: {info['width']} x {info['height']}")  # 26
        print(f"Aspect ratio: {info['ratio_str']}")               # 27
    except Exception as e:
        print("Error calculando aspect ratio:", e)  # 28
