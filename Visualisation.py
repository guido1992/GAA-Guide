# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:12:34 2021

@author: Alex
"""

# Visualisation.py
import streamlit as st
def app():
    st.title('📈 Data Visualisation')
    st.write('A page to find information about data visualisation ideas and techniques')
    
    # Paragraph
    st.write("""
             Data visualization has become essential in the business world and I would argue 
             the same if not more so applies to sports. Especially the ability to quickly 
             identif data trends, which would otherwise be a hassle. The pictorial 
             representation of data sets allows analysts to visualize concepts and new patterns. 
             It also ensures that a coach/manager/selector understands patterns and trends that
             are occuring in play.
             
             With the increasing surge in data every day, making sense of the quintillion bytes 
             of data on offer is virtually impossible without data visualisation. Every team
             benefits greatly from understanding their data, so data visualization is branching 
             out to all fields where data exists. For every manager/team, information is their 
             most significant leverage. Through visualization, one can prolifically convey 
             their points and take advantage of that information.
             
             The next question is - how do I present this information?
             
             A dashboard, graph, infographics, map, chart, video, slide, etc? All of these 
             mediums can be used for visualizing and understanding data. Visualizing the data
             enables decision-makers to interrelate the data to find better insights and reap 
             the importance of data visualisation.
             
             Below I have given two examples of blog posts which capture this information reall
             well.
             """)
             
    # Line break
    st.write("""
             """)
             
    # Text
    st.write("""
             ##### Interview Q&A with Johnny Bradley - Data creation, manipulation and visualisation
             
             * https://www.crowdcast.io/e/interview-qa-with-johnny-bradley/register
             """)
    
    # Line break
    st.write("""
             """)
    
    # Text
    st.write("""
             ##### Getting the most out of your performance analysis data - Integrating Nacsport with Tableau
             
             * https://www.crowdcast.io/e/integrating-nacsport-with-tableau/register
             """)
             
    # Line break
    st.write("""
             """)
             
    # Sub header
    st.subheader("""
                 Data Visualisation Tools
                 """)
                 
    # Tools
    st.write("""
             - Tableau
             - Power BI
             - Google Looker
             - Qlik
             - Python
             - R
             """)