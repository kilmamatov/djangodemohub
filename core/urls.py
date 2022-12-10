from django.urls import path
import core.views

urlpatterns = [
    path('', core.views.index),
    path('persons/', core.views.persons),
    path('todolist/<int:id>/', core.views.todolist),
    path('todo/<int:id>/', core.views.todo),
]
