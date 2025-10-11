import flet as ft
import pyautogui as pg
from time import sleep

# Função principal do app Flet
def main(page: ft.Page):
    # Configurações da janela
    page.title = "Finder CV"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLUE_GREY_100
    page.window.height = 500
    page.window.width = 300
    page.window.resizable = False
    page.window.maximizable = False

    # Função: pesquisa automática usando pyautogui
    def pesquisar(e):
        pg.press("win")
        sleep(1)
        pg.write("zen")  # Nome do navegador
        sleep(1)
        pg.press("enter")
        sleep(2)

        # Acessa LinkedIn
        pg.write("https://www.linkedin.com/feed/")
        sleep(1)
        pg.press("enter")
        sleep(5)
        for _ in range(6):
            pg.press("tab")
        sleep(1)
        pg.write(nome.value)
        sleep(1)
        pg.press("enter")
        sleep(1)

        # Acessa Google Maps
        pg.hotkey("ctrl", "t")
        sleep(1)
        pg.write("https://www.google.com/maps/")
        sleep(1)
        pg.press("enter")
        sleep(5)
        pg.write(endereco.value)
        sleep(1)
        pg.press("enter")
        sleep(1)

        # Acessa ligaram-me.com
        pg.hotkey("ctrl", "t")
        sleep(1)
        pg.write("https://ligaram-me.com/")
        sleep(1)
        pg.press("enter")
        sleep(5)
        for _ in range(2):
            pg.press("tab")
        pg.write(telefone.value)
        pg.press("enter")

    # Função: guardar dados num arquivo de texto
    def guardar(e):
        with open("dados.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write("------ NOVO REGISTRO ------\n")
            arquivo.write(f"Nome: {nome.value}\n")
            arquivo.write(f"Telefone: {telefone.value}\n")
            arquivo.write(f"Endereço: {endereco.value}\n")
        arquivo.write("\n")  # Linha em branco para separar
    # Título da interface
    titulo = ft.Text(
        "Qual é a pessoa que deseja encontrar?",
        color=ft.Colors.BLACK87,
        size=20,
        weight=ft.FontWeight.BOLD
    )

    # Campo de texto: Nome
    nome = ft.TextField(
        label="Nome",
        hint_text="Digite o nome completo",
        color=ft.Colors.BLACK87,
        label_style=ft.TextStyle(color=ft.Colors.GREY_700),
        hint_style=ft.TextStyle(color=ft.Colors.GREY_500),
        border_color=ft.Colors.GREY_300,
        focused_border_color=ft.Colors.BLUE_600,
        bgcolor=ft.Colors.WHITE,
    )

    # Campo de texto: Telefone
    telefone = ft.TextField(
        label="Telefone",
        hint_text="Digite o número de telefone",
        width=300,
        height=50,
        color=ft.Colors.BLACK87,
        label_style=ft.TextStyle(color=ft.Colors.GREY_700),
        hint_style=ft.TextStyle(color=ft.Colors.GREY_500),
        border_color=ft.Colors.GREY_300,
        focused_border_color=ft.Colors.BLUE_600,
        bgcolor=ft.Colors.WHITE,
    )

    # Campo de texto: Endereço
    endereco = ft.TextField(
        label="Endereço",
        hint_text="Digite o endereço",
        width=300,
        height=50,
        color=ft.Colors.BLACK87,
        label_style=ft.TextStyle(color=ft.Colors.GREY_700),
        hint_style=ft.TextStyle(color=ft.Colors.GREY_500),
        border_color=ft.Colors.GREY_300,
        focused_border_color=ft.Colors.BLUE_600,
        bgcolor=ft.Colors.WHITE,
    )

    # Botão de pesquisa
    bt_pesquisar = ft.ElevatedButton(
        text="Pesquisar",
        width=100,
        height=50,
        bgcolor=ft.Colors.INDIGO_500,
        color=ft.Colors.WHITE,
        elevation=10,
        on_click=pesquisar,
    )

    # Botão de guardar
    bt_guardar = ft.ElevatedButton(
        text="Guardar",
        width=100,
        height=50,
        bgcolor=ft.Colors.INDIGO_500,
        color=ft.Colors.WHITE,
        elevation=10,
        on_click=guardar,
    )

    # Layout principal
    layout = ft.Column(
        controls=[
            titulo,
            nome,
            telefone,
            endereco,
            ft.Row(
                controls=[bt_pesquisar, bt_guardar],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )

    # Adiciona layout dentro de um container com sombra e margem
    page.add(
        ft.Container(
            content=layout,
            padding=20,
            border_radius=10,
            bgcolor=ft.Colors.WHITE,
            shadow=ft.BoxShadow(
                blur_radius=12,
                color=ft.Colors.BLACK26,
                offset=ft.Offset(4, 4)
            )
        )
    )

# Executa o app Flet
ft.app(target=main)
