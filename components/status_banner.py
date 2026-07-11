import streamlit as st

from utils.constants import DUPLICATE_WARNING


def show_duplicate_warning() -> None:
    st.warning(DUPLICATE_WARNING)


def show_error(message: str) -> None:
    st.error(message)


def show_success(message: str = "Brief processed successfully.") -> None:
    st.success(message)
