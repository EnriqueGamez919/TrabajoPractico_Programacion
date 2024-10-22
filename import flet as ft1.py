import flet as ft

def main(page: ft.Page):
    page.window_width = 600
    page.window_height = 400
    page.title = "Lista de compras"

    # Crear un campo de texto para la entrada
    new_task = ft.TextField(
        hint_text="¿Qué necesitas comprar?", 
        width=300, 
        border_radius=10,  # Bordes redondeados
        filled=True,  # Fondo gris claro
        bgcolor=ft.colors.LIGHT_BLUE_50,  # Color de fondo del campo
        border_color=ft.colors.BLUE_ACCENT  # Color del borde
    )

    # Función para agregar una tarea
    def add_clicked(e):
        if new_task.value:  # Asegúrate de que el campo no esté vacío
            task_name = new_task.value
            checkbox = ft.Checkbox(label=task_name)
            task_row = ft.Row(
                controls=[
                    checkbox,
                    ft.IconButton(icon=ft.icons.CREATE, 
                                  on_click=lambda e: edit_task(checkbox),
                                  icon_color=ft.colors.GREEN),  # Botón para editar
                    ft.IconButton(icon=ft.icons.DELETE, 
                                  on_click=lambda e: remove_task(task_row),
                                  icon_color=ft.colors.RED)  # Botón para eliminar
                ],
                alignment="spaceBetween",  # Distribuir el espacio entre los controles
                spacing=10  # Espacio entre los botones
            )
            page.add(task_row)
            new_task.value = ""  # Limpiar el campo de texto
            new_task.focus()  # Regresar el foco al campo de texto
            page.update()

    # Función para editar una tarea
    def edit_task(checkbox):
        edit_field = ft.TextField(value=checkbox.label)

        def save_edit(e):
            checkbox.label = edit_field.value  # Actualizar el texto del checkbox
            page.remove(edit_field_row)  # Quitar el campo de edición
            page.update()

        save_button = ft.ElevatedButton(text="Guardar", on_click=save_edit, bgcolor=ft.colors.BLUE)
        edit_field_row = ft.Row([edit_field, save_button], spacing=10)  # Añadir espaciado entre los controles
        page.add(edit_field_row)
        page.update()

    # Función para eliminar una tarea
    def remove_task(task_row):
        page.remove(task_row)
        page.update()

    # Logo y texto del encabezado
    logo = ft.Image(src="C:/Users/Admin/Documents/tp/logo.jpg", width=150, height=150)
    header_text = ft.Text(
        "Bienvenidos a la App de Lista de Compras", 
        size=20, 
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE_ACCENT
    )
    # Organizar el logo y el texto en una columna
    header = ft.Column(
        [
            logo,
            header_text
        ], 
        alignment="center",  # Alinear al centro
        horizontal_alignment="center",
        spacing=10  # Espacio entre el logo y el texto
    )

    # Agregar los elementos a la página
    page.add(
        header,
        ft.Divider(height=20),  # Divisor entre el encabezado y el resto de la página
        ft.Row(
            [new_task, 
             ft.ElevatedButton("Agregar", on_click=add_clicked, bgcolor=ft.colors.BLUE, color=ft.colors.WHITE)], 
            alignment="center", 
            spacing=10  # Espacio entre el campo de texto y el botón
        )
    )
# Ejecutar la aplicación
ft.app(target=main)
