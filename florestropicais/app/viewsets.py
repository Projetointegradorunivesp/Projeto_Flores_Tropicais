from rest_framework.viewsets import ModelViewSet

from app.models import Produto
from app.serializer import ProdutoSereializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSereializer
