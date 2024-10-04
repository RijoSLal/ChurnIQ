import streamlit as st
import joblib
import pandas as pd

# Load your model using joblib
model = joblib.load('model.joblib')

# Configure page settings
st.set_page_config(page_title="ChurnIQ", layout="centered", initial_sidebar_state="collapsed")

# Title and instructions
st.title("ChurnIQ ﮩ٨ـﮩﮩ٨ـ")
st.write("Enter the customer details to predict whether they will stay or leave.")

# Centered form layout with container
with st.container():
    # Add CSS styling
    st.markdown(
        """
        <style>
        
        
        .centered-btn {
            text-align: center;
            margin:15px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Begin form layout
    with st.form("customer_form"):
        st.markdown('<div class="main-container">', unsafe_allow_html=True)

        # Collect user inputs for each feature
        gender = st.selectbox("Gender", ['Male', 'Female'])
        senior = st.slider("Age", 0, 110, 1)  # Age slider
        senior_citizen = 1 if senior > 50 else 0  # Convert age to binary
        partner = st.selectbox("Partner", ['Yes', 'No'])
        dependents = st.selectbox("Dependents", ['Yes', 'No'])
        tenure = st.slider("Tenure (Months)", 0, 72, 1)
        phone_service = st.selectbox("Phone Service", ['Yes', 'No'])
        multiple_lines = st.selectbox("Multiple Lines", ['Yes', 'No', 'No phone service'])
        internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
        online_security = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
        online_backup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
        device_protection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
        tech_support = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
        streaming_tv = st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
        streaming_movies = st.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service'])
        contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
        paperless_billing = st.selectbox("Paperless Billing", ['Yes', 'No'])
        payment_method = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
        monthly_charges = st.number_input("Monthly Charges", min_value=0.0, step=0.1)
        total_charges = st.number_input("Total Charges", min_value=monthly_charges, step=0.1)

        # Submit button in center
        submit_button = st.form_submit_button("Predict")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Placeholder for prediction message
    prediction_placeholder = st.empty()

    # Prediction handling
    if submit_button:

        # Prepare input data
        input_data = pd.DataFrame([[gender, senior_citizen, partner, dependents, tenure,
                                    phone_service, multiple_lines, internet_service, online_security,
                                    online_backup, device_protection, tech_support, streaming_tv,
                                    streaming_movies, contract, paperless_billing, payment_method,
                                    monthly_charges, total_charges]],
                                  columns=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
                                           'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
                                           'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
                                           'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
                                           'MonthlyCharges', 'TotalCharges'])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        # Display the prediction message within the container
        if prediction == 1:
            st.error("The customer is likely to **leave** 😔")
        else:
            st.success("The customer is likely to **stay** 😀")
        
        