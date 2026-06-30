"""Custom widgets for PC Optimizer UI."""

from PyQt6.QtWidgets import QPushButton, QFrame, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QIcon
from ui.theme import Color, Font, Spacing, BorderRadius


class CustomButton(QPushButton):
    """Custom styled button."""

    def __init__(self, text: str, button_type: str = "primary"):
        """Initialize custom button.

        Args:
            text: Button text
            button_type: primary, secondary, danger, success
        """
        super().__init__(text)
        self.button_type = button_type
        self.setup_style()

    def setup_style(self) -> None:
        """Setup button style."""
        font = QFont(Font.PRIMARY)
        font.setPointSize(Font.HEADING_SMALL)
        font.setBold(True)
        self.setFont(font)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(40)
        self.setMinimumWidth(80)

        color_map = {
            "primary": Color.PRIMARY,
            "secondary": Color.BG_TERTIARY,
            "danger": Color.DANGER,
            "success": Color.SUCCESS,
            "warning": Color.WARNING,
        }
        bg_color = color_map.get(self.button_type, Color.PRIMARY)

        self.setStyleSheet(f"""
            CustomButton {{
                background-color: {bg_color};
                color: {Color.TEXT_PRIMARY};
                border: none;
                border-radius: {BorderRadius.MEDIUM}px;
                padding: 8px 16px;
                font-weight: bold;
            }}
            CustomButton:hover {{
                opacity: 0.8;
            }}
            CustomButton:pressed {{
                opacity: 0.6;
            }}
        """)


class CardWidget(QFrame):
    """Card-style widget with rounded corners and shadow."""

    def __init__(self):
        """Initialize card widget."""
        super().__init__()
        self.setup_style()

    def setup_style(self) -> None:
        """Setup card style."""
        self.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Plain)
        self.setStyleSheet(f"""
            CardWidget {{
                background-color: {Color.BG_SECONDARY};
                border: 1px solid {Color.BORDER};
                border-radius: {BorderRadius.LARGE}px;
                padding: {Spacing.MD}px;
            }}
        """)


class SectionHeader(QLabel):
    """Section header label."""

    def __init__(self, text: str):
        """Initialize section header.

        Args:
            text: Header text
        """
        super().__init__(text)
        font = QFont(Font.PRIMARY)
        font.setPointSize(Font.HEADING)
        font.setBold(True)
        self.setFont(font)
        self.setStyleSheet(f"color: {Color.TEXT_PRIMARY};")
