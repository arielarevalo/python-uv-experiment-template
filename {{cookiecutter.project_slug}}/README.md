# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Prerequisites

- Python {{ cookiecutter.python_version }}+
- [uv](https://docs.astral.sh/uv/) for dependency management
- [DVC](https://dvc.org/) for data versioning

## Setup

```bash
# Install dependencies
uv sync

# Configure DVC remote (optional, for data versioning)
dvc remote add -d myremote <s3://bucket/path or gs://bucket/path>

# Pull data (if DVC remote is configured)
dvc pull
```

## Data Setup

Place your datasets in the `data/` directory:

```bash
# Track a dataset with DVC
dvc add data/your_dataset.csv
git add data/your_dataset.csv.dvc data/.gitignore
git commit -m "Add dataset"
```

## Run Experiments

### Jupyter Notebooks

```bash
# Start Jupyter notebook server
uv run jupyter notebook

# Or use JupyterLab
uv run jupyter lab
```

Notebooks are located in `notebooks/`. Run them interactively for exploration and visualization.

### Scripts

```bash
# Run an experiment script
uv run python scripts/experiment_name.py
```

Scripts are for reproducible experiments. Outputs are saved to `outputs/`.

## Testing

```bash
# Run tests for utilities in src/
uv run pytest

# Run with coverage
uv run pytest --cov={{ cookiecutter.package_name }} --cov-report=html
```

Note: Notebooks are not tested automatically. Verify manually by running top-to-bottom.

## Code Quality

```bash
# Lint
uv run ruff check --fix .

# Format
uv run ruff format .

# Type check
uvx ty check
```

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── notebooks/          # Jupyter notebooks for exploration
├── scripts/            # Reproducible experiment scripts
├── src/
│   └── {{ cookiecutter.package_name }}/  # Reusable utilities and helpers
├── tests/              # Tests for src/ utilities
├── data/               # Input datasets (gitignored)
├── outputs/            # Experiment results (gitignored)
├── .dvc/               # DVC configuration
├── pyproject.toml      # Project metadata and dependencies
└── README.md           # This file
```

## Results Summary

<!-- Update this section as you complete experiments -->

### Experiment 1: [Name]

- **Goal**: [What you're trying to learn/achieve]
- **Approach**: [Brief description of methodology]
- **Key Findings**: [Main results]
- **Artifacts**: [Links to notebooks, plots, or outputs]

---

**Note**: This is an experiment repository. Code in `notebooks/` and `scripts/` is exploratory. Production-quality utilities should be in `src/` with full test coverage.
