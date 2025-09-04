from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Client(models.Model):
    client_name = models.CharField(max_length=255,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)


class Project(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name="projects")
    project_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    users = models.ManyToManyField(User,related_name="projects")
