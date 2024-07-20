from pydantic import BaseModel, Field
from datetime import datetime

class Message(BaseModel):
    sender_id: str
    sent_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    text: str

class Conversation(BaseModel):
    _id: str | None = None
    initiator_id: int
    participant_id: int
    messages: list[Message | None] = []