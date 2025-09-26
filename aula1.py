"""
    Aula1 - Minha primeira automação
    Autor: Eu mesmo
    Data: 26/09/25
    
"""
import pyautogui

from time import sleep

sleep(5)
pyautogui.moveTo(414,167,duration=0.5)
pyautogui.doubleClick(414,167,interval=0.25)
pyautogui.write("Teste de automação",interval=0.25)
pyautogui.write(" - eu mesmo",interval=0.25)
pyautogui.press("enter")