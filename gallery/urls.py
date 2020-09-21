from django.conf.urls import url, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^images/(\d+)', views.show,name = 'show'),
    url(r'^showcase/', views.showcase, name='showcase'),
    url(r'^show/', views.show, name='show'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)