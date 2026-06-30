"""System metrics data models."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class CPUMetrics:
    """CPU metrics."""

    percent: float
    frequency_mhz: float
    core_count: int
    thread_count: int
    per_core_percent: list


@dataclass
class MemoryMetrics:
    """Memory/RAM metrics."""

    percent: float
    used_mb: float
    available_mb: float
    total_mb: float
    used_percent: float


@dataclass
class DiskMetrics:
    """Disk I/O metrics."""

    read_bytes_per_sec: float
    write_bytes_per_sec: float
    io_counter_read: int
    io_counter_write: int


@dataclass
class GPUMetrics:
    """GPU metrics."""

    percent: float
    memory_percent: float
    memory_used_mb: float
    memory_total_mb: float
    temperature: Optional[float]


@dataclass
class NetworkMetrics:
    """Network metrics."""

    sent_bytes_per_sec: float
    recv_bytes_per_sec: float
    packets_sent: int
    packets_recv: int
    errors_in: int
    errors_out: int


@dataclass
class TemperatureMetrics:
    """Temperature metrics."""

    cpu_temp: Optional[float]
    gpu_temp: Optional[float]
    ssd_temp: Optional[float]
    battery_temp: Optional[float]
    fan_speed: Optional[float]
    thermal_throttling: bool


@dataclass
class BatteryMetrics:
    """Battery metrics."""

    percent: float
    is_charging: bool
    time_left_minutes: Optional[int]
    health_percent: Optional[float]
    cycle_count: Optional[int]


@dataclass
class SystemMetrics:
    """Complete system metrics snapshot."""

    timestamp: datetime
    cpu: CPUMetrics
    memory: MemoryMetrics
    disk: DiskMetrics
    gpu: Optional[GPUMetrics]
    network: NetworkMetrics
    temperature: TemperatureMetrics
    battery: BatteryMetrics

    def __repr__(self) -> str:
        """String representation."""
        return (
            f"SystemMetrics("
            f"cpu={self.cpu.percent}%, "
            f"mem={self.memory.percent}%, "
            f"disk_write={self.disk.write_bytes_per_sec:.2f}B/s"
            f")"
        )
