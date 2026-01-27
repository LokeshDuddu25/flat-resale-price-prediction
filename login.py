import streamlit as st
import hashlib
import re
import storing

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validate_mail(email):
    return re.match(r'^[a-zA-Z0-9_+-.]+@[a-z]+\.[a-z]{2,}$', email)

def login_user(email, password):
    user = storing.execute(
        "SELECT password FROM registration WHERE email = ?",
        (email,),
        fetch=True
    )

    if not user:
        st.error("Invalid email or password")
        return False

    if user[0][0] == hash_password(password):
        st.success(f"Welcome {email}")
        return True
    else:
        st.error("Invalid email or password")
        return False

def login_ui():
    st.subheader("Login")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    email = st.text_input("Email", key="log_email")
    password = st.text_input("Password", type="password", key="log_pass")

    if st.button("Login"):
        if validate_mail(email) and login_user(email, password):
            st.session_state.logged_in = True
            st.rerun()
