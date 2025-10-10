import flet as ft
import pyautogui as pg
from time import sleep

def main(page: ft.Page):
    page.title = "bot"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#6495ED"

    img = ft.Image(src="https://diario98.com/wp-content/uploads/2021/07/programa-espiao_para_celular.jpg",width=700, height=400)

    txt = ft.Text("oque deseja procurar?",color=ft.Colors.BLACK)

    resposta = ft.TextField()


    def pesquisar(e):
        pg.press("win")
        sleep(1)
        pg.write("edge")
        sleep(1)
        pg.press("enter")
        sleep(2)
        pg.write(resposta.value)
        sleep(1)
        pg.press("enter")
        sleep(1)
        pg.hotkey("ctrl", "t")
        sleep(1)
        pg.write("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal")
        sleep(1)
        pg.press("enter")
        sleep(1)
        for i in range(4):
            pg.press("tab")
        pg.write(resposta.value)
        pg.press("enter")
        sleep(1)
        pg.hotkey("ctrl","t")
        sleep(1)
        pg.write("https://www.youtube.com/")
        sleep(1)
        pg.press("enter")
        sleep(3)
        for i in range(4):
            pg.press("tab")
        pg.write(resposta.value)
        pg.press("enter")

    bt = ft.ElevatedButton(text="Pesquisar", on_click=pesquisar,width=100, height=50,bgcolor=ft.Colors.BLACK)

    page.add(
        ft.Column(
            controls=[
                img,
                txt,
                resposta,
                bt
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )



ft.app(target=main)