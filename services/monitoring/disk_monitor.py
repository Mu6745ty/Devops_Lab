"""Disk monitoring service."""

import psutil
from typing import Optional

from loguru import logger

from core.base_service import BaseService
from models.system_metrics import DiskMetrics


class DiskMonitor(BaseService):
    """Monitors disk I/O metrics using psutil."""

    def __init__(self) -> None:
        """Initialize disk monitor."""
        super().__init__("DiskMonitor")
        self._last_io = psutil.disk_io_counters()
        self._last_read = 0.0
        self._last_write = 0.0

    def start(self) -> None:
        """Start disk monitoring."""
        self.is_running = True
        logger.info("Disk monitor started")

    def stop(self) -> None:
        """Stop disk monitoring."""
        self.is_running = False
        logger.info("Disk monitor stopped")

    def get_metrics(self) -> Optional[DiskMetrics]:
        """Get current disk metrics.

        Returns:
            DiskMetrics or None if error
        """
        try:
            io_counters = psutil.disk_io_counters()
            if not io_counters:
                return None

            return DiskMetrics(
                read_bytes_per_sec=self._last_read,
                write_bytes_per_sec=self._last_write,
                io_counter_read=io_counters.read_bytes,
                io_counter_write=io_counters.write_bytes,
            )
        except Exception as e:
            self.set_error(e)
            logger.error(f"Error getting disk metrics: {e}")
            return None
