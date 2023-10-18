import django_filters
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import *
from .models import *
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'perevall.html'


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()


class PerevalAddedViewSet(viewsets.ModelViewSet):
    serializer_class = PerevalAddedSerializer
    queryset = Pereval_added.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('users__email',)
    http_method_names = ['get', 'post', 'head', 'patch', 'options']

    # переопределяем метод, чтобы получить требуемые сообщения по ТЗ
    def create(self, request, *args, **kwargs):
        serializer = PerevalAddedSerializer(data=request.data)
        # print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': 'Успех',
                    'id': serializer.data['id']
                }
            )
        if status.HTTP_400_BAD_REQUEST:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'не успех',
                    'id': None
                }
            )
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response(
                {
                    'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'message': 'Ошибка при выполнении операции',
                    'id': None
                }
            )

    # даем возможность частично изменять перевал
    def partial_update(self, request, *args, **kwargs):
        perevall = self.get_object()
        if perevall.status == 'new':
            serializer = PerevalAddedSerializer(perevall, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'state': '1',
                        'message': 'Изменения успешно внесены'
                    }
                )
            else:
                return Response(
                    {
                        'state': '0',
                        'message': serializer.errors
                    }
                )
        else:
            return Response(
                {
                    'state': '0',
                    'message': f'Текущий статус: {perevall.get_status_display()}, данные не могут быть изменены!'
                }
            )

    def get_queryset(self):
        queryset = Pereval_added.objects.all()
        perevall_id = self.request.query_params.get('perevall_id', None)
        users_id = self.request.query_params.get('users_id', None)
        if perevall_id is not None:
            queryset = queryset.filter(users__perevall_id=perevall_id)
        if users_id is not None:
            queryset = queryset.filter(users_id=users_id)
            return queryset
