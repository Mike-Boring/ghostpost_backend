from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from homepage.models import BoastsRoasts, MyUser


# Register your models here.

admin.site.register(MyUser, UserAdmin)
admin.site.register(BoastsRoasts)
