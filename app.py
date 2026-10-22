
import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import requests
from streamlit_lottie import st_lottie
import time


# -------------------------------------------------------
# LOAD LOTTIE FROM URL
# -------------------------------------------------------
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# -------------------------------------------------------
# PAGE SETTINGS
# -------------------------------------------------------
st.set_page_config(
    page_title=" Salary Predictor",
    layout="wide",
)

# -------------------------------------------------------
# BACKGROUND IMAGE + GRADIENT OVERLAY
# -------------------------------------------------------
background_image = "bg.jpg"  # local image file

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("{background_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        animation: fadein 1.5s ease-in-out;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            rgba(0,0,0,0.55),
            rgba(0,0,0,0.65)
        );
        z-index: -1;
    }}

    @keyframes fadein {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}

    /* Glassmorphism Panels */
    .glass {{
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 18px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}

    .big-title {{
        font-size: 46px;
        font-weight: 900;
        color: #ffffff;
        text-shadow: 3px 3px 10px black;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------------
# LOAD MODEL
# -------------------------------------------------------
@st.cache_resource
def load_model():
    with open("model (3).pkl", "rb") as f:
        return pickle.load(f)

model = load_model()


# -------------------------------------------------------
# LOAD ENCODERS FROM CSV
# -------------------------------------------------------
@st.cache_resource
def load_encoders():
    df = pd.read_csv("salaries.csv")
    enc = {}
    for col in df.columns:
        if df[col].dtype == "object":
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            enc[col] = le
    return enc

encoders = load_encoders()


# -------------------------------------------------------
# LOTTIE FILES
# -------------------------------------------------------
hero_animation = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_kyu7xb1v.json")
side_animation = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_tll0j4bb.json")
loading_animation = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_usmfx6bp.json")

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------
st.markdown("<h1 class='big-title'>⚡ Salary Predictor</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1])

with col1:
    if hero_animation:
        st_lottie(hero_animation, height=280)

with col2:
    st.markdown("### 🚀 Enter job details and watch your salary prediction come alive!")
    st.markdown("### 💡 Sleek animations  Glassmorphism UI")


# -------------------------------------------------------
# INPUT FORM WITH GLASS EFFECT
# -------------------------------------------------------
st.markdown("<div class='glass'>", unsafe_allow_html=True)

left, right = st.columns(2)

with left:
    work_year = st.number_input("Work Year", 1900, 2100, 2023)
    experience_level = st.selectbox("Experience Level", ["EN", "MI", "SE", "EX"])
    employment_type = st.selectbox("Employment Type", ["FT", "PT", "CT", "FL"])
    job_title = st.text_input("Job Title", "Data Scientist")

with right:
    salary = st.number_input("Salary", 0, 500000, 10000)
    salary_currency = st.text_input("Salary Currency", "USD")
    employee_residence = st.text_input("Employee Residence", "US")
    remote_ratio = st.slider("Remote Ratio", 0, 100, 0)
    company_location = st.text_input("Company Location", "US")
    company_size = st.selectbox("Company Size", ["S", "M", "L"])

st.markdown("</div>", unsafe_allow_html=True)


# -------------------------------------------------------
# ANIMATED SHINY BUTTON
# -------------------------------------------------------
st.markdown(
    """
    <style>
    .shine-btn {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        padding: 14px 24px;
        border-radius: 14px;
        color: white;
        font-size: 22px;
        font-weight: bold;
        border: none;
        width: 100%;
        text-align: center;
        cursor: pointer;
        transition: 0.3s;
        box-shadow: 0px 0px 14px rgba(0, 255, 255, 0.65);
        position: relative;
        overflow: hidden;
    }

    .shine-btn:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 24px rgba(0, 255, 255, 1);
    }

    .shine-btn:before {
        content: "";
        position: absolute;
        top: 0;
        left: -120%;
        width: 50%;
        height: 100%;
        background: rgba(255,255,255,0.5);
        transform: skewX(-25deg);
        transition: 0.6s;
    }

    .shine-btn:hover:before {
        left: 200%;
    }
    </style>
    """,
    unsafe_allow_html=True
)


btn = st.button("✨ Predict Salary", key="predict")


# -------------------------------------------------------
# PREDICTION + LOADING ANIMATION
# -------------------------------------------------------
if btn:
    with st.spinner("AI analyzing your inputs…"):

        if loading_animation:
            st_lottie(loading_animation, height=180)
        time.sleep(2)

        row = {
            "work_year": work_year,
            "experience_level": experience_level,
            "employment_type": employment_type,
            "job_title": job_title,
            "salary": salary,
            "salary_currency": salary_currency,
            "employee_residence": employee_residence,
            "remote_ratio": remote_ratio,
            "company_location": company_location,
            "company_size": company_size
        }

        # Encode text to numbers
        for col, encoder in encoders.items():
            if col in row:
                row[col] = encoder.transform([row[col]])[0]

        df_input = pd.DataFrame([row])
        pred = model.predict(df_input)[0]

    st.success(f"💰 **Predicted Salary: {pred:,.2f} USD**")
    st.balloons()

    if side_animation:
        st_lottie(side_animation, height=180)
