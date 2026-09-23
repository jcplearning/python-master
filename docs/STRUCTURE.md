# Repository structure

This repository is organized as a progressive learning path rather than as an installable Python package. The numbered chapter directories are intentionally kept at the top level so learners can move through the material in order.

## Directory responsibilities

| Directory | Purpose |
| --- | --- |
| `Chapter_01_PrintMessages` through `Chapter_25_dask` | Standalone lesson examples, ordered from fundamentals to data processing |
| `inbound` | Small input fixtures consumed by scripts |
| `outbound` | Files produced by scripts during demonstrations |
| `Logs` | Runtime logs and example reports |
| `docs` | Repository-level documentation |

## Adding a new lesson

1. Put the example in the chapter that teaches the relevant concept.
2. Preserve the existing numeric prefix when extending an established chapter.
3. Use lowercase `snake_case` for new filenames.
4. Keep sample input and generated output out of chapter directories.
5. Update the root README when adding a new chapter or a new shared data directory.

## Data and generated files

Examples should use paths relative to the repository root when practical. Do not add caches, virtual environments, editor settings, or ad-hoc logs to version control; the root `.gitignore` covers these files.
