from django.shortcuts import render
from . import models

def Index(request):
    return render(request, "chat/index.html")

def RoomList(request):
    rooms_obj = models.Room.objects.filter(status= 'pennding').all()
    return render(request, "chat/RoomList.html", context={"rooms":rooms_obj})

