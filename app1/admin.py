from django.contrib import admin
from .models import CustomUser,Todo
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser,UserAdmin)
admin.site.register(Todo)
