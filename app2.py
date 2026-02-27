import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Pick a Finger 💖", page_icon="👉")

# ---------------- RESULT PLACEHOLDER (TOP) ----------------
result_container = st.empty()

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

# ---------------- TITLE ----------------
st.markdown(
    "<h1 style='text-align: center;'>👉 Pick a Finger 💖</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align: center;'>Let Aarushii choose for you</h4>",
    unsafe_allow_html=True
)

st.write("")

# ---------------- INPUT ----------------
option1 = st.text_input("Index Finger")
option2 = st.text_input("Small Finger")

st.write("")

# ---------------- BUTTON ----------------
if st.button("✨ Pick for me ✨"):

    if option1.strip() == "" or option2.strip() == "":
        st.warning("Please enter both options 💌")

    else:
        choice = random.choice([1, 2])

        st.balloons()

        # ---------------- SHOW RESULT AT TOP ----------------
        with result_container:
            if choice == 1:
                st.markdown(
                    f"<h2 style='text-align: center; color: hotpink;'>Aarush has selected Index Finger 💖</h2>",
                    unsafe_allow_html=True
                )
                st.markdown(
                    f"<h3 style='text-align: center;'>{option1} 😋</h3>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"<h2 style='text-align: center; color: violet;'>Aarush has selected Small Finger 💕</h2>",
                    unsafe_allow_html=True
                )
                st.markdown(
                    f"<h3 style='text-align: center;'>{option2} 😋</h3>",
                    unsafe_allow_html=True
                )