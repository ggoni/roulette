"""Tests for database connection and base models."""

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db, init_db, Base
from app.models.base import BaseModel, UUIDMixin, TimestampMixin


class TestDatabaseConnection:
    """Test database connection functionality."""
    
    @pytest.mark.asyncio
    async def test_get_db_session(self):
        """Test that get_db returns a valid database session."""
        async for db in get_db():
            assert isinstance(db, AsyncSession)
            assert db.is_active
            break  # Only test first yield
    
    @pytest.mark.asyncio
    async def test_init_db(self):
        """Test database initialization creates tables."""
        # This will be implemented once we have a test database setup
        await init_db()
        # Add assertions once we have proper test database


class TestUUIDMixin:
    """Test UUID mixin functionality."""
    
    def test_uuid_mixin_has_id_column(self):
        """Test that UUIDMixin provides UUID id column."""
        assert hasattr(UUIDMixin, 'id')
        # Additional column introspection would require actual SQLAlchemy setup


class TestTimestampMixin:
    """Test timestamp mixin functionality."""
    
    def test_timestamp_mixin_has_timestamp_columns(self):
        """Test that TimestampMixin provides timestamp columns."""
        assert hasattr(TimestampMixin, 'created_at')
        assert hasattr(TimestampMixin, 'updated_at')


class TestBaseModel:
    """Test base model functionality."""
    
    def test_base_model_inheritance(self):
        """Test that BaseModel inherits from Base and mixins."""
        assert issubclass(BaseModel, Base)
        assert hasattr(BaseModel, 'id')  # From UUIDMixin
        assert hasattr(BaseModel, 'created_at')  # From TimestampMixin
        assert hasattr(BaseModel, 'updated_at')  # From TimestampMixin
    
    def test_base_model_has_to_dict_method(self):
        """Test that BaseModel provides to_dict method."""
        assert hasattr(BaseModel, 'to_dict')
        assert callable(getattr(BaseModel, 'to_dict'))
    
    def test_base_model_has_repr_method(self):
        """Test that BaseModel provides __repr__ method."""
        assert hasattr(BaseModel, '__repr__')
        assert callable(getattr(BaseModel, '__repr__'))