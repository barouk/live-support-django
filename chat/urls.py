# chat/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.Index, name="index"),
    path("room/list/", views.RoomList, name="RoomList"),
    path("room/list/<str:room_name>/", views.RoomAdmin, name="RoomAdmin"),

]