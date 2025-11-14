"""SQLAlchemy models package."""

from app.models.base import Base, BaseModel
from app.models.user import User
from app.models.name import Name
from app.models.game_result import GameResult

# Import all models to ensure they're registered with SQLAlchemy
__all__ = [
    "Base",
    "BaseModel", 
    "User",
    "Name",
    "GameResult",
]