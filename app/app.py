import streamlit as st

from utils.filtering import filter_by_budget
from utils.data_cleaning import clean_data, attributes
from utils.scoring import apply_role_score
from utils.load_weights import get_desired_role_key, get_roles, load_weights
from utils.load_data import load_dataset, test_csv

st.set_page_config(
    page_title="FM24 Moneyball",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ FM24 Moneyball Analysis")
st.markdown("Find undervalued players using data-driven scouting.")

st.sidebar.title("Setup")
with st.sidebar.expander("❓ Show Getting Started Guide", expanded=True):
        st.markdown(
            """
            ### 🏁 To Get Started
            
            Please follow these steps in order to process your data:
            
            1.  **Download** the necessary FM Table View file using the button on the main page.
            2.  **Import** the downloaded view file into your Football Manager save game.
            3.  **Apply** the new view to the relevant squad/player table in FM.
            4.  **Export** the table view as a **`.html` file** by right-clicking the table and selecting **'Export Table...'** (or similar option).
            5.  **Upload** the exported `.html` file using the upload widget below.
            6.  **Select a role** from the options to generate the scoring results and analysis.
            7.  **Select the max transfer value** to filter 
            """
        )

FM_VIEW = "fm_moneyball_player_search_view.fmf"
FM_VIEW_PATH = f"data/{FM_VIEW}"
FMF_MIME_TYPE = "application/octet-stream"

file_bytes = None
try:
    with open(FM_VIEW_PATH, "rb") as file:
        file_bytes = file.read()
except FileNotFoundError:
    st.error(f"Error: The required file '{FM_VIEW}' was not found at the expected path.")
    st.info("Please ensure 'custom_data.fmf' is in the same directory as your Streamlit app script.")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred while reading the file: {e}")
    st.stop()

st.sidebar.download_button(
    label="Download FM table view",
    data=file_bytes,
    file_name=FM_VIEW,
    mime=FMF_MIME_TYPE
)

file = st.sidebar.file_uploader("Upload html file", type=['html'])
weights = load_weights()
roles = get_roles(weights)

role = st.sidebar.selectbox("Select role:", roles)
max_value = st.sidebar.slider("Max Transfer Value (M)", min_value=0, max_value=500, value=500)

if file:
    df = load_dataset(file)
    # df = test_csv(file)
    df_cleaned = clean_data(df)
    key = get_desired_role_key(role,weights)
    # st.dataframe(df_cleaned)

    # df_role = df_cleaned[df_cleaned['best_pos'] == role]

    # apply score
    df_role = apply_role_score(df_cleaned, key, weights)

    df_role = filter_by_budget(df_role,max_value)

    st.dataframe(
        df_role.sort_values(f"{key.lower()}_score", ascending=False)
                [["name", f"{key.lower()}_score", 'position', 'best_pos', "age", "nation", "height", "weight", "style", "club", "division", "transfer_value", "wages", "expires"] + attributes]
                .reset_index(drop=True).style.format({f"{key.lower()}_score":"{:.2f}","age":"{:.0f}","height":"{:.0f}","weight":"{:.0f}"})
    )
else:
    st.markdown("")
