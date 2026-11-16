# HFpEF Transcriptomics Repositories

**Version:** 1.0.0

A metadata catalog and interactive framework for organizing, standardizing, and exploring transcriptomic datasets, demonstrated through its application to heart failure with preserved ejection fraction (HFpEF).

## Overview

The HFpEF Transcriptomics Repositories project provides a structured approach to cataloging and exploring transcriptomic datasets through standardized metadata and interactive visualizations.

The project combines a curated metadata catalog with a Quarto-based interactive dashboard, enabling the exploration of biological, experimental, and technical characteristics across datasets.

Although the current implementation focuses on HFpEF-related research, its metadata organization and data exploration workflow may serve as a foundation for similar transcriptomic data cataloging initiatives in other research contexts.

## Features

- **Repository overview:** summary metrics showing the number of cataloged species and total datasets.
- **Species profiles:** summaries of dataset characteristics for each cataloged species.
- **Interactive dashboard:** visualizations of omics approaches, sampled tissues, recorded biological sex, sequencing platforms, and molecular biotypes.
- **Dynamic filters:** explore datasets by species, sampled tissue, sex, omics approach, platform, and raw or processed data availability.
- **Curated metadata table:** inspect detailed dataset records according to the selected filters.

## Metadata

The catalog uses a standardized metadata framework to describe the biological, experimental, and technical characteristics of each transcriptomic dataset.

The metadata dictionary defines the attributes and their corresponding descriptions, supporting consistent data organization and facilitating comparisons across studies.

The catalog includes information on:

- Species and study description
- Sampled tissue and strain or ethnicity
- Recorded biological sex and sample age
- Number of biological individuals and biosamples
- Experimental conditions
- Omics approach, sequencing platform, and sequencing layout
- Raw and processed data availability
- Molecular biotype and publication information
- Dataset access links and methodological notes

Explicitly recorded values, such as `Not reported`, are preserved as meaningful metadata categories. Blank fields are treated separately, maintaining the distinction between information explicitly reported as unavailable and information not provided in the catalog.

## Project Structure

```text
bioinfo-hfpef-transcriptomics-catalog/
├── assets/
│   └── hfpef_hero.png
├── src/
│   └── hfpef_catalog/
│       ├── __init__.py
│       ├── config.py
│       ├── data_loader.py
│       ├── processing.py
│       └── visualization.py
├── styles/
│   └── custom.scss
├── .gitignore
├── environment.yml
├── pyproject.toml
├── report_hfpef.qmd
└── README.md
```

- `report_hfpef.qmd`: main Quarto report and interactive dashboard.
- `assets/`: contains visual assets used in the report.
- `src/hfpef_catalog/config.py`: defines configuration parameters for accessing the source spreadshee.
- - `src/hfpef_catalog/data_loader.py`: loads and consolidates species-specific datasets.
- `src/hfpef_catalog/processing.py`: provides functions for metadata normalization, summarization, and filtering.
- `src/hfpef_catalog/visualization.py`: contains reusable functions for generating Plotly visualizations.
- `custom.scss`: defines the visual styles of the report and dashboard.
- `environment.yml`: specifies the Conda environment and project dependencies.
- `pyproject.toml`: defines the Python package configuration and dependencies.


## Requirements

- Git
- Conda (Miniconda or Anaconda)
- Quarto
- Python 3.11 or later
- Quarto support for interactive Shiny documents

## Installation

Clone the repository:

```bash
git clone https://github.com/Ludimila-Araujo/bioinfo-hfpef-transcriptomics-catalog.git
cd bioinfo-hfpef-transcriptomics-catalog
```

Create and activate the Conda environment:

```bash
conda env create -f environment.yml
conda activate quarto-env
```

Install the project in editable mode:

```bash
pip install -e .
```

Make sure Quarto is installed and available in your system path before running the report.


## Run the Report

From the project root directory, render the Quarto report:

```bash
quarto render report_hfpef.qmd
```

To launch the report locally with interactive dashboard functionality, use:

```bash
quarto preview report_hfpef.qmd
```

The interactive dashboard runs through Quarto's Shiny integration. Make sure the required dependencies are installed and the Conda environment is activated before running the report.

## Data Source

The catalog is populated from species-specific tabs in a Google Sheets spreadsheet configured in the project.

The spreadsheet contains the curated dataset metadata and the definitions used by the metadata catalog. The report retrieves the data directly from the configured source.

Dataset availability and metadata may change as the source spreadsheet is updated. Access to the spreadsheet must be maintained for the report to load successfully.

## Version

**Current version: v1.0.0**

This version includes the curated metadata catalog, species profiles, interactive dashboard, filtering functionality, and detailed dataset table.

## Authors

**Ludimila Araújo**  
BioME / UFRN

**Caio César**  
BioME / UFRN
