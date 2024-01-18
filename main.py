import profile
import os
import pandas as pd
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import pickle

# Load your trained pickle model
model_var = 'random_forest_classifier.pkl'  # Assuming your model file is saved as a pickle file
with open(model_var, 'rb') as model_file:
    model = pickle.load(model_file)

with st.sidebar:
    st.image("https://www.maxwellgeosystems.com/img/mos/Smart_Dashboards.png", width=250)
    st.title("Navigation Bar")

nav = st.sidebar.radio("Navigation", ["Home", "Upload Data File", "Search"])

if nav == "Home":
    # Your existing content
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.markdown("""<b><h1>Welcome to Rock - Your Guardian Against Fraud!</h1>

Unlock the Power of Fraud Detection with Ease:

Are you worried about potential fraud in your transactions? Fret not! Our Fraud Detection Website is designed to make safeguarding your business easy and interactive.

<h2>Key Features:</h2>

<h4>1. Effortless CSV Upload:</h4>
Simply upload your transaction data in CSV format, and let our magic begin! Our backend, powered by a smart Random Forest machine learning model, digs deep to spot any unusual patterns in your data.

<h4>2. Smart Random Forest Algorithm:</h4>
Meet your fraud-fighting ally! Our Random Forest algorithm is like a superhero for your data, detecting tricky patterns and uncovering potential fraud. Your peace of mind is our mission!

<h4>3. Quick MerchantID and ClientID Search:</h4>
Take control in a click! Enter a MerchantID or ClientID to fetch instant, useful data. Get the scoop on individual transactions, spot risks, and make informed choices to keep fraud at bay.

<h4>4. Understandable Fraud Details:</h4>
We're not here to confuse you. Our platform not only flags potential fraud but also breaks down the details. Understand the 'what' and 'why' behind each red flag, and make decisions with confidence.

Why Choose Us:

Accuracy, No Fuss: Our Random Forest model is accurate and keeps false alarms to a minimum.
User-Friendly Fun: Navigate effortlessly, upload data in a breeze, and get results with a smile.
Safety First: Your data's security is our priority. We've got the tech to keep your info safe and sound.
Don't let fraud sneak in! Join us at [Your Website Name] and enjoy a hassle-free journey into fraud detection. Make data your ally, and let's keep your business secure together.</b>""", True)

if nav == "Upload Data File":
    sub_nav1 = st.sidebar.file_uploader("Upload your dataset here")
    if not sub_nav1:
        st.warning("Please upload data to proceed.")
    else:
        df = pd.read_csv(sub_nav1, index_col=None)

        # Create a mapping dictionary for Category encoding
        category_mapping = {'Food': 0, 'Online': 1, 'Other': 2, 'Retail': 3, 'Travel': 4}

        # Convert 'Timestamp' to 'Hour' and 'gap'
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], format="%d-%m-%Y %H:%M")
        df['Hour'] = df['Timestamp'].dt.hour
        df['gap'] = (df['Timestamp'] - df['Timestamp'].shift()).fillna(pd.Timedelta(seconds=0))
        df['gap'] = df['gap'].dt.total_seconds()
        # Map 'Category' values to encoded values
        df['Category'] = df['Category'].map(category_mapping)

        df.to_csv("sourcedata.csv", index=None)  # Save the uploaded file

        st.dataframe(df)
        st.title("Detailed Analysis")

        show_eda = st.checkbox("Would You Like To See Stats About The Data?", value=False)
        if show_eda:
            st.text("Showing Result")
            profile_report = df.profile_report()
            st_profile_report(profile_report)

        # Assuming your model takes input features from the DataFrame
        x = df[['Category', 'TransactionAmount', 'AnomalyScore', 'Amount', 'AccountBalance', 'SuspiciousFlag', 'Hour', 'gap']]
        # Make predictions
        predictions = model.predict(x)

        # Add predictions to the DataFrame
        df['PredictedFraud'] = predictions

        # Remove 'FraudIndicator' and 'SuspiciousFlag' columns
        df_result = df.drop(['FraudIndicator', 'SuspiciousFlag'], axis=1)
        # Display only the rows where PredictedFraud is 1
        st.title("Predicted Frauds")
        st.dataframe(df_result[df_result['PredictedFraud'] == 1])

if nav == "Search":
    sub_nav2 = st.sidebar.file_uploader("Upload your dataset here")
    if not sub_nav2:
        st.warning("Please upload a CSV file to proceed.")
    else:
        df = pd.read_csv(sub_nav2, index_col=None)

        # Convert 'Timestamp' to 'Hour' and 'gap'
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], format="%d-%m-%Y %H:%M")
        df['Hour'] = df['Timestamp'].dt.hour
        df['gap'] = (df['Timestamp'] - df['Timestamp'].shift()).fillna(pd.Timedelta(seconds=0))

        df.to_csv("sourcedata.csv", index=None)  # Save the uploaded file

        st.dataframe(df)

        option = st.selectbox(
            'How would you like to be contacted?',
            ('CustomerID', 'MerchantID'))

        st.write('You selected:', option)
        number = st.number_input('Enter no.')

        # Filter DataFrame based on user selection
        filtered_df = df.loc[df[option] == number]

        # Display the filtered DataFrame
        st.dataframe(filtered_df)
 