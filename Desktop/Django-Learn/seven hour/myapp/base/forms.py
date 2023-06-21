from django.forms import ModelForm
from .models import *


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'


# class LangaugeForm(ModelForm):

#     class Meta:
#         model = Langauge
#         fields = '__all__'