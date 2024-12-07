import streamlit as st

def set_transparent_container():
    st.markdown(
        """
        <div class="mainContent">
        <style>
        .stApp {
            background: url('https://www.datasciencecentral.com/wp-content/uploads/2022/03/AdobeStock_283882447.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

        /* Nadpisanie głównego kontenera Streamlit */
        .block-container {
            background-color: rgba(0, 0, 0, 0.5);
            padding: 40px 20px; 
            border-radius: 15px; 
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.5); 
            max-width: 1200px; 
            margin: 50px auto; 
            color: white; 
            overflow: scroll; 
        }
        h1, h2, h3, p, label {
            text-align: center;
            color: white;
        }
        .stSelectbox, .stButton {
            margin: auto;
            width: 90%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def end_transparent_container():
    st.markdown(
        """
        <style>
        </style>
        """,
        unsafe_allow_html=True
    )
