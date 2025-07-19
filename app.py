import pandas as pd
import numpy as np
import streamlit as st
import joblib
import warnings
warnings.filterwarnings('ignore')

model = joblib.load('xgb_model_static.pkl')
scaler = joblib.load('scaler_static.pkl')

st.title('🛠 Predictive Maintenance Predictor')
st.markdown("Enter values to get prediction, probability and action recommendation.")

footfall = st.number_input("Number of people or objects passing by the machine", min_value=0, step=1)
tempmode = st.number_input("Temperature mode or setting of the machine", min_value=0, step=1)
aqi = st.number_input("Air quality index near the machine", min_value=0, step=1)
uss = st.number_input("Ultrasonic sensor data", min_value=0, step=1)
cs = st.number_input("Current sensor readings", min_value=0, step=1)

if st.button('Predict'):
    input_data = np.array([[footfall,tempmode,aqi,uss,cs]])
    scaled_data = scaler.transform(input_data)

    predictions = model.predict(scaled_data)[0]
    probabilities = model.predict_proba(scaled_data)[0][1]

    action = "🔧 Replacement" if probabilities > 0.9 else "⚠️ Urgent Maintenance" if probabilities > 0.7 else "🧐 Monitor" if probabilities > 0.5 else "✅ No Action Required"
    prediction_text = "Failure" if predictions == 1 else "No Failure"

    st.success(f"**Prediction:** {prediction_text}")
    st.info(f"**Probability:** {probabilities:.4f}")
    st.warning(f"**Recommended Action:** {action}")