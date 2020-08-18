from django.contrib import admin
admin.autodiscover()
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

#from usersapp import views as registerForm
from django.contrib.auth import views as logViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    #path('reg/', registerForm.register, name='reg'),
    path('log/', logViews.LoginView.as_view(template_name='login.html'), name='log'),
    #path('exit/', logViews.LogoutView.as_view(template_name='exit.html'), name='exit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)