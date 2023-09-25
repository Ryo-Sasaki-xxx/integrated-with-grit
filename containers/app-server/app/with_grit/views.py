from rest_framework import mixins, generics, views, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django_filters import rest_framework as filters

from .models import Goal, Task, If_then

from .serializers import GoalSerializer, TaskSerializer, GoalTaskListSerializer, If_thenSerializer

from .custom_permission import GoalPermission,TaskPermission, If_thenPermission
from rest_framework import permissions



class GoalViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = (GoalPermission, permissions.IsAuthenticated,)

class TaskViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (TaskPermission, permissions.IsAuthenticated,)

class If_thenViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = If_then.objects.all()
    serializer_class = If_thenSerializer
    permission_classes = (If_thenPermission, permissions.IsAuthenticated,)

class GoalTaskListFilter(filters.FilterSet):
    class Meta:
        model = Goal
        fields = ['user']
    def qs(self, request):
        parent = super().qs
        user = request.user.id
        return parent.filter(user=user)

class GoalTaskListAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        filterset = GoalTaskListFilter(request.query_params, queryset=Goal.objects.all())
        if not filterset.is_valid():
            raise ValidationError(filterset.erros)
        serializer = GoalTaskListSerializer(instance=filterset.qs(request))
        return Response(serializer.data)