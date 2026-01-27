# 🏢 Flat Resale Price Prediction – Streamlit Web Application

A full-stack **machine learning web application** that predicts flat resale prices based on location, flat configuration, lease details, and property characteristics.  
The application provides a clean UI, secure login system, and real-time predictions using a trained ML model.

This project demonstrates **end-to-end ML deployment**, from data preprocessing and model training to frontend deployment on the cloud.

---

## 📌 Problem Statement

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

## 🚀 Features

### 🔐 Authentication
- User **Login & Registration**
- Password hashing for security
- SQLite database (demo purpose)
- Logout functionality

### 📊 Prediction System
- ML-powered price prediction
- Handles multiple user inputs
- Real-time inference
- Styled prediction output for clarity

### 🎨 User Interface
- Clean and responsive Streamlit UI
- Background image styling
- Dropdown placeholders for better UX
- Text-based explanations rendered cleanly
- Predict & Logout buttons aligned professionally

### ☁️ Deployment
- Code hosted on **GitHub**
- Application deployed on **Streamlit Community Cloud**
- Publicly accessible web interface

---

## 🧠 Machine Learning Details

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

## 🧰 Tech Stack

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

---

## 📁 Project Structure

flat-resale-price-prediction/
│
├── app.py # Main application entry
├── prediction.py # Prediction logic
├── login.py # Login functionality
├── register.py # Registration functionality
├── search.py # Dropdown data loading
├── text_files.py # Text rendering logic
├── background.py # Background styling
├── storing.py # Database operations
├── model_xg.pkl # Trained ML model
├── users.db # SQLite database
│
├── assets/
│ └── background.jpg
│
├── json_files/
│ ├── town.json
│ ├── street_name.json
│ ├── flat_type.json
│ └── flat_model.json
│
├── Text files/
│ ├── Homepage.txt
│ ├── About Month & Year.txt
│ ├── About Flat Type.txt
│ ├── About Flat Model.txt
│ ├── About Storey Range.txt
│ ├── table_flat_model.txt
│ └── table_flat_type.txt
│
├── requirements.txt
└── README.md
