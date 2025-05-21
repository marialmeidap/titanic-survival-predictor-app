# 🚢 Titanic Survival Predictor App

This machine learning project predicts whether a passenger would survive the Titanic disaster, based on demographic and travel-related information.

## 🔍 Project Overview

Using the classic [Titanic dataset](https://www.kaggle.com/competitions/titanic/), we built a classification model using **Random Forest** to predict survival. The model was trained on the cleaned and preprocessed training data and deployed as a **Streamlit web app**.

## 📦 Features Used

- Pclass (Ticket Class)
- Age
- SibSp (Number of siblings/spouses aboard)
- Parch (Number of parents/children aboard)
- Fare (Ticket price)
- Sex (encoded)
- Embarked (Port of embarkation, encoded)

## 🎯 Model Performance (Validation Set)

- **Accuracy**: 80.4%
- **F1 Score (Class 1 - Survived)**: 0.77
- **Recall (Class 1)**: 0.84

## 🌐 Live Demo

👉 Try the live app here:  
[https://titanic-survival-predictor-app-nzljgbmbpatqn6qtfxcbp4.streamlit.app](https://titanic-survival-predictor-app-nzljgbmbpatqn6qtfxcbp4.streamlit.app)

## 📁 Files Included

- `titanic_model.pkl`: Trained machine learning model
- `app.py`: Streamlit app script
- `titanic.csv`: Cleaned dataset (optional)
- `notebook.ipynb`: Full development notebook
- `requirements.txt`: Python dependencies

## 🚀 How to Run Locally

```bash
git clone https://github.com/yourusername/titanic-survival-predictor-app.git
cd titanic-survival-predictor-app
pip install -r requirements.txt
streamlit run app.py

