import streamlit as st
import json

@st.cache_data
def load_weights():
    with open("data/weights.json") as f:
        return json.load(f)

def get_roles(data):
    roles = []
    for _, val in data.items():
        roles.extend(val['Positions'])
    return roles

def get_desired_role_key(role, weights):
    for key, val in weights.items():
        if role in val['Positions']:
            return key

