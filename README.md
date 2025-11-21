# Football Manager Moneyball: Data-Driven Player Evaluation

<p align="center">
  <img src="assets/banner.png" alt="Football Manager Moneyball Banner" width="80%">
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white"></a>
  <a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/pandas-data%20analysis-orange.svg?logo=pandas"></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-Interactive%20App-red.svg?logo=streamlit"></a>
  <a href="https://scipy.org/"><img src="https://img.shields.io/badge/Scipy-Stats-lightgrey.svg?logo=scipy"></a>
  <a href="https://matplotlib.org/"><img src="https://img.shields.io/badge/Matplotlib-Visualization-yellow.svg?logo=plotly"></a>
  <a href="https://github.com/Phantom-L0rd/fm24-moneyball"><img src="https://img.shields.io/badge/Status-In%20Progress-brightgreen"></a>
</p>

##  Overview
This project applies a **Moneyball-style analytical approach** to Football Manager 2025 data — using statistics and player attributes to identify undervalued players across leagues.  
The goal is to determine which **attribute weight model** best predicts player performance and use it to recommend top players for each position.

## Objectives
- Collect and clean player data from Football Manager 2025.
- Design weighted models for attributes by position (e.g., striker, midfielder, defender).
- Evaluate which weight configuration best correlates with player performance.
- Build an interactive **Streamlit app** to find the best players per position using the optimal model.

## Dataset
- **Source:** Exported player attributes and season performance data from Football Manager 2025.  
- **Leagues Included:** *(e.g., Premier League, La Liga, Serie A)*  
- **Size:** ~X,XXX players across multiple positions and roles.  
- **Key Features:**
  - Player attributes (technical, mental, physical)
  - Performance metrics (average rating, goals, assists, xG, etc.)
  - Positional categories


## Methodology

### 1. Data Collection
- Extracted player data from Football Manager using in-game editor exports or third-party tools.
- Merged multiple league datasets for variety and robustness.

### 2. Data Cleaning
- Handled missing or inconsistent attributes.
- Standardized scales and normalized metrics.
- Categorized players by **primary position** and **role**.

### 3. Weighted Model Design
- Developed custom weighting schemes for each position based on role importance.
- Used domain knowledge + football analytics literature to determine initial weights.
- Example:
  - Strikers: 40% finishing, 30% composure, 15% off the ball, 15% pace.

### 4. Correlation & Evaluation
- Tested models using **Spearman’s rank correlation (ρ)** to measure association between:
  - Weighted attribute score ↔ average performance rating.
- Selected the model with the **highest positive correlation** as the best predictor.

### 5. Streamlit App
Built an interactive app where users can:
- Select a league and position.
- View top players based on the chosen weight model.
- Compare results across multiple weight configurations.

Run locally:
```bash
cd app
pip install -r requirements.txt
streamlit run app.py
```

## Tools & Technologies

| Category        | Tools Used                    |
| --------------- | ----------------------------- |
| Programming     | Python (pandas, numpy, scipy) |
| Visualization   | matplotlib, seaborn           |
| App Development | Streamlit                     |
| Data Management | CSV, pandas                   |
| Version Control | Git + GitHub                  |


## Results

* **Best-performing model:** Model X (Spearman ρ = [your result])
* Example Output:

  * 🥇 Top 5 Strikers: [Player A, Player B, Player C...]
  * 🧠 Insights: Technical attributes had stronger correlation with performance than physical ones for midfielders.

## Key Insights

* Data-driven weighting models can reveal undervalued players.
* Certain attributes (e.g., decision-making, composure) consistently correlate with high performance.
* Approach can generalize across leagues and seasons with tuning.


## Repository Structure

```
fm_moneyball/
├── README.md
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_weight_model_analysis.ipynb
│   ├── 03_model_evaluation.ipynb
│   └── 04_visualization.ipynb
├── app/
│   ├── app.py
│   ├── utils.py
│   └── requirements.txt
├── src/
│   ├── data_prep.py
│   ├── weights.py
│   ├── evaluation.py
│   └── visualization.py
└── tests/
    └── test_weights.py
```


## Future Work

* Include multiple FM seasons to track player development.
* Train ML models for predictive scouting.
* Integrate real-world player market values for investment analysis.
* Deploy Streamlit app online (e.g., Streamlit Cloud).


## Acknowledgments

Inspired by the *Moneyball* concept and Football Manager’s rich dataset.
Special thanks to football analytics communities and open-source tools enabling this project.


## Author

**Arop Kuol**
Data Science & Analytics Enthusiast
📍 Based in South Africa | 🌍 Open to remote roles
🔗 [LinkedIn](https://linkedin.com/in/your-profile) | [GitHub](https://github.com/your-username)
