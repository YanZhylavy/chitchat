from bson import ObjectId
from pymongo.collection import Collection

from chitchat.settings import DB
from .schemas import Conversation, Message


class MongoManager:

    collection: Collection = DB["conversations"]

    @classmethod
    def get_or_create_conversation(cls, initiator_id: int, participant_id: int) -> dict:
        if (existing_conversation := cls.get_conversation(initiator_id, participant_id, projection=["participant_id",])):
            return existing_conversation
        model = Conversation(initiator_id=initiator_id,
                             participant_id=participant_id)
        cls.collection.insert_one(model.model_dump())
        return model.model_dump()

    @classmethod
    def get_conversation(cls, participant_1: int, participant_2: int, projection=None) -> dict | None:
        query = {"$or": [
            {"initiator_id": participant_1, "participant_id": participant_2},
            {"initiator_id": participant_2, "participant_id": participant_1}
        ]}
        conversation = cls.collection.find_one(query, projection=projection)
        if conversation:
            return str(conversation["_id"])

    @classmethod
    def push_message(cls, document_id: str, message: dict) -> tuple[int, dict]:
        validated_message = Message(**message).model_dump()
        filter = {"_id": ObjectId(document_id)}
        query = {"$push": {"messages": validated_message}}
        result = cls.collection.update_one(filter, query)
        return  (result.modified_count, validated_message)

    @classmethod
    def get_paginated_messages(cls, conversation_id, chunk, chunk_size=20):
        skip = (chunk - 1) * chunk_size   
        result = cls.collection.find_one(
            {"_id": ObjectId(conversation_id)},
            {"messages": {"$slice": [skip, chunk_size]}}
        ) 
        return result["messages"] if result else []