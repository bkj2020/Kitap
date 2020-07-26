from django.contrib import admin
# import all models from myapp.models.py
from .models import Publisher, Genre, Language, Author, Book

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Book)