"""
    Aula1 - Minha primeira automação
    Autor: Eu mesmo
    Data: 26/09/25
"""
import pyautogui

from time import sleep

pyautogui.press("win")
sleep(1)
pyautogui.write("notepad")
sleep(1)
pyautogui.press("enter")
sleep(2)
pyautogui.write("Teste de automação",interval=0.25)
pyautogui.write(" - eu mesmo",interval=0.25)