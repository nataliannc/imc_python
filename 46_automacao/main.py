#instalar biblioteca pip install pyautogui

#importar biblioteca
import pyautogui as auto
import time

auto.PAUSE = 0.5

#abre o menu iniciar
auto.press("win")

#abre o chrome
auto.write("crome")
auto.press("enter")

#maximizar tela
auto.hotkey("alt", "space")
auto.press("enter")

#abre o github
auto.write("github.com")
auto.press("enter")

#abre o classroom, em uma nova guia
time.sleep(3)#abre a segunda aba após 3 segundos
auto.hotkey("ctrl", "t") #hotkley - tecla de atalho
auto.write("classroom.google.com")
auto.press("enter")

#istalar biblioteca pip install cx_Freeze   
#cxfreeze main.py --target-dir nome_da_pasta
