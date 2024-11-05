from django.urls import path
from . import view

urlpatterns = [
    path('', view.home, name='home')
]