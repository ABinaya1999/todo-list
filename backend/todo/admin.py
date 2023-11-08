from django.contrib import admin
from . import models

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ["body", "completed", "updated","created"]
admin.site.register(models.Todo)