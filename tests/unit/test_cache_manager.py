"""Unit tests for cache manager."""

import pytest
import time
from core.cache_manager import CacheManager


class TestCacheManager:
    """Test cases for CacheManager."""

    @pytest.fixture
    def cache(self):
        """Create cache manager instance."""
        return CacheManager(max_size=10)

    def test_set_and_get(self, cache):
        """Test setting and getting cache values."""
        cache.set("key1", "value1")
        assert cache.get("key1") == "value1"

    def test_delete(self, cache):
        """Test deleting cache values."""
        cache.set("key1", "value1")
        cache.delete("key1")
        assert cache.get("key1") is None

    def test_clear(self, cache):
        """Test clearing cache."""
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        cache.clear()
        assert cache.get("key1") is None
        assert cache.get("key2") is None

    def test_expiration(self, cache):
        """Test cache expiration."""
        cache.set("key1", "value1", ttl=1)
        assert cache.get("key1") == "value1"
        time.sleep(1.1)
        assert cache.get("key1") is None

    def test_max_size(self, cache):
        """Test max size enforcement."""
        for i in range(15):
            cache.set(f"key{i}", f"value{i}")
        assert len(cache._cache) <= 10

    def test_stats(self, cache):
        """Test cache statistics."""
        cache.set("key1", "value1")
        stats = cache.get_stats()
        assert "size" in stats
        assert "max_size" in stats
        assert "usage_percent" in stats
