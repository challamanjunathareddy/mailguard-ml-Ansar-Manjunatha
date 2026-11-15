"""MailGuard ML - Streamlit entry point.

Run locally:  streamlit run app.py
"""

from __future__ import annotations

import streamlit as st

st.set_page_config(page_title="MailGuard ML", page_icon=":material/shield:", layout="wide")

from src.app_resources import get_model_bundle, get_service  # noqa: E402

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(ellipse at 86% 0%, rgba(13, 148, 136, 0.07), transparent 34rem),
            #f5f8fa;
    }
    [data-testid="stHeader"] {
        background: rgba(245, 248, 250, 0.82);
    }
    [data-testid="stSidebar"] {
        background: #102a36;
        border-right: 1px solid rgba(255, 255, 255, 0.08);
    }
    [data-testid="stSidebar"] > div:first-child {
        background: transparent;
    }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"],
    [data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
        color: #b6c8cf;
    }
    [data-testid="stSidebar"] [data-testid="stNavigation"] {
        padding-top: 0.4rem;
    }
    [data-testid="stSidebar"] [data-testid="stSidebarNav"] {
        padding-top: 0;
    }
    [data-testid="stSidebar"] a {
        border-radius: 0.7rem;
    }
    [data-testid="stSidebar"] a[aria-current="page"] {
        background: rgba(45, 212, 191, 0.13);
        color: #5eead4;
    }
    .block-container {
        max-width: 1440px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    .mg-brand {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        margin: 0.35rem 0 1.15rem;
    }
    .mg-brand-mark {
        display: grid;
        width: 2.7rem;
        height: 2.7rem;
        place-items: center;
        border: 1px solid rgba(94, 234, 212, 0.32);
        border-radius: 0.85rem;
        background: rgba(45, 212, 191, 0.12);
        color: #5eead4;
        font-size: 1rem;
        font-weight: 800;
        letter-spacing: -0.06em;
    }
    .mg-brand-name {
        color: #f2f7f8;
        font-size: 1rem;
        font-weight: 750;
        letter-spacing: -0.02em;
    }
    .mg-brand-tagline {
        margin-top: 0.1rem;
        color: #8fa9b2;
        font-size: 0.62rem;
        font-weight: 700;
        letter-spacing: 0.13em;
    }
    .st-key-mg-page-hero {
        position: relative;
        isolation: isolate;
        overflow: hidden;
        margin: 0 0 1.6rem;
        padding: 1.4rem 1.6rem 1.45rem;
        border: 1px solid #e1eaed;
        border-radius: 1.1rem;
        background: linear-gradient(115deg, rgba(255, 255, 255, 0.98), rgba(237, 247, 246, 0.9));
        box-shadow: 0 8px 26px rgba(16, 42, 54, 0.045);
        animation: mg-hero-enter 420ms cubic-bezier(0.2, 0.8, 0.2, 1) both;
    }
    .st-key-mg-page-hero::before {
        position: absolute;
        z-index: -1;
        top: -5rem;
        right: -2rem;
        width: 18rem;
        height: 18rem;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(45, 212, 191, 0.13), transparent 68%);
        content: "";
        animation: mg-glow-drift 5s ease-in-out infinite alternate;
        pointer-events: none;
    }
    .st-key-mg-page-hero::after {
        position: absolute;
        top: 0;
        left: 1.6rem;
        width: 4.5rem;
        height: 3px;
        border-radius: 0 0 3px 3px;
        background: linear-gradient(90deg, #0f766e, #5eead4);
        content: "";
        transform-origin: left;
        animation: mg-accent-draw 380ms 100ms ease-out both;
        pointer-events: none;
    }
    .mg-page-eyebrow {
        position: relative;
        animation: mg-text-enter 320ms 60ms ease-out both;
        margin-bottom: 0.45rem;
        color: #0f766e;
        font-size: 0.68rem;
        font-weight: 800;
        letter-spacing: 0.15em;
    }
    .st-key-mg-page-hero h1 {
        position: relative;
        animation: mg-text-enter 360ms 90ms ease-out both;
        margin: 0;
        color: #142c38;
        font-size: clamp(1.7rem, 3vw, 2.25rem);
        font-weight: 760;
        letter-spacing: -0.045em;
        line-height: 1.12;
    }
    .mg-page-byline {
        position: relative;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        margin-top: 0.8rem;
        padding: 0.36rem 0.68rem;
        border: 1px solid rgba(15, 118, 110, 0.14);
        border-radius: 999px;
        background: rgba(15, 118, 110, 0.06);
        color: #365c60;
        font-size: 0.77rem;
        font-weight: 650;
        animation: mg-text-enter 380ms 140ms ease-out both;
    }
    .mg-byline-dot {
        width: 0.45rem;
        height: 0.45rem;
        border-radius: 50%;
        background: #0f9b8e;
        box-shadow: 0 0 0 0 rgba(15, 155, 142, 0.34);
        animation: mg-dot-pulse 1.5s 450ms ease-out infinite;
    }
    .mg-page-description {
        position: relative;
        max-width: 58rem;
        margin: 0.55rem 0 0;
        color: #5c707a;
        font-size: 0.94rem;
        line-height: 1.55;
        animation: mg-text-enter 380ms 180ms ease-out both;
    }
    @keyframes mg-hero-enter {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes mg-text-enter {
        from { opacity: 0; transform: translateY(7px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes mg-accent-draw {
        from { transform: scaleX(0); }
        to { transform: scaleX(1); }
    }
    @keyframes mg-glow-drift {
        from { transform: translate3d(0, 0, 0) scale(0.92); }
        to { transform: translate3d(-1.3rem, 1rem, 0) scale(1.08); }
    }
    @keyframes mg-dot-pulse {
        0% { box-shadow: 0 0 0 0 rgba(15, 155, 142, 0.34); }
        70%, 100% { box-shadow: 0 0 0 7px rgba(15, 155, 142, 0); }
    }
    @media (prefers-reduced-motion: reduce) {
        .st-key-mg-page-hero,
        .st-key-mg-page-hero::before,
        .st-key-mg-page-hero::after,
        .mg-page-eyebrow,
        .st-key-mg-page-hero h1,
        .mg-page-byline,
        .mg-page-description,
        .mg-byline-dot {
            animation: none;
        }
    }
    [data-testid="stMetric"] {
        padding: 1rem 1.1rem;
        border: 1px solid #e3ebee;
        border-radius: 0.9rem;
        background: rgba(255, 255, 255, 0.88);
        box-shadow: 0 4px 14px rgba(16, 42, 54, 0.035);
    }
    [data-testid="stMetricLabel"] {
        color: #637780;
        font-size: 0.8rem;
    }
    [data-testid="stMetricValue"] {
        color: #183541;
        font-weight: 720;
    }
    .stButton > button,
    [data-testid="stDownloadButton"] > button {
        border-radius: 0.7rem;
        font-weight: 650;
        transition: border-color 120ms ease, box-shadow 120ms ease, transform 120ms ease;
    }
    .stButton > button:hover,
    [data-testid="stDownloadButton"] > button:hover {
        border-color: #0f766e;
        box-shadow: 0 4px 12px rgba(15, 118, 110, 0.12);
        transform: translateY(-1px);
    }
    [data-testid="stTabs"] [role="tab"] {
        font-weight: 620;
    }
    [data-testid="stDataFrame"] {
        border: 1px solid #e3ebee;
        border-radius: 0.8rem;
        overflow: hidden;
    }
    hr {
        border-color: #e2eaed;
    }
    @media (max-width: 700px) {
        .block-container {
            padding: 1.2rem 1rem 2rem;
        }
        .st-key-mg-page-hero {
            padding: 1.15rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

pages = [
    st.Page("views/analyzer.py", title="Email Analyzer", icon=":material/mail:", default=True),
    st.Page("views/evaluation.py", title="Model Evaluation", icon=":material/analytics:"),
    st.Page("views/monitoring.py", title="Monitoring", icon=":material/monitor_heart:"),
    st.Page("views/model_info.py", title="Model Information", icon=":material/info:"),
]

get_service()  # warm up model + metrics store once per process
model, model_error = get_model_bundle()

with st.sidebar:
    st.markdown(
        '<div class="mg-brand"><div class="mg-brand-mark">MG</div>'
        '<div><div class="mg-brand-name">MailGuard</div>'
        '<div class="mg-brand-tagline">EMAIL INTELLIGENCE</div></div></div>',
        unsafe_allow_html=True,
    )
    st.caption("MODEL STATUS")
    if model is not None:
        st.success(f"Model ready: {model.display_name} v{model.version}", icon=":material/check_circle:")
    else:
        st.error("Model unavailable - see Model Information.", icon=":material/error:")
    st.divider()
    st.caption(
        "A spam-detection demo trained on the public SpamAssassin corpus. "
        "Emails are analysed in memory and are never stored or logged."
    )

st.navigation(pages).run()
