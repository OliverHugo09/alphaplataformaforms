from django.urls import path
from django.urls.resolvers import URLPattern
from modulo_password import views

app_name = 'modulo_password'
urlpatterns = [
    path('inicio', views.home, name='home'),
]