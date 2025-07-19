# MACHINE PREICTIVE MAINTENANCE APP

## Overview
A Streamlit app to predict equipment failures using an XGBoost model, designed for maintenance scheduling in renewable energy equipment. Deployed on Streamlit Community Cloud.

## Features
- Input: footfall, tempMode, AQI, USS, CS
- Output: Failure/No Failure, Probability, Action (Replacement, Urgent Maintenance, Monitor, No Action)
- Accuracy: 92.20% (Test), 88.86% ± 4.45% (CV)

## Dataset
[Machine Failure Prediction Dataset](https://www.kaggle.com/datasets/umerrtx/machine-failure-prediction-using-sensor-data)

## Deployment
- Hosted on [Streamlit Community Cloud](https://share.streamlit.io/)
- Test at: [Machine Maintenance Predictor](https://machines-predictive-maintenance.streamlit.app/)

## Limitations
- No temporal patterns or LSTM due to static dataset.
- Future work: Incorporate time-series data.

## How to Run Locally
1. Install dependencies: `pip install -r requirements.txt`
2. Run: `streamlit run app.py`
