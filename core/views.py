from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now
from core import models
from django.shortcuts import render
from core import filters
from core import serializers
from django_filters.rest_framework import DjangoFilterBackend


# class RegisterUser(GenericAPIView):
#     queryset = models.User
#
#     def post(self, request):
#         # todo
#         pass


class TagViewSet(ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    queryset = models.Tag.objects.all()
    serializer_class = serializers.Tag
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.Tag


class TodoViewSet(ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    serializer_class = serializers.Todo
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.Todo

    def get_queryset(self):
        return models.Todo.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post', 'put', 'patch'])
    def set_done(self, request, pk=None):
        todo: models.Todo = self.get_object()
        if not todo.done:
            todo.done = now()
            todo.save(update_fields=['done'])
        serializer = serializers.Todo(instance=todo)
        return Response(serializer.data)

    @action(detail=True, methods=['post', 'put', 'patch'])
    def unset_done(self, request, pk=None):
        todo: models.Todo = self.get_object()
        if todo.done:
            todo.done = None
            todo.save(update_fields=['done'])
        serializer = serializers.Todo(instance=todo)
        return Response(serializer.data)


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
    response = render(request, 'core/index.html', context={'title': 'Главная страница'})
    return response


# def test(request):
#     object_list = []
#     for p in models.Todo.objects.all():
#         object_list.append({
#             'id': p.id,
#             'name': p.name,
#             'content': p.content,
#             'created': p.created,
#             'done': p.done
#         })
#     return JsonResponse({'result': object_list})


# def todolist(request, id):
#     """
#     Указываем через запрос id
#     получаем все данные обьекта
#     :param request:
#     :param id:
#     :return:
#     """
#     p = models.TodoList.objects.get(id=id)
#     return render(request, 'core/todo.html', context={
#         'title': 'TodoList',
#         'name': p.title,
#         'content': p.content,
#         'created': p.created,
#         'due_date': p.due_date,
#     })


# def todojson(request, id):
#     p = get_object_or_404(models.TodoList, id=id)
#     detail = {
#         'id': p.id,
#         'name': p.title,
#         'content': p.content,
#         'created': p.created,
#         'due_date': p.due_date,
#     }
#     return JsonResponse({'User': detail}, status=200)


# def tags(request):
#     search_serializer = serializers.TagSearch(data=request.GET)
#     if not search_serializer.is_valid():
#         return JsonResponse(search_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     f = filters.Tag(request.GET, queryset=models.Tag.objects.all())
#     serializer = serializers.Tag(instance=f.qs, many=True)
#     return JsonResponse({'results': serializer.data})





