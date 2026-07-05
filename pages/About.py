import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️", layout="wide")

st.title("ℹ️ About This AI System")
st.caption("Breast Cancer Detection using Machine Learning (SVM Model)")

st.markdown("---")

# ==========================
# HERO SECTION
# ==========================

st.markdown("""
## 🩺 AI-Powered Breast Cancer Detection

This application is a **Machine Learning-based clinical decision support system**
designed to predict whether a breast tumor is **Benign** or **Malignant**.

It uses a trained **Support Vector Machine (SVM)** model built on the
**Wisconsin Breast Cancer Diagnostic Dataset**.
""")

st.markdown("---")

# ==========================
# CARDS SECTION
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
### 🎯 Objective

- Early cancer detection  
- Assist medical diagnosis  
- Improve accuracy using ML  
""")

with col2:
    st.info("""
### 🤖 Model Details

- Algorithm: SVM  
- Accuracy: 98.25%  
- Dataset: 569 samples  
""")

with col3:
    st.warning("""
### ⚠ Disclaimer

This tool is for **educational purposes only**  
Not a substitute for professional medical advice
""")

st.markdown("---")

# ==========================
# TECHNOLOGIES
# ==========================

st.subheader("⚙️ Technologies Used")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.success("🐍 Python")

with tech2:
    st.success("📊 Pandas & NumPy")

with tech3:
    st.success("🤖 Scikit-Learn")

with tech4:
    st.success("🎨 Streamlit")

st.markdown("---")

# ==========================
# WORKFLOW
# ==========================

st.subheader("🚀 Machine Learning Workflow")

workflow = [
    "📂 Data Collection (Wisconsin Dataset)",
    "🧹 Data Preprocessing",
    "📊 Exploratory Data Analysis",
    "⚙ Feature Engineering & Scaling",
    "🤖 Model Training (SVM, Decision Tree)",
    "📈 Model Evaluation",
    "🚀 Deployment using Streamlit"
]

for step in workflow:
    st.write(step)

st.markdown("---")

# ==========================
# MODEL PERFORMANCE
# ==========================

st.subheader("📊 Model Performance Comparison")

col1, col2 = st.columns(2)

with col1:
    st.metric("Support Vector Machine", "98.25% Accuracy")

with col2:
    st.metric("Decision Tree", "92.10% Accuracy")

st.markdown("---")

# ==========================
# FUTURE IMPROVEMENTS
# ==========================

st.subheader("🚀 Future Improvements")

st.markdown("""
- 🔍 Hyperparameter tuning  
- 🧠 Deep Learning models (CNN, ANN)  
- 📊 Explainable AI (SHAP/LIME)  
- 📁 CSV batch prediction  
- ☁ Cloud deployment  
- 📈 Real-time monitoring system  
""")

st.markdown("---")

# ==========================
# FOOTER
# ==========================

st.info("""
👩‍💻 Developed as an End-to-End Machine Learning Project  
Built using Streamlit + Scikit-Learn
""")