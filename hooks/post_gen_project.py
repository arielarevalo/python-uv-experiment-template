#!/usr/bin/env python3
"""Post-generation hook for python-uv-experiment-template."""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], error_msg: str) -> None:
    """Run a command and handle errors."""
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✓ {' '.join(cmd)}")
    except subprocess.CalledProcessError as e:
        print(f"✗ {error_msg}")
        print(f"  stdout: {e.stdout}")
        print(f"  stderr: {e.stderr}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"✗ {error_msg} - command not found: {cmd[0]}")
        sys.exit(1)


def main() -> None:
    """Run post-generation setup."""
    print("Setting up experiment repository...")

    # Initialize git
    run_command(["git", "init"], "Failed to initialize git")

    # Initialize DVC
    print("\nInitializing DVC...")
    run_command(["dvc", "init"], "Failed to initialize DVC")

    # Install dependencies with uv
    print("\nInstalling dependencies...")
    run_command(["uv", "sync"], "Failed to install dependencies")

    # Stage initial files
    print("\nStaging initial files...")
    run_command(["git", "add", "."], "Failed to stage files")

    print("\n✓ Experiment repository created successfully!")
    print("\nNext steps:")
    print("  1. Configure DVC remote: dvc remote add -d myremote <url>")
    print("  2. Add your data: dvc add data/your_dataset.csv")
    print("  3. Start Jupyter: uv run jupyter notebook")
    print("  4. Review AGENTS.md for project conventions")


if __name__ == "__main__":
    main()
