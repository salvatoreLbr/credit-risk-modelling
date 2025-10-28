import streamlit as st

from credit_risk_modelling.lang.language import TEXTS


def change_language():
    st.sidebar.selectbox(
        label=TEXTS[st.session_state["lang_key"]]["language_select"],
        options=["Italiano", "English"],
        key="language_selector",
        on_change=set_language,
        index=0 if st.session_state["lang_key"] == "it" else 1,
    )


def get_language() -> str | None:
    if "lang_key" not in st.session_state:
        init_streamlit_session()
    return st.session_state["lang_key"]


def get_language_dict() -> dict:
    lang_key = st.session_state["lang_key"]
    st.session_state["lang_dict"] = TEXTS[lang_key]["home_page"]
    return TEXTS[lang_key]["home_page"]


def init_streamlit_session():
    if "lang_key" not in st.session_state:
        st.session_state["lang_key"] = "it"


def set_language():
    # Questa funzione viene chiamata quando la lingua viene cambiata
    if st.session_state["language_selector"] == "Italiano":
        st.session_state["lang_key"] = "it"
    else:
        st.session_state["lang_key"] = "en"
    _ = get_language_dict()


def set_sidebar():
    with st.sidebar:
        change_language()
        st.divider()

