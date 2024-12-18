import streamlit as st

st.set_page_config(page_icon="✨", layout="wide")
st.title("Segmented Control Widget")

with st.echo():
    options = ["North", "East", "South", "West"]
    selection = st.segmented_control("Directions", options, selection_mode="multi")
    st.markdown(f"Your selected options: {selection}.")

st.divider()

with st.echo():
    # Define a map of numbers to Material Design icons
    option_map = {
        0: ":material/add:",  # Option 0 shows this icon
        1: ":material/zoom_in:",  # Option 1 shows this icon
        2: ":material/zoom_out:",  # Option 2 shows this icon
        3: ":material/zoom_out_map:",  # Option 3 shows this icon
    }

    # Create a segmented control with numbers as options
    selection = st.segmented_control(
        "Tool",  # Label for the control
        options=option_map.keys(),  # Use the keys (0, 1, 2, 3) as options
        format_func=lambda x: option_map[x],  # Show icons instead of numbers
        selection_mode="single",  # Allow only one selection at a time
    )

    # Display the selected icon (or None if nothing is selected)
    st.write(
        "Your selected option: ", None if selection is None else option_map[selection]
    )
