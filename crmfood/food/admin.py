from django.contrib import admin

from .models import *
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class TableInline(admin.TabularInline):
    model = Table
    extra = 1

class RoleInline(admin.TabularInline):
    model = Role
    extra = 1

class CourseAdmin(admin.ModelAdmin):  
    inlines = [TableInline, RoleInline] 

