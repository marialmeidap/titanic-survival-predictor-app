
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("titanic_model.pkl")

st.title("🚢 Titanic Survival Prediction App")
st.markdown("Enter passenger details to predict if they would survive.")

pclass = st.selectbox("Ticket Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 100, 25)
sibsp = st.number_input("Number of Siblings/Spouses Aboard", 0, 10, 0)
parch = st.number_input("Number of Parents/Children Aboard", 0, 10, 0)
fare = st.number_input("Ticket Fare ($)", 0.0, 500.0, 50.0)
embarked = st.selectbox("Port of Embarkation", ["S", "C", "Q"])

sex = 1 if sex == "male" else 0
embarked_S = 1 if embarked == "S" else 0
embarked_C = 1 if embarked == "C" else 0
embarked_Q = 1 if embarked == "Q" else 0

input_data = pd.DataFrame({
    'Pclass': [pclass],
    'Age': [age],
    'SibSp': [sibsp],
    'Parch': [parch],
    'Fare': [fare],
    'Sex_male': [sex_male],
    'Embarked_Q': [embarked_Q],
    'Embarked_S': [embarked_S]
})

prediction = model.predict(input_data)[0]
result = "🟢 Survived" if prediction == 1 else "🔴 Did not survive"

st.subheader("Prediction Result:")
st.markdown(f"### {result}")
