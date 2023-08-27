from django.db import models

# Create your models here.
class ToDo(models.Model):
    name = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)