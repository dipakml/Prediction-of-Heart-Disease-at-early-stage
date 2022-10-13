# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 02:20:31 2020

@author: Dipak Argade
"""

# -*- coding: utf-8 -*-
"""
Created on 05/05/2022

@Created by: DA
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

pickle_in = open("sv.pkl","rb")
sv=pickle.load(pickle_in)  

def predict(Age,Sex,RestingBP,Cholesterol,FastingBS,MaxHR,ExerciseAngina,Oldpeak,ChestPainType_ATA,ChestPainType_NAP,ChestPainType_TA,RestingECG_Normal,RestingECG_ST,ST_Slope_Flat,ST_Slope_Up):
   
    prediction=sv.predict([[Age,Sex,RestingBP,Cholesterol,FastingBS,MaxHR,ExerciseAngina,Oldpeak, ChestPainType_ATA,ChestPainType_NAP,ChestPainType_TA,RestingECG_Normal,RestingECG_ST,ST_Slope_Flat,ST_Slope_Up]])
    print(prediction)
    return prediction



def main():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Heart Disease Prediction </h2>
    </div>
    """
    
    
    header_container = st.container()    
    with header_container:
	# for example a logo or a image that looks like a website header
        st.image('img2.png')
        
   
    
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.number_input("Enter Age between 28 to 77")
    Sex = st.selectbox("Sex",("Male","Female"))
    if Sex =='Male':
        Sex = 1
    else:
        Sex = 0
    RestingBP	 = st.number_input("Enter RestingBP between 80 to 200")
    Cholesterol	 = st.number_input("Enter Cholesterol between 0 to 603")

    FastingBS	 = st.number_input("Enter FastingBS 0 or 1")
    MaxHR	 = st.number_input("Enter MaxHR between 60 to 202")
    ExerciseAngina = st.selectbox("ExerciseAngina",("N","Y"))
    if ExerciseAngina =='Y':
        ExerciseAngina = 1
    else:
        ExerciseAngina = 0
    Oldpeak	 = st.number_input("Enter Oldpeak between -2.6 to 6.2")
    ChestPainType = st.sidebar.selectbox("ChestPainType",("ATA","NAP","ASY","TA"))
    if ChestPainType == 'ATA':
        ChestPainType_ATA = 1
        ChestPainType_NAP = 0
        ChestPainType_TA = 0
    elif ChestPainType == 'NAP':
        ChestPainType_ATA = 0
        ChestPainType_NAP = 1
        ChestPainType_TA = 0
    else:
        ChestPainType_ATA = 0
        ChestPainType_NAP = 0
        ChestPainType_TA = 0
    RestingECG	 = st.sidebar.selectbox("RestingECG",("Normal","ST","LVH"))
    if RestingECG == 'Normal':
        RestingECG_Normal = 1
        RestingECG_ST = 0
    elif RestingECG == 'ST':
        RestingECG_Normal = 0
        RestingECG_ST = 1
    else:
        RestingECG_Normal = 0
        RestingECG_ST = 0
    
    ST_Slope	 = st.sidebar.selectbox("ST Slope",("Up","Flat","Down"))
    if ST_Slope == 'Up':
        ST_Slope_Flat = 0
        ST_Slope_Up = 1
    elif ST_Slope == 'Flat':
        ST_Slope_Flat = 1
        ST_Slope_Up = 0
    else:
        ST_Slope_Flat = 0
        ST_Slope_Up = 0
    
    result=""
    if st.button("Predict"):
        result=predict(Age,Sex,RestingBP,Cholesterol,FastingBS,MaxHR,ExerciseAngina,Oldpeak,
            ChestPainType_ATA,ChestPainType_NAP,ChestPainType_TA,RestingECG_Normal,RestingECG_ST,ST_Slope_Flat,ST_Slope_Up)
        if result ==1:
            return st.header('Heart Disease predicted')
        else:
            return st.header('No Heart Disease')
if __name__=='__main__':
    main()
    
    
    