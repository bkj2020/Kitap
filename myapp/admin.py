from django.contrib import admin
# import all models from myapp.models.py
from . models import Publisher, Genre, Language, Author, Book, Predmet, Kafedra, Teacher, Lection #, Prezintation

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Predmet)
admin.site.register(Kafedra)
admin.site.register(Teacher)
admin.site.register(Lection)
#admin.site.register(Prezintation)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """
    list_display = ('last_name', 'first_name', 'email', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


class BookAdmin(admin.ModelAdmin):
    """Administration object for Book models.
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    list_display = ('fk_genre', 'title', 'fk_author', 'fk_language')


admin.site.register(Book, BookAdmin)