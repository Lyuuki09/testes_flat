import flet as ft

def AddMusicModal(page: ft.Page, file_picker: ft.FilePicker):
    # Adiciona a lógica para fechar o diálogo
    def close_modal(e):
        e.control.page.dialog.open = False
        e.control.page.update()

    # Componente da imagem da capa da música para atualização dinâmica
    music_cover_image = ft.Image(src='assets/svgs/image.svg', width=60, height=60)

    def on_dialog_result(e: ft.FilePickerResultEvent):
        if e.files:
            selected_file_path = e.files[0].path
            music_cover_image.src = selected_file_path
            page.update()

    # Associa o callback ao file_picker
    file_picker.on_result = on_dialog_result

    return ft.AlertDialog(
        modal=True,
        open=False,
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("Adicionar música", size=20, weight=ft.FontWeight.BOLD, color="#D6AB5F"),
                            ft.IconButton(ft.Icons.CLOSE, on_click=close_modal, icon_color="#D6AB5F", icon_size=24),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.TextField(
                        label="Nome da Música",
                        prefix_icon=ft.Image(src='assets/svgs/music_note.svg', width=24, height=24),
                        border_radius=ft.border_radius.all(10),
                        label_style=ft.TextStyle(color=ft.Colors.WHITE60),
                        border_color="#1B1A1B",
                        focused_border_color=ft.Colors.AMBER,
                        cursor_color=ft.Colors.AMBER,
                        text_style=ft.TextStyle(color="#8A8881"),
                        content_padding=ft.padding.only(top=10, bottom=10, left=12, right=12),
                        filled=True,
                        fill_color="#121212"
                    ),
                    ft.TextField(
                        label="Nome do artista",
                        prefix_icon=ft.Image(src='assets/svgs/person.svg', width=24, height=24),
                        border_radius=ft.border_radius.all(10),
                        label_style=ft.TextStyle(color=ft.Colors.WHITE60),
                        border_color="#1B1A1B",
                        focused_border_color=ft.Colors.AMBER,
                        cursor_color=ft.Colors.AMBER,
                        text_style=ft.TextStyle(color="#8A8881"),
                        content_padding=ft.padding.only(top=10, bottom=10, left=12, right=12),
                        filled=True,
                        fill_color="#121212"
                    ),
                    ft.TextField(
                        label="Gênero",
                        prefix_icon=ft.Image(src='assets/svgs/disco.svg', width=24, height=24),
                        border_radius=ft.border_radius.all(10),
                        label_style=ft.TextStyle(color=ft.Colors.WHITE60),
                        border_color="#1B1A1B",
                        focused_border_color=ft.Colors.AMBER,
                        cursor_color=ft.Colors.AMBER,
                        text_style=ft.TextStyle(color="#8A8881"),
                        content_padding=ft.padding.only(top=10, bottom=10, left=12, right=12),
                        filled=True,
                        fill_color="#121212"
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                music_cover_image,
                                ft.Text("Adicionar capa da música", color=ft.Colors.WHITE60),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=5
                        ),
                        width=300,
                        height=150,
                        bgcolor=ft.Colors.BLACK87,
                        border=ft.border.all(1, ft.Colors.AMBER_400),
                        border_radius=ft.border_radius.all(10),
                        on_click=lambda _: file_picker.pick_files(allow_multiple=False)),
                    ft.Row(
                        [
                            ft.ElevatedButton("Adicionar", bgcolor="#D6AB5F", color=ft.Colors.BLACK, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))),
                            ft.OutlinedButton("Cancelar", style=ft.ButtonStyle(color="#D6AB5F", shape=ft.RoundedRectangleBorder(radius=10)), on_click=close_modal),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                        spacing=10
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            padding=20,
            width=350
        ),
        bgcolor="#111111",
    ) 