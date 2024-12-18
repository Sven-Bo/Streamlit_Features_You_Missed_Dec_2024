import streamlit as st
import pathlib

st.set_page_config(page_icon="✨", layout="wide")
st.title("Custom CSS")

with st.expander("assets/styles.css"):
    st.image(pathlib.Path(__file__).parents[1] / "assets" / "demo_css.png")
    styles_css = """
        .st-key-green button {
            background-color: green;
        }

        /* Animated button with pulse effect */
        .st-key-pulse button {
            background-color: #4CAF50;
            border-radius: 10px;
            padding: 20px 60px;
            animation: pulse 2s infinite;
        }

        .st-key-pulse button p {
            font-size: 24px;
            font-family: 'Comic Sans MS', sans-serif;
        }

        /* Hover effect for the button */
        .st-key-pulse button:hover {
            background-color: #45a049; /* Darker green */
            border: none;
        }

        .st-key-pulse button:hover p {
            color: #FFD700; /* Gold color */
        }

        /* Override the focus states to prevent default red border */
        .st-key-pulse button:focus {
            background-color: #45a049; /* Keep the same as hover */
            border: none;
        }

        /* Apply the same text color during focus states */
        .st-key-pulse button:focus p {
            color: #FFD700;
        }


        @keyframes pulse {
            0% {
                box-shadow: 0 0 0 0 rgba(76, 175, 80, 0.7);
            }
            70% {
                box-shadow: 0 0 0 20px rgba(76, 175, 80, 0);
            }
            100% {
                box-shadow: 0 0 0 0 rgba(76, 175, 80, 0);
            }
        }
        """
    st.code(styles_css, language="css")

with st.echo():
    # Function to load CSS from the 'assets' folder
    def load_css(file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Load the external CSS
    css_path = pathlib.Path(__file__).parents[1] / "assets" / "styles.css"
    load_css(css_path)

    # Sytled Button
    st.header("Buttons")
    st.button("I'm a green button", key="green")
    if st.button("Full custom CSS tutorial", key="pulse"):
        st.link_button(
            label="check it out here...",
            url="https://youtu.be/jbJpAdGlKVY?si=EwEFkON1gN_Ux4hE",
        )
