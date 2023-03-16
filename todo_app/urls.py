from django.urls import path
from .views import get_todos, create_todo, update_todo, delete_todo, get_todo

urlpatterns = [
    path('todos/', get_todos),
    path('create-todo/', create_todo),
    path('update-todo/<int:pk>/', update_todo),
    path('delete-todo/<int:pk>/', delete_todo),
    path('todo/<int:pk>/', get_todo)
]