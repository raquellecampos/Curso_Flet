import flet as ft

def main(page: ft.Page):
    img = ft.Image(
        # src='https://th.bing.com/th/id/OIP.5hIx18FWXLCeG5rKG8II9AHaHa?rs=1&pid=ImgDetMain',
        src='assets/img/barbershop1',
        border_radius= ft.border_radius.horizontal(left=10, right=10),
        height=500,
        width=500,
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
            ft.MaterialState.HOVERED: ft.colors.PINK,
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

ft.app(target=main, assets_dir='assets')