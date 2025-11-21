import streamlit as st

from utils.filtering import filter_by_budget
from utils.data_cleaning import clean_data
from utils.scoring import apply_role_score
from utils.load_weights import get_desired_role_key, get_roles, load_weights
from utils.load_data import load_dataset

st.set_page_config(
    page_title="FM24 Moneyball",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ FM24 Moneyball Analysis")
st.markdown("Find undervalued players using data-driven scouting.")

st.sidebar.title("Setup")
st.sidebar.info("To start:\n- Upload a csv file\n- Select a role to score")

file = st.sidebar.file_uploader("Upload CSV", type=['csv'])
weights = load_weights()
roles = get_roles(weights)

role = st.sidebar.selectbox("Select role:", roles)
max_value = st.sidebar.slider("Max Transfer Value (M)", min_value=0, max_value=500, value=50)

if file:
    df = load_dataset(file)
    df_cleaned = clean_data(df)
    key = get_desired_role_key(role,weights)

    df_role = df_cleaned[df_cleaned['best_pos'] == role]

    # apply score
    df_role = apply_role_score(df_role, key, weights)

    df_role = filter_by_budget(df_role,max_value)

    st.dataframe(
        df_role.sort_values("score", ascending=False)
                [["name", "score", "age", "nation", "height", "weight", "style", "club", "division", "transfer_value", "wages", "expires"]]
                .reset_index(drop=True).style.format({"score":"{:.2f}","age":"{:.0f}","height":"{:.0f}","weight":"{:.0f}"})
    )
else:
    st.markdown("<h2 style='text-align: center;'>No Data</h2>", unsafe_allow_html=True)
