from django.contrib import admin

# Register your models here.
from .models import *

class StudentDetailA(admin.ModelAdmin):
    list_display = ('full_name', 'country')
    list_filter = ('country', )

admin.site.register(StudentDetail)

