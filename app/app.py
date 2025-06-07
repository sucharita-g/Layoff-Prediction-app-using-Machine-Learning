import streamlit as st
import joblib
import pandas as pd
import numpy as np


# Load saved model
model = joblib.load(r"C:\Users\pawan\OneDrive\Documents\Layoff-predictor_app\models\random_forest_model.pkl")

# Mapping dictionaries (from notebook)
industry_map = {
    0: 'AI', 1: 'Aerospace', 2: 'Construction', 3: 'Consumer', 4: 'Crypto', 5: 'Data', 6: 'Education',
    7: 'Energy', 8: 'Finance', 9: 'Fitness', 10: 'Food', 11: 'HR', 12: 'Hardware', 13: 'Healthcare',
    14: 'Infrastructure', 15: 'Legal', 16: 'Logistics', 17: 'Manufacturing', 18: 'Marketing', 19: 'Media',
    20: 'Other', 21: 'Product', 22: 'Real Estate', 23: 'Recruiting', 24: 'Retail', 25: 'Sales',
    26: 'Security', 27: 'Support', 28: 'Transportation', 29: 'Travel', 30: None
}

country_map = {
    0: 'Argentina', 1: 'Australia', 2: 'Austria', 3: 'Bahrain', 4: 'Belgium', 5: 'Brazil', 6: 'Bulgaria',
    7: 'Canada', 8: 'Cayman Islands', 9: 'Chile', 10: 'China', 11: 'Colombia', 12: 'Cyprus',
    13: 'Czech Republic', 14: 'Denmark', 15: 'Egypt', 16: 'Estonia', 17: 'Finland', 18: 'France',
    19: 'Germany', 20: 'Ghana', 21: 'Greece', 22: 'Hong Kong', 23: 'Hungary', 24: 'India', 25: 'Indonesia',
    26: 'Ireland', 27: 'Israel', 28: 'Italy', 29: 'Japan', 30: 'Kenya', 31: 'Lithuania', 32: 'Luxembourg',
    33: 'Malaysia', 34: 'Malta', 35: 'Mexico', 36: 'Myanmar', 37: 'Netherlands', 38: 'New Zealand',
    39: 'Nigeria', 40: 'Norway', 41: 'Pakistan', 42: 'Peru', 43: 'Philippines', 44: 'Poland',
    45: 'Portugal', 46: 'Romania', 47: 'Russia', 48: 'Saudi Arabia', 49: 'Senegal', 50: 'Seychelles',
    51: 'Singapore', 52: 'South Africa', 53: 'South Korea', 54: 'Spain', 55: 'Sweden', 56: 'Switzerland',
    57: 'Thailand', 58: 'Turkey', 59: 'UAE', 60: 'Ukraine', 61: 'United Arab Emirates', 62: 'United Kingdom',
    63: 'United States', 64: 'Uruguay', 65: 'Vietnam'
}

stage_map = {
    0: 'Acquired', 1: 'Post-IPO', 2: 'Private Equity', 3: 'Seed', 4: 'Series A', 5: 'Series B',
    6: 'Series C', 7: 'Series D', 8: 'Series E', 9: 'Series F', 10: 'Series G', 11: 'Series H',
    12: 'Series I', 13: 'Series J', 14: 'Subsidiary', 15: 'Unknown', 16: None
}

# Reverse maps for label → number (to convert selected string back to encoded number)
industry_rev_map = {v: k for k, v in industry_map.items() if v is not None}
country_rev_map = {v: k for k, v in country_map.items()}
stage_rev_map = {v: k for k, v in stage_map.items() if v is not None}


# Title and description
st.markdown("<h2 style='text-align: left; color: white;'>Layoff Prediction App</h2>", unsafe_allow_html=True)
st.write("Enter company features to predict if a layoff is likely.")


industry_label = st.selectbox("Industry", list(industry_map.values()))
industry = list(industry_map.keys())[list(industry_map.values()).index(industry_label)]


country_label = st.selectbox("Country", list(country_map.values()))
country = list(country_map.keys())[list(country_map.values()).index(country_label)]

stage_label = st.selectbox("Stage", list(stage_map.values()))
stage = list(stage_map.keys())[list(stage_map.values()).index(stage_label)]


raised = st.number_input("$ Raised (in millions)", min_value=0.0, value=150.0)
year = st.number_input("Year", min_value=2015, max_value=2030, value=2023)

if st.button("Predict Layoff"):
    input_data = np.array([[industry, country, raised, stage, year]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk: Layoff is likely.")
    else:
        st.success("✅ Good News: Layoff is not likely.")