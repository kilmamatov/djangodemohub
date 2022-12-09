from django.urls import path
import core.views

urlpatterns = [
    path('', core.views.index),
    path('persons/', core.views.persons),
    path('todolist/', core.views.todolist),
    path('todo/', core.views.todo),
]
