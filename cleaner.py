# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:37:10 2025

@author: NobertTurihohabwe
"""

import streamlit as st
import pandas as pd
import numpy as np
import functions as fx

st.subheader('My data cleaning app')


file = st.file_uploader("Select a file", type='xlsx')

if file is not None:

    data = pd.read_excel(file)
    
    df = fx.Clean(data)
    
    st.write(df.shape)
    st.write(df.head())
    
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        #Show Loan Amount
        amount = df['Loan_amount'].sum()
        st.metric('The loan amount is:', amount)
    
    with col2:
        #Show Number of Loans
        number = df['Borrower_ID'].count()
        st.metric('Number of loans is:', number)
    
    with col3:
        #Show Number of youths
        mask = df['Age']<=35
        youths = df[mask]['Borrower_ID'].count()
        st.metric('Number of youths is:', youths)
    
    
    with col1:
        #Show Number of Loans
        mask = df['Gender']== 'Female'
        women = df[mask]['Borrower_ID'].count()
        st.metric('Number of women is:', women)
    
    
    with col2:
        #Show Number of Young women
        mask = (df['Gender']== 'Female') & (df['Age']<=35)
        youngwomen = df[mask]['Borrower_ID'].count()
        st.metric('Number of young women is:', youngwomen)
    
    
    with col3:
        #Show Interest rate
        rate = round(df['Interest_rate'].mean(),2)
        st.metric('average interest rate is:', rate)
        
        
    
    df.to_excel("data.xlsx", index = False)
    
     #Add button to Download Data
    st.download_button(
         label= 'Click to Download data',
         data= df.to_csv(index = False), # Convert DataFrame to Excel data
         file_name= 'Clean data.csv',  # Set file name
    )