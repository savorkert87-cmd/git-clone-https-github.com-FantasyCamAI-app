"""
FastAPI Main Application - Updated with AI Endpoints
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os

# Import routes
from app.routes import avatars, chat

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="FantasyCamAI API",
    description="AI-powered virtual girlfriend - Chat, customize, connect",
    version="0.2.0"
)

# CORS Configuration
ORIGINS = [
    os.getenv("FRONTEND_URL", "http://localhost:3000"),
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============ HEALTH & INFO ENDPOINTS ============

@app.get("/api/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "ok",
        "version": "0.2.0",
        "service": "FantasyCamAI API"
    }


@app.get("/api/", tags=["Welcome"])
async def root():
    """Welcome to FantasyCamAI API"""
    return {
        "message": "Welcome to FantasyCamAI - Your Virtual AI Girlfriend",
        "version": "0.2.0",
        "features": [
            "🎨 Customize your virtual girlfriend (FREE)",
            "💬 Chat with your avatar in real-time (PAID)",
            "🎥 Webcam integration with lip-sync",
            "🗣️ Multiple languages supported",
            "😊 AI-powered conversations"
        ],
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/api/features", tags=["Info"])
async def get_features():
    """Get available features"""
    return {
        "avatar_customization": {
            "tier": "FREE",
            "description": "Create and customize your virtual girlfriend",
            "features": [
                "Choose name and personality",
                "Select appearance (hair, eyes, style)",
                "Set language preference",
                "Add bio"
            ]
        },
        "webcam_chat": {
            "tier": "PAID",
            "description": "Chat with your avatar in real-time via webcam",
            "features": [
                "Live video conversation",
                "Voice recognition (speech-to-text)",
                "AI-powered responses",
                "Lip-sync animation",
                "Emotion detection"
            ],
            "pricing": {
                "free_trial": "5 minutes",
                "pay_per_minute": "$0.99/minute",
                "monthly_subscription": "$9.99/month"
            }
        }
    }


# ============ INCLUDE ROUTERS ============

app.include_router(avatars.router)
app.include_router(chat.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
