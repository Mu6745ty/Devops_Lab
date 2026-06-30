# PC Optimizer - AI-Powered Windows System Optimizer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyQt6](https://img.shields.io/badge/PyQt6-Latest-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Status](https://img.shields.io/badge/Status-Phase%202-yellow)

## Overview

PC Optimizer is a next-generation, AI-powered Windows system optimization tool built with Python and PyQt6. It provides real-time monitoring, intelligent recommendations, and advanced performance management.

### Features

- 🖥️ **Real-time System Monitoring** - CPU, RAM, GPU, Disk, Network, Temperature, Battery
- 🤖 **AI-Powered Recommendations** - Intelligent analysis and actionable insights
- 📊 **Advanced Dashboards** - Beautiful, responsive dark-themed UI
- ⚙️ **Process Management** - Superior to Windows Task Manager
- 🎮 **Gaming Mode** - Optimize for gaming with one click
- 🌡️ **Thermal Management** - Temperature monitoring and alerts
- 💾 **Storage Analysis** - Disk usage visualization and cleanup
- 🔋 **Battery Intelligence** - Health monitoring for laptops
- 📈 **Performance Reports** - Daily, weekly, monthly analysis with PDF export
- 🔐 **Security Scanner** - Driver status, Windows Updates, suspicious processes

## System Requirements

- **OS**: Windows 10 / Windows 11
- **Python**: 3.10+
- **RAM**: 2 GB minimum
- **Disk**: 200 MB for installation

## Installation & Setup

### From Source

```bash
# Clone the repository
git clone https://github.com/Mu6745ty/Devops_Lab.git
cd Devops_Lab
git checkout phase-2-core-services

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v

# Run the application
python main.py
```

### Project Structure

```
PC-Optimizer/
├── config/              # Configuration and constants
├── core/                # Core infrastructure
├── models/              # Data models
├── services/            # Business logic
│   ├── monitoring/      # System monitoring
│   ├── process/         # Process management
│   ├── system/          # System information
│   ├── optimization/    # Optimization tools
│   ├── ai/              # AI analysis
│   ├── reporting/       # Report generation
│   └── database/        # Database layer
├── ui/                  # User interface (Phase 3)
├── tests/               # Test suite
├── build/               # Build scripts
├── docs/                # Documentation
└── main.py              # Entry point
```

## Architecture

- **MVC/MVVM Pattern** - Separation of concerns
- **Service Layer** - Independent, testable modules
- **Thread-Safe** - Concurrent monitoring without blocking UI
- **Event Bus** - Inter-module communication
- **Type Hints** - Full static typing
- **Comprehensive Logging** - Debug and production monitoring

## Development

### Setup Development Environment

```bash
pip install -r requirements-dev.txt
pre-commit install
```

### Code Quality

```bash
black .
flake8 .
mypy .
```

### Run Tests

```bash
pytest tests/ -v --cov=services --cov-report=html
```

## Roadmap

- [x] Phase 1: Architecture Design
- [x] Phase 2: Core Services (CURRENT)
- [ ] Phase 3: UI Framework
- [ ] Phase 4: Feature Implementation
- [ ] Phase 5: Testing & Polish
- [ ] Phase 6: Build & Release

## License

MIT License - see LICENSE file for details

---

**Status**: Phase 2 core infrastructure complete with monitoring services, database layer, and comprehensive testing.
