from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=16, unique=True, verbose_name='телефон')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создание')
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name='возраст')

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo', verbose_name='пользовател')
    title = models.CharField(max_length=255, verbose_name='тема')
    description = models.TextField(blank=True, verbose_name='описание')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    image = models.ImageField(upload_to='todo_images/', blank=True, verbose_name='фотография')
