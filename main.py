import subprocess
import time

lista_antiga = []
lista_nova = []
atualizar_antiga = False
commitar = False

while True:
    print("Waiting for change!")
    if commitar:
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", '"a"'])
        subprocess.run(["git", "push", "-u", "origin", "main"])
        commitar = False
    if atualizar_antiga:
        lista_antiga = open("minha_lista.m3u", "r").read()
        atualizar_antiga = False

    lista_nova = open("minha_lista.m3u", "r").read()
    if lista_nova != lista_antiga:
        atualizar_antiga = True
        commitar = True
