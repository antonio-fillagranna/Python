def get_livros():
    response = requests.get('http://127.0.0.1:8000/api/livros')
    return response.json()
    lista_livros = ft.ListView()
    def carregar_livros():
        lista_livros.controls.clear()
        for i in get_livros():
            lista_livros.controls.append(
            ft.Container(
            ft.Text(i['nome']),
            bgcolor=ft.colors.BLACK12,
            padding=15,alignment=ft.alignment.center,
            margin=3,
            border_radius=10,

        )
    )
        page.update()
    carregar_livros()
    page.views.append(
        ft.View(
            "/",
            controls=[
                nome_input,
                streaming_select,
                cadastrar_btn,
                lista_livros
            ]
        )
    )
on_click=lambda e: page.go(f"/review?id={i['id']}")