import flet as ft

def main(page: ft.Page):
    img = ft.Image(
       # src='https://th.bing.com/th/id/OIP.5hIx18FWXLCeG5rKG8II9AHaHa?rs=1&pid=ImgDetMain',
       src='/Users/raque/Documents/GitHub/Curso_Flet/assets/img.png',
        border_radius= ft.border_radius.horizontal(left=10, right=10),
        height=500,
        width=500,
        fit=ft.ImageFit.COVER,
    )

    page.add(img)

ft.app(target=main, assets_dir='assets')