from django.db import models


class Person(models.Model):
    name = models.CharField('Имя', max_length=15)
    phone = models.IntegerField('Номер телефона')

    class Meta:
        verbose_name_plural = 'Заказчики'

    def __str__(self):
        return self.name
