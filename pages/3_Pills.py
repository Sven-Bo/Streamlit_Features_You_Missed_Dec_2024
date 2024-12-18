import streamlit as st

st.set_page_config(page_icon="✨", layout="wide")
st.title("Pills")

with st.echo():
    options = ["North", "East", "South", "West"]
    selection = st.pills("Directions", options, selection_mode="multi")
    st.markdown(f"Your selected options: {selection}.")
