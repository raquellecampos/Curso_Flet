import flet as ft

def main(page: ft.Page):
    img = ft.Image(
        # src='https://th.bing.com/th/id/OIP.5hIx18FWXLCeG5rKG8II9AHaHa?rs=1&pid=ImgDetMain',
        src='assets/img/barbershop1.jpg',
        border_radius= ft.border_radius.horizontal(left=10, right=10),
        height=300,
        width=1000,
        fit=ft.ImageFit.CONTAIN,
        tooltip='Barbearia',
    )

    icon = ft.Icon(name=ft.icons.CAMERA, color=ft.colors.BLUE)



    btn1 = ft.ElevatedButton(text='Clique aqui', icon=ft.icons.CHECK)
    btn2 = ft.ElevatedButton(text='Não clique aqui', icon=ft.icons.CANCEL, disabled=True)

    estilo = ft.ButtonStyle(
        color={
            ft.MaterialState.HOVERED: ft.colors.WHITE,
            ft.MaterialState.DEFAULT: ft.colors.BLACK,
        },
        bgcolor={
            ft.MaterialState.HOVERED: ft.colors.PINK, # TODO: Pode ser feito com o color.from_hex("#ff00ff")
            ft.MaterialState.DEFAULT: ft.colors.AMBER,
            '': ft.colors.AMBER,
        },
        animation_duration=1000,

    )

    btn3 = ft.ElevatedButton(text='Botão com estilo personalizado', style=estilo)

    page.add(img,icon, btn1, btn2, btn3)

    def button_clicked(e):
        e.control.data += 1
        texto.value = f'Contagem: {e.control.data}'
        texto.update()
        btn.update()

    btn = ft.ElevatedButton(text='Botão com contagem', icon=ft.icons.CABIN_SHARP, on_click=button_clicked, data=0)
    texto = ft.Text(value='Contagem: 0', color=ft.colors.WHITE)

    page.add(btn, texto)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.DELETE,
        tooltip='Adicionar',
        bgcolor=ft.colors.BROWN,
        mini=False,
        on_click=lambda e: print('CLICADO!'), # TODO: Lambda é uma função anônima estudar sobre / pode ser também on_click=adcionar_item,
    )

    btn4 = ft.IconButton(
        icon = ft.icons.DELETE_FOREVER_ROUNDED,
        icon_color=ft.colors.WHITE,
        bgcolor=ft.colors.RED,
        tooltip='Remover',
    )

    def play_pause(e):
        e.control.selected = not e.control.selected
        e.control.update()
    
    btn5 = ft.IconButton(
        icon=ft.icons.PLAY_ARROW,
        selected=True,
        selected_icon=ft.icons.PAUSE,
        icon_size=50,
        on_click=play_pause,
        style=ft.ButtonStyle(
            color={
                ft.MaterialState.SELECTED: ft.colors.WHITE,
                ft.MaterialState.DEFAULT: ft.colors.RED,
            }
        )
    )

    page.add(page.floating_action_button, btn4, btn5)

ft.app(target=main, assets_dir='assets')