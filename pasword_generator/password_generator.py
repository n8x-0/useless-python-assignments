import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Page Configuration
st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
        .main { text-align: center; }
        .stButton>button { background-color: #4CAF50; color: white; font-size: 16px; padding: 10px 20px; border-radius: 8px; }
        .stButton>button:hover { background-color: #45a049; }
        .stSlider .css-1aumxhk { color: #4CAF50; }
        .stCheckbox label { font-size: 16px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.markdown("<h1 style='text-align: center;'>Random Password Generator</h1>", unsafe_allow_html=True)

# Input Options
with st.container():
    length = st.slider("Select password length", min_value=6, max_value=32, value=12)
    col1, col2 = st.columns(2)
    with col1:
        use_digits = st.checkbox("Include digits")
    with col2:
        use_special = st.checkbox("Include special characters")

# Generate Button
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success("Generated Password:")
    st.code(password, language="text")
