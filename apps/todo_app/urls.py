from django.urls import path
from .views import UserRegistrationView, TodoListCreateView, TodoDetailView, TodoDeleteAllView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('todos/', TodoListCreateView.as_view(), name='todo_list_create'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('todos/delete_all/', TodoDeleteAllView.as_view(), name='todo_delete_all'),
]
