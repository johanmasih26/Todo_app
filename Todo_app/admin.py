from Todo_app.models import Task
from django.contrib import admin

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user','title','complete','description','created']

admin.site.register(Task,TaskAdmin)