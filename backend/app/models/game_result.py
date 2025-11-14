"""Game result model for analytics and tracking."""

from sqlalchemy import Column, String, Integer, ForeignKey, UUID, Text
from sqlalchemy.dialects.postgresql import JSONB, INET
from sqlalchemy.orm import relationship, validates

from app.models.base import BaseModel


class GameResult(BaseModel):
    """Game result model for tracking roulette spins and analytics."""
    
    __tablename__ = "game_results"
    
    session_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    selected_name_id = Column(
        UUID(as_uuid=True),
        ForeignKey("names.id", ondelete="SET NULL"),
        nullable=True
    )
    selected_name_snapshot = Column(JSONB, nullable=False)
    available_names = Column(JSONB, nullable=False)
    spin_duration_ms = Column(Integer, nullable=True)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )
    user_ip = Column(INET, nullable=True)
    user_agent = Column(Text, nullable=True)
    
    # Relationships
    selected_name = relationship("Name", back_populates="game_results")
    user = relationship("User", back_populates="game_results")
    
    @validates('session_id')
    def validate_session_id(self, key: str, session_id) -> str:
        """Validate session ID is provided."""
        if session_id is None:
            raise ValueError("Session ID is required")
        return session_id
    
    @validates('selected_name_snapshot')
    def validate_selected_name_snapshot(self, key: str, snapshot: dict) -> dict:
        """Validate selected name snapshot contains required fields."""
        if not isinstance(snapshot, dict):
            raise ValueError("Selected name snapshot must be a dictionary")
        
        required_fields = {'id', 'name'}
        if not all(field in snapshot for field in required_fields):
            raise ValueError(f"Selected name snapshot must contain fields: {required_fields}")
        
        return snapshot
    
    @validates('available_names')
    def validate_available_names(self, key: str, names: list) -> list:
        """Validate available names is a list of name data."""
        if not isinstance(names, list):
            raise ValueError("Available names must be a list")
        
        if len(names) == 0:
            raise ValueError("Available names cannot be empty")
        
        # Validate each name entry has required fields
        for name_data in names:
            if not isinstance(name_data, dict):
                raise ValueError("Each available name must be a dictionary")
            if 'id' not in name_data or 'name' not in name_data:
                raise ValueError("Each available name must have 'id' and 'name' fields")
        
        return names
    
    @validates('spin_duration_ms')
    def validate_spin_duration(self, key: str, duration: int | None) -> int | None:
        """Validate spin duration is reasonable."""
        if duration is not None:
            if duration < 0:
                raise ValueError("Spin duration cannot be negative")
            if duration > 300000:  # 5 minutes max
                raise ValueError("Spin duration cannot exceed 5 minutes")
        return duration
    
    @validates('user_agent')
    def validate_user_agent(self, key: str, user_agent: str | None) -> str | None:
        """Validate user agent length."""
        if user_agent is not None and len(user_agent) > 1000:
            raise ValueError("User agent cannot exceed 1000 characters")
        return user_agent
    
    def __repr__(self) -> str:
        """String representation of game result."""
        selected_name = self.selected_name_snapshot.get('name', 'Unknown') if self.selected_name_snapshot else 'Unknown'
        return f"<GameResult(id={self.id}, session={self.session_id}, selected='{selected_name}')>"