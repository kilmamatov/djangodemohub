import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.timezone import now


class Person(models.Model):
    name = models.CharField('Имя', max_length=15)
    phone = models.IntegerField('Номер телефона')

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    def __str__(self):
        return self.name


class TodoList(models.Model):
    title = models.CharField('Имя', max_length=25)
    content = models.TextField('Задачи', blank=True)
    created = models.DateField('Дата начала', default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField('Дата завершения', default=timezone.now().strftime("%Y-%m-%d"))

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.title


User = get_user_model()


class Todo(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='todo')
    name = models.CharField('Название', unique=True, max_length=255, blank=True,)
    content = models.TextField('Описание', help_text='Какая либо подсказка, если имеет смысл')
    priority = models.IntegerField('Приоритет сортировки', default=1)
    done = models.DateTimeField('Выполнено', null=True, blank=True)  # BooleanField так же можно использовать
    created = models.DateTimeField('Создан', auto_now_add=True,)
    update = models.DateTimeField('Обновлен', auto_now=True)

    class Meta:
        verbose_name = 'Дела'
        verbose_name_plural = 'Список дел'

    def __str__(self):
        return self.name

    def duration(self) -> datetime.timedelta:
        return now() - self.created
