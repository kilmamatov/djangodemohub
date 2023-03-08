from django.urls import path
from rest_framework.routers import DefaultRouter
import core.views

urlpatterns = [
    path('', core.views.index, name='home'),
    # path('tags/', core.views.Tags.as_view()),
    # path('tags/<pk>', core.views.Tag.as_view()),
    # path('test/', core.views.tags),
]

router = DefaultRouter()
router.register('tags', core.views.TagViewSet, basename="tag")
router.register('todo', core.views.TodoViewSet, basename='todo')
urlpatterns += router.urls
