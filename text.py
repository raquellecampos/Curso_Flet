import flet as ft


def main(page: ft.Page):
    page.window_height = 800 # altura
    page.window_width = 500 # largura
    page.window_max_height = 800 # altura máxima
    page.window_max_width = 500 # largura máxima
    #page.window_icon = ft.load_image('icon.png')
    page.window_top = 10 # posição vertical
    page.window_left = -500 # posição horizontal
    page.fonts = {
        'Dragon_Slayer': 'fonts/Dragon Slayer.ttf'
    }

    text1 = ft.Text(
        value='Texto 1 rsrsrsrsrsrsrsrsrsrsrsrrsrsrs',
        style=ft.TextThemeStyle.BODY_LARGE,
        bgcolor=ft.colors.RED,
        color=ft.colors.WHITE,
        #font_family='Dragon_Slayer'
        italic=True,
        #max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS,
        no_wrap=True, # não quebra linha
        selectable=True,

        )

    page.update()
    page.add(
        text1,
        
    )

ft.app(target=main, assets_dir='assets') # faz a renderização do app