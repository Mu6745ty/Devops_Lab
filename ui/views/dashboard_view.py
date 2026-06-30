"""Dashboard view - main system metrics display."""

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
    QGridLayout,
    QLabel,
)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QFont
from loguru import logger

from ui.components.stat_card import StatCard
from ui.components.progress_ring import ProgressRing
from ui.components.chart_widget import ChartWidget
from ui.theme import Color, Font, Spacing
from services.monitoring import (
    CPUMonitor,
    MemoryMonitor,
    DiskMonitor,
    NetworkMonitor,
    BatteryMonitor,
)


class DashboardView(QWidget):
    """Main dashboard view with real-time metrics."""

    metrics_updated = pyqtSignal(dict)

    def __init__(self):
        """Initialize dashboard view."""
        super().__init__()
        self.cpu_monitor = CPUMonitor()
        self.mem_monitor = MemoryMonitor()
        self.disk_monitor = DiskMonitor()
        self.net_monitor = NetworkMonitor()
        self.battery_monitor = BatteryMonitor()

        self.cpu_history = []
        self.mem_history = []

        self.setup_ui()
        self.setup_monitors()
        self.setup_timer()

    def setup_ui(self) -> None:
        """Setup dashboard UI."""
        layout = QVBoxLayout()
        layout.setContentsMargins(Spacing.XL, Spacing.XL, Spacing.XL, Spacing.XL)
        layout.setSpacing(Spacing.XL)

        # Title
        title = QLabel("📊 System Dashboard")
        title_font = QFont(Font.PRIMARY)
        title_font.setPointSize(Font.TITLE)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setStyleSheet(f"color: {Color.TEXT_PRIMARY};")
        layout.addWidget(title)

        # Main metrics grid
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background-color: transparent; border: none;")

        scroll_widget = QWidget()
        grid_layout = QGridLayout()
        grid_layout.setSpacing(Spacing.LG)

        # CPU Metrics
        cpu_card = StatCard("CPU Usage", "0%", "cores", "⚙️")
        cpu_card.setMinimumHeight(120)
        self.cpu_card = cpu_card

        # Memory Metrics
        mem_card = StatCard("Memory", "0%", "GB", "🧠")
        mem_card.setMinimumHeight(120)
        self.mem_card = mem_card

        # Battery Metrics
        battery_card = StatCard("Battery", "--", "charging", "🔋")
        battery_card.setMinimumHeight(120)
        self.battery_card = battery_card

        # Network Metrics
        net_card = StatCard("Network", "0 Mbps", "↕️", "🌐")
        net_card.setMinimumHeight(120)
        self.net_card = net_card

        # Progress Rings
        cpu_ring = ProgressRing(size=120, label="CPU")
        cpu_ring.set_color(Color.PRIMARY)
        self.cpu_ring = cpu_ring

        mem_ring = ProgressRing(size=120, label="RAM")
        mem_ring.set_color(Color.WARNING)
        self.mem_ring = mem_ring

        # Add to grid (2x2)
        grid_layout.addWidget(cpu_card, 0, 0)
        grid_layout.addWidget(mem_card, 0, 1)
        grid_layout.addWidget(battery_card, 1, 0)
        grid_layout.addWidget(net_card, 1, 1)

        scroll_widget.setLayout(grid_layout)
        scroll.setWidget(scroll_widget)

        layout.addWidget(scroll)
        self.setLayout(layout)

        # Styling
        self.setStyleSheet(f"background-color: {Color.BG_PRIMARY};")

    def setup_monitors(self) -> None:
        """Start all monitoring services."""
        try:
            self.cpu_monitor.start()
            self.mem_monitor.start()
            self.disk_monitor.start()
            self.net_monitor.start()
            self.battery_monitor.start()
            logger.info("All monitors started")
        except Exception as e:
            logger.error(f"Error starting monitors: {e}")

    def setup_timer(self) -> None:
        """Setup update timer."""
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_metrics)
        self.timer.start(1000)  # Update every second

    def update_metrics(self) -> None:
        """Update all metrics from monitors."""
        try:
            # CPU
            cpu_metrics = self.cpu_monitor.get_metrics()
            if cpu_metrics:
                self.cpu_card.set_value(f"{cpu_metrics.percent:.1f}%", f"{cpu_metrics.core_count} cores")
                self.cpu_ring.set_progress(cpu_metrics.percent)
                self.cpu_history.append(cpu_metrics.percent)
                if len(self.cpu_history) > 100:
                    self.cpu_history.pop(0)

            # Memory
            mem_metrics = self.mem_monitor.get_metrics()
            if mem_metrics:
                used_gb = mem_metrics.used_mb / 1024
                total_gb = mem_metrics.total_mb / 1024
                self.mem_card.set_value(
                    f"{mem_metrics.percent:.1f}%",
                    f"{used_gb:.1f}GB / {total_gb:.1f}GB",
                )
                self.mem_ring.set_progress(mem_metrics.percent)
                self.mem_history.append(mem_metrics.percent)
                if len(self.mem_history) > 100:
                    self.mem_history.pop(0)

            # Battery
            battery_metrics = self.battery_monitor.get_metrics()
            if battery_metrics:
                status = "🔌 Charging" if battery_metrics.is_charging else "🔋 Discharging"
                self.battery_card.set_value(f"{battery_metrics.percent:.0f}%", status)

            # Network
            net_metrics = self.net_monitor.get_metrics()
            if net_metrics:
                total_mbps = (net_metrics.sent_bytes_per_sec + net_metrics.recv_bytes_per_sec) / (1024 * 1024)
                self.net_card.set_value(f"{total_mbps:.2f} Mbps", "↕️")

        except Exception as e:
            logger.error(f"Error updating metrics: {e}")

    def closeEvent(self, event) -> None:
        """Cleanup on close."""
        self.timer.stop()
        self.cpu_monitor.stop()
        self.mem_monitor.stop()
        self.disk_monitor.stop()
        self.net_monitor.stop()
        self.battery_monitor.stop()
        logger.info("Dashboard closed, all monitors stopped")
        super().closeEvent(event)
