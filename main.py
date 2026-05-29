# codebasics ML course: codebasics.io, all rights reserved

import streamlit as st
from prediction_helper import predict

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Health Insurance Cost Predictor",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    color: #1f77b4;
    margin-bottom: 1px;
}

.sub-title {
    text-align: center;
    color: #666;
    margin-bottom: 1px;
    font-size: 16px;
}

.card {
    background-color: #ffffff;
    # padding: 20px;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    margin-bottom: 0px;
}

.section-header {
    font-size: 18px;
    font-weight: 600;
    color: #1f77b4;
    margin-bottom: 5px;
    border-left: 5px solid #1f77b4;
    padding-left: 10px;
}

.stButton>button {
    background-color: #1f77b4;
    color: white;
    font-size: 18px;
    padding: 12px;
    border-radius: 10px;
    border: none;
}

.stButton>button:hover {
    background-color: #155a8a;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<div class='main-title'>🏥 Health Insurance Cost Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Enter your details to estimate insurance cost using Machine Learning</div>", unsafe_allow_html=True)

# ---------------- OPTIONS ----------------
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease',
        'Diabetes & Thyroid', 'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# ---------------- PERSONAL INFO ----------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>👤 Personal Information</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', 18, 100, step=1)
    with col2:
        number_of_dependants = st.number_input('Dependants', 0, 20, step=1)
    with col3:
        income_lakhs = st.number_input('Income (Lakhs)', 0, 200, step=1)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FINANCIAL ----------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>💰 Financial Information</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        genetical_risk = st.number_input('Genetical Risk', 0, 5, step=1)
    with col2:
        insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
    with col3:
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PERSONAL DETAILS ----------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>👥 Personal Details</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox('Gender', categorical_options['Gender'])
    with col2:
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
    with col3:
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- HEALTH INFO ----------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>❤️ Health Information</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
    with col2:
        region = st.selectbox('Region', categorical_options['Region'])
    with col3:
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- INPUT DICT ----------------
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# ---------------- PREDICTION ----------------
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    predict_button = st.button("🔮 Predict Insurance Cost", use_container_width=True)

if predict_button:
    prediction = predict(input_dict)

    st.markdown("### 📊 Prediction Result")
    st.success(f"💰 Estimated Insurance Cost: {prediction}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray; font-size:12px;'>"
    "Health Insurance Cost Predictor | Built with Streamlit + Machine Learning"
    "</p>",
    unsafe_allow_html=True
)