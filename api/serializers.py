from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = ('number', 'name', 'type1', 'type2', 'height', 'weight', 'description')
