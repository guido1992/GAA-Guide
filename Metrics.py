# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:13:26 2021

@author: Alex
"""

# Metrics.py
import streamlit as st
def app():
    st.title('📊 Analysis Metrics')
    st.write('A page to find different metrics used in practice.')
    
    # 
    st.write("""
             #### Productivity in Gaelic Football
             
             This metric was developed by Ben McGuckin and Kevin McGuigan. It is a method
             of measuring possession effectiveness. 
             
             """)
     
    # 
    st.write("You can access the presentation via this [link](https://www.dropbox.com/s/ykauoerieiqqaii/Productivity%20in%20Gaelic%20football.pptx?dl=0).")
             
    # 
    st.write("""
            Furthermore, the following video is a great example of how to bring the
            'Productivity' score into a Nacsport dashboard.
            
            * https://www.youtube.com/watch?v=Y5aXAi6jRlc&ab_channel=AnalysisPro
             """)