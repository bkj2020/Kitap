# === - import django belong classes - ===
from django.shortcuts import render
from django.views.generic.list import View
from django.http import HttpResponse
from .forms import ContactForm

# === - import table from database - ===
from .models import Book

# === - look for metadata  request.META - ===
def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
# === - end of request.META - ===


# Create your views here.
class MainPageView(View):
    template_name = 'base.html'

    def get(self, request):

        return render(request, 'base.html')


# === - search function- ===
# def search(request):
#     errors = []
#     if 'zapros' in request.GET:
#         zapros = request.GET['zapros']
#         if not zapros:
#             errors.append('Введите поисковый запрос.')
#         elif len(zapros) > 20:
#             errors.append('Введите не более 20 символов.')
#         else:
#             kniga = Book.objects.filter(title__icontains=zapros)
#             return render(request, 'search_results.html', {'kniga': kniga, 'query': zapros})
#     return render(request, 'search_form.html', {'errors': errors})

# new one
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


# === - search form  function - ===
# def search_form(request):
#
#     return render(request, 'search_form.html')
# End of === - search form  function - ===
