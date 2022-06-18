from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(blank=True, null=True)
    Author = models.ForeignKey(
        get_user_model(), blank=True, null=True, on_delete=models.CASCADE)
    Created_date = models.DateTimeField(blank=True, null=True)
    Published_date = models.DateTimeField(blank=True, null=True)
