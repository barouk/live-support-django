import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from . import models

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = str (self.scope["url_route"]["kwargs"]["room_name"])
        self.room_group_name = "chat_%s"%self.room_name
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        self.room_obj = self.craeteroom()
        self.accept()
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        self.save_message(message)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message , "username":username}
        )
    #@database_sync_to_async
    def craeteroom(self):
        return  models.Room.objects.create(room_id=self.room_group_name)

    def save_message(self,message):
        models.Message.objects.create(user='user', message=message ,room=self.room_obj  )
    def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        self.send(text_data=json.dumps({"message": message ,"username":username}))







class ChatConsumerAdmin(WebsocketConsumer):
    def connect(self):
        self.room_name = str (self.scope["url_route"]["kwargs"]["room_name"])
        self.room_group_name = "%s"%self.room_name

        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        self.room_obj = self.getroom()
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        self.save_message(message)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message,"username":username}
        )
    #@database_sync_to_async
    def getroom(self):
        return  models.Room.objects.filter(room_id=self.room_group_name).first()

    def save_message(self,message):
        models.Message.objects.create(user='admin', message=message ,room=self.room_obj  )

    def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        self.send(text_data=json.dumps({"message": message ,"username":username}))




