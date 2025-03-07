import streamlit as st
import random
import string

def password_generator(length, digits, special_char):
    characters = string.ascii_letters  # Corrected 'ascli_letters' to 'ascii_letters'

    if digits:
        characters += string.digits  # Use += instead of == to add numbers

    if special_char:
        characters += string.punctuation  # Use 'string.punctuation' for special characters
    
    return "".join(random.choice(characters) for _ in range(length))



st.title("🔐 Password Generator App 🚀")

st.write("✨ Create strong passwords instantly with this simple tool! ✨")

Length = st.slider("📏 Select Your Password Length:", min_value=8, max_value=20, value=10)

Use_Digits = st.checkbox("🔢 Include Digits")
Use_Special_Characters = st.checkbox("🔣 Include Special Characters")


if st.button("🔄 Generate Password"):
    password = password_generator(Length, Use_Digits, Use_Special_Characters)
    st.success(f"✅ Your Secure Password: `{password}`")

st.write("🔒 Stay Secure! Developed with ❤️ by [**Muzna Amir**](https://github.com/MuznaZuberi)");
