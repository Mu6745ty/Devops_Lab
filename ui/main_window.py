"""Main application window."""

from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QPushButton,
    QLabel,
)
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtGui import QFont, QIcon
from loguru import logger

from ui.theme import Color, Font, Spacing, BorderRadius
from ui.views.dashboard_view import DashboardView
from version import get_version_info


class MainWindow(QMainWindow):
    """Main application window with navigation."""

    def __init__(self):
        """Initialize main window."""
        super().__init__()
        self.setWindowTitle("PC Optimizer")
        self.setGeometry(100, 100, 1400, 900)
        self.setup_ui()
        self.apply_theme()
        logger.info("Main window initialized")

    def setup_ui(self) -> None:
        """Setup main UI."""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Sidebar
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar)

        # Content area
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)

        # Header
        header = self.create_header()
        content_layout.addWidget(header)

        # Stacked widget for views
        self.stacked_widget = QStackedWidget()
        self.dashboard_view = DashboardView()
        self.stacked_widget.addWidget(self.dashboard_view)
        content_layout.addWidget(self.stacked_widget)

        main_layout.addWidget(content, 1)

    def create_header(self) -> QWidget:
        """Create top header."""
        header = QWidget()
        header.setMaximumHeight(60)
        header.setStyleSheet(f"background-color: {Color.BG_SECONDARY}; border-bottom: 1px solid {Color.BORDER};")

        layout = QHBoxLayout(header)
        layout.setContentsMargins(Spacing.XL, Spacing.MD, Spacing.XL, Spacing.MD)

        # Title
        title = QLabel("⚡ PC Optimizer")
        title_font = QFont(Font.PRIMARY)
        title_font.setPointSize(Font.HEADING)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setStyleSheet(f"color: {Color.PRIMARY};")

        # Version info
        version = QLabel(f"v0.3.0 • Phase 3: UI Framework")
        version_font = QFont(Font.PRIMARY)
        version_font.setPointSize(Font.BODY_SMALL)
        version.setFont(version_font)
        version.setStyleSheet(f"color: {Color.TEXT_SECONDARY};")

        layout.addWidget(title)
        layout.addSpacing(Spacing.XL)
        layout.addWidget(version)
        layout.addStretch()

        return header

    def create_sidebar(self) -> QWidget:
        """Create left sidebar with navigation."""
        sidebar = QWidget()
        sidebar.setMaximumWidth(200)
        sidebar.setStyleSheet(f"background-color: {Color.BG_SECONDARY};")

        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(Spacing.MD, Spacing.XL, Spacing.MD, Spacing.XL)
        layout.setSpacing(Spacing.MD)

        # Navigation items
        nav_items = [
            ("📊", "Dashboard"),
            ("⚙️", "Hardware"),
            ("📋", "Processes"),
            ("🚀", "Startup"),
            ("💾", "Storage"),
            ("🧹", "Cleaner"),
            ("🎮", "Gaming"),
            ("🌡️", "Temperature"),
            ("🔋", "Battery"),
            ("🌐", "Network"),
            ("📊", "Reports"),
            ("⚙️", "Settings"),
        ]

        for icon, label in nav_items:
            btn = QPushButton(f"{icon} {label}")
            btn.setMinimumHeight(40)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: transparent;
                    color: {Color.TEXT_SECONDARY};
                    border: none;
                    border-left: 3px solid transparent;
                    padding-left: 10px;
                    text-align: left;
                    font-weight: bold;
                }}
                QPushButton:hover {{
                    background-color: {Color.BG_TERTIARY};
                    color: {Color.TEXT_PRIMARY};
                }}
                QPushButton:pressed {{
                    border-left: 3px solid {Color.PRIMARY};
                    color: {Color.PRIMARY};
                }}
            """)
            layout.addWidget(btn)

        layout.addStretch()

        # Footer
        footer = QLabel("Made with ❤️")
        footer_font = QFont(Font.PRIMARY)
        footer_font.setPointSize(Font.CAPTION)
        footer.setFont(footer_font)
        footer.setStyleSheet(f"color: {Color.TEXT_TERTIARY}; text-align: center;")
        layout.addWidget(footer)

        return sidebar

    def apply_theme(self) -> None:
        """Apply dark theme to entire application."""
        from ui.theme import Theme

        self.setStyleSheet(Theme.get_stylesheet())
        self.setWindowIcon(QIcon())
        logger.info("Dark theme applied")

    def closeEvent(self, event) -> None:
        """Cleanup on application close."""
        logger.info("Application closing")
        self.dashboard_view.closeEvent(event)
        super().closeEvent(event)
