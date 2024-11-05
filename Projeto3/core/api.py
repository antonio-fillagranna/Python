from ninja import NinjaAPI
from livros.api import livros_router

api = NinjaAPI()
api.add_router('livros/', livros_router)
