"""Unit tests for memory monitor."""

import pytest
from services.monitoring.memory_monitor import MemoryMonitor


class TestMemoryMonitor:
    """Test cases for MemoryMonitor."""

    @pytest.fixture
    def monitor(self):
        """Create memory monitor instance."""
        return MemoryMonitor()

    def test_initialization(self, monitor):
        """Test monitor initialization."""
        assert monitor.name == "MemoryMonitor"
        assert not monitor.is_running

    def test_get_metrics(self, monitor):
        """Test getting memory metrics."""
        monitor.start()
        metrics = monitor.get_metrics()
        assert metrics is not None
        assert hasattr(metrics, "percent")
        assert hasattr(metrics, "used_mb")
        assert hasattr(metrics, "available_mb")
        assert hasattr(metrics, "total_mb")
        assert 0 <= metrics.percent <= 100
        monitor.stop()
