import streamlit as st
import streamlit_option_menu as som

from pathlib import Path
from PIL import Image

# paths
current_dir = Path(__file__).parent
css_file = current_dir / "styles" / "style.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
professional_pic = current_dir / "assets" / "Professional_Photo.JPG"


st.set_page_config(page_title="Soumil Gad", page_icon="smiley", layout="wide")


selected = som.option_menu(
    menu_title=None,
    options=["Projects", "Home", "Photography"],
    icons=["folder", "house", "camera"],
    default_index=1,
    orientation="horizontal",
    styles={
        "container": {"padding": "0px", "margin": "0px", "background-color": "#fafafa"},
        "icon": {"color": "gold", "font-size": "25px", "display": "block", "margin-bottom": "0px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#eee", "display": "block"},
        "nav-link-selected": {"background-color": "peach"},
    }
)

if selected == "Home":
    st.title(f"{selected}")

if selected == "Projects":
    st.title(f"{selected}")
    st.write('Work in Progress!')

if selected == "Photography":
    st.title(f"{selected}")
    st.write('Work in Progress!')