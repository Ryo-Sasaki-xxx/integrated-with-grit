from django.urls import path, include

from django.contrib import admin
from with_grit import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

router1 = routers.SimpleRouter()
router1.register('goals', views.GoalViewSet)
router2 = routers.SimpleRouter()
router2.register('tasks', views.TaskViewSet)
router3 = routers.SimpleRouter()
router3.register('if-then', views.If_thenViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/goal-task-list/', views.GoalTaskListAPIView.as_view()),
    path('api/', include(router1.urls)),
    path('api/', include(router2.urls)),
    path('api/', include(router3.urls)),
    path('api-auth/jwt/', jwt_views.TokenObtainPairView.as_view()),
    path('api-auth/jwt/refresh', jwt_views.TokenRefreshView.as_view()),
]