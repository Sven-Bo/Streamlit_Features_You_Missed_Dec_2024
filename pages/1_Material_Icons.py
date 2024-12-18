import streamlit as st


st.set_page_config(page_icon="✨", layout="wide")
st.title("Using material icons and emojis")
st.subheader("https://fonts.google.com/icons")

with st.echo():
    st.markdown(
        "You can use google materials icons, e.g. in markdown: :material/table_convert:"
    )
    st.button("Click me", icon="😮")
