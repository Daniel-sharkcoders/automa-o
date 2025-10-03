"""Automatizando tarefas com Python
   Aula 2 - programa que abre o paint e usa  lápis para desenhar um quadrado 200 x 200 pixels
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
pyautogui.press("P")  # Seleciona a ferramenta lápis
sleep(1)
pyautogui.click(x=500, y=500)  # Clica na tela do paint
sleep(1)
# Desenha o quadrado
pyautogui.drag(200, 0, duration=0.5)   # Move para a direita
pyautogui.drag(0, 200, duration=0.5)   # Move para baixo
pyautogui.drag(-200, 0, duration=0.5)  # Move para a esquerda
pyautogui.drag(0, -200, duration=0.5)  # Move para cima