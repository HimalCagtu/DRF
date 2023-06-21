from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

# Create your models here.
class Room(models.Model):
    host= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null =True)
    
    name = models.CharField(max_length=30)
    description = models.TextField(null= True, blank=True)
    # participants = 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.name

class Message(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    room=models.ForeignKey(Room , on_delete=models.CASCADE )
    body = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.body[:50]
    



# class Langauge(models.Model):

#     name = models.CharField(max_length=10)
#     age = models.IntegerField()
#     description = models.TextField(max_length=200, null =True)
#     created =models.DateField(auto_now_add=True)

#     def __str__(self) -> str:
#         return self.name
    
#     class Meta:
#         ordering = ['-created']

