import streamlit as st

st.set_page_config(
    page_title="Breast Cancer AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------
# Custom CSS
# ------------------------------
st.markdown("""
<style>
/* Hide Streamlit default UI */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* App background */
.stApp {
    background: #f4f7fb;
    color: #1e293b;
}

/* Main container spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
    max-width: 100%;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #12355B 0%, #0f2d4a 100%);
    border-right: 1px solid rgba(255,255,255,0.08);
    padding-top: 1rem;
}

/* Sidebar text visibility fix */
section[data-testid="stSidebar"] .stMarkdown,
section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] .stMarkdown li,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: #ffffff !important;
}

/* Sidebar metric cards */
section[data-testid="stSidebar"] div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 12px;
    box-shadow: none;
}

/* Sidebar metric label */
section[data-testid="stSidebar"] div[data-testid="stMetricLabel"] {
    color: #dbeafe !important;
    font-size: 14px;
    font-weight: 600;
}

/* Sidebar metric value */
section[data-testid="stSidebar"] div[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-size: 22px;
    font-weight: 700;
}

/* Sidebar success box */
section[data-testid="stSidebar"] div[data-testid="stAlert"] {
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.15);
    background: rgba(255,255,255,0.08);
    color: #ffffff !important;
}

/* Sidebar success/info box text */
section[data-testid="stSidebar"] div[data-testid="stAlert"] p,
section[data-testid="stSidebar"] div[data-testid="stAlert"] span,
section[data-testid="stSidebar"] div[data-testid="stAlert"] div {
    color: #ffffff !important;
}

/* Main page metric cards */
div[data-testid="stMetric"] {
    background: #ffffff;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
    border: 1px solid #e5e7eb;
    text-align: center;
}

/* Main metric label */
div[data-testid="stMetricLabel"] {
    color: #64748b !important;
    font-weight: 600;
    font-size: 15px;
}

/* Main metric value */
div[data-testid="stMetricValue"] {
    color: #0f172a !important;
    font-weight: 700;
    font-size: 30px;
}

/* Main info box */
div[data-testid="stAlert"] {
    border-radius: 14px;
    border: 1px solid #bfdbfe;
    background: #eff6ff;
    color: #1d4ed8;
    padding: 14px 16px;
}

/* Horizontal rule */
hr {
    border: none;
    height: 1px;
    background: #e2e8f0;
    margin: 1.5rem 0;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.markdown("# 🩺 Breast Cancer AI")
st.sidebar.markdown("---")

st.sidebar.markdown("## 🤖 Model")
st.sidebar.success("Support Vector Machine")

st.sidebar.markdown("---")

st.sidebar.markdown("## 📊 Statistics")
st.sidebar.metric("Accuracy", "98.25%")
st.sidebar.metric("Dataset", "569")
st.sidebar.metric("Features", "30")

st.sidebar.markdown("---")

st.sidebar.markdown("## ⚙ Technology")
st.sidebar.markdown("""
- Python
- Scikit-Learn
- Pandas
- NumPy
- Streamlit
""")

st.sidebar.markdown("---")
st.sidebar.info("""
Developed by  
**Jahnavi Korukonda**

End-to-End Machine Learning Project
""")

# ------------------------------
# Main Home Page
# ------------------------------
st.markdown("""
<div style="padding: 10px 0 20px 0;">
    <h1 style="color:#0f172a; margin-bottom:8px;">🩺 Breast Cancer Detection System</h1>
    <h3 style="color:#2563eb; margin-top:0;">AI-powered Clinical Decision Support</h3>
    <p style="font-size:18px; color:#475569;">
        Predict whether a breast tumor is <b>Benign</b> or <b>Malignant</b>
        using a trained <b>Support Vector Machine (SVM)</b> model.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Patients", "569")
with col2:
    st.metric("Features", "30")
with col3:
    st.metric("Best Model", "SVM")
with col4:
    st.metric("Accuracy", "98.25%")

st.markdown("<br>", unsafe_allow_html=True)

st.info("👈 Select **Home**, **Predict**, or **About** from the sidebar to navigate through the application.")