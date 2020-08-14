# === - import django belong classes - ===
import os
from django.shortcuts import render
from django.http import HttpResponse

# отображения списка — класс, который наследуется от существующего отображения (ListView).
from django.views.generic import ListView, DetailView, View
# for arange own logging files
import logging

#from django.views.decorators.cache import cache_page #if need cache function if class do it with urls.py

# import all table from models.py 
from  myapp.models import Publisher, Genre, Language, Author, Book

# for searsh book 
from django.db.models import Q

# Gets or creates a logger in file
logger = logging.getLogger(__name__) 
logging.basicConfig(filename='mylog.log', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level='ERROR')

# === - look for real metadata request.META from sevrer - ===
def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
# === - end of request.META - ===


# search for title field in database
def search(request):
    errors = []
    if 'zapros' in request.GET:
        zapros = request.GET['zapros']
        if not zapros:
            errors.append('Введите поисковый запрос.')
        elif len(zapros) > 20:
            errors.append('Введите не более 20 символов.')
        else:
            kniga = Book.objects.filter(title__icontains=zapros)
            return render(request, 'search_results.html', {'kniga': kniga, 'query': zapros})
    return render(request, 'search_form.html', {'errors': errors})
# End of === - search function  - ===


# base page for all pages in this project
def index(request):
   """View function for home page of site."""
   # Generate counts of some of the main objects
   num_books = Book.objects.all().count()
   num_authors = Author.objects.all().count()
   num_categorise = Genre.objects.all().count()
   return render(request, 'index.html', context={
       'num_books':num_books, 'num_authors':num_authors, 'num_categorise':num_categorise})


class BookListView(ListView):
    """Generic class-based view for a list of books."""
    model = Book
    template_name = 'book_list.html'


class BookDetailView(DetailView):
    """Generic class-based detail view for a book."""
    model = Book
    template_name = 'book_detail.html'


class AuthorListView(ListView):
    """Generic class-based list view for a list of authors."""
    model = Author
    template_name = 'author_list.html'


class AuthorDetailView(DetailView):
    """Generic class-based detail view for an author."""
    model = Author
    template_name = 'author_detail.html'


class CategoryListView(ListView):
    """Generic class-based view for a list of category."""
    model = Genre
    template_name = 'genre_list.html'



class CategoryDetailView(DetailView):
    """Generic class-based detail view for a Genre."""
    model = Genre
    template_name = 'category_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        context['categorya'] = self.model.objects.all()
        context['books_from_genre'] = self.get_object().book_set.all()
        return context






def hi(request):
   """View function for home page of site."""
   # Generate counts of some of the main objects
   return render(request, 'tap.html')





class SearchView(View):
    model = Book
    template_name = 'tapmaly.html'

    def get_context_data(self, *args, **kwargs):
        query = self.request.GET.get('q')
        found_books = Book.objects.filter(title__icontains=query)
        context = {'found_books': found_books }
        return render(self.request, self.template_name, context)
