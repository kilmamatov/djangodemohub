from django.contrib import admin
from core import models


@admin.register(models.Person)
class Person(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')
    pass


@admin.register(models.TodoList)
class TodoList(admin.ModelAdmin):
    list_display = ('title', 'created', 'id')
    search_fields = ('title',)
    list_filter = ('created',)


@admin.register(models.Todo)
class Todo(admin.ModelAdmin):
    list_display = ('name', 'id', 'priority', 'created', 'update', 'done')
    search_fields = ('name', 'id')
    list_filter = ('created', 'done')
