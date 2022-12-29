from django.utils import timezone
from django.http import JsonResponse
from core import models
import project.settings
from django.shortcuts import render, get_object_or_404
# from django.views.generic import TemplateView, ListView


"""
class Index(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['dt'] = timezone.now()
        return c
"""


def index(request):
    """
    Вариант через классы
    class Index(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['dt'] = timezone.now()
        return c
    :param request:
    :return:
    """
    now = timezone.now()
    your_time_zone = project.settings.TIME_ZONE
    response = render(request, 'core/index.html', context={'title': 'Главная страница', 'dt': now, 'tp': your_time_zone})
    return response


"""
class Persons(ListView):
    model = models.Person
"""


def test(request):
    object_list = []
    for p in models.Todo.objects.all():
        object_list.append({
            'id': p.id,
            'name': p.name,
            'content': p.content,
            'created': p.created,
            'done': p.done
        })
    return JsonResponse({'result': object_list})


def todolist(request, id):
    """
    Указываем через запрос id
    получаем все данные обьекта
    :param request:
    :param id:
    :return:
    """
    p = models.TodoList.objects.get(id=id)
    return render(request, 'core/todo.html', context={
        'title': 'TodoList',
        'name': p.title,
        'content': p.content,
        'created': p.created,
        'due_date': p.due_date,
    })


def todojson(request, id):
    p = get_object_or_404(models.TodoList, id=id)
    detail = {
        'id': p.id,
        'name': p.title,
        'content': p.content,
        'created': p.created,
        'due_date': p.due_date,
    }
    return JsonResponse({'User': detail}, status=200)



