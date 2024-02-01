from django.urls import path
from users import views as users_views
from mainapp import views as mainapp_views
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('api/tasks/', mainapp_views.TaskListView.as_view(), name='task-list'),
    path('api/tasks/add/', mainapp_views.TaskCreateView.as_view(), name='task-create'),
    path('register/', users_views.RegisterView.as_view(), name='registration'),
    path('login/', users_views.MyObtainTokenPairView.as_view(), name='login'),
    path('login/refresh', TokenRefreshView.as_view(), name='token'),
]