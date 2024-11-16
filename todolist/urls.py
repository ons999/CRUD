from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('', views.index, name='todolist'),  # Home page of the todo app
    path('del/<str:item_id>/', views.remove, name='del'),  # URL for deleting an item
]
