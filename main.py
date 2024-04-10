import streamlit as st
import pandas as pd 
import numpy as np

path = './car_data.csv'
car_data = pd.read_csv(path)
filtered_data = car_data


# Codes for Filtering conditions  
# 1.a) tect box
car_name = st.sidebar.text_input("Input the car_name you want to lookup")

with st.sidebar:
    # 1.b) multiselect 
    options = st.multiselect(
        'Manual and/or Automatic?',
        ['Manual', 'Automatic']
        )
    option_list =[]
    idx = len(options)

    # 1.c ~ 1.d) sliders 
    selling_price = st.slider('selling_price',0,20, (5,10)) 
    year = st.slider('year',2000,2024, (2001, 2003)) 

    # produce filtered car data 
    car_name , options, selling_price, year
    if len(car_name)>0:
        filtered_data = filtered_data[ filtered_data['Car_Name'] == car_name ] 
    if len(options)>0: 
        filtered_data = filtered_data[ filtered_data['Transmission'].isin(options) ] 
    if len(selling_price)>0: 
        filtered_data = filtered_data[ (filtered_data['Selling_Price'] >= selling_price[0]) & (filtered_data['Selling_Price'] <= selling_price[1]) ]
    if len(year)>2000 : 
        filtered_data = filtered_data[ (filtered_data['Year'] >= year[0]) & (filtered_data['Year'] <= year[1]) ] 


    # 1.e) submit button 
    submit = st.button("SUBMIT")
    

if submit : 
    st.dataframe(filtered_data)
else : 
    st.dataframe(car_data)

