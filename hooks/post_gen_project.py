import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Vamos lo mas rapido!")
print(f"Iniciando repositorio de GIT...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Primer commit por default'])

print(f"{MESSAGE_COLOR}¡El comienzo de tu destino está definido ahora! ¡Crea y diviértete!{RESET_ALL}")