import streamlit as st
import streamlit_option_menu as som
from streamlit_extras.let_it_rain import rain
from streamlit_extras.stylable_container import stylable_container

from pathlib import Path
from PIL import Image

import os

# paths
current_dir = Path(__file__).parent
css_file = current_dir / "styles" / "styles.css"
resume_file = current_dir / "assets" / "resume.pdf"

profile_pic = current_dir / "assets" / "profile-pic-13.png"
professional_pic = current_dir / "assets" / "Professional_Photo.JPG"

photo_cats = ["landscapes", "miscellaneous", "bumi"]

# general settings
PAGE_TITLE = "Soumil Gad"
PAGE_ICON = "random"
NAME = "Soumil Gad"
DESCRIPTION = """
Junior at UC Davis studying Computer Science. Passionate about data science, machine learning, and software engineering. Likes taking photos in free time.
"""
EMAIL = "soumilgad03@gmail.com"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
professional_pic = Image.open(professional_pic)

st.markdown("<center><h1>Welcome to my website!</h1></center>", unsafe_allow_html=True)

selected = som.option_menu(
    menu_title=None,
    options=["Projects", "Home", "Photography"],
    icons=["folder", "house", "camera"],
    default_index=1,
    orientation="horizontal",
    styles={
        "container": {"padding": "0px", "margin": "0px", "background-color": "transparent"},
        "icon": {"color": "gold", "font-size": "25px", "display": "block", "margin-bottom": "0px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#586e75", "display": "block"},
        "nav-link-selected": {"background-color": "transparent"},
    }
)

if selected == "Home":
    col1, col2 = st.columns(2, gap="small")
    with col1:
        spacer, actual = st.columns(2)
        with actual:
            st.image(profile_pic, use_column_width=True)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)
        st.write("📍", "Cupertino, CA")

    st.divider()

    st.markdown('''
                <h3 align="center">Socials:</h3>
                <p align="center">
                <a href="https://linkedin.com/in/soumil-gad" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="soumil-gad" height="30" width="40" /></a>
                <a href="https://stackoverflow.com/users/22341476" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/stack-overflow.svg" alt="22341476" height="30" width="40" /></a>
                <a href="https://kaggle.com/soumil101" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="soumil101" height="30" width="40" /></a>
                <a href="https://fb.com/soumilgad" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="soumilgad" height="30" width="40" /></a>
                <a href="https://medium.com/@soumilgad" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/medium.svg" alt="@soumilgad" height="30" width="40" /></a>
                <a href="https://www.hackerrank.com/soumilgad" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/hackerrank.svg" alt="soumilgad" height="30" width="40" /></a>
                <a href="https://www.leetcode.com/soumil101" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/leet-code.svg" alt="soumil101" height="30" width="40" /></a>
                </p>
                ''', 
                unsafe_allow_html=True
        )

    st.markdown('''
                <h3 align="center">Technologies</h3>
                <p align="center">
                <a href="https://azure.microsoft.com/en-in/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" alt="azure" width="40" height="40"/></a> 
                <a href="https://www.cprogramming.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg" alt="c" width="40" height="40"/></a> 
                <a href="https://www.w3schools.com/cpp/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="cplusplus" width="40" height="40"/></a> 
                <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/></a> 
                <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/></a> 
                <a href="https://www.figma.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/figma/figma-icon.svg" alt="figma" width="40" height="40"/></a> 
                <a href="https://cloud.google.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" alt="gcp" width="40" height="40"/></a> 
                <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/></a> 
                <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/></a> 
                <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/></a> 
                <a href="https://kubernetes.io" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/kubernetes/kubernetes-icon.svg" alt="kubernetes" width="40" height="40"/></a> 
                <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/></a> 
                <a href="https://www.mathworks.com/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/Matlab_Logo.png" alt="matlab" width="40" height="40"/></a> 
                <a href="https://opencv.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="opencv" width="40" height="40"/></a> 
                <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/></a> 
                <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> 
                <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/></a> 
                <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a> 
                <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/></a> 
                <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/></a> 
                <a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="40" height="40"/></a> 
                </p>
                ''',
                unsafe_allow_html=True
        )

if selected == "Projects":
    st.title(f"{selected}")
    st.write('Work in Progress!')

if selected == "Photography":
    st.markdown("<center><h4>My Photo Gallery!</h4></center>", unsafe_allow_html=True)
    st.markdown("<left><p>One of the things I enjoy in my free time is photography. Although I love photography, I enjoy the editing aspect more! This is why I haven't actually upgrade from shooting on my phone yet. All photos captured on iPhone 13 Pro. Edited on Lightroom / Photomator.</p></left>", unsafe_allow_html=True)
    selected = som.option_menu(
        menu_title=None,
        options=["Landscapes", "Miscellaneous", "Bumi"],
        icons=["mountain", "random", "dog"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0px", "margin": "0px", "background-color": "transparent"},
            "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#586e75", "display": "block"},
            "nav-link-selected": {"color": "gray", "background-color": "#F5EFC4"},
        }
    )

    # selected = st.selectbox(
    #     label="Select a category",
    #     options=["Landscapes", "Miscellaneous", "Bumi"],
    #     index=0,
    #     help="Choose a category to display",
    # )

    if selected == "Landscapes":
        '''If you can't tell, I really love shooting the sky'''
        path = f"pictures/{selected.lower()}"
        photo_number = 0
        photos = []
        # write a for loop to iterate through all the photoes in the folder pictures and assign them a variable photo_number
        for filename in os.listdir(path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                photo_number += 1
                photo = Image.open(os.path.join(path, filename))
                photos.append(photo)
        # create a column layout with 3 columns
        col1, col2, col3 = st.columns(3)
        # iterate through the photos list and display each photo in a column
        for i in range(photo_number):
            if i % 3 == 0:
                with col1:
                    st.image(photos[i], use_column_width=True)
            elif i % 3 == 1:
                with col2:
                    st.image(photos[i], use_column_width=True)
            else:
                with col3:
                    st.image(photos[i], use_column_width=True)

    if selected == "Miscellaneous":
        st.markdown("<center><p>Couldn't really classify these</p></center>", unsafe_allow_html=True)
        path = f"pictures/{selected.lower()}"
        photo_number = 0
        photos = []
        # write a for loop to iterate through all the photoes in the folder pictures and assign them a variable photo_number
        for filename in os.listdir(path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                photo_number += 1
                photo = Image.open(os.path.join(path, filename))
                photos.append(photo)
        # create a column layout with 3 columns
        col1, col2, col3 = st.columns(3)
        # iterate through the photos list and display each photo in a column
        for i in range(photo_number):
            if i % 3 == 0:
                with col1:
                    st.image(photos[i], use_column_width=True)
            elif i % 3 == 1:
                with col2:
                    st.image(photos[i], use_column_width=True)
            else:
                with col3:
                    st.image(photos[i], use_column_width=True)

    if selected == "Bumi":
        st.markdown("<p style='text-align: right;'>My brother's dog, Bumi, is the best model</p>", unsafe_allow_html=True)
        path = f"pictures/{selected.lower()}"
        photo_number = 0
        photos = []
        # write a for loop to iterate through all the photoes in the folder pictures and assign them a variable photo_number
        for filename in os.listdir(path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                photo_number += 1
                photo = Image.open(os.path.join(path, filename))
                photos.append(photo)
        # create a column layout with 3 columns
        col1, col2, col3 = st.columns(3)
        # iterate through the photos list and display each photo in a column
        for i in range(photo_number):
            if i % 3 == 0:
                with col1:
                    st.image(photos[i], use_column_width=True)
            elif i % 3 == 1:
                with col2:
                    st.image(photos[i], use_column_width=True)
            else:
                with col3:
                    st.image(photos[i], use_column_width=True)

    # if selected:
    #     path = f"pictures/{selected.lower()}"
    #     photo_number = 0
    #     photos = []
    #     # write a for loop to iterate through all the photoes in the folder pictures and assign them a variable photo_number
    #     for filename in os.listdir(path):
    #         if filename.endswith(".jpg") or filename.endswith(".png"):
    #             photo_number += 1
    #             photo = Image.open(os.path.join(path, filename))
    #             photos.append(photo)
    #     # create a column layout with 3 columns
    #     col1, col2, col3 = st.columns(3)
    #     # iterate through the photos list and display each photo in a column
    #     for i in range(photo_number):
    #         if i % 3 == 0:
    #             with col1:
    #                 st.image(photos[i], use_column_width=True)
    #         elif i % 3 == 1:
    #             with col2:
    #                 st.image(photos[i], use_column_width=True)
    #         else:
    #             with col3:
    #                 st.image(photos[i], use_column_width=True)