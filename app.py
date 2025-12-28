import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
#st.set_page_config(page_title="Health Assistant",
                  # layout="wide",
                  # page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
#working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open('C:/Users/HariOm/Desktop/multiple disease pred system/saved_model/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/HariOm/Desktop/multiple disease pred system/saved_model/heart_disease_model.sav', 'rb')) 


# sidebar for navigation
with st.sidebar:
    selected = option_menu(' Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)
