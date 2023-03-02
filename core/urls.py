from django.urls import path
import core.views

urlpatterns = [
    path('', core.views.index, name='home'),
    path('tags/', core.views.Tags.as_view()),
    path('test/', core.views.tags),
]
