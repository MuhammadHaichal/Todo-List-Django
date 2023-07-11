from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path('remove/(?P<removeItems>[0-9]+)', views.remove, name="remove_taks"),
    re_path('clear/', views.clear, name="clear_taks"),

]
