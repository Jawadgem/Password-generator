import streamlit as st
import random
import string

# Function to generate a password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Include all letters (a-z, A-Z)
    
    if use_digits:
        characters += string.digits  # Add numbers (0-9)

    if use_special:
        characters += string.punctuation  # Add special characters (!@#$%^&*)

    # Generate a random password
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Generator")

length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"✅ Generated Password: `{password}`")

st.write("-----")

# Footer
st.markdown("Build with 😉 by **Jawad Nasir**")
