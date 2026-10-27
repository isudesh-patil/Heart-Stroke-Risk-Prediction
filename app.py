import streamlit as st
import pandas as pd
import joblib

model = joblib.load("KNN_heart_stoke_prediction.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.title("Heart Stroke Prediction❤️")
st.markdown("Please provide the following imformation")
age = st.slider("AGE", 18,100,40)
sex = st.selectbox("SEX",['Male',"Female"])
chest_pain = st.selectbox("Chest Pain Type",['ATA','NAP','ASY','TA'])
resting_bp = st.number_input("Resting Bloop pressure(mm HG)",80, 200, 180)
cholesterol = st.number_input('Cholesterol(mg/dl)',100, 600, 200)
fasting_bs = st.selectbox("Fasting blood sugar > 120 mg/dl", [0,1])
resting_ecg = st.selectbox('Resting Eletrocardigraphic results',['Normal','ST','LVH'])
max_hr = st.slider("Maximum Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Induced Angina", ['Yes','No'])
oldpeak = st.slider("OldPeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST SLope",['UP','Flat','Down'])


if st.button("Predict"):
    raw_input = {
        "Age" : age,
        "RestingBP" : resting_bp,  
        "Cholesterol" : cholesterol,
        "FastingBS" : fasting_bs,
         "MaxHR" : max_hr,
        "Oldpeak" : oldpeak,
        "Sex" + sex : 1,
        "ChestPainType" + chest_pain : 1,
        "RestingECG" + resting_ecg : 1,
        "ExerciseAngina" + exercise_angina : 1,
        "ST_Slope" + st_slope : 1
     }
    input_df = pd.DataFrame([raw_input])
    for col in columns :
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[columns]
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]
    if prediction == 1:
        st.error(" High risk of Heart Stroke")
    else:
        st.success("Low rirsk of Heart Stroke")