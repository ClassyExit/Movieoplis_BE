from django.contrib import admin

# Register your models here.
from .models import User, UserVideoPermissionQueue



admin.site.register(User)
admin.site.register(UserVideoPermissionQueue)