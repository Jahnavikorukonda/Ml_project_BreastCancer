import streamlit as st
import pandas as pd
import time
from src.predict import predict
import plotly.graph_objects as go

st.set_page_config(page_title="Prediction", page_icon="🧬", layout="wide")

st.title("🧬 Breast Cancer Diagnosis AI")
st.caption("Advanced ML-powered diagnostic assistant (SVM Model)")

st.markdown("---")

# ==========================
# INPUT SECTION
# ==========================

col_left, col_right = st.columns([2, 1])

with col_left:

    st.subheader("📋 Patient Measurements")

    with st.expander("Mean Features", expanded=True):
        c1, c2 = st.columns(2)

        with c1:
            mean_radius = st.number_input("Mean Radius", 14.12)
            mean_texture = st.number_input("Mean Texture", 19.29)
            mean_perimeter = st.number_input("Mean Perimeter", 91.97)
            mean_area = st.number_input("Mean Area", 654.89)
            mean_smoothness = st.number_input("Mean Smoothness", 0.09)

        with c2:
            mean_compactness = st.number_input("Mean Compactness", 0.10)
            mean_concavity = st.number_input("Mean Concavity", 0.08)
            mean_concave_points = st.number_input("Mean Concave Points", 0.05)
            mean_symmetry = st.number_input("Mean Symmetry", 0.18)
            mean_fractal_dimension = st.number_input("Mean Fractal Dimension", 0.06)

    with st.expander("Error Features"):
        c1, c2 = st.columns(2)

        with c1:
            radius_error = st.number_input("Radius Error", 0.40)
            texture_error = st.number_input("Texture Error", 1.21)
            perimeter_error = st.number_input("Perimeter Error", 2.86)
            area_error = st.number_input("Area Error", 40.33)
            smoothness_error = st.number_input("Smoothness Error", 0.007)

        with c2:
            compactness_error = st.number_input("Compactness Error", 0.02)
            concavity_error = st.number_input("Concavity Error", 0.03)
            concave_points_error = st.number_input("Concave Points Error", 0.01)
            symmetry_error = st.number_input("Symmetry Error", 0.02)
            fractal_dimension_error = st.number_input("Fractal Dimension Error", 0.003)

    with st.expander("Worst Features"):
        c1, c2 = st.columns(2)

        with c1:
            worst_radius = st.number_input("Worst Radius", 16.27)
            worst_texture = st.number_input("Worst Texture", 25.67)
            worst_perimeter = st.number_input("Worst Perimeter", 107.26)
            worst_area = st.number_input("Worst Area", 880.58)
            worst_smoothness = st.number_input("Worst Smoothness", 0.13)

        with c2:
            worst_compactness = st.number_input("Worst Compactness", 0.25)
            worst_concavity = st.number_input("Worst Concavity", 0.27)
            worst_concave_points = st.number_input("Worst Concave Points", 0.11)
            worst_symmetry = st.number_input("Worst Symmetry", 0.29)
            worst_fractal_dimension = st.number_input("Worst Fractal Dimension", 0.08)

    predict_btn = st.button("🚀 Predict Diagnosis", use_container_width=True)

with col_right:

    st.info("""
### 🧠 AI Guidance

- Enter all 30 tumor measurements  
- Click **Predict Diagnosis**  
- View AI result + probabilities  

⚠ This is an educational tool only
""")

# ==========================
# PREDICTION
# ==========================

if predict_btn:

    patient_data = pd.DataFrame([{
        "mean radius": mean_radius,
        "mean texture": mean_texture,
        "mean perimeter": mean_perimeter,
        "mean area": mean_area,
        "mean smoothness": mean_smoothness,
        "mean compactness": mean_compactness,
        "mean concavity": mean_concavity,
        "mean concave points": mean_concave_points,
        "mean symmetry": mean_symmetry,
        "mean fractal dimension": mean_fractal_dimension,

        "radius error": radius_error,
        "texture error": texture_error,
        "perimeter error": perimeter_error,
        "area error": area_error,
        "smoothness error": smoothness_error,
        "compactness error": compactness_error,
        "concavity error": concavity_error,
        "concave points error": concave_points_error,
        "symmetry error": symmetry_error,
        "fractal dimension error": fractal_dimension_error,

        "worst radius": worst_radius,
        "worst texture": worst_texture,
        "worst perimeter": worst_perimeter,
        "worst area": worst_area,
        "worst smoothness": worst_smoothness,
        "worst compactness": worst_compactness,
        "worst concavity": worst_concavity,
        "worst concave points": worst_concave_points,
        "worst symmetry": worst_symmetry,
        "worst fractal dimension": worst_fractal_dimension
    }])

    start = time.time()
    result = predict(patient_data)
    end = time.time()

    prediction = result["prediction"]
    confidence = result["confidence"]
    benign_prob = result["benign_probability"]
    malignant_prob = result["malignant_probability"]

    st.markdown("---")

    # ==========================
    # RESULT SECTION
    # ==========================

    st.subheader("📊 Diagnosis Result")

    if prediction == "Benign":
        st.success("🟢 BENIGN - Low Risk Detected")
    else:
        st.error("🔴 MALIGNANT - High Risk Detected")

    col1, col2, col3 = st.columns(3)

    col1.metric("Confidence", f"{confidence:.2f}%")
    col2.metric("Prediction Time", f"{end - start:.4f}s")
    col3.metric("Model", "SVM (98.25%)")

    st.markdown("---")

    # ==========================
    # PROBABILITY GAUGE
    # ==========================

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=["Benign", "Malignant"],
        y=[benign_prob, malignant_prob],
        marker_color=["green", "red"]
    ))

    fig.update_layout(
        title="Prediction Probability",
        yaxis_title="Probability (%)"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    with st.expander("📄 Patient Data"):
        st.dataframe(patient_data)