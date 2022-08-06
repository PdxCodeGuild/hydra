from django.urls import path
from . import views

app_name = 'journal_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('journal/', views.journal, name='journal'),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('add_entry', views.add_entry, name="add_entry"),
    path('listing', views.listing, name='listing'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('save/<int:id>', views.save, name='save'),
]