#!/usr/bin/env python3
"""Example experiment script.

This script demonstrates how to structure a reproducible experiment.
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from {{ cookiecutter.package_name }}.utils import hello_experiment


def run_experiment(*, output_dir: Path, param1: float) -> None:
    """Run the example experiment.

    Args:
        output_dir: Directory to save results.
        param1: Example parameter for the experiment.
    """
    print(hello_experiment())
    print(f"Running experiment with param1={param1}")

    # Example: Generate some data
    x = np.linspace(0, 10, 100)
    y = param1 * np.sin(x)

    # Example: Create a plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title(f"Example Plot (param1={param1})")
    plt.xlabel("x")
    plt.ylabel("y")

    # Save results
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"experiment_param1_{param1}.png"
    plt.savefig(output_path)
    print(f"Saved plot to {output_path}")


def main() -> None:
    """Parse arguments and run experiment."""
    parser = argparse.ArgumentParser(description="Run example experiment")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs"),
        help="Directory to save results",
    )
    parser.add_argument(
        "--param1",
        type=float,
        default=1.0,
        help="Example parameter",
    )

    args = parser.parse_args()
    run_experiment(output_dir=args.output_dir, param1=args.param1)


if __name__ == "__main__":
    main()
