import flet as ft

from views.add_music_modal import AddMusicModal

def main(page: ft.Page):
    page.title = "Urna Mobile"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#111111"

    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)

    add_music_modal = AddMusicModal(page, file_picker)
    page.overlay.append(add_music_modal)

    def open_modal(e):
        page.dialog = add_music_modal
        add_music_modal.open = True
        page.update()

    page.add(
        ft.ElevatedButton(
            "Open Add Music Modal",
            on_click=open_modal
        )
    )

if __name__ == "__main__":
    ft.app(target=main) 