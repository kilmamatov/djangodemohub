import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now


User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Todo(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='items')
    name = models.CharField('Название', max_length=25, blank=True, unique=True,)
    content = models.TextField('Описание', help_text='Какая либо подсказка, если имеет смысл')
    priority = models.IntegerField('Приоритет сортировки', default=1)
    done = models.DateTimeField('Выполнено', null=True, blank=True)  # BooleanField так же можно использовать
    created = models.DateTimeField('Создан', auto_now_add=True)
    update = models.DateTimeField('Обновлен', auto_now=True)
    tags = models.ManyToManyField(Tag, verbose_name='Тэги', blank=True, related_name='items')

    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Список дел'

    def __str__(self):
        return self.name

    def duration(self) -> datetime.timedelta:
        return now() - self.created


class TodoResult(models.Model):
    item = models.OneToOneField(Todo, on_delete=models.CASCADE)
    image = models.ImageField()
