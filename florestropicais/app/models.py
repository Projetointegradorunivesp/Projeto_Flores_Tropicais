from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)
    preco = models.FloatField()
    img = models.ImageField(upload_to='media', blank=True, null=True)


    def __str__(self):
        return self.nome

