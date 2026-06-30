"""SQLAlchemy ORM models for database."""

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class SystemMetricsModel(Base):
    """ORM model for system metrics."""

    __tablename__ = "system_metrics"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    cpu_percent = Column(Float)
    cpu_freq_mhz = Column(Float)
    ram_percent = Column(Float)
    ram_used_mb = Column(Float)
    ram_available_mb = Column(Float)
    gpu_percent = Column(Float, nullable=True)
    gpu_memory_percent = Column(Float, nullable=True)
    disk_read_bytes_per_sec = Column(Float)
    disk_write_bytes_per_sec = Column(Float)
    network_sent_bytes_per_sec = Column(Float)
    network_recv_bytes_per_sec = Column(Float)
    battery_percent = Column(Float, nullable=True)
    battery_is_charging = Column(Boolean, nullable=True)


class ProcessModel(Base):
    """ORM model for processes."""

    __tablename__ = "processes"

    id = Column(Integer, primary_key=True)
    pid = Column(Integer, index=True)
    name = Column(String(255))
    executable = Column(String(500))
    cpu_percent = Column(Float)
    memory_percent = Column(Float)
    memory_mb = Column(Float)
    created_time = Column(DateTime)
    terminated_time = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    user = Column(String(255))
    status = Column(String(50))
    num_threads = Column(Integer)
