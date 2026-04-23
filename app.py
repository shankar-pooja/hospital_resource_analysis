import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# LOAD USERS
# -------------------------------
def load_users():
    return pd.read_csv("users.csv")

def save_user(username, password):
    new_user = pd.DataFrame([[username, password]], columns=["username", "password"])
    new_user.to_csv("users.csv", mode='a', header=False, index=False)

# -------------------------------
# SESSION
# -------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -------------------------------
# LOGIN PAGE
# -------------------------------
def login():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        users = load_users()

        if ((users["username"] == username) & (users["password"] == password)).any():
            st.session_state.logged_in = True
            st.success("Login Successful")
        else:
            st.error("Invalid credentials")

# -------------------------------
# REGISTER PAGE
# -------------------------------
def register():
    st.title("📝 Register")

    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")

    if st.button("Register"):
        save_user(new_user, new_pass)
        st.success("Account created! Go to Login.")

# -------------------------------
# DASHBOARD
# -------------------------------
def dashboard():
    st.title("🏥 Hospital Dashboard")

    data = pd.read_csv("hospital_data.csv")

    data['Admission_Date'] = pd.to_datetime(data['Admission_Date'])
    data['Discharge_Date'] = pd.to_datetime(data['Discharge_Date'])
    data['Length_of_Stay'] = (data['Discharge_Date'] - data['Admission_Date']).dt.days

    st.subheader("📊 Summary")
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Patients", len(data))
    col2.metric("Avg Stay", round(data['Length_of_Stay'].mean(), 2))
    col3.metric("Avg Cost", int(data['Cost'].mean()))

    st.subheader("📈 Analysis")

    fig1, ax1 = plt.subplots()
    sns.countplot(x='Department', data=data, ax=ax1)
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    data['Bed_Type'].value_counts().plot(kind='bar', ax=ax2)
    st.pyplot(fig2)

    fig3, ax3 = plt.subplots()
    sns.histplot(data['Length_of_Stay'], bins=5, ax=ax3)
    st.pyplot(fig3)

    fig4, ax4 = plt.subplots()
    sns.histplot(data['Cost'], bins=5, ax=ax4)
    st.pyplot(fig4)

# -------------------------------
# MAIN APP
# -------------------------------
st.sidebar.title("Navigation")

menu = st.sidebar.radio("Go to", ["Login", "Register"])

if st.session_state.logged_in:
    dashboard()
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
else:
    if menu == "Login":
        login()
    else:
        register()