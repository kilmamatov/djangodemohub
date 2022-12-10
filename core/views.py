from django.utils import timezone
from django.http import JsonResponse
from core import models
import project.settings
from django.shortcuts import render



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
    name = models.TodoList.objects.get(id=id).title
    content = models.TodoList.objects.get(id=id).content
    created = models.TodoList.objects.get(id=id).created
    due_date = models.TodoList.objects.get(id=id).due_date
    return render(request, 'core/todo.html', context={
        'title': 'TodoList',
        'name': name,
        'content': content,
        'created': created,
        'due_date': due_date,
    })


def todo(request, id):
    p = models.TodoList.objects.get(id=id)
    detail = {
        'id': p.id,
        'name': p.title,
        'content': p.content,
        'created': p.created,
        'due_date': p.due_date,
    }
    return JsonResponse({'User': detail}, status=200)
