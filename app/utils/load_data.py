import streamlit as st
import pandas as pd
from pathlib import Path

@st.cache_data
def load_dataset(path: str = "data/processed/players_2024_clean.csv"):
    return pd.read_csv(path)


