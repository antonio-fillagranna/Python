from ninja import Router
from .models import Livros, Categorias
from .schemas import LivroSchema

livros_router = Router()
@livros_router.post('/', response={200: LivroSchema})
def create_livro(request, livro_schema: LivroSchema):
    nome = livro_schema.dict()['nome']
    streaming = livro_schema.dict()['streaming']
    categorias = livro_schema.dict()['categorias']
    livro = Livros(nome=nome, streaming=streaming)
    livro.save()

    for categoria in categorias:
        livro.categorias.add(Categorias.objects.get(id=categoria))
    livro.save()
    return livro
