"""Dark theme configuration for PC Optimizer."""

from dataclasses import dataclass
from typing import Dict


@dataclass
class Color:
    """Color scheme."""

    # Primary Colors
    PRIMARY = "#007AFF"  # iOS Blue
    PRIMARY_DARK = "#0051D5"
    PRIMARY_LIGHT = "#5AC8FA"

    # Background Colors
    BG_PRIMARY = "#1e1e1e"  # Dark background
    BG_SECONDARY = "#2d2d2d"  # Slightly lighter
    BG_TERTIARY = "#3a3a3a"  # Even lighter

    # Text Colors
    TEXT_PRIMARY = "#ffffff"  # White text
    TEXT_SECONDARY = "#a0a0a0"  # Gray text
    TEXT_TERTIARY = "#707070"  # Lighter gray

    # Status Colors
    SUCCESS = "#34C759"  # Green
    WARNING = "#FF9500"  # Orange
    DANGER = "#FF3B30"  # Red
    INFO = "#30B0C0"  # Cyan

    # Border Colors
    BORDER = "#404040"
    BORDER_LIGHT = "#505050"


@dataclass
class Font:
    """Font configuration."""

    # Font Family
    PRIMARY = "Segoe UI"
    MONO = "Consolas"

    # Font Sizes (pt)
    TITLE_LARGE = 28
    TITLE = 24
    TITLE_SMALL = 20
    HEADING = 16
    HEADING_SMALL = 14
    BODY = 12
    BODY_SMALL = 11
    CAPTION = 10

    # Font Weights
    BOLD = "bold"
    SEMI_BOLD = "600"
    NORMAL = "normal"
    LIGHT = "300"


@dataclass
class Spacing:
    """Spacing configuration."""

    XS = 4
    SM = 8
    MD = 12
    LG = 16
    XL = 24
    XXL = 32
    XXXL = 48


@dataclass
class BorderRadius:
    """Border radius configuration."""

    SMALL = 4
    MEDIUM = 8
    LARGE = 12
    XLARGE = 16
    CIRCLE = 999


@dataclass
class Shadow:
    """Shadow configuration."""

    SMALL = "0px 2px 4px rgba(0, 0, 0, 0.2)"
    MEDIUM = "0px 4px 8px rgba(0, 0, 0, 0.3)"
    LARGE = "0px 8px 16px rgba(0, 0, 0, 0.4)"


class Theme:
    """Unified theme for the application."""

    color = Color()
    font = Font()
    spacing = Spacing()
    border_radius = BorderRadius()
    shadow = Shadow()

    @staticmethod
    def get_stylesheet() -> str:
        """Get global QSS stylesheet."""
        return f"""
        * {{
            font-family: {Color.PRIMARY};
            background-color: {Color.BG_PRIMARY};
            color: {Color.TEXT_PRIMARY};
        }}

        QMainWindow {{
            background-color: {Color.BG_PRIMARY};
        }}

        QWidget {{
            background-color: {Color.BG_PRIMARY};
        }}

        QPushButton {{
            background-color: {Color.PRIMARY};
            color: {Color.TEXT_PRIMARY};
            border: none;
            border-radius: {Color.MEDIUM}px;
            padding: 8px 16px;
            font-weight: bold;
            font-size: 12pt;
        }}

        QPushButton:hover {{
            background-color: {Color.PRIMARY_LIGHT};
        }}

        QPushButton:pressed {{
            background-color: {Color.PRIMARY_DARK};
        }}

        QLineEdit {{
            background-color: {Color.BG_SECONDARY};
            color: {Color.TEXT_PRIMARY};
            border: 1px solid {Color.BORDER};
            border-radius: {Color.SMALL}px;
            padding: 8px;
            font-size: 12pt;
        }}

        QLineEdit:focus {{
            border: 1px solid {Color.PRIMARY};
        }}

        QLabel {{
            color: {Color.TEXT_PRIMARY};
        }}

        QScrollArea {{
            background-color: {Color.BG_PRIMARY};
            border: none;
        }}

        QScrollBar:vertical {{
            background-color: {Color.BG_SECONDARY};
            width: 8px;
        }}

        QScrollBar::handle:vertical {{
            background-color: {Color.BORDER_LIGHT};
            border-radius: 4px;
        }}

        QScrollBar::handle:vertical:hover {{
            background-color: {Color.TEXT_SECONDARY};
        }}
        """
