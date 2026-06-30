"""Application entry point with PyQt6 integration."""

import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from loguru import logger

from config.logging_config import setup_logging
from version import get_version_info
from ui.main_window import MainWindow


def main() -> int:
    """Main application entry point."""
    # Setup logging
    setup_logging()
    logger.info("=" * 80)
    logger.info(get_version_info())
    logger.info("=" * 80)

    try:
        # Create QApplication
        app = QApplication(sys.argv)
        app.setApplicationName("PC Optimizer")
        app.setApplicationVersion("0.3.0")

        # Set window icon
        app.setStyle("Fusion")

        # Create main window
        logger.info("Creating main window...")
        window = MainWindow()
        window.show()

        logger.info("Application started")
        return app.exec()

    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
