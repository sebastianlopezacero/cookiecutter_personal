import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m" # To change the terminal color
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith("x"):
    print(f'{ERROR_COLOR}ERROR: {project_slug=} Lo siento, esto no es un nombre valido para la carpeta.{RESET_ALL}')

    sys.exit(1)

print(f"{MESSAGE_COLOR}Listo, empecemos a crear un nuevo proyecto! un paso mas a ser el mejor")
print(f"creando proyecto en { os.getcwd() }{RESET_ALL}")