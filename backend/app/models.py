"""
Database models for FantasyCamAI
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# ============ AVATAR MODELS ============

class AvatarCreate(BaseModel):
    """Model for creating a new avatar"""
    name: str
    personality: str  # "douce", "flirtante", "amie", etc.
    hair_color: str
    eye_color: str
    style: str
    language: str = "fr"
    bio: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Luna",
                "personality": "douce",
                "hair_color": "blond",
                "eye_color": "bleu",
                "style": "casual",
                "language": "fr",
                "bio": "Je suis Luna, votre amie virtuelle douce et attentive!"
            }
        }


class AvatarUpdate(BaseModel):
    """Model for updating an avatar"""
    name: Optional[str] = None
    personality: Optional[str] = None
    hair_color: Optional[str] = None
    eye_color: Optional[str] = None
    style: Optional[str] = None
    bio: Optional[str] = None


class Avatar(BaseModel):
    """Avatar response model"""
    id: str
    user_id: str
    name: str
    personality: str
    hair_color: str
    eye_color: str
    style: str
    language: str
    bio: Optional[str]
    avatar_image_url: Optional[str]
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        json_schema_extra = {
            "example": {
                "id": "avatar_123",
                "user_id": "user_456",
                "name": "Luna",
                "personality": "douce",
                "hair_color": "blond",
                "eye_color": "bleu",
                "style": "casual",
                "language": "fr",
                "bio": "Je suis Luna!",
                "avatar_image_url": "https://...",
                "created_at": "2026-07-08T12:00:00Z",
                "updated_at": "2026-07-08T12:00:00Z",
                "is_active": True
            }
        }


# ============ CHAT MODELS ============

class MessageCreate(BaseModel):
    """Model for sending a chat message"""
    content: str
    user_id: str
    avatar_id: str
    language: Optional[str] = "fr"


class Message(BaseModel):
    """Message response model"""
    id: str
    chat_id: str
    sender: str  # "user" or "avatar"
    content: str
    audio_url: Optional[str]  # URL to TTS audio
    video_url: Optional[str]  # URL to avatar video response
    timestamp: datetime
    emotion: Optional[str]  # Detected emotion

    class Config:
        json_schema_extra = {
            "example": {
                "id": "msg_123",
                "chat_id": "chat_456",
                "sender": "avatar",
                "content": "Salut! Comment ça va?",
                "audio_url": "https://...",
                "video_url": "https://...",
                "timestamp": "2026-07-08T12:00:00Z",
                "emotion": "happy"
            }
        }


class ChatCreate(BaseModel):
    """Model for starting a new chat"""
    user_id: str
    avatar_id: str
    language: str = "fr"


class Chat(BaseModel):
    """Chat session response model"""
    id: str
    user_id: str
    avatar_id: str
    language: str
    created_at: datetime
    updated_at: datetime
    message_count: int
    duration_seconds: int
    is_active: bool
    messages: Optional[list[Message]] = []

    class Config:
        json_schema_extra = {
            "example": {
                "id": "chat_123",
                "user_id": "user_456",
                "avatar_id": "avatar_789",
                "language": "fr",
                "created_at": "2026-07-08T12:00:00Z",
                "updated_at": "2026-07-08T12:05:00Z",
                "message_count": 5,
                "duration_seconds": 300,
                "is_active": True,
                "messages": []
            }
        }


# ============ USER MODELS ============

class UserCreate(BaseModel):
    """Model for creating a new user"""
    email: str
    username: str
    password: str


class User(BaseModel):
    """User response model"""
    id: str
    email: str
    username: str
    created_at: datetime
    subscription_plan: str  # "free", "premium"
    free_minutes_used: int
    avatars: Optional[list[Avatar]] = []


# ============ RESPONSE MODELS ============

class SuccessResponse(BaseModel):
    """Generic success response"""
    success: bool
    message: str
    data: Optional[dict] = None


class ErrorResponse(BaseModel):
    """Generic error response"""
    success: bool
    error: str
    code: str
