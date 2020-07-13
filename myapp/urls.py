# for defined path template to conect with url
from django.urls import path, include
from myapp.views import MainPageView
from myapp import views

urlpatterns = [
    path('', MainPageView.as_view(), name='app-base'),
    path('search/', views.search, name='app-poisk'),
    path('display_meta/', views.display_meta),

]
