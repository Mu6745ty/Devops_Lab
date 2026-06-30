"""Integration tests for system components."""

import pytest
from services.database.db_manager import DatabaseManager
from services.monitoring.cpu_monitor import CPUMonitor
from services.monitoring.memory_monitor import MemoryMonitor
from core.event_system import get_event_bus, EventType


class TestSystemIntegration:
    """Integration tests for system components."""

    def test_database_manager(self):
        """Test database manager lifecycle."""
        db = DatabaseManager()
        db.start()
        assert db.is_running
        session = db.get_session()
        assert session is not None
        db.close_session(session)
        db.stop()
        assert not db.is_running

    def test_monitors(self):
        """Test monitors working together."""
        cpu_monitor = CPUMonitor()
        mem_monitor = MemoryMonitor()

        cpu_monitor.start()
        mem_monitor.start()

        cpu_metrics = cpu_monitor.get_metrics()
        mem_metrics = mem_monitor.get_metrics()

        assert cpu_metrics is not None
        assert mem_metrics is not None

        cpu_monitor.stop()
        mem_monitor.stop()

    def test_event_bus(self):
        """Test event bus functionality."""
        bus = get_event_bus()
        events_received = []

        def callback(event):
            events_received.append(event)

        bus.subscribe(EventType.CPU_ALERT, callback)
        assert bus.get_subscriber_count(EventType.CPU_ALERT) > 0

        from core.event_system import Event
        event = Event(type=EventType.CPU_ALERT, data={"value": 95.0}, source="test")
        bus.publish(event)

        assert len(events_received) == 1
        bus.unsubscribe(EventType.CPU_ALERT, callback)
