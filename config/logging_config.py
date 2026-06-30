"""Logging configuration for PC Optimizer."""

import sys

from loguru import logger

from config.constants import LOG_FORMAT, LOG_LEVEL, LOG_RETENTION, LOG_ROTATION, LOGS_DIR


def setup_logging(level: str = LOG_LEVEL, log_file: bool = True) -> None:
    """Configure logging for the application.

    Args:
        level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Whether to write to log file
    """
    # Remove default handler
    logger.remove()

    # Add console handler
    logger.add(
        sys.stderr,
        format=LOG_FORMAT,
        level=level,
        colorize=True,
    )

    # Add file handler
    if log_file:
        logger.add(
            LOGS_DIR / "pc_optimizer.log",
            format=LOG_FORMAT,
            level=level,
            rotation=LOG_ROTATION,
            retention=LOG_RETENTION,
        )
        logger.add(
            LOGS_DIR / "pc_optimizer_error.log",
            format=LOG_FORMAT,
            level="ERROR",
            rotation=LOG_ROTATION,
            retention=LOG_RETENTION,
        )

    logger.info("Logging initialized")


def get_logger(name: str = "pc_optimizer"):
    """Get logger instance.

    Args:
        name: Logger name

    Returns:
        Logger instance
    """
    return logger.bind(name=name)
