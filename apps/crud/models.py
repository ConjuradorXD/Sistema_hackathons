from django.db import models


class Item(models.Model):
    codigo_item = models.AutoField(primary_key=True)
    nome_item = models.CharField(max_length=100, default="")
    tipo_item = models.CharField(max_length=100, default="")
    peso = models.CharField(max_length=30, default="")
    raridade = models.CharField(max_length=50, default="")
    descricao_item = models.TextField(blank=True, default="")
    nome_encontrador = models.CharField(max_length=100, default="")
    graduacao = models.CharField(max_length=50, default="")
    local_encontrado = models.CharField(max_length=150, default="")
    data_encontrado = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome_item
