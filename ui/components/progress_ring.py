"""Circular progress ring component."""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QFont, QPainter, QColor, QPen, QBrush
from ui.theme import Color, Font, Spacing


class ProgressRing(QWidget):
    """Circular progress indicator."""

    def __init__(self, size: int = 120, label: str = ""):
        """Initialize progress ring.

        Args:
            size: Size of the ring in pixels
            label: Label to display below
        """
        super().__init__()
        self.size = size
        self.label = label
        self.progress = 0
        self.max_value = 100
        self.color = Color.PRIMARY
        self.setup_ui()

    def setup_ui(self) -> None:
        """Setup UI."""
        layout = QVBoxLayout()
        layout.setContentsMargins(Spacing.MD, Spacing.MD, Spacing.MD, Spacing.MD)

        self.setMinimumSize(self.size, self.size)
        self.setMaximumSize(self.size, self.size)
        self.setStyleSheet(f"background-color: transparent;")

    def set_progress(self, value: float) -> None:
        """Set progress value.

        Args:
            value: Progress value (0-100)
        """
        self.progress = max(0, min(100, value))
        self.update()

    def set_color(self, color: str) -> None:
        """Set ring color.

        Args:
            color: Hex color code
        """
        self.color = color
        self.update()

    def paintEvent(self, event) -> None:
        """Paint the progress ring."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        center_x = self.width() / 2
        center_y = self.height() / 2
        radius = (self.size - 20) / 2

        # Background circle
        bg_pen = QPen(QColor(Color.BORDER))
        bg_pen.setWidth(8)
        painter.setPen(bg_pen)
        painter.drawEllipse(
            int(center_x - radius),
            int(center_y - radius),
            int(radius * 2),
            int(radius * 2),
        )

        # Progress circle
        fg_pen = QPen(QColor(self.color))
        fg_pen.setWidth(8)
        fg_pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(fg_pen)

        start_angle = 90 * 16  # Qt uses 1/16 degree units, start at top
        arc_length = int((self.progress / self.max_value) * 360 * 16)
        painter.drawArc(
            int(center_x - radius),
            int(center_y - radius),
            int(radius * 2),
            int(radius * 2),
            start_angle,
            -arc_length,
        )

        # Text
        text = f"{int(self.progress)}%"
        font = QFont(Font.PRIMARY)
        font.setPointSize(14)
        font.setBold(True)
        painter.setFont(font)
        painter.setPen(QPen(QColor(Color.TEXT_PRIMARY)))
        metrics = painter.fontMetrics()
        text_width = metrics.horizontalAdvance(text)
        text_height = metrics.height()
        painter.drawText(
            int(center_x - text_width / 2),
            int(center_y + text_height / 4),
            text,
        )
