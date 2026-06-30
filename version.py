"""Version management for PC Optimizer."""

__version__ = "0.2.0"
__author__ = "Mu6745ty"
__license__ = "MIT"

VERSION_INFO = {
    "major": 0,
    "minor": 2,
    "patch": 0,
    "phase": "Phase 2: Core Services",
    "status": "Production Ready",
}

def get_version() -> str:
    """Get formatted version string."""
    return f"v{__version__}"

def get_version_info() -> str:
    """Get detailed version information."""
    return (
        f"PC Optimizer {get_version()}\n"
        f"Phase: {VERSION_INFO['phase']}\n"
        f"Status: {VERSION_INFO['status']}"
    )
