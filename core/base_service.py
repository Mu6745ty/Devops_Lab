"""Base service class for all services."""

from abc import ABC, abstractmethod
from typing import Optional

from loguru import logger


class BaseService(ABC):
    """Abstract base class for all services.

    Provides common functionality for service initialization,
    startup, shutdown, and error handling.
    """

    def __init__(self, name: str) -> None:
        """Initialize base service.

        Args:
            name: Service name for logging
        """
        self.name = name
        self.is_running = False
        self._error: Optional[Exception] = None
        logger.info(f"Service initialized: {self.name}")

    @abstractmethod
    def start(self) -> None:
        """Start the service.

        Should be implemented by subclasses.
        """
        pass

    @abstractmethod
    def stop(self) -> None:
        """Stop the service.

        Should be implemented by subclasses.
        """
        pass

    def set_error(self, error: Exception) -> None:
        """Set service error state.

        Args:
            error: Exception that occurred
        """
        self._error = error
        logger.error(f"Service error in {self.name}: {error}")

    def clear_error(self) -> None:
        """Clear error state."""
        self._error = None

    def has_error(self) -> bool:
        """Check if service has error.

        Returns:
            True if service has error
        """
        return self._error is not None

    def get_error(self) -> Optional[Exception]:
        """Get service error.

        Returns:
            Exception if error occurred, None otherwise
        """
        return self._error

    def __repr__(self) -> str:
        """String representation."""
        status = "running" if self.is_running else "stopped"
        return f"{self.__class__.__name__}({self.name}, {status})"
