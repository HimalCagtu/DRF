from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=20)
    avatar = models.ImageField(null=True, default='xyz.jpeg')
    password = models.CharField(max_length=200)

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS= []
    
    def __str__(self) -> str:
        return self.username
        

class Product(models.Model):

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    digital = models.BooleanField(default=False)
    image = models.ImageField(null = True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateField(auto_now_add=True)
    transaction_id = models.CharField(max_length=200)
    


    def __str__(self) -> str:
        return self.id


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True,blank=True)
    quantity =models.IntegerField(default=0, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAdderess(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)