from rest_framework import mixins, generics, views, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django_filters import rest_framework as filters

from .models import Goal, Task, If_then, User, Help

from .serializers import GoalSerializer, TaskSerializer, GoalTaskListSerializer, If_thenSerializer, UserSerializer, HelpSerializer

from .custom_permission import GoalPermission,TaskPermission, If_thenPermission, UserPermission
from rest_framework import permissions


class GoalViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = (GoalPermission, permissions.IsAuthenticated,)

    def get_serializer_context(self):
        self.request.data["user"] = self.request.user.id
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission, permissions.IsAuthenticated,)

class SignInViewset(viewsets.GenericViewSet, mixins.CreateModelMixin,):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

class HelpViewset(viewsets.GenericViewSet, mixins.CreateModelMixin,):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer
    permission_classes = (permissions.AllowAny,)