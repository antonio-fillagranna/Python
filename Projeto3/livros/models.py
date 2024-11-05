from django.db import models

# Create your models here.
class Categorias(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Livros(models.Model):
    streaming_choices = (('N', 'Netflix'), ('A', 'Amazon Prime'))
    nome = models.CharField(max_length=50)
    streaming = models.CharField(max_length=2, choices=streaming_choices)
    nota = models.IntegerField(null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)
    categorias = models.ManyToManyField(Categorias)

    def __str__(self):
        return self.nome
