"""Pytest configuration and fixtures."""

import pytest
from pathlib import Path
import sys

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from config.logging_config import setup_logging


@pytest.fixture(scope="session", autouse=True)
def setup_logging_for_tests():
    """Setup logging for tests."""
    setup_logging(level="DEBUG", log_file=False)
