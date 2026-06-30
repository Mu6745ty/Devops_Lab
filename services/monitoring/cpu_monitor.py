"""CPU monitoring service."""

import psutil
from typing import Optional

from loguru import logger

from core.base_service import BaseService
from models.system_metrics import CPUMetrics


class CPUMonitor(BaseService):
    """Monitors CPU metrics using psutil."""

    def __init__(self) -> None:
        """Initialize CPU monitor."""
        super().__init__("CPUMonitor")
        self._last_percent: list = []

    def start(self) -> None:
        """Start CPU monitoring."""
        self.is_running = True
        logger.info("CPU monitor started")

    def stop(self) -> None:
        """Stop CPU monitoring."""
        self.is_running = False
        logger.info("CPU monitor stopped")

    def get_metrics(self) -> Optional[CPUMetrics]:
        """Get current CPU metrics.

        Returns:
            CPUMetrics or None if error
        """
        try:
            percent = psutil.cpu_percent(interval=0.1)
            freq = psutil.cpu_freq()
            per_core = psutil.cpu_percent(interval=0.1, percpu=True)

            return CPUMetrics(
                percent=percent,
                frequency_mhz=freq.current if freq else 0,
                core_count=psutil.cpu_count(logical=False) or 1,
                thread_count=psutil.cpu_count(logical=True) or 1,
                per_core_percent=per_core,
            )
        except Exception as e:
            self.set_error(e)
            logger.error(f"Error getting CPU metrics: {e}")
            return None
