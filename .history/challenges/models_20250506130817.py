from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Challenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    points = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title
    
class UserChallenge(models.Model):
    user = models.For
    
