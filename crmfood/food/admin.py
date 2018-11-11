from django.contrib import admin

from .models import *
# Register your models here.

class TableInline(admin.TabularInline):
    model = Table
    extra = 1

class RoleInline(admin.TabularInline):
    model = Role
    extra = 1

class CourseAdmin(admin.ModelAdmin):  
    inlines = [TableInline, RoleInline] 


admin.site.register(User)
admin.site.register(Meal)