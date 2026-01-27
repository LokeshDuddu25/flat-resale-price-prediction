# 🏢 Flat Resale Price Prediction – Streamlit Web Application

A full-stack **machine learning web application** that predicts flat resale prices based on location, flat configuration, lease details, and property characteristics.

The application provides a clean UI, secure login system, and real-time predictions using a trained ML model.

This project demonstrates **end-to-end ML deployment**, from data preprocessing and model training to frontend deployment on the cloud.

---

## Problem Statement

Flat resale prices depend on multiple factors such as:
- Location (town & street)
- Flat type and model
- Floor area
- Lease commencement year
- Storey range
- Time of resale

Manually estimating prices is inefficient and inaccurate.  
This application helps users **instantly estimate resale prices** using a trained machine learning model.

---

##  Features

###  Authentication
- User **Login & Registration**
- Password hashing for security
- SQLite database (demo purpose)
- Logout functionality

###  Prediction System
- ML-powered price prediction
- Handles multiple user inputs
- Real-time inference
- Styled prediction output for clarity

###  User Interface
- Clean and responsive Streamlit UI
- Background image styling
- Dropdown placeholders for better UX
- Text-based explanations rendered cleanly
- Predict & Logout buttons aligned professionally

###  Deployment
- Code hosted on **GitHub**
- Application deployed on **Streamlit Community Cloud**
- Publicly accessible web interface

---

##  Machine Learning Details

- **Model Used:** XGBoost Regressor
- **Input Features:**
  - Month
  - Town
  - Flat Type
  - Street Name
  - Floor Area (sqm)
  - Flat Model
  - Lease Commence Year
  - Remaining Lease
  - Storey Range
  - Year
- **Preprocessing:**
  - Categorical encoding using JSON mappings
  - Feature selection and scaling
- **Output:**
  - Predicted flat resale price

---

##  Tech Stack

### Frontend
- Streamlit
- HTML/CSS (via Streamlit markdown)

### Backend
- Python
- SQLite (authentication)

### Machine Learning
- XGBoost
- Pandas
- NumPy
- Scikit-learn

### Deployment
- GitHub
- Streamlit Community Cloud


