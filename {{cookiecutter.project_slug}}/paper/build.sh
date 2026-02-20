#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "==> Building paper..."
cd "${SCRIPT_DIR}"

pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1
bibtex main > /dev/null 2>&1
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1

# Clean auxiliary files
rm -f main.aux main.bbl main.blg main.log main.out main.toc main.synctex.gz

echo "==> Done. PDF is at ${SCRIPT_DIR}/main.pdf"
