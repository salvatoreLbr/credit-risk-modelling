import streamlit as st

from credit_risk_modelling.front_end.utils import (
    get_language,
    get_language_dict,
    set_sidebar
)


class Cmd:
    def __init__(self):
        self.lang_key: str = get_language()
        self.lang_dict: dict = get_language_dict()

    def show_sidebar():
        set_sidebar()

