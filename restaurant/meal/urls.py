from django.urls import path
from . import views

app_name='meal'
urlpatterns = [
    path('', views.index,name='items'),
]