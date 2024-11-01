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
        size= 30,
        #text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.W_100,
        )

    link_style = ft.TextStyle(
        color=ft.colors.BLUE,
        decoration=ft.TextDecoration.UNDERLINE,
        decoration_color=ft.colors.BLUE, 
        decoration_style=ft.TextDecorationStyle.SOLID,
    )

    texto2 = ft.Text(
        spans=[
            ft.TextSpan(text='Texto com link ', style=link_style, url='https://google.com'),
            ft.TextSpan(text='continuação do texto...', style=ft.TextStyle(color=ft.colors.GREEN)),
            ft.TextSpan(text='texto em destaque!!!!'),
        ],
        size= 20,
    )

    page.update()
    page.add(
        text1,
        texto2,
        
    )

ft.app(target=main, assets_dir='assets') # faz a renderização do app