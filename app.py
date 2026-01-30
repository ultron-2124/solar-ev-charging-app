import streamlit as st
import joblib
import numpy as np
import os

st.title("☀️ Solar EV Charging Recommendation System")

MODEL_PATH = "model/solar_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("❌ Model file not found")
else:
    model = joblib.load(MODEL_PATH)

    ambient = st.number_input("Ambient Temperature (°C)")
    module = st.number_input("Module Temperature (°C)")
    irradiation = st.number_input("Irradiation (W/m²)")

    if st.button("Predict"):
        features = np.array([[ambient, module, irradiation]])
        prediction = model.predict(features)[0]

        st.write(f"🔋 Predicted DC Power: {prediction:.2f}")

        if prediction > 800:
            st.success("✅ Recommendation: CHARGE")
        elif prediction > 300:
            st.warning("⏳ Recommendation: WAIT")
        else:
            st.error("❌ Recommendation: AVOID")
