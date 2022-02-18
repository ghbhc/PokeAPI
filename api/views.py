from rest_framework import viewsets

from .models import Pokemon
from .serializers import PokemonSerializer

# Create your views here.

class PokemonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    def get_queryset(self):
        queryset = Pokemon.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset
