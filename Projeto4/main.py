import flet as ft
from conect import review
from urllib.parse import urlparse, parse_qs

def main(page: ft.Page):
    page.title = 'Cadastro App'
    page.window_width = 400

   def home_page():
        nome_input = ft.TextField(label="Nome do Produto", text_align=ft.TextAlign.LEFT)
        streaming_select = ft.Dropdown(
            options=[
                ft.dropdown.Option("AK", text="Amazon Kindle"),
                ft.dropdown.Option("F", text="Físico"),
            ],
            label="Selecione a streaming"
        )
        def cadastrar(e):
            data = {
                'nome': nome_input.value,
                'streaming': streaming_select.value,
                'categorias': []
            }
        response = requests.post('http://127.0.0.1:8000/api/livros/', json=data)
        cadastrar_btn = ft.ElevatedButton("Cadastrar", on_click=cadastrar)

        page.views.append(
            ft.View(
                "/",
                controls=[
                    nome_input,
                    streaming_select,
                    cadastrar_btn,

                ]
            )
        )
        def route_change(e):
            page.views.clear()
            if page.route == "/":
                home_page()
            elif page.route.startswith("/review"):
                parsed_url = urlparse(page.route)
                query_params = parse_qs(parsed_url.query)
                livro_id = query_params.get('id', [None])[0]
                review_page(livro_id)

            page.update()
def review_page(livro_id):
    nota_input = ft.TextField(label="Nota (inteiro)", text_align=ft.TextAlign.LEFT, value="0", width=100)
    comentario_input = ft.TextField(label="Comentário", multiline=True, expand=True)
    avaliar_btn = ft.ElevatedButton("Avaliar", on_click=avaliar)
    voltar_btn = ft.ElevatedButton("Voltar", on_click=lambda _: page.go('/'))
    page.views.append(
    ft.View(
    "/review",
    controls=[
    ft.Text("Review Page"),
    ft.Text(f"Detalhes do livro com ID: {livro_id}"),
    nota_input,
    comentario_input,
    avaliar_btn,
    voltar_btn
    ]
    )
 )
def avaliar(e):
    data = {
    'nota': int(nota_input.value),
    'comentarios': comentario_input.value
    }

    try:
        response = requests.put(f'http://127.0.0.1:8000/api/livros/{livro_id}', json=data)
        if response.status_code == 200:
            page.snack_bar = ft.SnackBar(ft.Text("Avaliação enviada com sucesso!"))
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Erro ao enviar a avaliação."))
            page.snack_bar.open = True
    except Exception as ex:
        page.snack_bar = ft.SnackBar(ft.Text(f"Erro de conexão: {ex}"))
        page.snack_bar.open = True
        page.update()