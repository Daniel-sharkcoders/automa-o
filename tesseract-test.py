import pytesseract
import cv2
import flet as ft

# Caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Daniel\Desktop\tesseract\tesseract.exe'


def main(page: ft.Page):
    page.title = "Image to Text Converter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    selected_file_path = ""


    txt = ft.Text("Nenhum arquivo selecionado")
    result = ft.Text("")

    def on_file_picked(e: ft.FilePickerResultEvent):
        nonlocal selected_file_path

        if e.files:
            selected_file_path = e.files[0].path
            txt.value = f"Arquivo selecionado:\n{selected_file_path}"
        else:
            txt.value = "Nenhum arquivo selecionado."

        page.update()


    file_picker = ft.FilePicker(on_result=on_file_picked)
    page.overlay.append(file_picker)

    def pick_file(e):
        file_picker.pick_files(allow_multiple=False)


    def converter(e):
        if not selected_file_path:
            result.value = "Selecione um arquivo primeiro!"
            page.update()
            return

        imagem = cv2.imread(selected_file_path)
        texto = pytesseract.image_to_string(imagem)

        result.value = f"Texto extraído:\n\n{texto}"
        page.update()

 
    pick_button = ft.ElevatedButton("Selecionar Imagem", on_click=pick_file)
    convert_button = ft.ElevatedButton("Converter para Texto", on_click=converter)

    coluna = ft.Column(
        controls=[txt, 
                  ft.Row(controls=[convert_button, pick_button], alignment=ft.MainAxisAlignment.CENTER), 
                  result],
        alignment=ft.MainAxisAlignment.CENTER,)
    


    page.add(coluna)


ft.app(target=main)
