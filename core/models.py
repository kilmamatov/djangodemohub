from django.db import models
from django.utils import timezone


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
        return self.title, self.content



