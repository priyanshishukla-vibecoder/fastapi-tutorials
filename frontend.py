import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import streamlit as st
import requests


# Load hashed passwords from file
file_path=Path(__file__).parent/"hashed_pw.pkl"
with file_path.open('rb') as f:
    hashed_passwords=pickle.load(f)

# ✅ NEW CONFIG FORMAT
config = {
    "credentials": {
        "usernames": {
            "priyanshi": {
                "name": "Priyanshi Shukla",
                "password": hashed_passwords[0]
            },
            "arjun": {
                "name": "Arjun Gupta",
                "password": hashed_passwords[1]
            }
        }
    },
    "cookie": {
        "name": "some_cookie_name",
        "key": "some_signature_key",
        "expiry_days": 30
    }
}


# ✅ Correct initialization
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)



authenticator.login(location='main')

authentication_status = st.session_state.get("authentication_status")
name = st.session_state.get("name")
username = st.session_state.get("username")

if authentication_status==False:
    st.error('Username/password is incorrect')

if authentication_status==None:
    st.warning('Please enter your username and password')

if authentication_status:
    st.write(f'Welcome *{name}*')
    authenticator.logout('Logout', 'main')

    # API_URL = "http://127.0.0.1:8000/predict" 

    API_URL = "http://16.171.21.30:8000/predict"

    st.title("Insurance Premium Category Predictor")
    st.markdown("Enter your details below:")

    # Input fields
    age = st.number_input("Age", min_value=1, max_value=119, value=30)
    weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
    height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
    income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
    smoker = st.selectbox("Are you a smoker?", options=[True, False])
    city = st.text_input("City", value="Mumbai")
    occupation = st.selectbox(
        "Occupation",
        ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
    )

    if st.button("Predict Premium Category"):
        input_data = {
            "age": age,
            "weight": weight,
            "height": height,
            "income_lpa": income_lpa,
            "smoker": smoker,
            "city": city,
            "occupation": occupation
        }

        try:
            response = requests.post(API_URL, json=input_data)
            result = response.json()

            if response.status_code == 200 and "response" in result:
                prediction = result["response"]
                st.success(f"Predicted Insurance Premium Category: **{prediction['predicted_category']}**")
                st.write("Confidence:", prediction["confidence"])
                st.write("Class Probabilities:")
                st.json(prediction["class_probabilities"])

            else:
                st.error(f"API Error: {response.status_code}")
                st.write(result)

        except requests.exceptions.ConnectionError:
            st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")

    