"""Automatizando tarefas com Python
   Aula 2 - programa que abre o paint e usa usar o oval pra desenhar, usar balde e pintar o oval de azul
"""
import pyautogui
from time import sleep

# Abre o paint
pyautogui.press("win")
sleep(1)
pyautogui.write("paint")
sleep(1)
pyautogui.press("enter")
sleep(1)
for i in range(17):
    pyautogui.press("tab")
sleep(1)
for i in range(2):
    pyautogui.press("right")
pyautogui.press("enter")
sleep(2)
# Desenha o oval
pyautogui.moveTo(500, 500)
sleep
pyautogui.dragTo(800, 700, button="left", duration=1)
sleep
for i in range(37):
    pyautogui.press("tab")
    for i in range(4):
        pyautogui.press("right")
sleep(1)
pyautogui.press("enter")
sleep(1)
pyautogui.press("b")
pyautogui.moveTo(650, 600)
sleep(1)
pyautogui.click()
