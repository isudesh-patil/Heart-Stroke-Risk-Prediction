import streamlit as st
import pandas as pd
import joblib

model = joblib.load("KNN_heart_stoke_prediction.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

