import streamlit as st
import requests


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Enterprise AI Operations Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

API_URL = "http://127.0.0.1:8000/ask"


# ==================================================
# SESSION STATE
# ==================================================

if "history" not in st.session_state:
    st.session_state.history = []          # list of {"question": ..., "answer": ...}

if "pending_question" not in st.session_state:
    st.session_state.pending_question = ""


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    /* ---------- Global ---------- */
    .stApp {
        background: linear-gradient(180deg, #f9fafb 0%, #eef2ff 100%);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 760px;
    }

    /* Hide default streamlit chrome for a cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* ---------- Header ---------- */
    .header {
        text-align: center;
        padding: 1rem 0 2rem 0;
    }

    .header-icon {
        font-size: 3rem;
        margin-bottom: 0.25rem;
    }

    .header-title {
        font-size: 2.1rem;
        font-weight: 800;
        color: #111827;
        letter-spacing: -0.02em;
        margin-bottom: 0.35rem;
    }

    .header-subtitle {
        font-size: 1rem;
        color: #6b7280;
    }

    .header-badges {
        margin-top: 0.9rem;
        display: flex;
        justify-content: center;
        gap: 0.5rem;
        flex-wrap: wrap;
    }

    .badge {
        background: #eef2ff;
        color: #4338ca;
        border: 1px solid #e0e7ff;
        border-radius: 999px;
        padding: 0.25rem 0.75rem;
        font-size: 0.75rem;
        font-weight: 600;
    }

    /* ---------- Cards ---------- */
    .card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        padding: 1.5rem 1.5rem 1.25rem 1.5rem;
        margin-top: 1.25rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
    }

    .card-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: #374151;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }

    /* ---------- Answer card ---------- */
    .answer-card {
        background: #f5f8ff;
        border: 1px solid #dbeafe;
        border-radius: 18px;
        padding: 1.5rem;
        margin-top: 1.5rem;
    }

    .answer-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 0.85rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }

    .answer-question {
        font-size: 0.85rem;
        color: #6366f1;
        font-weight: 600;
        margin-bottom: 0.6rem;
    }

    .source {
        margin-top: 1.1rem;
        padding-top: 0.8rem;
        border-top: 1px solid #dbeafe;
        font-size: 0.8rem;
        color: #6b7280;
    }

    /* ---------- History ---------- */
    .history-item {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 1rem 1.15rem;
        margin-bottom: 0.75rem;
    }

    .history-q {
        font-weight: 700;
        color: #111827;
        font-size: 0.9rem;
        margin-bottom: 0.35rem;
    }

    .history-a {
        color: #4b5563;
        font-size: 0.87rem;
        line-height: 1.5;
    }

    /* ---------- Buttons ---------- */
    div.stButton > button {
        border-radius: 12px;
        font-weight: 700;
        padding: 0.65rem 0;
        border: none;
        background: linear-gradient(90deg, #4f46e5, #6366f1);
        color: white;
        transition: transform 0.05s ease-in-out, opacity 0.15s ease-in-out;
    }

    div.stButton > button:hover {
        opacity: 0.92;
    }

    div.stButton > button:active {
        transform: scale(0.99);
    }

    /* Secondary (example) buttons */
    .example-chip button {
        background: #f3f4f6 !important;
        color: #374151 !important;
        border: 1px solid #e5e7eb !important;
        font-weight: 500 !important;
        font-size: 0.8rem !important;
        padding: 0.4rem 0.9rem !important;
    }

    /* ---------- Footer ---------- */
    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 0.78rem;
        padding: 2.5rem 0 0.5rem 0;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ==================================================
# HEADER
# ==================================================

st.markdown(
    """
    <div class="header">
        <div class="header-icon">🤖</div>
        <div class="header-title">Enterprise AI Operations Assistant</div>
        <div class="header-subtitle">Ask anything about company HR policies and get instant, sourced answers</div>
        <div class="header-badges">
            <span class="badge">RAG-powered</span>
            <span class="badge">Live knowledge base</span>
            <span class="badge">Instant answers</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ==================================================
# QUESTION SECTION
# ==================================================

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">💬 Ask a question</div>', unsafe_allow_html=True)

question = st.text_area(
    "Question",
    value=st.session_state.pending_question,
    placeholder="Example: How many paid leave days are employees entitled to?",
    height=110,
    label_visibility="collapsed",
    key="question_input",
)

st.markdown("</div>", unsafe_allow_html=True)


# ==================================================
# EXAMPLE QUESTIONS (as clickable chips)
# ==================================================

st.markdown("<div style='margin-top: 1rem; font-size: 0.85rem; font-weight: 600; color: #374151;'>Try an example</div>", unsafe_allow_html=True)

example_questions = [
    "How many paid leave days are employees entitled to?",
    "What is the procedure for taking 5 days off?",
    "What should employees do for emergency leave?",
]

chip_cols = st.columns(len(example_questions))
for col, example in zip(chip_cols, example_questions):
    with col:
        st.markdown('<div class="example-chip">', unsafe_allow_html=True)
        if st.button(example, key=f"chip_{example}", use_container_width=True):
            st.session_state.pending_question = example
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)


# ==================================================
# ASK AI BUTTON
# ==================================================

st.write("")  # small spacer
ask_clicked = st.button("🚀  Ask AI", use_container_width=True)

if ask_clicked:

    current_question = question.strip()

    if not current_question:
        st.warning("Please enter a question first.")

    else:
        with st.spinner("Searching the knowledge base and generating an answer..."):

            try:
                response = requests.post(
                    API_URL,
                    json={"question": current_question},
                    timeout=60,
                )

                if response.status_code == 200:
                    result = response.json()
                    answer = result.get("answer", "No answer was returned.")

                    # Save to history (most recent first)
                    st.session_state.history.insert(
                        0, {"question": current_question, "answer": answer}
                    )
                    st.session_state.pending_question = ""

                else:
                    st.error(
                        f"The AI service returned an error (status {response.status_code}). "
                        "Please make sure FastAPI is running correctly."
                    )

            except requests.exceptions.ConnectionError:
                st.error(
                    "Could not connect to the FastAPI backend. "
                    f"Please make sure FastAPI is running on {API_URL}."
                )

            except requests.exceptions.Timeout:
                st.error("The request took too long. Please try again.")

            except Exception as error:
                st.error(f"Something went wrong: {error}")


# ==================================================
# LATEST ANSWER
# ==================================================

if st.session_state.history:

    latest = st.session_state.history[0]

    st.markdown('<div class="answer-card">', unsafe_allow_html=True)
    st.markdown('<div class="answer-title">✨ AI Response</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="answer-question">Q: {latest["question"]}</div>', unsafe_allow_html=True)

    st.write(latest["answer"])

    st.markdown(
        """
        <div class="source">📚 Powered by the enterprise HR knowledge base using RAG</div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)


# ==================================================
# HISTORY (previous Q&A, collapsed by default)
# ==================================================

if len(st.session_state.history) > 1:

    with st.expander(f"🕘 Previous questions ({len(st.session_state.history) - 1})"):
        for item in st.session_state.history[1:]:
            st.markdown(
                f"""
                <div class="history-item">
                    <div class="history-q">{item['question']}</div>
                    <div class="history-a">{item['answer']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    if st.button("🗑️ Clear history", use_container_width=True):
        st.session_state.history = []
        st.rerun()


# ==================================================
# FOOTER
# ==================================================

st.markdown(
    """
    <div class="footer">
        Enterprise AI Operations Assistant
        <br>
        Gemini • Pinecone • RAG • FastAPI
    </div>
    """,
    unsafe_allow_html=True,
)