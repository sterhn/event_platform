from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)# Create your models here.
    
    def __str__(self):
        return self.name