import flet as ft

def main(page: ft.Page):
    #page.bgcolor = '#B12B12'
    page.bgcolor = ft.colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment= ft.MainAxisAlignment.START

    #page.padding = 20
    #page.spacing = 20
    page.title = 'Raquelle'
    page.window_always_on_top = True # sempre visível
    page.window_title_bar_buttons_hidden = True # botões escondidos do topo
    page.window_frameless = False # sem borda
    page.window_full_screen = False # tela cheia
    page.window_borderless = False # sem borda
    page.window_resizable = False # sem redimensionamento
    page.window_minimizable = False # sem minimização
    page.window_maximizable = False # sem maximização
    page.window_height = 800 # altura
    page.window_width = 500 # largura
    page.window_max_height = 800 # altura máxima
    page.window_max_width = 500 # largura máxima

    #page.window_icon = ft.load_image('icon.png')
    page.window_top = 10 # posição vertical
    page.window_left = -500 # posição horizontal
    page.window_movable = True # movivel    
    page.window_prevent_close = True # não fecha, programar mensagem de confirmação para sair
    page.window_progress_bar = 0.5 # progress bar

    print(page.platform) # plataforma

    # def window_event(e):
    #     match e.data:
    #         case 'close':
    #             print('Fechar')
    #         case 'minimize':
    #             print('Minimizar')
    #         case 'maximize':
    #             print('Maximizar')
    #         case 'restore':
    #             print('Restaurar')
    #         case 'move':
    #             print('Mover')
    #         case 'resize':
    #             print('Redimensionar')
          

    # page.on_window_event = window_event
    

    page.add(
        ft.Text('testando', bgcolor=ft.colors.BROWN),
        ft.Container(ft.Text('teste'), bgcolor=ft.colors.GREEN)
    )

    page.update() # atualiza a tela


ft.app(target=main) # faz a renderização do app

