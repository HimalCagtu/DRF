from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import *

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User , null=True,blank =True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False)
    created = models.DateField(auto_now_add=True)
    due = models.DateField(null=True, blank=False)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name
    
    

class Completed(models.Model):
    user = models.ForeignKey(User , null=True,blank =True, on_delete=models.CASCADE)
    ctask = models.CharField(max_length=200)
    created =models.DateTimeField(auto_now_add=True)



    def __str__(self) -> str:
        return self.ctask