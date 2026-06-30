"""Network monitoring service."""

import psutil
from typing import Optional

from loguru import logger

from core.base_service import BaseService
from models.system_metrics import NetworkMetrics


class NetworkMonitor(BaseService):
    """Monitors network metrics using psutil."""

    def __init__(self) -> None:
        """Initialize network monitor."""
        super().__init__("NetworkMonitor")
        self._last_sent = 0
        self._last_recv = 0

    def start(self) -> None:
        """Start network monitoring."""
        self.is_running = True
        logger.info("Network monitor started")

    def stop(self) -> None:
        """Stop network monitoring."""
        self.is_running = False
        logger.info("Network monitor stopped")

    def get_metrics(self) -> Optional[NetworkMetrics]:
        """Get current network metrics.

        Returns:
            NetworkMetrics or None if error
        """
        try:
            net_io = psutil.net_io_counters()

            return NetworkMetrics(
                sent_bytes_per_sec=self._last_sent,
                recv_bytes_per_sec=self._last_recv,
                packets_sent=net_io.packets_sent,
                packets_recv=net_io.packets_recv,
                errors_in=net_io.errin,
                errors_out=net_io.errout,
            )
        except Exception as e:
            self.set_error(e)
            logger.error(f"Error getting network metrics: {e}")
            return None
