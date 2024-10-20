#pip install streamlit
#pip install category_encoders
import streamlit as st
import pandas as pd
import category_encoders as ce
from sklearn.ensemble import RandomForestClassifier
import joblib

st.set_page_config(page_title="AI Account Predictor", layout='wide')

# Placeholder function to load your model and make predictions
def predict_payment_account(PO, TRS, Order):
    # Load the model from the file
    clf_loaded = joblib.load('rf_model.pkl')  # Update the path if necessary
    # Load the encoder from the file
    encoder_loaded = joblib.load('category_encoder.pkl')  # Update the path if necessary

    # Create the test DataFrame with user input
    test = pd.DataFrame({'PO#': [PO], 'TRS': [TRS], 'Order#': [Order]})

    # Transform the test data using the encoder
    test_encoded = encoder_loaded.transform(test)

    # Make the prediction
    prediction = clf_loaded.predict(test_encoded)

    # Return the prediction
    return prediction[0]

# Streamlit UI Layout
# Title of the app
st.title("Cost Centre Approval")

# Sidebar Project Information
st.sidebar.header("Project Information")
st.sidebar.write("""
**Business Case:** Automated Expense Categorization
**Objective:** Streamline expense categorization using machine learning for financial accuracy.
**Benefits:**
- Increases efficiency by reducing manual effort
- Minimizes human errors in expense tracking
- Provides scalability for growing transaction volumes
""")

# Main form for user input
st.header("Enter Transaction Details")
with st.form("account_form"):
    po = st.text_input("Enter Purchase Order", placeholder="Enter Purchase Order Number Pxxxxxxxxxx")
    trs = st.text_input("Enter Project Code", placeholder="Enter Project Code Cxxxxxxx")
    order = st.text_input("Internal Order#", placeholder="Enter Order Number Rxxxxxxxxxx")
    
    # Submit button
    submitted = st.form_submit_button("Request approval from this Cost Centre")

# When form is submitted
if submitted:
    # Call the model prediction function
    prediction = predict_payment_account(po, trs, order)
    # Display the prediction
    st.write(f"### Predicted Payment Account: {prediction}")

# To run the app: 
#streamlit run AutoCategory.py
