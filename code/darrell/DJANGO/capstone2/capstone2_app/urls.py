from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('claims/', views.claims, name='claims'),
    path('email/', views.email, name='email'),
    path('add_claims/', views.add_claims, name='add_claims')
]
