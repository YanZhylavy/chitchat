from asgiref.sync import sync_to_async
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from .managers import MongoManager as mngr


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        sucsess, processed_message = await self.apush_message(
            self.room_name, text_data_json)

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": processed_message})

    async def chat_message(self, event):
        message = event["message"]

        await self.send(text_data=json.dumps(message))

    @sync_to_async
    def apush_message(self, *args, **kwargs): 
        return mngr.push_message(*args, **kwargs)

