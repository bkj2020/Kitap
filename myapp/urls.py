# for defined path template to conect with url
from django.urls import path, include
from . import views
from django.conf.urls import url
from django.views.decorators.cache import cache_page


urlpatterns = [
    # if need cache base page    
    #path('', cache_page(10 * 60)(MainPageView.as_view()), name='app-base'),

    # receive base page 
    path('', views.index, name='index'),
    path('search/', views.search, name='poisk'),   

    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
     # === - look for real metadata request.META from sevrer - ===
    path('display_meta/', views.display_meta),
]
