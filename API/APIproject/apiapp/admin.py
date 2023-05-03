from django.contrib import admin
from .models import PythonModel

# Register your models here.
class PythonAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','email','mobile']

admin.site.register(PythonModel,PythonAdmin)
