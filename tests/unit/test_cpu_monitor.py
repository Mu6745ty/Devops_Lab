"""Unit tests for CPU monitor."""

import pytest
from services.monitoring.cpu_monitor import CPUMonitor


class TestCPUMonitor:
    """Test cases for CPUMonitor."""

    @pytest.fixture
    def monitor(self):
        """Create CPU monitor instance."""
        return CPUMonitor()

    def test_initialization(self, monitor):
        """Test monitor initialization."""
        assert monitor.name == "CPUMonitor"
        assert not monitor.is_running

    def test_start(self, monitor):
        """Test monitor start."""
        monitor.start()
        assert monitor.is_running
        monitor.stop()

    def test_stop(self, monitor):
        """Test monitor stop."""
        monitor.start()
        monitor.stop()
        assert not monitor.is_running

    def test_get_metrics(self, monitor):
        """Test getting CPU metrics."""
        monitor.start()
        metrics = monitor.get_metrics()
        assert metrics is not None
        assert hasattr(metrics, "percent")
        assert hasattr(metrics, "frequency_mhz")
        assert hasattr(metrics, "core_count")
        assert hasattr(metrics, "thread_count")
        assert 0 <= metrics.percent <= 100
        monitor.stop()

    def test_error_handling(self, monitor, mocker):
        """Test error handling."""
        mocker.patch("psutil.cpu_percent", side_effect=Exception("Test error"))
        monitor.start()
        metrics = monitor.get_metrics()
        assert metrics is None
        assert monitor.has_error()
        monitor.stop()
