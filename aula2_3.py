import pyautogui
from time import sleep

pergunta =input("O que deseja pesquisar? ")

pyautogui.press("win")
sleep(1)
pyautogui.write("edge")
sleep(1)
pyautogui.press("enter")
sleep(2)
pyautogui.write(f"{pergunta}", interval=0.25)
sleep(1)
pyautogui.press("enter")
sleep(2)
pyautogui.hotkey("ctrl", "t")
sleep
pyautogui.write("https://www.wikipedia.org/", interval=0.25)
sleep(1)
pyautogui.press("enter")
sleep(2)
pyautogui.click()
sleep(1)

pyautogui.press("tab")
sleep(1)
pyautogui.write(f"{pergunta}", interval=0.25)
