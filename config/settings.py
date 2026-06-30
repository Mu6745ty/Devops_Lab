"""Settings management for PC Optimizer."""

import json
from pathlib import Path
from typing import Any, Dict, Optional

from loguru import logger

from config.constants import DATA_DIR


class Settings:
    """Application settings manager."""

    def __init__(self, config_file: Optional[Path] = None) -> None:
        """Initialize settings manager.

        Args:
            config_file: Path to config file. Defaults to data/settings.json
        """
        self.config_file = config_file or (DATA_DIR / "settings.json")
        self._settings: Dict[str, Any] = self._load_settings()
        logger.info(f"Settings loaded from {self.config_file}")

    def _load_settings(self) -> Dict[str, Any]:
        """Load settings from file or return defaults."""
        if self.config_file.exists():
            try:
                with open(self.config_file, "r") as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load settings: {e}. Using defaults.")
                return self._get_defaults()
        return self._get_defaults()

    @staticmethod
    def _get_defaults() -> Dict[str, Any]:
        """Get default settings."""
        return {
            "theme": "dark",
            "enable_notifications": True,
            "notification_interval_minutes": 5,
            "enable_ai_assistant": True,
            "enable_gaming_mode_auto_detect": False,
            "thermal_alert_threshold": 80.0,
            "battery_alert_threshold": 30.0,
            "startup_on_boot": False,
            "minimize_to_tray": True,
            "check_updates": True,
            "telemetry_enabled": False,
        }

    def save(self) -> None:
        """Save settings to file."""
        try:
            self.config_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_file, "w") as f:
                json.dump(self._settings, f, indent=2)
            logger.info(f"Settings saved to {self.config_file}")
        except Exception as e:
            logger.error(f"Failed to save settings: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value.

        Args:
            key: Setting key
            default: Default value if key not found

        Returns:
            Setting value or default
        """
        return self._settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set setting value.

        Args:
            key: Setting key
            value: New value
        """
        self._settings[key] = value
        logger.debug(f"Setting {key} = {value}")

    def update(self, updates: Dict[str, Any]) -> None:
        """Update multiple settings.

        Args:
            updates: Dictionary of key-value pairs to update
        """
        self._settings.update(updates)
        logger.debug(f"Updated {len(updates)} settings")

    def reset_to_defaults(self) -> None:
        """Reset all settings to defaults."""
        self._settings = self._get_defaults()
        logger.info("Settings reset to defaults")

    def __repr__(self) -> str:
        """String representation."""
        return f"Settings({self.config_file})"
