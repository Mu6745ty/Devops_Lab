"""Hardware information data models."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class CPUInfo:
    """CPU hardware information."""

    brand: str
    model: str
    cores: int
    threads: int
    max_frequency_mhz: float
    architecture: str
    cache_mb: Optional[float]


@dataclass
class GPUInfo:
    """GPU hardware information."""

    brand: str
    model: str
    memory_mb: int
    driver_version: Optional[str]
    compute_capability: Optional[str]


@dataclass
class RAMInfo:
    """RAM hardware information."""

    total_mb: int
    modules: int
    type: str
    frequency_mhz: Optional[int]
    manufacturer: Optional[str]


@dataclass
class StorageDevice:
    """Storage device information."""

    name: str
    device_path: str
    total_mb: int
    used_mb: int
    free_mb: int
    type: str  # SSD, HDD, NVMe
    model: Optional[str]
    serial: Optional[str]


@dataclass
class HardwareInfo:
    """Complete hardware information."""

    cpu: CPUInfo
    gpu: Optional[GPUInfo]
    ram: RAMInfo
    uptime_seconds: int

    def __repr__(self) -> str:
        """String representation."""
        return (
            f"HardwareInfo("
            f"{self.cpu.brand} {self.cpu.model}, "
            f"{self.ram.total_mb // 1024}GB RAM"
            f")"
        )
