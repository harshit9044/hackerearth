from django.urls import path, include
from . import views

app_name = 'wine'
urlpatterns = [

    path('', views.search, name='search'),

    ]
