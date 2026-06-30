"""Stat card component for displaying key metrics."""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from ui.theme import Color, Font, Spacing, BorderRadius


class StatCard(QWidget):
    """Beautiful stat card for displaying metrics."""

    def __init__(self, title: str, value: str, unit: str = "", icon: str = "📊"):
        """Initialize stat card.

        Args:
            title: Card title
            value: Main value to display
            unit: Unit of measurement
            icon: Emoji icon
        """
        super().__init__()
        self.title = title
        self.value = value
        self.unit = unit
        self.icon = icon
        self.setup_ui()

    def setup_ui(self) -> None:
        """Setup UI components."""
        layout = QVBoxLayout()
        layout.setContentsMargins(
            Spacing.MD,
            Spacing.MD,
            Spacing.MD,
            Spacing.MD,
        )
        layout.setSpacing(Spacing.SM)

        # Icon and Title
        title_label = QLabel(f"{self.icon} {self.title}")
        title_font = QFont(Font.PRIMARY)
        title_font.setPointSize(Font.HEADING_SMALL)
        title_label.setFont(title_font)
        title_label.setStyleSheet(f"color: {Color.TEXT_SECONDARY}; font-weight: bold;")

        # Value
        value_label = QLabel(self.value)
        value_font = QFont(Font.PRIMARY)
        value_font.setPointSize(Font.TITLE_SMALL)
        value_font.setBold(True)
        value_label.setFont(value_font)
        value_label.setStyleSheet(f"color: {Color.PRIMARY};")

        # Unit
        if self.unit:
            unit_label = QLabel(self.unit)
            unit_font = QFont(Font.PRIMARY)
            unit_font.setPointSize(Font.BODY_SMALL)
            unit_label.setFont(unit_font)
            unit_label.setStyleSheet(f"color: {Color.TEXT_SECONDARY};")

        layout.addWidget(title_label)
        layout.addWidget(value_label)
        if self.unit:
            layout.addWidget(unit_label)
        layout.addStretch()

        self.setLayout(layout)

        # Styling
        self.setStyleSheet(f"""
            StatCard {{
                background-color: {Color.BG_SECONDARY};
                border: 1px solid {Color.BORDER};
                border-radius: {BorderRadius.MEDIUM}px;
            }}
        """)

    def set_value(self, value: str, unit: str = "") -> None:
        """Update card value.

        Args:
            value: New value
            unit: New unit
        """
        self.value = value
        self.unit = unit
        self.setup_ui()
