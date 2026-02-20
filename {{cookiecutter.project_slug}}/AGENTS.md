# Agent Instructions

## Project Type

**experiment**

This is a research/exploration repository for {{ cookiecutter.project_description.lower() }}.

## Key Commands

### Run Experiments

```bash
# Start Jupyter for interactive exploration
uv run jupyter notebook

# Run a specific experiment script
uv run python scripts/<experiment_name>.py
```

### Data Management

```bash
# Pull latest data from DVC remote
dvc pull

# Track a new dataset
dvc add data/new_dataset.csv
git add data/new_dataset.csv.dvc data/.gitignore

# Push data to remote
dvc push
```

### Testing & Quality

```bash
# Run tests (for src/ utilities only)
uv run pytest

# Lint and format
uv run ruff check --fix .
uv run ruff format .

# Type check
uvx ty check
```

## Project Conventions

### Code Organization

- **`notebooks/`**: Interactive exploration, visualization, one-off analysis
  - Name with descriptive prefixes: `01_data_exploration.ipynb`, `02_model_comparison.ipynb`
  - Should run top-to-bottom without errors (Restart Kernel & Run All)
  - Document findings and insights inline with markdown cells

- **`scripts/`**: Reproducible experiments with consistent outputs
  - Parameterized with CLI arguments or config files
  - Save results to `outputs/` with timestamped or versioned names
  - Type-hinted and linted, but can be more exploratory than production code

- **`src/{{ cookiecutter.package_name }}/`**: Reusable utilities and helpers
  - Production-quality code: type-hinted, documented, tested
  - Functions used across multiple notebooks/scripts
  - Must have 80% test coverage

### Testing Requirements

- **Full testing for `src/`**: Unit + integration tests, 80% coverage
- **Smoke tests for `scripts/`**: Verify imports and basic execution
- **Manual verification for `notebooks/`**: Run top-to-bottom, no automated tests

### Data & Outputs

- All datasets go in `data/` (tracked with DVC if > 10MB)
- All experiment outputs go in `outputs/` (gitignored)
- Document data sources and preprocessing steps in README
- Use descriptive names: `data/raw_dataset.csv`, `outputs/experiment1_results.png`

### Commits

- Commit notebooks with cleared outputs for cleaner diffs:
  ```bash
  jupyter nbconvert --clear-output --inplace notebooks/*.ipynb
  ```
- Always commit with passing tests (for `src/` utilities)
- Update README "Results Summary" section when completing experiments

### Paper

```bash
# Build the PDF (requires pdflatex and bibtex)
bash paper/build.sh
```

Edit sections in `paper/sections/`. The output PDF is `paper/main.pdf` (gitignored).

## Common Workflows

### Starting a New Experiment

1. Create notebook in `notebooks/` or script in `scripts/`
2. Import utilities from `src.{{ cookiecutter.package_name }}`
3. Load data from `data/` (pull with `dvc pull` if needed)
4. Explore, analyze, visualize
5. Save results to `outputs/`
6. Document findings in README or notebook markdown

### Adding a Reusable Utility

1. Write function in `src/{{ cookiecutter.package_name }}/`
2. Add type hints and docstring
3. Write tests in `tests/`
4. Verify coverage: `uv run pytest --cov`
5. Use in notebooks/scripts

### Sharing Results

1. Clear notebook outputs: `jupyter nbconvert --clear-output --inplace notebooks/*.ipynb`
2. Commit code changes
3. Update README with experiment summary
4. Push data to DVC remote if needed: `dvc push`
5. Create PR or share findings

---

**Note**: This is an experiment repository. Focus on learning and exploration. Production code belongs in application repositories.
