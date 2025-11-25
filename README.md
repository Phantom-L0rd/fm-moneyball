# Football Manager Moneyball: Data-Driven Player Evaluation

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white"></a>
  <a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/pandas-data%20analysis-orange.svg?logo=pandas"></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-Interactive%20App-red.svg?logo=streamlit"></a>
  <a href="https://matplotlib.org/"><img src="https://img.shields.io/badge/Matplotlib-Visualization-yellow.svg?logo=plotly"></a>
  <a href="https://github.com/Phantom-L0rd/fm24-moneyball"><img src="https://img.shields.io/badge/Status-In%20Progress-brightgreen"></a>
</p>

##  Overview
This project applies a **Moneyball-style analytical approach** to Football Manager 2025 data — using player attributes and performance metrics to identify undervalued players across Europe's top leagues.  
The primary goal is to build a system that **ranks and discovers undervalued players** using weighted attribute models.


## Objectives
- Collect and clean player data exported from Football Manager 2025.
- Design weighted scoring models for each position (e.g., striker, midfielder, defender).
- Evaluate how well expert-weighted models perform.
- Build an interactive **Streamlit app** that allows users to upload FM data and retrieve position-based player rankings.


## Dataset
The dataset consists of exported Football Manager 2025 player attributes from the top five leagues (Premier League, Serie A, LaLiga, Bundesliga, Ligue 1), totaling **2,377 players**.  
It contains **159 columns**, including player details, club information, attributes, and performance statistics.


## Methodology

### 1. Data Collection
- Extracted FM player data through in-game table view exports.
- Merged multiple league datasets for variety and robustness.

### 2. Data Cleaning
- Filtered players with **at least 600 minutes played**.
- Removed non-numeric symbols from columns (e.g., `'cm'`, `'£'`, `'km'`).
- Converted left/right foot proficiency to integer values and created a combined `feet` metric.
- Parsed the `transfer_value` field into `min_value` and `max_value`.
- For attribute ranges such as `"12–15"`, used the midpoint.
- Imputed missing attribute values using the **mean value for players in the same position**.
- Converted all attribute and performance fields to numerical format.

### 3. Weighted Model Design
After extensive research into football attribute weighting, the project uses the popular and community-trusted **ykykyk attribute weight system**.  
These weights were compiled into a JSON file and mapped to each position to generate a reproducible score for every player.

Reference:  
[ykykyk Attribute Weights](https://fm-arena.com/thread/2182-important-attributes-for-blue-dm/)



### 5. Streamlit App
The interactive Streamlit app allows users to:

- Download a predefined FM table view for exporting data.
- Upload their FM-exported dataset.
- Select a position.
- View the highest-scoring players based on the weighted model.


Run locally:
```bash
# It is recommended to create and activate a virtual environment first.
pip install -r requirements.txt
cd app
streamlit run app.py
```

## Tools used
Python - pandas, numpy, matplotlib, streamlit, json, re

## Repository Structure

```
fm_moneyball/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   └── 02_weight_model_analysis.ipynb
├── app/
│   ├── app.py
│   └── utils/
│       ├── data_cleaning.py
│       ├── filtering.py
│       ├── load_data.py
│       ├── load_weights.py
│       └── scoring.py
├── README.md
└── requirements.txt
```


## Future Work

* Evaluate the scoring model and tune weights for improved accuracy.
* Add support for multiple FM seasons to track player development.
* Train ML models for predictive scouting.
* Add FM26 support once exporting becomes available.
* Deploy the app online (e.g., Streamlit Cloud).


## Acknowledgments

Inspired by the *Moneyball* concept and Football Manager’s rich dataset.
Special thanks to football analytics communities and open-source tools enabling this project.


## Author

**Arop Kuol** \
aropk03@gmail.com
