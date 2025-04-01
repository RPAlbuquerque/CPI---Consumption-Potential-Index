# CPI - Consumption Potential Index

This repository contains a reproducible pipeline for generating the Consumption Potential Index (CPI) at the census tract level. The CPI combines digital sentiment (e-WOM), mobility patterns, and time spent in locations and is intended to serve as a proxy for local economic activity.

---

## 📊 Overview

The CPI is computed as:

CPI = log(visits + 1) × log(dwell_time + 1) × sentiment_score


This index reflects three dimensions:
- **Mobility intensity** (number of visits)
- **Dwell time** (engagement)
- **Digital sentiment** (perception from social media)

---

## 📁 Project Structure
├── data/ │ ├── raw/ # Original input datasets (GeoJSONs, CSVs) │ └── processed/ # Processed outputs (CPI per sector, maps) ├── src/ │ ├── paths.py # Paths and constants used across the project │ ├── cpi_pipeline.py # Main CPI generation pipeline │ ├── map_generator.py # Map creation and exporting ├── notebooks/ # Jupyter Notebooks (optional exploration) └── README.md

---

## ⚙️ Requirements

- Python ≥ 3.8
- pandas
- numpy
- plotly
- seaborn
- scikit-learn

Install all dependencies with:
!pip install -r requirements.txt

🚀 Usage
1. Place your input files in data/raw/:
Mobility CSV
Sentiment CSV
Census GeoJSON (with census tract geometries)

2. Run the pipeline:
python src/cpi_pipeline.py

3. Generate an interactive map (optional):
python src/map_generator.py

4. Outputs will be saved in data/processed/:
Final CPI per sector (CSV)
GeoJSON with CPI values
Interactive HTML map


📌 Notes
This version is only available for one month (e.g., December 2020). Adjustments and parallelization strategies are required to scale for the full period (2010–2023).
This is a component of a broader research project on urban economic dynamics and digital behavior.



👨‍🔬 Author
Rafael Albuquerque
Visiting Fellow at the Center for Geographic Analysis – Harvard University
PhD Candidate in Marketing at Federal University of Rio Grande do Sul (UFRGS - Brazil)
