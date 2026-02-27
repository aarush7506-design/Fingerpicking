import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Pick a Finger 💖", page_icon="👉")

# ---------------- SESSION STATE ----------------
if "show_result" not in st.session_state:
    st.session_state.show_result = False

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #ffe6f0, #e6ccff);
    }
    .stButton>button {
        background-color: #ff99cc;
        color: white;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# =========================
# 🔹 INPUT SCREEN
# =========================
if not st.session_state.show_result:

    st.markdown(
        "<h1 style='text-align: center;'>👉 Pick a Finger 💖</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h4 style='text-align: center;'>Let Aarushii choose for you</h4>",
        unsafe_allow_html=True
    )

    st.write("")

    option1 = st.text_input("Index Finger")
    option2 = st.text_input("Small Finger")

    st.write("")

    if st.button("✨ Pick for me ✨"):

        if option1.strip() == "" or option2.strip() == "":
            st.warning("Please enter both options 💌")

        else:
            # Store result in session
            st.session_state.choice = random.choice([1, 2])
            st.session_state.option1 = option1
            st.session_state.option2 = option2

            st.session_state.show_result = True
            st.rerun()

# =========================
# 🔹 RESULT SCREEN
# =========================
else:

    st.balloons()

    if st.session_state.choice == 1:
        st.markdown(
            f"<h1 style='text-align: center; color: hotpink;'>Aarush has selected Index Finger 💖</h1>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<h2 style='text-align: center;'>{st.session_state.option1} 😋</h2>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<h1 style='text-align: center; color: violet;'>Aarush has selected Small Finger 💕</h1>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<h2 style='text-align: center;'>{st.session_state.option2} 😋</h2>",
            unsafe_allow_html=True
        )

    st.write("")
    
    if st.button("🔙 Go Back"):
        st.session_state.show_result = False
        st.rerun()