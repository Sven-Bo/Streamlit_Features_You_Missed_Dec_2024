import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="Welcome Page", page_icon="✨", layout="wide")

# Page title
st.title("5 New Streamlit Features You Might Have Missed!")
st.write(
    "Check out these features to learn something new and make your Streamlit apps even better!"
)


# Navigation buttons
st.subheader("Navigate to:")

if st.button("Material Icons"):
    st.switch_page("pages/1_Material_Icons.py")

if st.button("Segmented Control Widget"):
    st.switch_page("pages/2_Segmented_Control_Widget.py")

if st.button("Pills"):
    st.switch_page("pages/3_Pills.py")

if st.button("Tertiary Button"):
    st.switch_page("pages/4_Tertiary_Button.py")

if st.button("Custom CSS"):
    st.switch_page("pages/5_Custom_CSS.py")


# Add a social media section
st.subheader("Connect with Me:")
st.write(
    """
    - [Subscribe on YouTube](https://youtube.com/@codingisfun)
    - [Visit my Website](https://pythonandvba.com)
    - [Support Me on Ko-Fi](https://pythonandvba.com/coffee-donation)
    """
)
