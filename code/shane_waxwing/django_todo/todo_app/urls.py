from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add/', views.add, name = 'add'),
    path('complete/', views.complete, name = 'complete'),
    path('delete/', views.delete, name='delete'),
]