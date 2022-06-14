from rest_framework import serializers
from app.models import Produto

class ProdutoSereializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = 'nome', 'descricao', 'preco', 'img'