from rest_framework import generics, permissions
from .models import User, Todo
from .serializers import UserSerializer, TodoSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

class TodoDeleteAllView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        request.user.todos.all().delete()
        return Response(status=204)
