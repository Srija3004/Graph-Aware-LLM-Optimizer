"""
Configuration management for the Graph-Aware LLM backend.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_parse_none_str='null'
    )
    
    # Mistral AI Configuration
    mistral_api_key: str = ""
    mistral_model: str = "mistral-medium"
    
    # Application Settings
    environment: str = "development"
    log_level: str = "INFO"
    
    # Performance Settings
    max_graph_size: int = 100
    timeout_seconds: int = 30


# Global settings instance
settings = Settings()

# CORS origins - defined separately to avoid parsing issues
CORS_ORIGINS = ["http://localhost:5173", "http://localhost:3000", "https://graph-aware-llm-optimizer.vercel.app"]
