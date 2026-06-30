"""Memory monitoring service."""

import psutil
from typing import Optional

from loguru import logger

from core.base_service import BaseService
from models.system_metrics import MemoryMetrics


class MemoryMonitor(BaseService):
    """Monitors memory/RAM metrics using psutil."""

    def __init__(self) -> None:
        """Initialize memory monitor."""
        super().__init__("MemoryMonitor")

    def start(self) -> None:
        """Start memory monitoring."""
        self.is_running = True
        logger.info("Memory monitor started")

    def stop(self) -> None:
        """Stop memory monitoring."""
        self.is_running = False
        logger.info("Memory monitor stopped")

    def get_metrics(self) -> Optional[MemoryMetrics]:
        """Get current memory metrics.

        Returns:
            MemoryMetrics or None if error
        """
        try:
            memory = psutil.virtual_memory()

            return MemoryMetrics(
                percent=memory.percent,
                used_mb=memory.used / (1024 * 1024),
                available_mb=memory.available / (1024 * 1024),
                total_mb=memory.total / (1024 * 1024),
                used_percent=memory.percent,
            )
        except Exception as e:
            self.set_error(e)
            logger.error(f"Error getting memory metrics: {e}")
            return None
