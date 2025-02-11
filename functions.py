# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:32:58 2025

@author: NobertTurihohabwe
"""
import pandas as pd

def Clean(data):
    data.drop(columns = ['id'], inplace = True)
    data['name_of_borrower'] = data['name_of_borrower'].str.title()
    data['email_of_borrower'] = data['email_of_borrower'].fillna('No_Email')
    data['highest_education_level'] = data['highest_education_level'].fillna('Not_Available')
    data['employment_status'] = data['employment_status'].str.replace('Self-employed','Self_Employed')
    data['Gender'] = data['Gender'].str.replace(' ','')
    data['Loan_amount'] = data['Loan_amount'].str.replace(' ','').str.replace(',','')
    data['Loan_amount'] = pd.to_numeric(data['Loan_amount'])
    data['Loan_amount'] = data['Loan_amount'].astype(int)
    data['Date_of_loan_issue'] = pd.to_datetime(data['Date_of_loan_issue'])
    data['Date_of_repayments_commencement'] = pd.to_datetime(data['Date_of_repayments_commencement'])
    data['Tenure_of_loan'] = round(pd.to_numeric(data['Tenure_of_loan'].str.replace('days',''))/30, 0)
    data['Interest_rate'] = data['Interest_rate']/100
    data['Loan_type'] = data['Loan_type'].str.replace(' ','')
    data['Loan_term_value'] = 'Months'
    data['Location_of_borrower'] = data['Location_of_borrower'].str.title()
    data['Expected_monthly_installment'] = pd.to_numeric(data['Expected_monthly_installment'].str.replace(',','')).astype(int)
    data = data.drop(columns = ['created'])
    data['Length_of_time_running'] = data['Date_of_loan_issue'] - pd.to_datetime(data['Length_of_time_running'], format = 'mixed', errors = 'coerce')
    data['Length_of_time_running'] = (data['Length_of_time_running'].dt.days//365).astype('Int64')
    data['Person_with_disabilities'] = data['Person_with_disabilities'].str.replace('false','No').str.replace(' ','')

    #Create a new column "Activity" that joins Loan putrpose and Line of Business
    data['Activity'] = data['Loan_purpose'] + data['Line_of_business']
    
    # Create a dictionary of sectors and their key words
    sector_keywords = {
        'Enterprise': ['business'],  
        'Agriculture': ['agri', 'GROWING'],
        'Transport':['BODA BODA']
        # Add more sectors and their associated keywords as needed
    }
    
    # Create a new column 'sector' and initialize with 'None'
    data['Sector'] = 'None'
    
    # Iterate over each row in the DataFrame
    for belz, harris in data.iterrows():
        andrew = harris['Activity']
        
        # Check for each sector's keywords in the 'line_of_business' column
        for a, b in sector_keywords.items():
            for bright in b:
                if bright in andrew:
                    data.at[belz, 'Sector'] = a
                    break # Exit the loop once a sector is identified for the current row


    # Define your Districts and corresponding keywords
    district_keywords = {
        'Kabale': ['kabale'],
        'Rukiga': ['rukiga'],
        'Ntungamo': ['ntungamo']
        # Add more districts and their associated keywords as needed
    }
    
    # Create a new column 'district' and initialize with 'None'
    data['District'] = 'None'
    
    # Iterate over each row in the DataFrame
    for index, row in data.iterrows():
        location = row['Location_of_borrower'].lower()
        # Iterate over each row in the DataFrame
        for district, loc in district_keywords.items():
            for a in loc:
                if a in location:
                    data.at[index, 'District'] = district
                    break# Exit the loop once a sector is identified for the current row


    # Define your Regions and corresponding keywords
    region_keywords = {
        'South Western': ['kabale','rukiga','ntungamo'],
        'Western': ['mbarara']
        # Add more districts and their associated keywords as needed
    }
     
    # Create a new column 'region' and initialize with 'None'
    data['Region'] = 'None'
     
    # Iterate over each row in the DataFrame
    for index, row in data.iterrows():
        location = row['District'].lower()
        # Iterate over each row in the DataFrame
        for region, loc in region_keywords.items():
            for a in loc:
                if a in location:
                    data.at[index, 'Region'] = region
                    break# Exit the loop once a sector is identified for the current row
                    
    return data