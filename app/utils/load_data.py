import streamlit as st
import pandas as pd
from pathlib import Path

@st.cache_data
def load_dataset(path: str):
    df = pd.read_html(path, encoding='utf-8')
    return df[0]


@st.cache_data
def test_csv(path):
    return pd.read_csv(path)