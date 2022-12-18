from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404


def Index(request):
    return render(request, "chat/index.html")

def RoomList(request):
    rooms_obj = models.Room.objects.filter(status= 'pennding',Room_Message__isnull = False).all()
    return render(request, "chat/RoomList.html", context={"rooms":set(rooms_obj)})

def  RoomAdmin(request,room_name):
    room_obj=get_object_or_404 (models.Room ,room_id=room_name)
    room_obj.status = 'active'
    room_obj.save()
    messages_obj= models.Message.objects.filter(room_id=room_obj.id).all()
    return render(request, "chat/Room.html",context={"room_name":room_name , "room_obj":room_obj ,"messages_obj":messages_obj })