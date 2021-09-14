from django.contrib import admin

# Register your models here.
from profiles_api import models

# UserProfileを管理画面に登録
admin.site.register(models.UserProfile)
