from django.urls import path
import core.views

urlpatterns = [
    # path('', core.views.Index.as_view()),
    path('', core.views.index, name='home'),
    path('test/', core.views.test, ),
    # path('persons/', core.views.Persons.as_view()),
    path('todolist/<int:id>/', core.views.todolist),
    path('todo/<int:id>/', core.views.todojson),
]
