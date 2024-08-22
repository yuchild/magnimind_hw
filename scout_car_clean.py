#!usr/bin/env Python3

import pandas as pd
import numpy as np

def clean_scout_car():
    
    # load data
    df_org = pd.read_json('./data/scout_car.json', lines=True)
    df = df_org.copy()

    
    # Replace special characters and spaces in column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r'[\s\n]+', '_', regex=True)
        .str.replace(r'[^a-z0-9_]', '', regex=True)
        .str.replace(r'_+', '_', regex=True)
    )


    # skip columns
    df.drop(['entertainment_media', 'safety_security', 'comfort_convenience', 'extras', 'kw'],axis=1,inplace=True)

    
    # fill nulls with 'none'
    df['short_description'].fillna('none', inplace=True)
    df['body_type'].fillna('none', inplace=True)
    df['vat'].fillna('none', inplace=True)
    df['prev_owner'].fillna('none',inplace=True)
    df['next_inspection'].fillna('none',inplace=True)
    
    # lower and/or underscore
    df['make_model'] = df['make_model'].str.lower().str.replace(' ', '_')
    df['body_type'] = df['body_type'].str.lower().str.replace(' ', '_').str.replace('-', '_')
    df['vat'] = df['vat'].str.lower().str.replace(' ', '_')
    df['prev_owner'] = df['prev_owner'].str.replace(' ', '_')


    # splits...
    # Split the 'registration' column into 'registration_month' and 'registration_year'
    df[['registration_month', 'registration_year']] = df['registration'].str.split('/', expand=True)
    
    # Replace invalid entries with 'none'
    df['registration_month'] = df['registration_month'].replace('-', 'none')
    df['registration_year'] = df['registration_year'].replace('-', 'none')


        



















if '__name__' == '__main__':
    ...