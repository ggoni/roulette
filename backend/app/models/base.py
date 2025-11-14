"""Base model with common fields and utilities."""

import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import Column, DateTime, UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

# Create the declarative base
Base = declarative_base()


class UUIDMixin:
    """Mixin for UUID primary key."""
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class TimestampMixin:
    """Mixin for created_at and updated_at timestamps."""
    
    created_at = Column(
        DateTime(timezone=True), 
        server_default=func.now(),
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )


class BaseModel(Base, UUIDMixin, TimestampMixin):
    """Base model class with UUID and timestamps."""
    
    __abstract__ = True
    
    def to_dict(self) -> dict[str, Any]:
        """Convert model instance to dictionary."""
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }
    
    def __repr__(self) -> str:
        """String representation of model."""
        return f"<{self.__class__.__name__}(id={self.id})>"