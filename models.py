from django.db import models
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    
class TaskHistory(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    deleted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
