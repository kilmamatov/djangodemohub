from django.contrib import admin
from core import models


class TodoResultInline(admin.TabularInline):
    model = models.TodoResult


@admin.register(models.Todo)
class Todo(admin.ModelAdmin):
    inlines = (TodoResultInline,)
    list_display = ('name', 'done',)
    search_fields = ('name',)

