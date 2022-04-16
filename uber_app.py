# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 02:26:52 2022

@author: sahan
"""

import streamlit as st
import pickle

infile = open('Uberfile', 'rb')
lr = pickle.load(infile)

st.header("Uber Price Prediciton")


pickup_longitude = st.text_input("Pickup Longitude", key=1)
pickup_latitude = st.text_input("Pickup Latitude", key=2)
dropoff_longitude = st.text_input("Dropoff Longitude", key=3)
dropoff_latitude = st.text_input("Dropoff Latitude", key=4)
passenger_count = st.text_input("Passenger Count", key=5)
date = st.text_input("Date", key=6) 
month = st.text_input("Month", key=7)    
year = st.text_input("Year", key=8)      
day = st.text_input("Day", key=9)         
hour = st.text_input("Hour", key=10)

#def pred():
#    output = lr.predict([pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count, date, month, day, hour])
#    st.write(output)
    
#st.button("Predict", on_click=pred())
#if st.button("Predict"):
#    result=pred(pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count, date, month, day, hour)

if st.button("Predict"):
    pred = str(lr.predict([[pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count, date, month, year, day, hour]]))
    st.success("Price_prediction : " + pred)