from django.contrib import admin

from movies.models import Person, Movie, PersonMovie

admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(PersonMovie)
