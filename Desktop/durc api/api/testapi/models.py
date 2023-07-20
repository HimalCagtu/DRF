from django.db import models

# Create your models here.
class Item(models.Model):

    name = models.CharField(max_length=222)
    created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    
