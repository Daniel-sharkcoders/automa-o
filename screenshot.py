import flet as ft
import pyautogui as pg
from time import sleep
import datetime

# Função principal do app Flet
def main(page: ft.Page):
    page.title = "Screenshot App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#EAEBED"
    page.window.height = 500
    page.window.width = 400
    page.window.resizable = False
    page.window.maximizable = False

    #função sreenshot
    def screenshot(e):
        sleep(2)
        for i in range(int(repetir.value)): #loop para repetir o  sreenshot a quantidade de vezes que o usuario pedir
            sleep(int(tempo.value))
            z = datetime.datetime.now()
            z = int(z.timestamp())
            z = "IMG_" + str(z)
            screenshot = pg.screenshot(region=(0, 0, int(x.value), int(y.value)))
            screenshot.save(z + ".png")
        

    repetir = ft.TextField(hint_text="Quantas vezes quer repetir o screenshot?", color="#006989", border_color="#A3BAC3")

    tempo = ft.TextField(hint_text="Qual o intervalo de tempo? (em segundos)", color="#006989", border_color="#A3BAC3")

    x = ft.TextField(label="Qual a coordenada X?", border_color="#A3BAC3", color="#006989")
    y = ft.TextField(label="Qual a coordenada Y?", border_color="#A3BAC3", color="#006989")
    txt = ft.Text("Clique no botão para tirar um screenshot em 2 segundos", size=20, color="#006989")

    btn = ft.ElevatedButton(text="Tirar screenshot", on_click=screenshot, bgcolor="#006989", color="#EAEBED")

    coluna = ft.Column(
                       controls=[txt,
                        x,
                         y,
                         repetir,
                           tempo,
                             ft.Row(
            controls=[btn],
              spacing=20,
              alignment=ft.MainAxisAlignment.CENTER
    )
    ],
      alignment=ft.MainAxisAlignment.CENTER,
      horizontal_alignment=ft.MainAxisAlignment.CENTER)


    page.add(coluna)

ft.app(target=main)
