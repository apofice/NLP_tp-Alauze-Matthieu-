# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 16:57:36 2022

@author: matth
"""

#streamlit

#!pip install streamlit

#import prediction
import streamlit as st
import pandas as pd
import numpy as np
from prediction import *

# Presentation de l'application

st.title('Application : RevieWAnalyzer')

monlabel = "Quel texte analyser ? "
options = pd.DataFrame(['Avis dataset', 'Texte libre'])

n_topics=st.number_input(label= "Le nombre de topics", min_value=0, max_value=15)

if st.button(label = "Détecter le sujet d'insatisfaction") == True:
    prediction(extractionPkl()[0],extractionPkl()[1],n_topics,text)[2]


with st.sidebar:
        st.radio(monlabel, options)
        st.text_input(label="Donnez nous votre avis")

#!streamlit run C:\matthieu\I3\tpNLP\jalon3.py

