"""Database management service."""

from sqlalchemy.orm import Session
from loguru import logger

from config.database import DatabaseConfig
from core.base_service import BaseService
from models.database_models import Base


class DatabaseManager(BaseService):
    """Manages database operations and lifecycle."""

    def __init__(self) -> None:
        """Initialize database manager."""
        super().__init__("DatabaseManager")
        self.config = DatabaseConfig()

    def start(self) -> None:
        """Initialize database and create tables."""
        try:
            engine = self.config.get_engine()
            Base.metadata.create_all(engine)
            self.is_running = True
            logger.info("Database initialized and tables created")
        except Exception as e:
            self.set_error(e)
            logger.error(f"Failed to initialize database: {e}")
            raise

    def stop(self) -> None:
        """Shutdown database."""
        try:
            self.config.dispose_engine()
            self.is_running = False
            logger.info("Database shutdown complete")
        except Exception as e:
            self.set_error(e)
            logger.error(f"Error during database shutdown: {e}")

    def get_session(self) -> Session:
        """Get new database session.

        Returns:
            New SQLAlchemy Session
        """
        return self.config.get_session()

    def close_session(self, session: Session) -> None:
        """Close database session.

        Args:
            session: Session to close
        """
        self.config.close_session(session)
