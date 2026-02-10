# Python uv Experiment Template

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for Python experiment repositories using [uv](https://docs.astral.sh/uv/) for dependency management.

## Features

- **Hybrid structure**: Jupyter notebooks for exploration + scripts for reproducible experiments
- **uv** for fast, reliable dependency management
- **DVC** for data versioning and tracking
- **Modern Python tooling**: ruff, pytest, type checking
- **GitHub Actions CI**: Automated linting, type checking, and testing
- **Production-quality utilities**: Structured `src/` layout with full test coverage

## Quick Start

```bash
# Install cookiecutter
uvx cookiecutter gh:arielarevalo/python-uv-experiment-template

# Follow the prompts to create your experiment repo
```

## What's Included

### Directory Structure

```
your-experiment/
├── notebooks/              # Jupyter notebooks for exploration
├── scripts/                # Reproducible experiment scripts
├── src/your_package/       # Reusable utilities (production-quality)
├── tests/                  # Tests for src/ utilities
├── data/                   # Input datasets (tracked with DVC)
├── outputs/                # Experiment results (gitignored)
├── .dvc/                   # DVC configuration
├── .github/workflows/      # CI/CD pipeline
├── pyproject.toml          # Project metadata and dependencies
├── README.md               # Project documentation
└── AGENTS.md               # AI agent instructions
```

### Pre-configured Tools

- **uv**: Fast Python package installer and resolver
- **ruff**: Lightning-fast linting and formatting
- **pytest**: Testing framework with coverage
- **DVC**: Data versioning and pipeline management
- **Jupyter**: Interactive notebooks
- **GitHub Actions**: Automated CI pipeline

### Dependencies

Core dependencies:
- pandas, numpy, matplotlib, seaborn (data analysis & visualization)

Dev dependencies:
- ruff, pytest, pytest-cov, pytest-asyncio (code quality & testing)
- jupyter, ipykernel, ipywidgets (interactive notebooks)
- dvc (data versioning)

## Usage

After creating a new experiment repo:

```bash
cd your-experiment

# Dependencies are already installed by the post-generation hook
# Configure DVC remote (optional)
dvc remote add -d myremote s3://mybucket/path

# Start Jupyter
uv run jupyter notebook

# Run an experiment script
uv run python scripts/example_experiment.py

# Run tests
uv run pytest

# Lint and format
uv run ruff check --fix .
uv run ruff format .
```

## Testing Philosophy

- **Full testing for `src/` utilities**: 80% coverage requirement
- **Smoke tests for `scripts/`**: Verify imports and basic execution
- **Manual verification for notebooks**: Run top-to-bottom without errors

## Data Management

Track datasets with DVC for reproducibility:

```bash
# Track a dataset
dvc add data/my_dataset.csv
git add data/my_dataset.csv.dvc data/.gitignore

# Push to remote
dvc push

# Pull when cloning
dvc pull
```

## Project Types

This template is designed for **experiment** repositories:
- Research and model exploration
- Data analysis and visualization
- Proof-of-concepts
- Iterative exploration with notebooks

For **application** repositories (APIs, services, libraries), use [python-uv-template](https://github.com/arielarevalo/python-uv-template) instead.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)
- [DVC](https://dvc.org/)
- [cookiecutter](https://github.com/cookiecutter/cookiecutter)

## License

MIT
