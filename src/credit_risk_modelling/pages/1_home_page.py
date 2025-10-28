import streamlit as st

from credit_risk_modelling.front_end.utils import set_sidebar
from credit_risk_modelling.lang.language import TEXTS


st.set_page_config(page_title="🏠 Home Page")
set_sidebar()
lang_key = st.session_state["lang_key"]
wording = TEXTS[lang_key]["home_page"]

st.title(wording["title"])
st.text(wording["welcome"])
st.text(wording["choose_topic"])
