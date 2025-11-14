"""Tests for Name model."""

import pytest
import uuid

from app.models.name import Name


class TestNameModel:
    """Test Name model validation and functionality."""
    
    def test_name_model_creation(self):
        """Test that Name model can be instantiated with valid data."""
        user_id = uuid.uuid4()
        name = Name(
            name="Test Name",
            description="A test name for roulette",
            is_active=True,
            weight=5,
            created_by=user_id
        )
        assert name.name == "Test Name"
        assert name.description == "A test name for roulette"
        assert name.is_active is True
        assert name.weight == 5
        assert name.created_by == user_id
    
    def test_name_model_validates_name(self):
        """Test that Name model validates name field."""
        # Valid names
        valid_names = ['John Doe', 'Alice', 'Bob Smith-Jones', 'Name with 123']
        for test_name in valid_names:
            name = Name(name=test_name)
            assert name.name == test_name.strip()
        
        # Name with whitespace should be stripped
        name = Name(name="  Spaced Name  ")
        assert name.name == "Spaced Name"
        
        # Empty name
        with pytest.raises(ValueError, match="Name cannot be empty"):
            Name(name="")
        
        # Whitespace only name
        with pytest.raises(ValueError, match="Name cannot be empty"):
            Name(name="   ")
        
        # Name too long
        with pytest.raises(ValueError, match="cannot exceed 255 characters"):
            Name(name="x" * 256)
    
    def test_name_model_validates_weight(self):
        """Test that Name model validates weight field."""
        # Valid weights
        valid_weights = [1, 5, 100, 999, 1000]
        for weight in valid_weights:
            name = Name(name="Test Name", weight=weight)
            assert name.weight == weight
        
        # Weight too low
        with pytest.raises(ValueError, match="Weight must be at least 1"):
            Name(name="Test Name", weight=0)
        
        with pytest.raises(ValueError, match="Weight must be at least 1"):
            Name(name="Test Name", weight=-5)
        
        # Weight too high
        with pytest.raises(ValueError, match="Weight cannot exceed 1000"):
            Name(name="Test Name", weight=1001)
    
    def test_name_model_validates_description(self):
        """Test that Name model validates description field."""
        # Valid descriptions
        name = Name(name="Test Name", description="Valid description")
        assert name.description == "Valid description"
        
        # None description
        name = Name(name="Test Name", description=None)
        assert name.description is None
        
        # Empty description should be None
        name = Name(name="Test Name", description="")
        assert name.description is None
        
        # Whitespace only description should be None  
        name = Name(name="Test Name", description="   ")
        assert name.description is None
        
        # Description with whitespace should be stripped
        name = Name(name="Test Name", description="  Valid description  ")
        assert name.description == "Valid description"
        
        # Description too long
        with pytest.raises(ValueError, match="cannot exceed 1000 characters"):
            Name(name="Test Name", description="x" * 1001)
    
    def test_name_model_default_values(self):
        """Test Name model default values."""
        name = Name(name="Test Name")
        assert name.is_active is True  # Default active status
        assert name.weight == 1  # Default weight
        assert name.description is None  # Default description
        assert name.created_by is None  # Default creator
    
    def test_name_model_repr(self):
        """Test Name model string representation."""
        name = Name(name="Test Name", is_active=True, weight=5)
        repr_str = repr(name)
        assert "Name" in repr_str
        assert "Test Name" in repr_str
        assert "active" in repr_str
        assert "weight=5" in repr_str
        
        # Test inactive name
        name = Name(name="Inactive Name", is_active=False)
        repr_str = repr(name)
        assert "inactive" in repr_str
    
    def test_name_model_inheritance(self):
        """Test that Name model inherits from BaseModel."""
        name = Name(name="Test Name")
        # Should have BaseModel methods
        assert hasattr(name, 'to_dict')
        assert hasattr(name, 'id')  # From UUIDMixin
        assert hasattr(name, 'created_at')  # From TimestampMixin
        assert hasattr(name, 'updated_at')  # From TimestampMixin
    
    def test_name_model_foreign_key_relationship(self):
        """Test Name model foreign key to User."""
        user_id = uuid.uuid4()
        name = Name(name="Test Name", created_by=user_id)
        assert name.created_by == user_id
        
        # Should accept None for created_by
        name = Name(name="Test Name", created_by=None)
        assert name.created_by is None