import streamlit as st
from src.database.db import create_subject

@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.write("Enter the subject code provided by teacher to enroll")
    join_code = st.text_input("Subject Code", placeholder="Eg: CS-AIML_412" )