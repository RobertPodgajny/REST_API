from rest_framework import serializers
from .models import Movie, Person


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'director', 'actors', 'year')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = 'name'


