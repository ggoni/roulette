"""Tests for GameResult model."""

import pytest
import uuid
from ipaddress import IPv4Address

from app.models.game_result import GameResult


class TestGameResultModel:
    """Test GameResult model validation and functionality."""
    
    def test_game_result_model_creation(self):
        """Test that GameResult model can be instantiated with valid data."""
        session_id = uuid.uuid4()
        name_id = uuid.uuid4()
        user_id = uuid.uuid4()
        
        selected_name_snapshot = {
            'id': str(name_id),
            'name': 'Selected Name',
            'weight': 1,
            'is_active': True
        }
        
        available_names = [
            {'id': str(name_id), 'name': 'Selected Name'},
            {'id': str(uuid.uuid4()), 'name': 'Other Name 1'},
            {'id': str(uuid.uuid4()), 'name': 'Other Name 2'}
        ]
        
        result = GameResult(
            session_id=session_id,
            selected_name_id=name_id,
            selected_name_snapshot=selected_name_snapshot,
            available_names=available_names,
            spin_duration_ms=2500,
            user_id=user_id,
            user_ip=IPv4Address('192.168.1.1'),
            user_agent='Test User Agent'
        )
        
        assert result.session_id == session_id
        assert result.selected_name_id == name_id
        assert result.selected_name_snapshot == selected_name_snapshot
        assert result.available_names == available_names
        assert result.spin_duration_ms == 2500
        assert result.user_id == user_id
        assert result.user_ip == IPv4Address('192.168.1.1')
        assert result.user_agent == 'Test User Agent'
    
    def test_game_result_validates_session_id(self):
        """Test that GameResult validates session_id field."""
        # Valid session ID
        session_id = uuid.uuid4()
        result = GameResult(
            session_id=session_id,
            selected_name_snapshot={'id': 'test', 'name': 'test'},
            available_names=[{'id': 'test', 'name': 'test'}]
        )
        assert result.session_id == session_id
        
        # None session ID should raise error
        with pytest.raises(ValueError, match="Session ID is required"):
            GameResult(
                session_id=None,
                selected_name_snapshot={'id': 'test', 'name': 'test'},
                available_names=[{'id': 'test', 'name': 'test'}]
            )
    
    def test_game_result_validates_selected_name_snapshot(self):
        """Test that GameResult validates selected_name_snapshot field."""
        session_id = uuid.uuid4()
        
        # Valid snapshot
        valid_snapshot = {'id': 'test-id', 'name': 'Test Name', 'extra': 'data'}
        result = GameResult(
            session_id=session_id,
            selected_name_snapshot=valid_snapshot,
            available_names=[{'id': 'test', 'name': 'test'}]
        )
        assert result.selected_name_snapshot == valid_snapshot
        
        # Non-dict snapshot
        with pytest.raises(ValueError, match="must be a dictionary"):
            GameResult(
                session_id=session_id,
                selected_name_snapshot="not a dict",
                available_names=[{'id': 'test', 'name': 'test'}]
            )
        
        # Missing required fields
        with pytest.raises(ValueError, match="must contain fields"):
            GameResult(
                session_id=session_id,
                selected_name_snapshot={'name': 'Test Name'},  # Missing 'id'
                available_names=[{'id': 'test', 'name': 'test'}]
            )
        
        with pytest.raises(ValueError, match="must contain fields"):
            GameResult(
                session_id=session_id,
                selected_name_snapshot={'id': 'test-id'},  # Missing 'name'
                available_names=[{'id': 'test', 'name': 'test'}]
            )
    
    def test_game_result_validates_available_names(self):
        """Test that GameResult validates available_names field."""
        session_id = uuid.uuid4()
        selected_name_snapshot = {'id': 'test', 'name': 'Test Name'}
        
        # Valid available names
        valid_names = [
            {'id': 'id1', 'name': 'Name 1'},
            {'id': 'id2', 'name': 'Name 2', 'extra': 'data'}
        ]
        result = GameResult(
            session_id=session_id,
            selected_name_snapshot=selected_name_snapshot,
            available_names=valid_names
        )
        assert result.available_names == valid_names
        
        # Non-list available names
        with pytest.raises(ValueError, match="must be a list"):
            GameResult(
                session_id=session_id,
                selected_name_snapshot=selected_name_snapshot,
                available_names="not a list"
            )
        
        # Empty available names
        with pytest.raises(ValueError, match="cannot be empty"):
            GameResult(
                session_id=session_id,
                selected_name_snapshot=selected_name_snapshot,
                available_names=[]
            )
        
        # Invalid name entry (not dict)
        with pytest.raises(ValueError, match="must be a dictionary"):
            GameResult(
                session_id=session_id,
                selected_name_snapshot=selected_name_snapshot,
                available_names=[{'id': 'test', 'name': 'test'}, "not a dict"]
            )
        
        # Missing required fields in name entry
        with pytest.raises(ValueError, match="must have 'id' and 'name' fields"):
            GameResult(
                session_id=session_id,
                selected_name_snapshot=selected_name_snapshot,
                available_names=[{'name': 'test'}]  # Missing 'id'
            )
    
    def test_game_result_validates_spin_duration(self):
        """Test that GameResult validates spin_duration_ms field."""
        session_id = uuid.uuid4()
        selected_name_snapshot = {'id': 'test', 'name': 'Test Name'}
        available_names = [{'id': 'test', 'name': 'test'}]
        
        # Valid durations
        valid_durations = [0, 1000, 5000, 300000]  # 0 to 5 minutes
        for duration in valid_durations:
            result = GameResult(
                session_id=session_id,
                selected_name_snapshot=selected_name_snapshot,
                available_names=available_names,
                spin_duration_ms=duration
            )
            assert result.spin_duration_ms == duration
        
        # None duration (should be allowed)
        result = GameResult(
            session_id=session_id,
            selected_name_snapshot=selected_name_snapshot,
            available_names=available_names,
            spin_duration_ms=None
        )
        assert result.spin_duration_ms is None
        
        # Negative duration
        with pytest.raises(ValueError, match="cannot be negative"):
            GameResult(
                session_id=session_id,
                selected_name_snapshot=selected_name_snapshot,
                available_names=available_names,
                spin_duration_ms=-1
            )
        
        # Duration too long (over 5 minutes)
        with pytest.raises(ValueError, match="cannot exceed 5 minutes"):
            GameResult(
                session_id=session_id,
                selected_name_snapshot=selected_name_snapshot,
                available_names=available_names,
                spin_duration_ms=300001
            )
    
    def test_game_result_validates_user_agent(self):
        """Test that GameResult validates user_agent field."""
        session_id = uuid.uuid4()
        selected_name_snapshot = {'id': 'test', 'name': 'Test Name'}
        available_names = [{'id': 'test', 'name': 'test'}]
        
        # Valid user agent
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        result = GameResult(
            session_id=session_id,
            selected_name_snapshot=selected_name_snapshot,
            available_names=available_names,
            user_agent=user_agent
        )
        assert result.user_agent == user_agent
        
        # None user agent
        result = GameResult(
            session_id=session_id,
            selected_name_snapshot=selected_name_snapshot,
            available_names=available_names,
            user_agent=None
        )
        assert result.user_agent is None
        
        # User agent too long
        with pytest.raises(ValueError, match="cannot exceed 1000 characters"):
            GameResult(
                session_id=session_id,
                selected_name_snapshot=selected_name_snapshot,
                available_names=available_names,
                user_agent="x" * 1001
            )
    
    def test_game_result_repr(self):
        """Test GameResult model string representation."""
        session_id = uuid.uuid4()
        selected_name_snapshot = {'id': 'test', 'name': 'Selected Name'}
        available_names = [{'id': 'test', 'name': 'test'}]
        
        result = GameResult(
            session_id=session_id,
            selected_name_snapshot=selected_name_snapshot,
            available_names=available_names
        )
        
        repr_str = repr(result)
        assert "GameResult" in repr_str
        assert str(session_id) in repr_str
        assert "Selected Name" in repr_str
    
    def test_game_result_inheritance(self):
        """Test that GameResult model inherits from BaseModel."""
        session_id = uuid.uuid4()
        result = GameResult(
            session_id=session_id,
            selected_name_snapshot={'id': 'test', 'name': 'Test Name'},
            available_names=[{'id': 'test', 'name': 'test'}]
        )
        
        # Should have BaseModel methods
        assert hasattr(result, 'to_dict')
        assert hasattr(result, 'id')  # From UUIDMixin
        assert hasattr(result, 'created_at')  # From TimestampMixin
        assert hasattr(result, 'updated_at')  # From TimestampMixin