from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    #this lets us see it is working
    def __str__(self):
        return self.title

