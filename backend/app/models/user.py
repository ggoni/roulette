"""User model for authentication and role management."""

from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import validates, relationship

from app.models.base import BaseModel


class User(BaseModel):
    """User model with authentication and role information."""
    
    __tablename__ = "users"
    
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False, default="user")
    is_active = Column(Boolean, default=True, nullable=False)
    
    # Relationships
    created_names = relationship("Name", back_populates="creator")
    game_results = relationship("GameResult", back_populates="user")
    
    @validates('role')
    def validate_role(self, key: str, role: str) -> str:
        """Validate that role is one of the allowed values."""
        allowed_roles = {'user', 'admin', 'analyst'}
        if role not in allowed_roles:
            raise ValueError(f"Role must be one of {allowed_roles}")
        return role
    
    @validates('username')
    def validate_username(self, key: str, username: str) -> str:
        """Validate username format and length."""
        if not username or len(username.strip()) < 3:
            raise ValueError("Username must be at least 3 characters long")
        if len(username) > 50:
            raise ValueError("Username cannot exceed 50 characters")
        # Allow alphanumeric, underscore, and hyphen
        if not username.replace('_', '').replace('-', '').isalnum():
            raise ValueError("Username can only contain letters, numbers, underscore, and hyphen")
        return username.strip()
    
    @validates('email')
    def validate_email(self, key: str, email: str) -> str:
        """Basic email format validation."""
        if not email or '@' not in email:
            raise ValueError("Valid email address is required")
        if len(email) > 255:
            raise ValueError("Email address cannot exceed 255 characters")
        return email.lower().strip()
    
    def __repr__(self) -> str:
        """String representation of user."""
        return f"<User(id={self.id}, username='{self.username}', role='{self.role}')>"