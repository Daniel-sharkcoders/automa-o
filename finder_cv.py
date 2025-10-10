import flet as ft
import pyautogui as pg
from time import sleep

def main(page: ft.Page):
    page.title = "bot"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#ffffff"

    txt = ft.Text("Qual é a pessoa que deseja encontrar?", color=ft.colors.BLACK, size=30)
    nome = ft.TextField(label="Nome", width=300, height=50)
    telefone = ft.TextField(label="Telefone", width=300, height=50)
    endereco = ft.TextField(label="Endereço", width=300, height=50)

    bt_pesquisar = ft.ElevatedButton(text="Pesquisar", width=100, height=50, bgcolor=ft.colors.RED)
    bt_guardar = ft.ElevatedButton(text="Guardar", width=100, height=50, bgcolor=ft.colors.GREEN)

    def pesquisar(e):
        pg.press("win")
        sleep(1)
        pg.write("edge")
        sleep(1)
        pg.press("enter")
        sleep(2)
        pg.write("https://www.linkedin.com/feed/")
        sleep(1)
        pg.press("enter")
        sleep(5)


        ft.column(
        controls=[
            nome,
            telefone,
            endereco,
            ft.Row(
                controls=[bt_pesquisar, bt_guardar],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    page.add()
ft.app(target=main)