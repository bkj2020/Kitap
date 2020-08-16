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
from  myapp.models import Publisher, Genre, Language, Author, Book, Predmet, Kafedra, Teacher, Lection, Prezintation

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


# base page for all pages in this project
def index(request):
   """View function for home page of site."""
   # Generate counts of some of the main objects

   return render(request, 'index.html')


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


class PredmetListView(ListView):
    """Generic class-based view for a list of Predmet."""
    model = Predmet
    template_name = 'predmet_list.html'


class PredmetDetailView(DetailView):
    """Generic class-based detail view for a Lection."""
    model = Predmet
    template_name = 'predmet_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PredmetDetailView, self).get_context_data(*args, **kwargs)
        context['subject'] = self.model.objects.all()
        context['subjects_from_predmet'] = self.get_object().lection_set.all()
        return context


class LectionDetailView(DetailView):
    """Generic class-based detail view for a book."""
    model = Lection
    template_name = 'lection_detail.html'


class PrezentListView(ListView):
    """Generic class-based view for a list of Predmet."""
    model = Predmet
    template_name = 'prezent_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PrezentListView, self).get_context_data(*args, **kwargs)
        context['prezent'] = self.model.objects.all()
        return context


class PresentationDetailView(DetailView):
    """Generic class-based detail view for a Lection."""
    model = Predmet
    template_name = 'presentations_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PresentationDetailView, self).get_context_data(*args, **kwargs)
        context['flush'] = self.model.objects.all()
        context['flush_from_predmet'] = self.get_object().prezintation_set.all()
        return context


class PowerpointDetailView(DetailView):
    """Generic class-based detail view for a book."""
    model = Prezintation
    template_name = 'powerpoint_detail.html'












# search for title field in database
class SearchView(View):
    model = Book
    template_name = 'search_form.html'
    
    def get(self, request, *args, **kwargs):
        errors = []
        if 'zapros' in request.GET:
            zapros = request.GET['zapros']
            if not zapros:
                errors.append('Введите поисковый запрос.')
            elif len(zapros) > 20:
                errors.append('Введите не более 20 символов.')
            else:
                kniga = Book.objects.filter(Q(title__icontains=zapros))
                return render(request, 'search_results.html', {'kniga': kniga, 'query': zapros})
        return render(request, 'search_form.html', {'errors': errors})
# End of === - search function  - ===