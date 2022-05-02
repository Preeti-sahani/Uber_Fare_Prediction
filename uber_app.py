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


pickup_longitude = st.number_input("Pickup Longitude", key=1)
pickup_latitude = st.number_input("Pickup Latitude", key=2)
dropoff_longitude = st.number_input("Dropoff Longitude", key=3)
dropoff_latitude = st.number_input("Dropoff Latitude", key=4)
passenger_count = st.number_input("Passenger Count", key=5)
date = st.number_input("Date", key=6) 
month = st.number_input("Month", key=7)    
year = st.number_input("Year", key=8)      
day = st.number_input("Day", key=9)         
hour = st.number_input("Hour", key=10)

if st.button("Predict"):
    pred = str(lr.predict([[pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count, date, month, year, day, hour]]))
    st.success("Price_prediction : " + pred)
    
    
