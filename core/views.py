from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import status
from core import models
from django.shortcuts import render, get_object_or_404
from core import filters
from core import serializers
from django_filters.rest_framework import DjangoFilterBackend


class TagViewSet(ReadOnlyModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.Tag
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.Tag


# class Tags(ListAPIView):
#     queryset = models.Tag.objects.all()
#     serializer_class = serializers.Tag
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = filters.Tag
#
#     def list(self, request, *args, **kwargs):
#         serializer = serializers.TagSearch(data=request.query_params)
#         serializer.is_valid(raise_exception=True)
#         return super().list(request, *args, **kwargs)
#
#
# class Tag(RetrieveAPIView):
#     queryset = models.Tag.objects.all()
#     serializer_class = serializers.Tag


def index(request):
    """
    Вариант через классы
    class Index(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['dt'] = timezone.now()
        return c
    :param request:
    :return:
    """
    response = render(request, 'core/index.html', context={'title': 'Главная страница',})
    return response


def test(request):
    object_list = []
    for p in models.Todo.objects.all():
        object_list.append({
            'id': p.id,
            'name': p.name,
            'content': p.content,
            'created': p.created,
            'done': p.done
        })
    return JsonResponse({'result': object_list})


def todolist(request, id):
    """
    Указываем через запрос id
    получаем все данные обьекта
    :param request:
    :param id:
    :return:
    """
    p = models.TodoList.objects.get(id=id)
    return render(request, 'core/todo.html', context={
        'title': 'TodoList',
        'name': p.title,
        'content': p.content,
        'created': p.created,
        'due_date': p.due_date,
    })


def todojson(request, id):
    p = get_object_or_404(models.TodoList, id=id)
    detail = {
        'id': p.id,
        'name': p.title,
        'content': p.content,
        'created': p.created,
        'due_date': p.due_date,
    }
    return JsonResponse({'User': detail}, status=200)


def tags(request):
    search_serializer = serializers.TagSearch(data=request.GET)
    if not search_serializer.is_valid():
        return JsonResponse(search_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    f = filters.Tag(request.GET, queryset=models.Tag.objects.all())
    serializer = serializers.Tag(instance=f.qs, many=True)
    return JsonResponse({'results': serializer.data})





