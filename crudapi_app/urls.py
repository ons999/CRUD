from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list),         # List and create books
    path('books/<int:pk>/', views.book_detail),  # Retrieve, update, or delete a specific book
]
