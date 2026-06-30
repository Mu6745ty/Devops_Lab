"""Battery monitoring service."""

import psutil
from typing import Optional

from loguru import logger

from core.base_service import BaseService
from models.system_metrics import BatteryMetrics


class BatteryMonitor(BaseService):
    """Monitors battery metrics using psutil."""

    def __init__(self) -> None:
        """Initialize battery monitor."""
        super().__init__("BatteryMonitor")

    def start(self) -> None:
        """Start battery monitoring."""
        self.is_running = True
        logger.info("Battery monitor started")

    def stop(self) -> None:
        """Stop battery monitoring."""
        self.is_running = False
        logger.info("Battery monitor stopped")

    def get_metrics(self) -> Optional[BatteryMetrics]:
        """Get current battery metrics.

        Returns:
            BatteryMetrics or None if no battery or error
        """
        try:
            battery = psutil.sensors_battery()
            if not battery:
                return None

            return BatteryMetrics(
                percent=battery.percent,
                is_charging=battery.power_plugged,
                time_left_minutes=int(battery.secsleft / 60) if battery.secsleft != -2 else None,
                health_percent=None,  # Requires WMI
                cycle_count=None,  # Requires WMI
            )
        except Exception as e:
            self.set_error(e)
            logger.error(f"Error getting battery metrics: {e}")
            return None
