import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        print(f'Coordenadas do rato: X={x} Y={y}', end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print('\nPrograma terminado.')