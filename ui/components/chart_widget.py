"""Chart widget for displaying metrics."""

from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from typing import List, Tuple


class ChartWidget(QWidget):
    """Simple line chart widget."""

    def __init__(self):
        """Initialize chart widget."""
        super().__init__()
        self.data: List[float] = []
        self.setup_ui()

    def setup_ui(self) -> None:
        """Setup UI."""
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setStyleSheet(
            """
            ChartWidget {
                background-color: #2d2d2d;
                border: 1px solid #404040;
                border-radius: 8px;
            }
        """
        )

    def set_data(self, data: List[float]) -> None:
        """Set chart data.

        Args:
            data: List of data points
        """
        self.data = data
        self.update()

    def add_data_point(self, value: float) -> None:
        """Add data point.

        Args:
            value: Data point value
        """
        self.data.append(value)
        if len(self.data) > 100:  # Keep last 100 points
            self.data.pop(0)
        self.update()
