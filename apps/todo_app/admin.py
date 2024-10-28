from django.contrib import admin
from .models import User, Todo

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'created_at', 'age']

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'description', 'image']