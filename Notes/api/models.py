from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    owner = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_created']
    
    