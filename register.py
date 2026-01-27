import streamlit as st
import re
import hashlib
import storing

def validate_mail(email):
    return re.match(r'^[a-zA-Z0-9_+-.]+@[a-z]+\.[a-z]{2,}$', email)

def validate_password(password):
    return re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[\\W_]).{6,16}$', password)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(email, password):
    user = storing.execute(
        "SELECT email FROM registration WHERE email = ?",
        (email,),
        fetch=True
    )

    if user:
        st.warning("Email already exists. Please login.")
    else:
        storing.execute(
            "INSERT INTO registration (email, password) VALUES (?, ?)",
            (email, hash_password(password))
        )
        st.success("Registration successful. Please login.")

def register_ui():
    st.subheader("Register")
    email = st.text_input("Email", key="reg_email")
    password = st.text_input("Password", type="password", key="reg_pass")
    confirm = st.text_input("Confirm Password", type="password", key="reg_conf")

    if st.button("Register"):
        if not validate_mail(email):
            st.error("Invalid email format")
        elif password != confirm:
            st.error("Passwords do not match")
        else:
            register_user(email, password)
