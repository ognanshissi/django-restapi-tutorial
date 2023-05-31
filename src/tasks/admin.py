from django.contrib import admin
from tasks.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", 'is_completed', 'created_at')


admin.site.register(Task, TaskAdmin)
