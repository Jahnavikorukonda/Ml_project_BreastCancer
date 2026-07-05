import streamlit as st
import pandas as pd

st.title("🩺 AI Clinical Dashboard")
st.caption("Machine Learning Based Breast Cancer Detection")

st.markdown("---")

# ==========================
# Hero Section
# ==========================

left, right = st.columns([2, 1])

with left:
    st.markdown("""
    ## Early Detection Saves Lives

    This application uses a trained **Support Vector Machine (SVM)** model
    to predict whether a breast tumor is **Benign** or **Malignant**
    based on diagnostic measurements.

    Navigate to **Predict** from the sidebar to analyze a patient.
    """)

with right:
    st.info("""
### 🤖 AI Model

**Support Vector Machine**

✔ Accuracy : **98.25%**

✔ Dataset : **569 Samples**

✔ Features : **30**
""")

st.markdown("---")

# ==========================
# Dashboard Cards
# ==========================

st.subheader("📊 Dashboard Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Dataset Size", "569")

with c2:
    st.metric("Input Features", "30")

with c3:
    st.metric("Best Model", "SVM")

with c4:
    st.metric("Accuracy", "98.25%")

st.markdown("---")

# ==========================
# Model Comparison
# ==========================

st.subheader("📈 Model Comparison")

comparison = pd.DataFrame({
    "Model": [
        "Support Vector Machine",
        "Decision Tree"
    ],
    "Accuracy": [
        98.25,
        92.10
    ]
})

st.bar_chart(
    comparison.set_index("Model"),
    use_container_width=True
)

st.markdown("---")

# ==========================
# Workflow
# ==========================

left, right = st.columns(2)

with left:

    st.subheader("🔬 Workflow")

    workflow = [
        "📂 Data Collection",
        "🧹 Data Cleaning",
        "📊 Exploratory Data Analysis",
        "⚙ Feature Scaling",
        "🤖 Model Training",
        "📈 Model Evaluation",
        "🚀 Deployment"
    ]

    for step in workflow:
        st.write(step)

with right:

    st.subheader("⚙ Technology Stack")

    st.success("🐍 Python")
    st.success("📊 Pandas")
    st.success("🔢 NumPy")
    st.success("🤖 Scikit-Learn")
    st.success("📈 Matplotlib")
    st.success("🎨 Streamlit")

st.markdown("---")

st.subheader("📌 About the Model")

st.write("""
The prediction model was trained using the **Wisconsin Breast Cancer Diagnostic Dataset**.

The deployed model is a **Support Vector Machine (SVM)** selected after comparing multiple machine learning algorithms based on classification performance.

Use the **Predict** page to enter patient measurements and receive a prediction along with confidence scores.
""")