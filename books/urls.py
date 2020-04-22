from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.book_new, name='book_new'),
    path('search/', views.search, name='search_direct'),
]