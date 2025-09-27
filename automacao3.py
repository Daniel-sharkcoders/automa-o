import pyautogui
from time import sleep

n1 = float(input("Qual o primeiro numero? "))

n2 = float(input("qual o segundo numero? "))

sinal = input("qual o sinal da conta?(+, -, *, /)")

SEPARADOR_DECIMAL = ','

def digitar_numero_na_calculadora(numero_float, separador):
    """Converte um float numa string com o separador correto e digita-o."""
    
    # 1. Converter para string e limitar casas decimais (opcional)
    # Aqui, convertemos o float para uma string com 4 casas decimais para manter a precisão
    string_com_ponto = f"{numero_float:.4f}" 
    
    # 2. Substituir o ponto (padrão do Python) pelo separador desejado
    string_final = string_com_ponto.replace('.', separador)
    pyautogui.typewrite(string_final)
    sleep(0.5)

pyautogui.press("win")

pyautogui.write("calculadora")
pyautogui.press("enter")
sleep(0.5)

digitar_numero_na_calculadora(n1, SEPARADOR_DECIMAL)
pyautogui.press(sinal)
digitar_numero_na_calculadora(n2, SEPARADOR_DECIMAL)
pyautogui.press("enter")
