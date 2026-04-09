from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('home/', views.home_page, name='home'),
    path('login/', views.login, name='login'),
    path('addBook/', views.addBook, name='addBook'),
    path('editBook/<int:pk>/', views.editBook, name='editBook'),
]