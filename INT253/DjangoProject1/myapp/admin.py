from django.contrib import admin

# Register your models here.
from .models import Student, Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'is_active', 'student')
    list_filter = ('is_active',)
    search_fields = ('name', 'email')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'duration')
    search_fields = ('name',)