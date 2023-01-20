from django.urls import path
from rango import views

app_name = 'rango'

urlspatterns = [
    path('', views.index, name='index'),
	]