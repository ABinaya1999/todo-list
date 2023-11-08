from django.db import models

# Create your models here.

class Todo(models.Model):
    body=models.CharField( max_length=500)
    completed=models.BooleanField(default=False)
    updated=models.DateField(auto_now=True)
    created=models.DateField(auto_now_add=True)
