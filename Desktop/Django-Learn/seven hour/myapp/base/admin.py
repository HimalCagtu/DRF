from django.contrib import admin
from . import models
from .models import *

# Register your models here.

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)

