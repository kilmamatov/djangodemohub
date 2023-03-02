from django.contrib import admin
from core import models


class TodoResultInline(admin.TabularInline):
    model = models.TodoResult


@admin.register(models.Tag)
class Tag(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(models.Todo)
class Todo(admin.ModelAdmin):
    inlines = (TodoResultInline, )
    list_display = ('name', 'done', 'duration')
    search_fields = ('name',)
