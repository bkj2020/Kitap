# for defined path template to conect with url
from django.urls import path, include
from myapp.views import MainPageView
from myapp import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    # if need cache base page    
    #path('', cache_page(10 * 60)(MainPageView.as_view()), name='app-base'),

    # receive base page 
    path('', MainPageView.as_view(), name='app-base'),
    path('search/', views.search, name='app-poisk'),

    # === - look for real metadata request.META from sevrer - ===
    path('display_meta/', views.display_meta),

]
