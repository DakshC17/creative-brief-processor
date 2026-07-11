import streamlit as st

from utils.constants import PRIORITY_COLORS

_SKIP_KEYS = {"Timestamp", "timestamp", "Original Request", "original_request"}


def render_result_card(data: dict, original_request: str) -> None:
    st.markdown("---")
    st.subheader("Structured Brief")

    display_items = [(k, v) for k, v in data.items() if k not in _SKIP_KEYS]

    mid = (len(display_items) + 1) // 2
    left_items = display_items[:mid]
    right_items = display_items[mid:]

    col1, col2 = st.columns(2)

    with col1:
        for key, value in left_items:
            _render_field(key, value)

    with col2:
        for key, value in right_items:
            _render_field(key, value)

    st.markdown("---")
    with st.expander("Original Request"):
        st.write(original_request)


def _render_field(key: str, value) -> None:
    label = str(key)
    val_str = str(value) if value is not None else "—"

    if label.lower() == "priority":
        color = PRIORITY_COLORS.get(val_str, "#6c757d")
        st.markdown(
            f"**{label}**  "
            f"<span style='background-color:{color};color:white;"
            f"padding:2px 10px;border-radius:4px;font-size:0.85rem'>"
            f"{val_str}</span>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(f"**{label}:** {val_str}")
