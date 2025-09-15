import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("churn_model.pkl")

st.title(" Customer Churn Prediction App")
st.write("""
This app predicts whether a customer is likely to **churn (leave the service)** 
based on their account information and service usage.
Fill in the details below and click **Predict** to see the result.
""")

# Sidebar inputs
st.sidebar.header(" Customer Information")

gender = st.sidebar.selectbox(
    "Gender", ["Male", "Female"],
    help="Customer’s gender as recorded in the system."
)

senior_citizen = st.sidebar.selectbox(
    "Senior Citizen", [0, 1],
    help="Indicates whether the customer is a senior citizen (1 = Yes, 0 = No)."
)

partner = st.sidebar.selectbox(
    "Partner", ["Yes", "No"],
    help="Does the customer have a spouse or partner?"
)

dependents = st.sidebar.selectbox(
    "Dependents", ["Yes", "No"],
    help="Does the customer live with dependents (e.g., children, relatives)?"
)

tenure = st.sidebar.number_input(
    "Tenure (months)", min_value=0, max_value=100, value=12,
    help="How many months the customer has stayed with the company."
)

phone_service = st.sidebar.selectbox(
    "Phone Service", ["Yes", "No"],
    help="Does the customer have a phone line service?"
)

multiple_lines = st.sidebar.selectbox(
    "Multiple Lines", ["Yes", "No", "No phone service"],
    help="Does the customer have multiple phone lines?"
)

internet_service = st.sidebar.selectbox(
    "Internet Service", ["DSL", "Fiber optic", "No"],
    help="The type of internet service the customer has."
)

online_security = st.sidebar.selectbox(
    "Online Security", ["Yes", "No", "No internet service"],
    help="Does the customer have online security add-on?"
)

online_backup = st.sidebar.selectbox(
    "Online Backup", ["Yes", "No", "No internet service"],
    help="Does the customer have cloud/online backup service?"
)

device_protection = st.sidebar.selectbox(
    "Device Protection", ["Yes", "No", "No internet service"],
    help="Does the customer have device protection (e.g., antivirus)?"
)

tech_support = st.sidebar.selectbox(
    "Tech Support", ["Yes", "No", "No internet service"],
    help="Does the customer have technical support service?"
)

streaming_tv = st.sidebar.selectbox(
    "Streaming TV", ["Yes", "No", "No internet service"],
    help="Does the customer stream TV channels through the service?"
)

streaming_movies = st.sidebar.selectbox(
    "Streaming Movies", ["Yes", "No", "No internet service"],
    help="Does the customer stream movies through the service?"
)

contract = st.sidebar.selectbox(
    "Contract", ["Month-to-month", "One year", "Two year"],
    help="The contract type chosen by the customer."
)

paperless_billing = st.sidebar.selectbox(
    "Paperless Billing", ["Yes", "No"],
    help="Does the customer receive bills online (paperless)?"
)

payment_method = st.sidebar.selectbox(
    "Payment Method", 
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"],
    help="The customer’s preferred payment method."
)

monthly_charges = st.sidebar.number_input(
    "Monthly Charges", min_value=0.0, value=70.0,
    help="The amount the customer pays monthly (in dollars)."
)

total_charges = st.sidebar.number_input(
    "Total Charges", min_value=0.0, value=500.0,
    help="The total amount charged to the customer (in dollars)."
)

# Collect inputs into a DataFrame
customer_data = pd.DataFrame({
    "gender": [gender],
    "SeniorCitizen": [senior_citizen],
    "Partner": [partner],
    "Dependents": [dependents],
    "tenure": [tenure],
    "PhoneService": [phone_service],
    "MultipleLines": [multiple_lines],
    "InternetService": [internet_service],
    "OnlineSecurity": [online_security],
    "OnlineBackup": [online_backup],
    "DeviceProtection": [device_protection],
    "TechSupport": [tech_support],
    "StreamingTV": [streaming_tv],
    "StreamingMovies": [streaming_movies],
    "Contract": [contract],
    "PaperlessBilling": [paperless_billing],
    "PaymentMethod": [payment_method],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges]
})

# Prediction
if st.button("🔮 Predict Churn"):
    prediction = model.predict(customer_data)[0]
    probability = model.predict_proba(customer_data)[0][1]

    st.subheader("Prediction Result")
    if prediction == "Yes":
        st.error(f" This customer is **likely to churn**. (Probability: {probability:.2f})")
    else:
        st.success(f" This customer is **not likely to churn**. (Probability: {probability:.2f})")
