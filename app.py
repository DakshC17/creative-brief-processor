import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from components.result_card import render_result_card
from components.status_banner import show_error, show_success
from services.webhook import WebhookError, send_request
from utils.constants import (
    APP_SUBTITLE,
    APP_TITLE,
    BUTTON_LABEL,
    SPINNER_TEXT,
    TEXT_AREA_PLACEHOLDER,
)

_env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(_env_path, override=True)

if not os.getenv("N8N_WEBHOOK_URL"):
    for line in _env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ[key.strip()] = value.strip()

st.set_page_config(page_title=APP_TITLE, layout="wide")
st.title(APP_TITLE)
st.subheader(APP_SUBTITLE)

user_input = st.text_area(
    label="Enter your creative request",
    height=180,
    placeholder=TEXT_AREA_PLACEHOLDER,
)

if st.button(BUTTON_LABEL, use_container_width=True):
    if not user_input.strip():
        st.warning("Please enter a request before processing.")
        st.stop()

    webhook_url = os.getenv("N8N_WEBHOOK_URL", "")
    if not webhook_url:
        st.error("N8N_WEBHOOK_URL is not configured. Add it to your .env file.")
        st.stop()

    status_holder = st.empty()
    status_holder.info("Status: Processing...")

    try:
        with st.spinner(SPINNER_TEXT):
            data = send_request(webhook_url, user_input)

        status_holder.empty()
        show_success()
        render_result_card(data, user_input)

    except WebhookError as exc:
        status_holder.empty()
        show_error(exc.message)
