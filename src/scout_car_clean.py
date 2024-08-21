#!usr/bin/env Python3

import pandas as pd
import numpy as np

def clean_scout_car():
    # load json file 
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
    
    df_to_clean = df_to_clean = df.drop(['entertainment_media', 'safety_security', 'comfort_convenience', 'extras'],axis=1).copy()

    return ...
























if '__name__' == '__main__':
    ...