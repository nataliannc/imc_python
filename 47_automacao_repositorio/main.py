"""
Crie um programa de automação que crie um repositório local e envie para um repositório remoto do GitHub indicado pelo usuário. Ao terminar, gere um executável e envie.
"""

import pyautogui as auto
import time

repositorio = input("Escreva o nome do repositório que você deseja criar:")

auto.PAUSE = 0.5

auto.press("win")
auto.write("cmd")
auto.press("enter")

auto.hotkey("ctrl", "j")
auto.write(f"mkdir {repositorio}")
auto.press("enter")
auto.write("exit")
auto.press("enter")

auto.write("git add .")
auto.press("enter")
auto.write("git commit -m 'versão 1.0'")
auto.press("enter")
auto.write("git push")