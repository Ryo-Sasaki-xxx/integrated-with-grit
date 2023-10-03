from django.urls import path, include

from django.contrib import admin
from with_grit import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

goal_router = routers.SimpleRouter()
goal_router.register('goals', views.GoalViewSet)

task_router = routers.SimpleRouter()
task_router.register('tasks', views.TaskViewSet)

if_then_router = routers.SimpleRouter()
if_then_router.register('if-then', views.If_thenViewSet)

user_router = routers.SimpleRouter()
user_router.register('users', views.UserViewSet)

sign_in_router = routers.SimpleRouter()
sign_in_router.register('sign-in', views.SignInViewset)

help_router = routers.SimpleRouter()
help_router.register('help', views.HelpViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/goal-task-list/', views.GoalTaskListAPIView.as_view()),
    path('api/', include(goal_router.urls)),
    path('api/', include(task_router.urls)),
    path('api/', include(if_then_router.urls)),
    path('api/', include(user_router.urls)),
    path('api/', include(sign_in_router.urls)),
    path('api/', include(help_router.urls)),
    path('api/auth-jwt/', jwt_views.TokenObtainPairView.as_view()),
    path('api/auth-jwt/refresh', jwt_views.TokenRefreshView.as_view()),
]