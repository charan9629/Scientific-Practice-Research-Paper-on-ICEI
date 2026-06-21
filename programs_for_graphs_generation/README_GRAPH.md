# Graph Generation Guide

## Overview

This directory contains the Python scripts used to generate the visualizations presented in the research paper:

**"IoT Conference Excellence Index (ICEI): A Multi-Dimensional Framework for Evaluating IoT Conferences"**

The figures provide graphical insights into conference quality, citation performance, and comparative rankings across major IoT conferences published during 2023 and 2024.

---

## Figure 1: ICEI Grouped Bar Chart

### Script

`main_ICEI_bar_chart.py`

### Purpose

This figure compares the calculated IoT Conference Excellence Index (ICEI) scores for all evaluated conferences across the 2023 and 2024 conference editions.

### Metric

ICEI is calculated as:

ICEI = 0.50(Citation Impact)
+ 0.15(Diversity)
+ 0.15(Reference Quality)
+ 0.10(Collaboration)
+ 0.10(Visual Communication)

### Visualization Type

Grouped Bar Chart

### Output

`Figure1_ICEI_Grouped_BarChart.png`

### Interpretation

* Higher ICEI values indicate stronger overall conference quality.
* Allows direct comparison between conference editions.
* Supports conference ranking and hypothesis validation.

---

## Figure 2: Citation Distribution Box Plot

### Script

`main_citations_box_plot.py`

### Purpose

This figure visualizes paper-level citation distributions for selected major IoT conferences.

### Selected Conferences

* BIOTC
* DCOSS-IoT
* EWSN
* SenSys
* WF-IoT

### Visualization Type

Box Plot

### Output

`Figure2_Selected_Conference_Boxplot.png`

### Interpretation

Each box plot represents:

* Median citation count
* Interquartile range (IQR)
* Citation variability
* Outlier papers

The figure enables comparison of citation performance between conference editions and highlights highly cited publications.

---

## Input Dataset

### Excel File

`Organised_Data_Sets.xlsx`

### Sheets Used

#### Figure 1

Sheet:
`statistical_evaluation`

Contains:

* Citation Impact Score
* Diversity Score
* Reference Quality Score
* Collaboration Score
* Visual Communication Score

#### Figure 2

Sheet:
`total_consolidated_data`

Contains paper-level information including:

* Conference Name
* Conference Year
* Google Scholar Citation Count

---

## Software Requirements

Python 3.x

Required Packages:

```bash
pip install pandas numpy matplotlib openpyxl
```

---

## Generated Files

| Figure       | Output File                             | Description                        |
| ------------ | --------------------------------------- | ---------------------------------- |
| Figure 1     | Figure1_ICEI_Grouped_BarChart.png       | ICEI comparison across conferences |
| Figure 2     | Figure2_Selected_Conference_Boxplot.png | Citation distribution analysis     |
| Table Output | ICEI_Calculated.xlsx                    | Computed ICEI scores               |

---

## Reproducibility

All figures are generated directly from the supplied dataset using Python scripts. The workflow ensures reproducible conference evaluation and visualization results.

