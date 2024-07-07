# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import numpy as np
import pandas as pd
import datetime
import xgboost as xgb

def main():
    html_temp="""
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black;text-align:centre;"> Car Price Prediction using Ml 
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.markdown("#### Are you planning to selling your car !? #### so lets try  evaluating the price ")
    
if __name__ == "__main__":
    main()