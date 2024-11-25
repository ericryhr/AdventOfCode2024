import os
import requests
from dotenv import load_dotenv
import sys

load_dotenv()

def descargar_input(dia, sesion):
    url = f"https://adventofcode.com/2024/day/{dia}/input"
    respuesta = sesion.get(url)
    if respuesta.status_code == 200:
        return respuesta.text
    else:
        raise Exception(f"Error al descargar el input: HTTP {respuesta.status_code}")


def crear_main_py(dia):
    ruta_template = "template.py"
    ruta_destino = f"day{dia}/main.py"

    with open(ruta_template, 'r') as file:
        contenido = file.read()

    contenido = contenido.replace("Day:", f"Day: {dia}")
    contenido = contenido.replace("input.txt", f"day{dia}/input.txt")

    with open(ruta_destino, 'w') as file:
        file.write(contenido)


def main(dia, sesion):
    carpeta_dia = f"day{dia}"
    if not os.path.exists(carpeta_dia):
        os.makedirs(carpeta_dia)

    crear_main_py(dia)

    archivo_input = os.path.join(carpeta_dia, "input.txt")
    with open(archivo_input, "w") as f:
        f.write(descargar_input(dia, sesion))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <dia>")
        sys.exit(1)

    dia = sys.argv[1]
    sesion = requests.Session()

    session_cookie = os.getenv('SESSION_COOKIE')

    # Aquí agregas la cookie de sesión
    sesion.cookies.set('session',
                       session_cookie) #Put your cookie here

    main(dia, sesion)
