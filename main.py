#!/usr/bin/env python
"""PC Optimizer - Main entry point."""

import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

from config.logging_config import setup_logging
from loguru import logger
from version import get_version_info


def main() -> int:
    """Main entry point."""
    # Setup logging
    setup_logging()
    logger.info("=" * 80)
    logger.info(get_version_info())
    logger.info("=" * 80)

    try:
        # Import after logging setup
        from services.database import DatabaseManager
        from services.monitoring import (
            CPUMonitor,
            MemoryMonitor,
            DiskMonitor,
            NetworkMonitor,
            BatteryMonitor,
        )
        from core.event_system import get_event_bus, EventType, Event
        from core.thread_manager import ThreadManager
        from core.cache_manager import CacheManager

        # Initialize core infrastructure
        logger.info("Initializing core infrastructure...")
        thread_mgr = ThreadManager()
        cache_mgr = CacheManager()
        event_bus = get_event_bus()
        logger.info(f"✓ {thread_mgr}")
        logger.info(f"✓ {cache_mgr}")
        logger.info(f"✓ Event bus initialized")

        # Initialize database
        logger.info("\nInitializing database...")
        db_manager = DatabaseManager()
        db_manager.start()
        logger.info(f"✓ {db_manager}")

        # Initialize monitors
        logger.info("\nInitializing monitoring services...")
        monitors = [
            CPUMonitor(),
            MemoryMonitor(),
            DiskMonitor(),
            NetworkMonitor(),
            BatteryMonitor(),
        ]

        for monitor in monitors:
            monitor.start()
            logger.info(f"✓ {monitor}")

        # Collect metrics
        logger.info("\nCollecting system metrics...")
        logger.info("-" * 80)

        cpu_metrics = monitors[0].get_metrics()
        if cpu_metrics:
            logger.info(f"CPU: {cpu_metrics.percent}% | "
                       f"{cpu_metrics.core_count} cores @ {cpu_metrics.frequency_mhz:.0f}MHz")

        mem_metrics = monitors[1].get_metrics()
        if mem_metrics:
            logger.info(f"Memory: {mem_metrics.percent}% | "
                       f"{mem_metrics.used_mb:.0f}MB / {mem_metrics.total_mb:.0f}MB")

        disk_metrics = monitors[2].get_metrics()
        if disk_metrics:
            logger.info(f"Disk I/O: Read {disk_metrics.read_bytes_per_sec:.2f}B/s | "
                       f"Write {disk_metrics.write_bytes_per_sec:.2f}B/s")

        net_metrics = monitors[3].get_metrics()
        if net_metrics:
            logger.info(f"Network: Sent {net_metrics.sent_bytes_per_sec:.2f}B/s | "
                       f"Recv {net_metrics.recv_bytes_per_sec:.2f}B/s")

        battery_metrics = monitors[4].get_metrics()
        if battery_metrics:
            status = "Charging" if battery_metrics.is_charging else "Discharging"
            logger.info(f"Battery: {battery_metrics.percent}% ({status})")
        else:
            logger.info("Battery: No battery detected")

        logger.info("-" * 80)

        # Test event bus
        logger.info("\nTesting event system...")
        events_received = []

        def test_callback(event):
            events_received.append(event)
            logger.info(f"Event received: {event.type}")

        event_bus.subscribe(EventType.CPU_ALERT, test_callback)
        test_event = Event(
            type=EventType.CPU_ALERT,
            data={"cpu_usage": cpu_metrics.percent if cpu_metrics else 0},
            source="main"
        )
        event_bus.publish(test_event)
        logger.info(f"✓ Event system working ({len(events_received)} events received)")

        # Test cache
        logger.info("\nTesting cache system...")
        cache_mgr.set("test_key", {"data": "test_value"})
        cached = cache_mgr.get("test_key")
        logger.info(f"✓ Cache system working: {cached}")
        logger.info(f"Cache stats: {cache_mgr.get_stats()}")

        # Cleanup
        logger.info("\nShutting down...")
        for monitor in monitors:
            monitor.stop()
            logger.info(f"✓ Stopped {monitor.name}")

        db_manager.stop()
        thread_mgr.shutdown()
        logger.info(f"✓ All services stopped")

        logger.info("=" * 80)
        logger.info("PC Optimizer - Shutdown complete")
        logger.info("=" * 80)
        return 0

    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
