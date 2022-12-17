from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User=get_user_model()


STATUS_CHOIEES=(
    ("closed","closed"),
    ("pennding","pennding"),
    ("active","active"),
)


class Room(models.Model):
    room_id= models.CharField(max_length=50 , null=False , blank=False)
    status = models.CharField(max_length=12 , null=False , blank=False , choices=STATUS_CHOIEES,default='pennding')
    support_user = models.ForeignKey(User , null=True , blank=False ,on_delete = models.SET_NULL)