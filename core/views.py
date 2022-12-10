from django.utils import timezone
from django.http import JsonResponse
from core import models
import project.settings
from django.shortcuts import render, get_object_or_404



def index(request):
    now = timezone.now()
    person = models.Person.objects.last().name
    phone = models.Person.objects.last().phone
    your_time_zone = project.settings.TIME_ZONE
    response = render(request, 'core/index.html', context={'dt': now, 'tp': your_time_zone, 'person': person, 'phone': phone})
    return response


def persons(request):
    object_list = []
    for p in models.Person.objects.all():
        object_list.append({
            'id': p.id,
            'name': p.name,
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


def todo(request, id):
    p = get_object_or_404(models.TodoList, id=id)
    detail = {
        'id': p.id,
        'name': p.title,
        'content': p.content,
        'created': p.created,
        'due_date': p.due_date,
    }
    return JsonResponse({'User': detail}, status=200)
