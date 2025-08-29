import streamlit as st
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import threading
import time

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InsuranceData(BaseModel):
    age: int
    weight: float
    height: float
    income_lpa: float
    smoker: bool
    city: str
    occupation: str

@app.post("/predict")
async def predict(data: InsuranceData):
    # Prediction logic
    premium_score = 0
    
    # Age factor
    if data.age < 25:
        premium_score += 1
    elif data.age > 60:
        premium_score += 3
    else:
        premium_score += 2
    
    # Smoker factor
    if data.smoker:
        premium_score += 3
    
    # Income factor
    if data.income_lpa > 20:
        premium_score += 2
    elif data.income_lpa > 10:
        premium_score += 1
    
    # Determine category
    if premium_score >= 5:
        category = "High"
    elif premium_score >= 3:
        category = "Medium"
    else:
        category = "Low"
    
    return {"predicted_category": category}

@app.get("/")
async def root():
    return {"message": "Insurance Premium Prediction API is running!"}

def run_fastapi():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="warning")


def main():
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
            
            time.sleep(0.5)
            
            response = requests.post("http://localhost:8000/predict", json=input_data)
            
            if response.status_code == 200:
                result = response.json()
                prediction = result["predicted_category"]
                st.success(f"Predicted Insurance Premium Category: **{prediction}**")
                
               
                st.info("**Factors considered:** Age, Smoking status, Income level")
                
            else:
                st.error(f"API Error: {response.status_code}")
                st.write("Error details:", response.text)

        except requests.exceptions.ConnectionError:
            st.error("❌ Could not connect to the FastAPI server.")
            st.info("💡 The server is starting up. Please wait a moment and try again.")
            
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    # Start FastAPI server in a separate thread
    fastapi_thread = threading.Thread(target=run_fastapi, daemon=True)
    fastapi_thread.start()
    time.sleep(2)
    main()