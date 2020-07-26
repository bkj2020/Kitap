# === - import django belong classes - ===
from django.shortcuts import render
from django.views.generic.list import View
from django.http import HttpResponse
from .forms import ContactForm
from .models import Book
import os
import logging
from django.views.decorators.cache import cache_page #if need cache function if class do it with urls.py

# Create your views here.

###############
# Gets or creates a logger in file
logger = logging.getLogger(__name__) 
logging.basicConfig(filename='mylog.log', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level='ERROR')
################

# === - look for real metadata request.META from sevrer - ===
def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
# === - end of request.META - ===


class MainPageView(View):
    template_name = 'base.html'

    def get(self, request):
        #import pdb; pdb.set_trace()
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