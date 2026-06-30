"""Event system for inter-module communication."""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Dict, List

from loguru import logger


class EventType(str, Enum):
    """Event types for the event bus."""

    # System events
    SYSTEM_STARTED = "system:started"
    SYSTEM_STOPPED = "system:stopped"
    SYSTEM_ERROR = "system:error"

    # Monitoring events
    METRICS_UPDATED = "monitoring:metrics_updated"
    CPU_ALERT = "monitoring:cpu_alert"
    MEMORY_ALERT = "monitoring:memory_alert"
    TEMPERATURE_ALERT = "monitoring:temperature_alert"
    BATTERY_ALERT = "monitoring:battery_alert"

    # Process events
    PROCESS_STARTED = "process:started"
    PROCESS_STOPPED = "process:stopped"
    PROCESS_LIST_UPDATED = "process:list_updated"

    # Gaming mode events
    GAMING_MODE_ENABLED = "gaming:enabled"
    GAMING_MODE_DISABLED = "gaming:disabled"

    # Storage events
    STORAGE_SCAN_COMPLETED = "storage:scan_completed"
    STORAGE_ALERT = "storage:alert"

    # AI events
    RECOMMENDATION_GENERATED = "ai:recommendation_generated"
    ANOMALY_DETECTED = "ai:anomaly_detected"


@dataclass
class Event:
    """Event data class."""

    type: EventType
    data: Any = None
    source: str = "unknown"


class EventBus:
    """Central event bus for inter-module communication.

    Implements publish-subscribe pattern for loosely coupled
    communication between modules.
    """

    def __init__(self) -> None:
        """Initialize event bus."""
        self._listeners: Dict[EventType, List[Callable]] = {}
        logger.info("Event bus initialized")

    def subscribe(self, event_type: EventType, callback: Callable) -> None:
        """Subscribe to an event type.

        Args:
            event_type: Type of event to listen for
            callback: Callable to invoke when event is published
        """
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(callback)
        logger.debug(f"Subscribed {callback.__name__} to {event_type}")

    def unsubscribe(self, event_type: EventType, callback: Callable) -> None:
        """Unsubscribe from an event type.

        Args:
            event_type: Type of event
            callback: Callback to remove
        """
        if event_type in self._listeners:
            if callback in self._listeners[event_type]:
                self._listeners[event_type].remove(callback)
                logger.debug(f"Unsubscribed {callback.__name__} from {event_type}")

    def publish(self, event: Event) -> None:
        """Publish an event to all subscribers.

        Args:
            event: Event to publish
        """
        if event.type in self._listeners:
            for callback in self._listeners[event.type]:
                try:
                    callback(event)
                except Exception as e:
                    logger.error(f"Error in event callback: {e}")
        logger.debug(f"Event published: {event.type} from {event.source}")

    def clear(self) -> None:
        """Clear all listeners."""
        self._listeners.clear()
        logger.info("Event bus cleared")

    def get_subscriber_count(self, event_type: EventType) -> int:
        """Get number of subscribers for an event type.

        Args:
            event_type: Event type to check

        Returns:
            Number of subscribers
        """
        return len(self._listeners.get(event_type, []))


# Global event bus instance
_event_bus: EventBus | None = None


def get_event_bus() -> EventBus:
    """Get or create global event bus.

    Returns:
        Global EventBus instance
    """
    global _event_bus
    if _event_bus is None:
        _event_bus = EventBus()
    return _event_bus
