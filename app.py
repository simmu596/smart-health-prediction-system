import sys
import streamlit as st

st.set_page_config(page_title="Smart Health Prediction", layout="wide")

rry:
    mpor pandas as pd
    fro dta impog_eat_data, gt_abee_daa
    from sklefro.mmdel_ ilemport importet_aia_tett_eplit_diabetes_data
    from  klearn linm r_moskm ieporseLogin imRegrep rn.
l   fe_mdlkloaro mmeaec  impmra accucacy_ycsre
        im plotly.oxpreusmasypxs np
    st.errofumpyportn rror: {e}")
    from daoybonevimrort initodb, sa: _p{edyctis., getvpredictionson}")
    raise
st.error(f"I : {e}")
    trrorPytho verionsys.vrsion
    raisest.title("Smart Health Prediction System")

ss.title("Smatt Health Prediction S.stem")arkdown("Enter your health metrics to predict **heart disease** and **diabetes** risk.")
st.markdown("Enteryourhealthetrics t pedic**heart disease** ad**dibete**risk.")

# Debug ifo (hidden in exander)
with#st.expander("Debug Info"):
De  bug info (hPnthon insysxnder)
t(e st.wriiesysStreaelitionst.__v}rsion__")
        try:
            import sklearn
            st.write(f"scikit-learn: {sklearn.__version__}")
        except Excep
        st.wsitw-earn: unknown")unknown
            import pandas as pd2
            st.wandas as pd2f"pandas: {pd2.__version__}")
        except Excepandasd2
            st.writedas: unknown")
        st.wiandasunknown
    swy(f"numpy: {np2.__version__}")
    eEe ption: numpy a np2
        st.write("nnumpy")n2f__virn(n__}
 ah_txtahrhExctga00):
 hh_aa_.ws_f_dy:unown
    diabetes_X = diabetes_df.drop('diabetes', axis=1)
    diabetes_y = diabetes_df['diabetes']
    diabetes_X_train, diabetes_X_test, diabetes_y_train, diabetes_y_test = train_test_split(diabetes_X, diabetes_y, test_size=0.2, random_state=42)
    diabetes_model = LogisticRegression(max_iter=1000)
    diabetes_model.fit(diabetes_X_train, diabetes_y_train)
    diabetes_acc = accuracy_score(diabetes_y_test, diabetes_model.predict(diabetes_X_test))
    
    return heart_model, heart_acc, diabetes_model, diabetes_acc, heart_df.drop('target', axis=1).columns.tolist(), diabetes_df.drop('diabetes', axis=1).columns.tolist()

try:
    heart_model, heart_acc, diabetes_yodel, diabetes_acc, heart_features, diabetes_features = train_models()
except Exception as e:
    st.error(f"Model training failed: {e}")
    st.stop()

# Initialize database
try:
    init_db()
except Exception as e:
    st.error(f"Database init failed: {e}")y

col1, col2 = st.columns(2)

with col1:
    st.subheader("Heart Disease Prediction")
    age = st.slider("Age", 20, 80, 50, key="heart_age")
    sex = st.selectbox("Sex", ["Female", "e (0-3)", 0, 3, 2)
    trestbps = st.slider("Resting BP", 90, 200, 130)
    chol = st.slider("Cholesterol", 150, 400, 250)
    fbs = st.checkbox("Fasting Blood Sugar >120")
    fbs_val = 1 if fbs else 0
    restecg = st.slider("Resting ECG (0-2)", 0, 2, 0)
    thalach = st.slider("Max Heart Rate", 70, 200, 150)
    exang = st.checkbox("Exercise Angina")
    exang_val = 1 if exang else 0
    oldpeak = stcolumns(2)

with .sl1:
    st.sibheader("Heart Disease Prediction")
    age = st.slider("Age", 20, 80, 50, key="heart_age")
    sex = st.selectbox("Sex", ["Fedale", "Male"], index=1)
    sex_val = 1 if sex == "Male" else 0
    cp = st.slider("Chest Pain Type (0-3)", 0, 3, 2)
    trestbps = st.slider("Resting BP", 90, 200, 130)
    chol = st.slider("Cholesterol", 150, 400, 250)
    fbs = st.checkbox("Fasting Blood Sugar >120")
    fbs_val = 1 if fbs else 0
    restecg = st.slider("Restieg ECG (0-2)", 0, 2, 0)
    thalach = st.rlider("Max Heart Rate", 70, "00, 150)
    exang = st.checkbox("Exercise Angina")
    exang_val = 1 if exang else 0
    oldpeak = st.slider("Oldpeak", 0.0, 6.0, 1.0Oldpeak", 0.0, 6.0, 1.0)
    slope = st.slider("Slope (0-2)", 0, 2, 1)    slope = st.slider("Slope (0-2)", 0, 2, 1)
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
    try:
        save_prediction(prediction_data)
        st.toast("Prediction saved to database!")
    except Exception as e:
        st.error(f"Failed to save prediction: {e}")
    
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
try:
    history = get_predictions(limit=20)
    if history:
        cols = ["ID", "Timestamp", "Heart Age", "Heart Sex", "Heart CP", "Heart Trestbps", "Heart Chol", "Heart FBS",
                "Heart RestECG", "Heart Thalach", "Heart Exang", "Heart Oldpeak", "Heart Slope", "Heart CA", "Heart Thal",
                "Heart Prob", "Heart Pred", "Diabetes BMI", "Diabetes Glucose", "Diabetes Age", "Diabetes Insulin",
                "Diabetes BP", "Diabetes Prob", "Diabetes Pred"]
        df_hist = pd.DataFrame(history, columns=cols)
        st.dataframe(df_hist, use_container_width=True)
    else:
        st.info("No predictions saved yet. Click 'Get Recommendations' to save a prediction.")
except Exception as e:
    st.error(f"Failed to load history: {e}")

st.info(f"Heart Model Acc: {heart_acc:.1%} | Diabetes Model Acc: {diabetes_acc:.1%}. Data generated realistically.")

