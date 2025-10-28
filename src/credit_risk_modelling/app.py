import streamlit as st

from credit_risk_modelling.front_end.utils import init_streamlit_session


init_streamlit_session()
st.switch_page("pages/1_home_page.py")
