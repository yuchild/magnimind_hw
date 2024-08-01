#!usr/bin/env python3

import pandas as pd

"""


15- Create a crosstab between state and category showing amount pledged as the value.
Please refer to the following link for this practice:

https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/ksprojects.csv
"""


def pandas_1_7():
    url = 'https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/ksprojects.csv'
    # 1- How many rows of data are in the DataFrame?
    df = pd.read_csv(url)
    rows = df.shape[0]

    # 2- What are the names and data types of the columns?
    df_col_names = df.columns
    df_data_types = df.dtypes
    
    
    # 3- Do any of the columns contain null values?
    df_nulls = df.isnull().sum()
    
    # 4- Find all successful documentary projects and sort them by the amount pledged. Print the top 10 highest pledges.
    top_10 = df[(df['category'] == 'documentary') & (df['state'] == 'duccessful')].sort_values(by='pledged', ascending=False).head(10).copy()
    
    # 5- Create a new column named average_per_backer and set its value to the total amount pledged / number of backers.
    # df['average_per_backer'] = df['pledged'] / df['backers']
    # 6- What happened to the rows with 0 backers? How can this be dealt with?
    # can't divide by zero
    # 7- Drop all rows with 0 backers then repeat the previous exercise.
    
    df = df[df['backers'] > 0].copy()
    df['average_per_backer'] = df['pledged'] / df['backers']
    
    return print(f"Rows in df: {rows}\nColumn Names: {df_col_names}\nColumn Data Types: {df_col_names}\nNull Counts: {df_nulls}\nTop 10 Successful Documentary by Pledge $ Amount: {top_10}\nFor 6- Can't Divide by 0 Backers")


def pandas_8():
    """
    8- Create a DataFrame whose index is the first 10 letters of the alphabet and contains two more columns with first 10 prime numbers and the first 10 fibonacci numbers.
    """

    alphabet = list('abcdefghij')
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    df = pd.DataFrame({'Prime Numbers': prime_numbers,
                       'Fibonacci Numbers': fibonacci_numbers
                      }, index=alphabet
                     )

    return df



def pandas_9_10():
    """
    9- Merge these two DataFrames into a single DataFrame: nycflights13.
    Please use the following dataset for merging purposes:

    https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/flights.csv

    https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/airlines.csv


    flights = pd.read_csv('https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/flights.csv')
    airline = pd.read_csv('https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/airlines.csv')
    
    10- Are there any missing values in this DataFrame? If so, drop them.
    """
    
    flights = pd.read_csv('https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/flights.csv')
    airline = pd.read_csv('https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/airlines.csv')

    nycflights13 = pd.merge(flights, airline, on='carrier')
    nycflights13.dropna(inplace=True)
    
    return nycflights13

def pandas_11_14():
    """
    11- Merge these two DataFrames into a single DataFrame called census.
    Please use the following dataset for merging purposes:

    'https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/state-populations.csv'

    'https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/census-divisions.csv'


    12- Re-shape census so that one column contains all population measures, and another the year attributes.

    13- Group the data by year and summarize it.

    14- Group the data by region, division and year and summarize it.
    """

    state_pop = pd.read_csv('https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/state-populations.csv')
    census_div = pd.read_csv('https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/census-divisions.csv')

    census = pd.merge(state_pop, census_div, on='state')
    
    melted_df = pd.melt(census, id_vars=['state', 'region', 'division'], 
                    value_vars=['2010', '2011', '2012', '2013', '2014', '2015', '2016'],
                    var_name='year', value_name='population')
    
    yearly_population = melted_df.groupby('year').agg({'population': 'sum'}).reset_index()
    grouped_summary = melted_df.groupby(['region', 'division', 'year']).agg({'population': 'sum'}).reset_index()
    
    return print(f'Group Data by Year: {yearly_population}\nGroup Data by Region, Division, and Year: {grouped_summary}')


def pandas_15():
    """
    15- Create a crosstab between state and category showing amount pledged as the value.
    Please refer to the following link for this practice:

    https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/ksprojects.csv
    """
    
    df = pd.read_csv('https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/ksprojects.csv')
    crosstab_df = pd.crosstab(index=df['state'], columns=df['category'], values=df['pledged'], aggfunc='sum', dropna=False)
    
    return print(f'Crosstab: {crosstab_df}')
    
    
    

if __name__ == "__main__":
    pandas_1_7()
    pandas_8()
    pandas_9_10()
    pandas_11_14()
    pandas_15()
    
    
    
    
    
    
    
    