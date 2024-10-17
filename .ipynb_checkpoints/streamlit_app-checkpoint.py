
import streamlit_app as st

# Placeholder function to load your model and make predictions
def predict_payment_account(order, po, project, account, vendor):
    # Replace this with your actual model loading and prediction code
    # For demonstration, a dummy prediction is returned.
    return "Predicted Account Name"
# Streamlit UI Layout
st.set_page_config(page_title="AI Account Predictor", layout='wide')
# Display a relevant image at the top
#image = Image.open('/Users/aroojqureshi/Desktop/ai_data_analyzer/logo.png')  # Load your image file here
#st.image(image, caption="Automated Expense Categorization", use_column_width=False, width=100)  # Set a smaller width
# Title of the app
st.title("AI Account Predictor")
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
    order = st.text_input("Order#", placeholder="Enter Order Number")
    po = st.text_input("PO#", placeholder="Enter Purchase Order Number")
    project = st.text_input("Project Name", placeholder="Enter Project Name")
    account = st.text_input("Account#", placeholder="Enter Account Number")
    vendor = st.text_input("Vendor", placeholder="Enter Vendor Name")
    # Submit button
    submitted = st.form_submit_button("Submit")
# When form is submitted
if submitted:
    # Call the model prediction function
    prediction = predict_payment_account(order, po, project, account, vendor)
    # Display the prediction
    st.write(f"### Predicted Payment Account: {prediction}")
[9:39 PM] Arooj A Qureshi
streamlit run app.py