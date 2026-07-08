"""
Configuration settings for FantasyCamAI
"""
import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Claude Model
CLAUDE_MODEL = "anthropic/claude-3-5-sonnet"

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./fantasycamai.db")

# Frontend
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

# Language settings
DEFAULT_LANGUAGE = "fr"  # French by default
SUPPORTED_LANGUAGES = ["fr", "en", "es", "de", "it", "pt", "ja", "zh"]

# Avatar settings
AVATAR_PERSONALITIES = {
    "douce": "Douce, empathique et chaleureuse",
    "flirtante": "Flirtante, amusante et jouense",
    "amie": "Amie fidèle et attentive",
    "intellectuelle": "Intelligente et cultivée",
    "aventuriere": "Aventurière et audacieuse"
}

AVATAR_STYLES = {
    "cheveux": ["blond", "brun", "roux", "noir", "gris"],
    "yeux": ["bleu", "brun", "vert", "gris", "noir"],
    "style": ["casual", "elegant", "sportif", "boheme", "futuriste"]
}

# TTS (Text-to-Speech)
TTS_ENGINE = "pyttsx3"  # pyttsx3 or google
TTS_VOICE_FEMALE = True
TTS_RATE = 150  # Words per minute
TTS_VOLUME = 0.9

# Pricing
FREE_TIER_MINUTES = 5  # Free trial in minutes
PREMIUM_TIER_PRICE = 9.99  # Per month
PAY_PER_MINUTE_PRICE = 0.99  # Per minute

print("✅ Configuration loaded successfully")
