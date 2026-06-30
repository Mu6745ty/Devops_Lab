"""Process information data models."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class ProcessInfo:
    """Information about a running process."""

    pid: int
    name: str
    executable: str
    cpu_percent: float
    memory_percent: float
    memory_mb: float
    user: str
    status: str
    created_time: datetime
    num_threads: int
    is_system: bool
    priority: Optional[str]
    io_read_bytes: Optional[int]
    io_write_bytes: Optional[int]

    @property
    def display_name(self) -> str:
        """Get display name for process."""
        return self.name or self.executable.split("\\")[-1]

    def __repr__(self) -> str:
        """String representation."""
        return (
            f"ProcessInfo("
            f"pid={self.pid}, "
            f"name={self.display_name}, "
            f"cpu={self.cpu_percent}%, "
            f"mem={self.memory_mb:.1f}MB"
            f")"
        )
