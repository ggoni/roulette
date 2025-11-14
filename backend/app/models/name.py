"""Name model for roulette participants."""

from sqlalchemy import Column, String, Text, Boolean, Integer, ForeignKey, UUID
from sqlalchemy.orm import relationship, validates

from app.models.base import BaseModel


class Name(BaseModel):
    """Name model for managing roulette participants."""
    
    __tablename__ = "names"
    
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False, index=True)
    weight = Column(Integer, default=1, nullable=False)
    created_by = Column(
        UUID(as_uuid=True), 
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )
    
    # Relationships
    creator = relationship("User", back_populates="created_names")
    game_results = relationship("GameResult", back_populates="selected_name")
    
    @validates('name')
    def validate_name(self, key: str, name: str) -> str:
        """Validate name format and length."""
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        name = name.strip()
        if len(name) < 1:
            raise ValueError("Name must be at least 1 character long")
        if len(name) > 255:
            raise ValueError("Name cannot exceed 255 characters")
        return name
    
    @validates('weight')
    def validate_weight(self, key: str, weight: int) -> int:
        """Validate weight is positive."""
        if weight < 1:
            raise ValueError("Weight must be at least 1")
        if weight > 1000:
            raise ValueError("Weight cannot exceed 1000")
        return weight
    
    @validates('description')
    def validate_description(self, key: str, description: str | None) -> str | None:
        """Validate description length."""
        if description is not None:
            if len(description) > 1000:
                raise ValueError("Description cannot exceed 1000 characters")
            return description.strip() if description.strip() else None
        return description
    
    def __repr__(self) -> str:
        """String representation of name."""
        status = "active" if self.is_active else "inactive"
        return f"<Name(id={self.id}, name='{self.name}', {status}, weight={self.weight})>"