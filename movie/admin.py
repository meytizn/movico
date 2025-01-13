from django.contrib import admin
from .models import Movie , Genre , Actor , Link , Comment

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Link)
admin.site.register(Comment)
# Register your models here.
