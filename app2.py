import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Pick a Finger 💖", page_icon="👉")

# ---------------- SESSION STATE ----------------
if "show_result" not in st.session_state:
    st.session_state.show_result = False

# ---------------- iOS STYLE ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f0f14, #1a1a25);
}

/* Glass container */
.block-container {
    max-width: 420px;
    margin: auto;
    padding: 25px;

    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    border-radius: 20px;

    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}

/* Inputs */
.stTextInput>div>div>input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 12px;
    height: 48px;
    color: #f5f3ff !important;
    transition: 0.2s;
}

/* Focus glow */
.stTextInput>div>div>input:focus {
    border: 1px solid #a78bfa !important;
    box-shadow: 0 0 10px rgba(167,139,250,0.4);
}

/* Button center */
.stButton {
    display: flex;
    justify-content: center;
}

/* Button */
.stButton>button {
    background: linear-gradient(135deg, #ff4da6, #7c3aed);
    color: white;
    border-radius: 14px;
    height: 3em;
    width: 220px;
    font-size: 16px;
    transition: all 0.15s ease;
}

/* Tap effect */
.stButton>button:active {
    transform: scale(0.96);
}

/* Hover */
.stButton>button:hover {
    box-shadow: 0 8px 25px rgba(124,58,237,0.4);
}

/* Fade animation */
.fade {
    animation: fadeIn 0.6s ease;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(10px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Result text */
.result {
    text-align: center;
    font-size: 26px;
    color: #f5f3ff;
    margin-top: 30px;
}

.subtitle {
    text-align: center;
    color: #c4b5fd;
    margin-bottom: 20px;
}

.title {
    text-align: center;
    font-size: 34px;
    font-weight: 600;
    color: #f5f3ff;
}

</style>
""", unsafe_allow_html=True)

# =========================
# INPUT SCREEN
# =========================
if not st.session_state.show_result:

    st.markdown("<div class='title'>👉 Pick a Finger 💖</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Let Aarushii choose for you</div>", unsafe_allow_html=True)

    option1 = st.text_input("Index Finger")
    option2 = st.text_input("Small Finger")

    if st.button("✨ Pick for me ✨"):

        if option1.strip() == "" or option2.strip() == "":
            st.warning("Please enter both options 💌")

        else:
            st.session_state.choice = random.choice([1, 2])
            st.session_state.option1 = option1
            st.session_state.option2 = option2
            st.session_state.show_result = True
            st.rerun()

# =========================
# RESULT SCREEN
# =========================
else:

    st.balloons()

    if st.session_state.choice == 1:
        st.markdown(
            f"<div class='result fade'>Aarush has selected Index Finger 💖</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<h3 style='text-align:center;'>{st.session_state.option1} 😋</h3>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='result fade'>Aarush has selected Small Finger 💕</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<h3 style='text-align:center;'>{st.session_state.option2} 😋</h3>",
            unsafe_allow_html=True
        )

    st.write("")

    if st.button("🔙 Go Back"):
        st.session_state.show_result = False
        st.rerun()