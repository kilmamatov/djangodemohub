from django.shortcuts import render
from django.utils import timezone
from core import models
import project.settings


def index(request):
    now = timezone.now()
    person = models.Person.objects.last()
    phone = models.Person.objects.last().phone
    your_time_zone = project.settings.TIME_ZONE
    return render(
        request,
        'core/index.html',
        context={
            'person': person,
            'dt': now,
            'phone': phone,
            'tp': your_time_zone,
        })

