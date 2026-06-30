"""Thread pool and concurrent execution management."""

from concurrent.futures import ThreadPoolExecutor, Future
from typing import Callable, Any, Optional

from loguru import logger

from config.constants import THREAD_POOL_SIZE, THREAD_POOL_TIMEOUT


class ThreadManager:
    """Manages thread pool for concurrent operations."""

    _instance: Optional['ThreadManager'] = None
    _executor: Optional[ThreadPoolExecutor] = None

    def __new__(cls) -> 'ThreadManager':
        """Singleton pattern."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """Initialize thread manager."""
        if self._executor is None:
            self._executor = ThreadPoolExecutor(
                max_workers=THREAD_POOL_SIZE,
                thread_name_prefix="PC-Optimizer",
            )
            logger.info(f"Thread pool initialized with {THREAD_POOL_SIZE} workers")

    def submit(self, func: Callable, *args: Any, **kwargs: Any) -> Future:
        """Submit a task to the thread pool.

        Args:
            func: Callable to execute
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Future object for the task
        """
        if self._executor is None:
            raise RuntimeError("Thread pool not initialized")
        return self._executor.submit(func, *args, **kwargs)

    def shutdown(self, wait: bool = True) -> None:
        """Shutdown thread pool.

        Args:
            wait: Whether to wait for pending tasks
        """
        if self._executor:
            self._executor.shutdown(wait=wait)
            self._executor = None
            logger.info("Thread pool shutdown")

    def __repr__(self) -> str:
        """String representation."""
        return f"ThreadManager(workers={THREAD_POOL_SIZE})"
