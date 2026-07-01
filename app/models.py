from pydantic import BaseModel
from typing import List


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


class Recommendation(BaseModel):
    name: str
    url: str
    test_type: str


class ChatResponse(BaseModel):
    reply: str
    recommendations: List[Recommendation]
    end_of_conversation: bool

from dataclasses import dataclass
from typing import List


@dataclass
class Assessment:
    entity_id: str
    name: str
    link: str
    description: str
    duration: str
    remote: str
    adaptive: str
    job_levels: List[str]
    languages: List[str]
    keys: List[str]