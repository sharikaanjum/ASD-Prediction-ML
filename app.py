import streamlit as st
import numpy as np
import pickle
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = pickle.load(open(os.path.join(BASE_DIR, 'model.pkl'), 'rb'))
gender_encoder = pickle.load(open(os.path.join(BASE_DIR, 'gender_encoder.pkl'), 'rb'))
ethnicity_encoder = pickle.load(open(os.path.join(BASE_DIR, 'ethnicity_encoder.pkl'), 'rb'))


# ── Dropdowns use the EXACT string labels the encoder knows ───────
gender_options    = list(gender_encoder.classes_)    # ['Female', 'Male']
ethnicity_options = list(ethnicity_encoder.classes_) # ['Asian', 'Black', ...]

# ── UI ────────────────────────────────────────────────────────────
st.set_page_config(page_title="Autism Prediction", page_icon="🧠")
st.title("🧠 Autism Prediction App")
st.markdown("Fill in the details below and click **Predict**.")

age       = st.number_input("Enter Age", min_value=1, max_value=100, value=10)
gender    = st.selectbox("Select Gender",              gender_options)
ethnicity = st.selectbox("Select Ethnicity",           ethnicity_options)
jaundice  = st.selectbox("Had Jaundice?",              ["Yes", "No"])
family    = st.selectbox("Family History of Autism?",  ["Yes", "No"])

# ── Predict ───────────────────────────────────────────────────────
if st.button("Predict"):
    try:
        gender_enc    = gender_encoder.transform([gender])[0]
        ethnicity_enc = ethnicity_encoder.transform([ethnicity])[0]
        jaundice_enc  = 1 if jaundice == "Yes" else 0
        austim_enc    = 1 if family   == "Yes" else 0

        input_data = np.array([[age, gender_enc, ethnicity_enc,
                                jaundice_enc, austim_enc]])

        # Safety check
        if input_data.shape[1] != model.n_features_in_:
            st.error(f"Feature mismatch: app has {input_data.shape[1]}, model expects {model.n_features_in_}. Please retrain.")
        else:
            prediction = model.predict(input_data)
            if prediction[0] == 1:
                st.error("⚠️ The model predicts: **Autism Likely**")
            else:
                st.success("✅ The model predicts: **No Autism Detected**")

    except Exception as e:
        st.error(f"Error: {e}")