# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:50:11 2021

@author: Alex
"""

# GAA Guide Application.py
import Home
import Accreditation
import BlogPost
import AcademicResearch
import Conferences
import Videos
import AnalysisTools
import Visualisation
import Metrics
import Influencers

import streamlit as st

PAGES = {
    "🏠 Home": Home,
    "📜 Accreditation": Accreditation,
    "🏐 Blog Post": BlogPost,
    "🎓 Academic Research": AcademicResearch,
    "🎟️ Conferences": Conferences,
    "🏐 Videos": Videos,
    "💻 Video Analysis Tools": AnalysisTools,
    "📈 Data Visualisation": Visualisation,
    "📊 Metrics": Metrics,
    "🙌 Influencers": Influencers
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to for page for specific topic",
                             list(PAGES.keys()))
page = PAGES[selection]
page.app()

### Remove Streamlit footnote
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)