from django.conf.urls import url, include
from .import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^showcase/', views.showcase, name='showcase'),
    url(r'^show/', views.show, name='show'),
]