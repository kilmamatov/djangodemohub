from django.contrib import admin
from core import models


@admin.register(models.Todo)
class Todo(admin.ModelAdmin):
    list_display = ('name', 'id', 'priority', 'created', 'update', 'done', 'duration')
    search_fields = ('name', 'id')
    list_filter = ('created', 'done')
