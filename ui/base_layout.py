import streamlit as st

def style_base_layout():

    st.markdown("""
                <style>
                        .stApp{
                            background: #586F2 !important;
                        }
                </style>

                """,unsafe_allow_html=True)