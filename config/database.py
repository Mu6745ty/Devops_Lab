"""Database configuration and connection management."""

from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool

from config.constants import DATABASE_POOL_TIMEOUT, DATABASE_URL
from loguru import logger


class DatabaseConfig:
    """Database configuration and session management."""

    _engine: Engine | None = None
    _session_factory: sessionmaker | None = None

    @classmethod
    def get_engine(cls) -> Engine:
        """Get or create database engine.

        Returns:
            SQLAlchemy Engine instance
        """
        if cls._engine is None:
            cls._engine = create_engine(
                DATABASE_URL,
                connect_args={"timeout": DATABASE_POOL_TIMEOUT},
                poolclass=StaticPool,
                echo=False,
                pool_pre_ping=True,
            )
            logger.info(f"Database engine created: {DATABASE_URL}")
        return cls._engine

    @classmethod
    def get_session_factory(cls) -> sessionmaker:
        """Get or create session factory.

        Returns:
            SQLAlchemy session factory
        """
        if cls._session_factory is None:
            cls._session_factory = sessionmaker(
                bind=cls.get_engine(),
                expire_on_commit=False,
            )
        return cls._session_factory

    @classmethod
    def get_session(cls) -> Session:
        """Get new database session.

        Returns:
            New SQLAlchemy Session
        """
        return cls.get_session_factory()()

    @classmethod
    def close_session(cls, session: Session) -> None:
        """Close database session.

        Args:
            session: Session to close
        """
        if session:
            session.close()

    @classmethod
    def dispose_engine(cls) -> None:
        """Dispose of engine and clear connection pool."""
        if cls._engine:
            cls._engine.dispose()
            cls._engine = None
            logger.info("Database engine disposed")


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_conn, connection_record):
    """Enable foreign keys for SQLite."""
    cursor = dbapi_conn.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
