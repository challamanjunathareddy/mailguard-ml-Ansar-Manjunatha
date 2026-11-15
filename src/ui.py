"""Shared presentation helpers for the Streamlit pages."""

from __future__ import annotations

import streamlit as st


def page_header(eyebrow: str, title: str, description: str, byline: str | None = None) -> None:
    with st.container(key="mg-page-hero"):
        st.markdown(f'<div class="mg-page-eyebrow">{eyebrow}</div>', unsafe_allow_html=True)
        st.title(title)
        if byline:
            st.markdown(
                f'<div class="mg-page-byline"><span class="mg-byline-dot"></span>{byline}</div>',
                unsafe_allow_html=True,
            )
        st.markdown(f'<div class="mg-page-description">{description}</div>', unsafe_allow_html=True)
