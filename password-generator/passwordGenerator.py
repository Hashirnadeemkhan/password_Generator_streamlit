import streamlit as st  # Import Streamlit for creating the web-based UI
import random  # Import random for generating random choices
import string  # Import string to use predefined character sets

# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Includes uppercase and lowercase letters

    if use_digits:
        characters += string.digits  # Adds numbers (0-9) if selected

    if use_special:
        characters += string.punctuation  # Adds special characters (!@#$%^&* etc.) if selected

    # Generate a password by randomly selecting characters based on the length provided
    return "".join(random.choice(characters) for _ in range(length))

# Function to evaluate password strength
def check_password_strength(length, use_digits, use_special):
    if length < 6:
        return "Weak"
    elif length < 12 and use_digits and not use_special:
        return "Medium"
    elif length >= 12 and use_digits and use_special:
        return "Strong"
    elif length >= 12 and (use_digits or use_special):
        return "Good"
    else:
        return "Weak"  # Default for short passwords or no complexity

# Streamlit UI setup
st.title("Simple Password Generator")  # Display the app title on the web page

# User input: password length (slider to select length between 6 and 32 characters)
length = st.slider("Select password length:",  max_value=32, value=12)

# Checkbox options for including numbers and special characters in the password
use_digits = st.checkbox("Include numbers", value=True)  # Default checked for better UX
use_special = st.checkbox("Include special characters")  # Checkbox for special characters

# Button to generate password
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)  # Generate the password
    strength = check_password_strength(length, use_digits, use_special)  # Check its strength
    st.write(f"Generated Password: `{password}`")  # Display the generated password
    st.write(f"Password Strength: **{strength}**")  # Display strength feedback