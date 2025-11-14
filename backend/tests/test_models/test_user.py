"""Tests for User model."""

import pytest
from sqlalchemy.exc import IntegrityError

from app.models.user import User


class TestUserModel:
    """Test User model validation and functionality."""
    
    def test_user_model_creation(self):
        """Test that User model can be instantiated with valid data."""
        user = User(
            username="testuser",
            email="test@example.com",
            password_hash="hashed_password",
            role="user"
        )
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.password_hash == "hashed_password"
        assert user.role == "user"
        assert user.is_active is True  # Default value
    
    def test_user_model_validates_role(self):
        """Test that User model validates role field."""
        # Valid roles should work
        for valid_role in ['user', 'admin', 'analyst']:
            user = User(
                username="testuser",
                email="test@example.com", 
                password_hash="hashed_password",
                role=valid_role
            )
            assert user.role == valid_role
        
        # Invalid role should raise ValueError
        with pytest.raises(ValueError, match="Role must be one of"):
            User(
                username="testuser",
                email="test@example.com",
                password_hash="hashed_password", 
                role="invalid_role"
            )
    
    def test_user_model_validates_username(self):
        """Test that User model validates username field."""
        # Valid usernames
        valid_usernames = ['user123', 'test_user', 'user-name', 'abc']
        for username in valid_usernames:
            user = User(
                username=username,
                email="test@example.com",
                password_hash="hashed_password"
            )
            assert user.username == username
        
        # Username too short
        with pytest.raises(ValueError, match="at least 3 characters"):
            User(
                username="ab",
                email="test@example.com",
                password_hash="hashed_password"
            )
        
        # Username too long
        with pytest.raises(ValueError, match="cannot exceed 50 characters"):
            User(
                username="x" * 51,
                email="test@example.com", 
                password_hash="hashed_password"
            )
        
        # Username with invalid characters
        with pytest.raises(ValueError, match="letters, numbers, underscore, and hyphen"):
            User(
                username="user@name",
                email="test@example.com",
                password_hash="hashed_password"
            )
        
        # Empty username
        with pytest.raises(ValueError, match="at least 3 characters"):
            User(
                username="",
                email="test@example.com",
                password_hash="hashed_password"
            )
    
    def test_user_model_validates_email(self):
        """Test that User model validates email field."""
        # Valid emails
        valid_emails = ['test@example.com', 'user.name@domain.co.uk', 'simple@test.org']
        for email in valid_emails:
            user = User(
                username="testuser",
                email=email,
                password_hash="hashed_password"
            )
            assert user.email == email.lower()  # Should be normalized to lowercase
        
        # Invalid email format
        with pytest.raises(ValueError, match="Valid email address is required"):
            User(
                username="testuser",
                email="invalid-email",
                password_hash="hashed_password"
            )
        
        # Email too long
        with pytest.raises(ValueError, match="cannot exceed 255 characters"):
            User(
                username="testuser",
                email="x" * 250 + "@example.com",
                password_hash="hashed_password"
            )
        
        # Empty email
        with pytest.raises(ValueError, match="Valid email address is required"):
            User(
                username="testuser",
                email="",
                password_hash="hashed_password"
            )
    
    def test_user_model_repr(self):
        """Test User model string representation."""
        user = User(
            username="testuser",
            email="test@example.com",
            password_hash="hashed_password",
            role="admin"
        )
        repr_str = repr(user)
        assert "User" in repr_str
        assert "testuser" in repr_str
        assert "admin" in repr_str
    
    def test_user_model_default_values(self):
        """Test User model default values."""
        user = User(
            username="testuser",
            email="test@example.com",
            password_hash="hashed_password"
        )
        assert user.role == "user"  # Default role
        assert user.is_active is True  # Default active status
    
    def test_user_model_inheritance(self):
        """Test that User model inherits from BaseModel."""
        user = User(
            username="testuser",
            email="test@example.com",
            password_hash="hashed_password"
        )
        # Should have BaseModel methods
        assert hasattr(user, 'to_dict')
        assert hasattr(user, 'id')  # From UUIDMixin
        assert hasattr(user, 'created_at')  # From TimestampMixin
        assert hasattr(user, 'updated_at')  # From TimestampMixin