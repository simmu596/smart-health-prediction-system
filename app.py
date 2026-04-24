import streamlit as st
import pandas as pd
from data import get_heart_data, get_diabetes_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import plotly.express as px
import numpy as np
from database import init_db, save_prediction, get_predictions

st.set_page_config(page_title="Smart Health Prediction", layout="wide")

st.title("Smart Health Prediction System")
st.markdown("Enter your health metrics to predict **heart disease** and **diabetes** risk.")

@st.cache_resource
def train_models():
    # Heart disease model
    heart_df = get_heart_data()
    heart_X = heart_df.drop('target', axis=1)
    heart_y = heart_df['target']
    heart_X_train, heart_X_test, heart_y_train, heart_y_test = train_test_split(heart_X, heart_y, test_size=0.2, random_state=42)
    heart_model = LogisticRegression(max_iter=1000)
    heart_model.fit(heart_X_train, heart_y_train)
    heart_acc = accuracy_score(heart_y_test, heart_model.predict(heart_X_test))
    
    # Diabetes model
    diabetes_df = get_diabetes_data()
    diabetes_X = diabetes_df.drop('diabetes', axis=1)
    diabetes_y = diabetes_df['diabetes']
    diabetes_X_train, diabetes_X_test, diabetes_y_train, diabetes_y_test = train_test_split(diabetes_X, diabetes_y, test_size=0.2, random_state=42)
    diabetes_model = LogisticRegression(max_iter=1000)
    diabetes_model.fit(diabetes_X_train, diabetes_y_train)
    diabetes_acc = accuracy_score(diabetes_y_test, diabetes_model.predict(diabetes_X_test))
    
    return heart_model, heart_acc, diabetes_model, diabetes_acc, heart_df.drop('target', axis=1).columns.tolist(), diabetes_df.drop('diabetes', axis=1).columns.tolist()

heart_model, heart_acc, diabetes_model, diabetes_acc, heart_features, diabetes_features = train_models()

# Initialize database
init_db()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Heart Disease Prediction")
    age = st.slider("Age", 20, 80, 50, key="heart_age")
    sex = st.selectbox("Sex", ["Female", "Male"], index=1)
    sex_val = 1 if sex == "Male" else 0
    cp = st.slider("Chest Pain Type (0-3)", 0, 3, 2)
    trestbps = st.slider("Resting BP", 90, 200, 130)
    chol = st.slider("Cholesterol", 150, 400, 250)
    fbs = st.checkbox("Fasting Blood Sugar >120")
    fbs_val = 1 if fbs else 0
    restecg = st.slider("Resting ECG (0-2)", 0, 2, 0)
    thalach = st.slider("Max Heart Rate", 70, 200, 150)
    exang = st.checkbox("Exercise Angina")
    exang_val = 1 if exang else 0
    oldpeak = st.slider("Oldpeak", 0.0, 6.0, 1.0)
    slope = st.slider("Slope (0-2)", 0, 2, 1)
    ca = st.slider("CA (0-3)", 0, 3, 0)
    thal = st.slider("Thal (0-3)", 0, 3, 2)
    
    heart_input = np.array([[age, sex_val, cp, trestbps, chol, fbs_val, restecg, thalach, exang_val, oldpeak, slope, ca, thal]])
    heart_prob = heart_model.predict_proba(heart_input)[0][1]
    heart_pred = "High Risk" if heart_prob > 0.5 else "Low Risk"
    
    st.metric("Heart Disease Risk", f"{heart_prob:.1%}", delta=heart_pred)

with col2:
    st.subheader("Diabetes Prediction")
    bmi = st.slider("BMI", 18.0, 50.0, 30.0)
    glucose = st.slider("Glucose", 70, 200, 120)
    d_age = st.slider("Age", 20, 80, 50, key="diabetes_age")
    insulin = st.slider("Insulin", 0, 500, 100)
    bp = st.slider("Blood Pressure", 60, 140, 80)
    
    diabetes_input = np.array([[bmi, glucose, d_age, insulin, bp]])
    diabetes_prob = diabetes_model.predict_proba(diabetes_input)[0][1]
    diabetes_pred = "High Risk" if diabetes_prob > 0.5 else "Low Risk"
    
    st.metric("Diabetes Risk", f"{diabetes_prob:.1%}", delta=diabetes_pred)

# Model accuracies
col3, col4 = st.columns(2)
col3.metric("Heart Model Accuracy", f"{heart_acc:.1%}")
col4.metric("Diabetes Model Accuracy", f"{diabetes_acc:.1%}")

if st.button("Get Recommendations"):
    prediction_data = {
        "heart_age": age,
        "heart_sex": sex_val,
        "heart_cp": cp,
        "heart_trestbps": trestbps,
        "heart_chol": chol,
        "heart_fbs": fbs_val,
        "heart_restecg": restecg,
        "heart_thalach": thalach,
        "heart_exang": exang_val,
        "heart_oldpeak": oldpeak,
        "heart_slope": slope,
        "heart_ca": ca,
        "heart_thal": thal,
        "heart_prob": heart_prob,
        "heart_pred": heart_pred,
        "diabetes_bmi": bmi,
        "diabetes_glucose": glucose,
        "diabetes_age": d_age,
        "diabetes_insulin": insulin,
        "diabetes_bp": bp,
        "diabetes_prob": diabetes_prob,
        "diabetes_pred": diabetes_pred,
    }
    save_prediction(prediction_data)
    st.toast("Prediction saved to database!")
    
    if heart_prob > 0.5 or diabetes_prob > 0.5:
        st.error("High Risk Detected! Consult a doctor. Recommendations: Exercise daily, low-sugar diet, monitor BP/cholesterol.")
    else:
        st.success("Low Risk. Maintain healthy lifestyle!")

# Charts
st.subheader("Risk Visualization")
fig = px.bar(x=["Heart Disease", "Diabetes"], y=[heart_prob, diabetes_prob], title="Predicted Risks")
st.plotly_chart(fig, use_container_width=True)

# Prediction History
st.subheader("Prediction History")
history = get_predictions(limit=20)
if history:
    import pandas as pd
    cols = ["ID", "Timestamp", "Heart Age", "Heart Sex", "Heart CP", "Heart Trestbps", "Heart Chol", "Heart FBS",
            "Heart RestECG", "Heart Thalach", "Heart Exang", "Heart Oldpeak", "Heart Slope", "Heart CA", "Heart Thal",
            "Heart Prob", "Heart Pred", "Diabetes BMI", "Diabetes Glucose", "Diabetes Age", "Diabetes Insulin",
            "Diabetes BP", "Diabetes Prob", "Diabetes Pred"]
    df_hist = pd.DataFrame(history, columns=cols)
    st.dataframe(df_hist, use_container_width=True)
else:
    st.info("No predictions saved yet. Click 'Get Recommendations' to save a prediction.")

st.info(f"Heart Model Acc: {heart_acc:.1%} | Diabetes Model Acc: {diabetes_acc:.1%}. Data generated realistically.")
