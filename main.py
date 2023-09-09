import streamlit as st
import streamlit_option_menu as som
from streamlit_extras.let_it_rain import rain
from streamlit_extras.stylable_container import stylable_container
from streamlit_carousel import carousel
from streamlit.components.v1 import html

from pathlib import Path
from PIL import Image

import os

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)

# paths
current_dir = Path(__file__).parent
css_file = current_dir / "styles" / "styles.css"
resume_file = current_dir / "assets" / "resume.pdf"

project_screenshots = current_dir / "assets" / "project_screenshots"

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
PROJECTS = {
    "FIFA 2022 World Cup Simulator - Using Machine Learning to predict the winner of the 2022 FIFA World Cup!": "https://youtu.be/Sb0A9i6d320",
    "Penalty Kick Encroachment Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

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
    st.markdown("<center><h4>Projects</h4></center>", unsafe_allow_html=True)
    st.markdown("<center><p>Here are some of the projects I've worked on!</p></center>", unsafe_allow_html=True)

    # test_items = [
    #     dict(
    #         title=None,
    #         text=None,
    #         interval=None,
    #         img="https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4",
    #     ),
    #     dict(
    #         title="Slide 2",
    #         text="A wooden bridge in a forest in Autumn",
    #         img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
    #     ),
    #     dict(
    #         title="Slide 3",
    #         text="A distant mountain chain preceded by a sea",
    #         img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
    #     ),
    # ]

    # carousel(items=test_items, width=1)
    
        
    # project 1
    with st.expander("FIFA 2022 World Cup Simulator - Using Machine Learning to predict the winner of the 2022 FIFA World Cup."):
        st.markdown("<hr style='margin-bottom: 10px; padding: 0px;'><p style='font-size: 13px;'>Description</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 12px; color: darkgrey;'>The predictor model used is trained on a dataset (from kaggle) of all of football's historical international matches. We weighted the training data based on recency. The algorithm utilizes the random forest classifier, a series of interconnected decision trees for training. Additionally, the predicotr relies on a 1000x monte carlo method to incorporate randomness. With all these features, we created probabilities for each team in every fixture. In summary, the model predicted ~60% of games properly and had Brazil beating Belgium in the final to win the World Cup. </p>", unsafe_allow_html=True)
        
        st.markdown("<p style='font-size: 13px;'>Technologies Used</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 12px; color: darkgrey;'>Python, Pandas, Scikit-Learn, Matplotlib, Numpy, Jupyter Notebook</p>", unsafe_allow_html=True)

        wc_photo1 = Image.open(project_screenshots / "worldcup" / "wcpredictor1.png")
        st.image(wc_photo1, width=600, caption="An example of the monte carlo sim being run on a fixture")

        st.write('')
        
        st.button('View Project on Github', on_click=open_page, args=('https://github.com/AggieSportsAnalytics/WorldCupPredictor',), use_container_width=True, key="1")


    # project 2
    with st.expander("Penalty Kick Encroachment Tracker - An automated way to track encroachment during penalty kicks."):
        st.markdown("<hr style='margin-bottom: 10px; padding: 0px;'><p style='font-size: 13px;'>Description</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 12px; color: darkgrey;'>During soccer penalty kicks, there are two basic rules: the keeper cannot move off of his/her line and the non-penalty taker players musn't enter the box until the penalty taker kicks the ball. Referees regularly watch for the former, but the latter oftentimes goes unnoticed. This problem is the inspiration for this project. Such an autonomous tool could create a more authentic refereeing experience, also eliminating human error. This project utilizes computer vision to provide real-time player tracking (via You Only Look Once object detection/segmentation) and penalty box detection (via OpenCV contours and hough lines). Once everything is detected, an algorithm is employed verifying that the ball is kicked before any player enters the penalty box.</p>", unsafe_allow_html=True)
        
        st.markdown("<p style='font-size: 13px;'>Technologies Used</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 12px; color: darkgrey;'>Python, Numpy, OpenCV, YOLOv8, YOLO Segmentation, Jupyter Notebook</p>", unsafe_allow_html=True)

        pen_photo1 = Image.open(project_screenshots / "penaltykick" / "pen1.png")
        pen_photo2 = Image.open(project_screenshots / "penaltykick" / "pen2.png")
        pen_photo3 = Image.open(project_screenshots / "penaltykick" / "pen3.png")
        pen_photo4 = Image.open(project_screenshots / "penaltykick" / "pen4.png")

        col1, col2 = st.columns(2)
        with col1:
            st.image(pen_photo1, width=600, caption="Starting video", use_column_width=True)
            st.image(pen_photo3, width=600, caption="Applying finer player tracking (segmentation) and team color detection (rgb color above head)", use_column_width=True)
        with col2:
            st.image(pen_photo2, width=600, caption="Applying player tracking", use_column_width=True)
            st.image(pen_photo4, width=600, caption="Applying box detection", use_column_width=True)

        st.write('')
        
        st.button('View Project on Github', on_click=open_page, args=('https://github.com/AggieSportsAnalytics/PenaltyEncroachment',), use_container_width=True, key="2")

    # project 3
    with st.expander("Analyzing patient wait times in infusion center ABC - performing data cleanup of a dataset to analyze patient wait times and draw conclusions for customer improvement in an infusion center."):
        st.markdown("<hr style='margin-bottom: 10px; padding: 0px;'><p style='font-size: 13px;'>Description</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 12px; color: darkgrey;'>Infusion center ABC has been struggling with ever increasing patient wait times. They've sent a dataset representing their patient journey. I performed ETL on this data, cleaning it and preparing it for analysis. Start and end data can be found in the repository. After doing so, I performed quantitative analysis on the final data and created a presentation about my findings and conclusions. This presentation is found on the Github repository and can also be downloaded below. </p>", unsafe_allow_html=True)
        
        st.markdown("<p style='font-size: 13px;'>Technologies Used</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 12px; color: darkgrey;'>Python, Pandas, Matplotlib, Numpy, Seaborn, Jupyter Notebook</p>", unsafe_allow_html=True)

        infusion_photo1 = Image.open(project_screenshots / "infusioncenter" / "graph1.png")
        infusion_photo2 = Image.open(project_screenshots / "infusioncenter" / "graph2.png")
        
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(infusion_photo1, width=600, caption="Patient wait times by day of week")
        with col2:
            st.image(infusion_photo2, width=522, caption="Patient wait times by hour of day")

        st.markdown("<center><p style='font-size: 12px; color: darkgrey;'>Example of graphs I generated to help me perform statistical analysis</p>", unsafe_allow_html=True)

        st.write('')

        infusion_pdf = project_screenshots / "infusioncenter" / "QuantitativeAnalysisResultsPresentation.pdf"
        
        with open(infusion_pdf, "rb") as pdf_file:
            infusion_PDFbyte = pdf_file.read()
        
        st.download_button(
            label="Download Presentation",
            data=infusion_PDFbyte,
            file_name=infusion_pdf.name,
            mime="application/octet-stream",
            use_container_width=True
        )        


        
        st.button('View Project on Github', on_click=open_page, args=('https://github.com/soumil101/Infusion_Center_Analysis',), use_container_width=True, key="3")

    # project 4
    with st.expander("Project 4"):
        st.markdown("<hr style='margin-bottom: 10px; padding: 0px;'><p style='font-size: 13px;'>Description</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 12px; color: darkgrey;'> </p>", unsafe_allow_html=True)
        
        st.markdown("<p style='font-size: 13px;'>Technologies Used</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 12px; color: darkgrey;'>Python, Pandas, Scikit-Learn, Matplotlib, Numpy, Jupyter Notebook</p>", unsafe_allow_html=True)

        wc_photo1 = Image.open(project_screenshots / "worldcup" / "wcpredictor1.png")
        st.image(wc_photo1, width=600, caption="An example of the monte carlo sim being run on a fixture")

        st.write('')
        
        st.button('View Project on Github', on_click=open_page, args=('https://github.com/AggieSportsAnalytics/WorldCupPredictor',), use_container_width=True, key="4")

    # project 5
    with st.expander("Project 5"):
        st.markdown("<hr style='margin-bottom: 10px; padding: 0px;'><p style='font-size: 13px;'>Description</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 12px; color: darkgrey;'> </p>", unsafe_allow_html=True)
        
        st.markdown("<p style='font-size: 13px;'>Technologies Used</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 12px; color: darkgrey;'>Python, Pandas, Scikit-Learn, Matplotlib, Numpy, Jupyter Notebook</p>", unsafe_allow_html=True)

        wc_photo1 = Image.open(project_screenshots / "worldcup" / "wcpredictor1.png")
        st.image(wc_photo1, width=600, caption="An example of the monte carlo sim being run on a fixture")

        st.write('')
        
        st.button('View Project on Github', on_click=open_page, args=('https://github.com/AggieSportsAnalytics/WorldCupPredictor',), use_container_width=True, key="5")

    # project 6
    with st.expander("CryptoCheck - A fullstack application complete with an interactive dashboard to track cryptocurrency prices/news and a feature-full bot that can trade for you using various market strategies."):
        st.markdown('''<hr style='margin-bottom: 10px; padding: 0px;'><p style='font-size: 10px; color: lemonchiffon;'>This project is a work in progress!</p>''', unsafe_allow_html=True)
        st.markdown("<p style='font-size: 13px;'>Planned features</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 12px; color: darkgrey;'>User login</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 12px; color: darkgrey;'>Interactive and heavily customizable dashboard where users can quickly get the information THEY want</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 12px; color: darkgrey;'>A crypto trading bot that can be customized to trade based on many trading strategies, such as scalping, arbitrage, mean reversion, etc...</p>", unsafe_allow_html=True)
        
        st.markdown("<p style='font-size: 13px;'>Technologies Used</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 12px; color: darkgrey;'>HTML, CSS, JavaScript, React, PostgreSQL, Python, Numpy, CoinbasePro API/Websocket, Binance API, Docker, Figma</p>", unsafe_allow_html=True)

        cc_main = Image.open(project_screenshots / "cryptocheck" / "CryptoCheck.png")
        cc_light = Image.open(project_screenshots / "cryptocheck" / "CryptoCheckLight.png")
        cc_dark = Image.open(project_screenshots / "cryptocheck" / "CryptoCheckDark.png")


        st.image(cc_main, width=600, use_column_width=True)

        st.write('')
        
        st.button('Track our Progress Here', on_click=open_page, args=('https://github.com/soumil101/cryptocheck',), use_container_width=True, key="6", help="Visit CryptoCheck on Github")

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