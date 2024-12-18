import streamlit as st

st.set_page_config(page_icon="✨", layout="wide")
st.title("Tertiary Button")

with st.echo():
    if st.button("Primary Button", type="primary"):
        st.write("Ahoy")

    if st.button("Secondary Button", type="secondary"):
        st.write("Ahoy")

    if st.button("Tertiary Button", type="tertiary"):
        st.write("Ciao")
