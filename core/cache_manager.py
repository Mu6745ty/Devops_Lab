"""In-memory caching for frequently accessed data."""

from datetime import datetime, timedelta
from typing import Any, Dict, Optional

from loguru import logger

from config.constants import CACHE_MAX_SIZE, CACHE_TTL


class CacheEntry:
    """Individual cache entry with TTL."""

    def __init__(self, key: str, value: Any, ttl: int = CACHE_TTL) -> None:
        """Initialize cache entry.

        Args:
            key: Cache key
            value: Cached value
            ttl: Time to live in seconds
        """
        self.key = key
        self.value = value
        self.created_at = datetime.now()
        self.expires_at = self.created_at + timedelta(seconds=ttl)

    def is_expired(self) -> bool:
        """Check if entry has expired.

        Returns:
            True if expired
        """
        return datetime.now() > self.expires_at


class CacheManager:
    """Simple in-memory cache with TTL support."""

    def __init__(self, max_size: int = CACHE_MAX_SIZE) -> None:
        """Initialize cache manager.

        Args:
            max_size: Maximum number of entries
        """
        self.max_size = max_size
        self._cache: Dict[str, CacheEntry] = {}
        logger.info(f"Cache initialized with max size {max_size}")

    def get(self, key: str) -> Optional[Any]:
        """Get value from cache.

        Args:
            key: Cache key

        Returns:
            Cached value or None if not found or expired
        """
        if key in self._cache:
            entry = self._cache[key]
            if entry.is_expired():
                del self._cache[key]
                return None
            return entry.value
        return None

    def set(self, key: str, value: Any, ttl: int = CACHE_TTL) -> None:
        """Set value in cache.

        Args:
            key: Cache key
            value: Value to cache
            ttl: Time to live in seconds
        """
        # Evict oldest entry if cache is full
        if len(self._cache) >= self.max_size and key not in self._cache:
            oldest_key = min(
                self._cache.keys(),
                key=lambda k: self._cache[k].created_at,
            )
            del self._cache[oldest_key]
            logger.debug(f"Evicted cache entry: {oldest_key}")

        self._cache[key] = CacheEntry(key, value, ttl)
        logger.debug(f"Cache set: {key} (ttl={ttl}s)")

    def delete(self, key: str) -> None:
        """Delete value from cache.

        Args:
            key: Cache key
        """
        if key in self._cache:
            del self._cache[key]
            logger.debug(f"Cache deleted: {key}")

    def clear(self) -> None:
        """Clear entire cache."""
        self._cache.clear()
        logger.info("Cache cleared")

    def cleanup_expired(self) -> None:
        """Remove all expired entries."""
        expired_keys = [k for k, v in self._cache.items() if v.is_expired()]
        for key in expired_keys:
            del self._cache[key]
        if expired_keys:
            logger.debug(f"Cleaned up {len(expired_keys)} expired cache entries")

    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics.

        Returns:
            Cache statistics
        """
        return {
            "size": len(self._cache),
            "max_size": self.max_size,
            "usage_percent": (len(self._cache) / self.max_size) * 100,
        }

    def __repr__(self) -> str:
        """String representation."""
        return f"CacheManager(size={len(self._cache)}/{self.max_size})"
