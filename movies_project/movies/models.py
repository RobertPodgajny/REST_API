from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=64)


class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='movie_director')  # relacja z powrotem, zamiast _set.
    actors = models.ManyToManyField(Person, through='PersonMovie')
    year = models.IntegerField()


class PersonMovie(models.Model):
    role = models.CharField(max_length=128)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
