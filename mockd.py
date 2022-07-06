# -*- coding: utf-8 -*-
"""MockD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UmwMwXA8vnbLEkC_Afmk9-RjED7jFy59
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

"""First step of the process

The very first step of EDA is Data Sourcing, we have seen how we can access data and load into the system.
"""

df=pd.read_csv('/content/MOCK_DATA.csv')
df.head()

df.describe()

df.info()

"""After completing the Data Sourcing, the next step in the process of EDA is Data Cleaning. It is very important to get rid of the irregularities and clean the data after sourcing it into the system."""

#we shall drop all the columns that are not relevant or important to the analysis
df.drop(["customer_id"], axis = 1, inplace=True)
df.drop(["id"], axis = 1, inplace=True)
df.drop(['email'],axis=1,inplace=True)

df.head()

df.dtypes

#df['income'].astype(str).astype(int)

# string to int
#pd.to_numeric(df['income'])

#df["income"] = df["income"].astype("int")
#df.dtypes

df.shape

def clean_currency(income):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(income, str):
        return(income.replace('$', '').replace(',', ''))
    return(income)

df['spending_per_month'] = df['spending_per_month'].str.replace(',','').str.replace('$','').astype('float')
df['loan_burden'] = df['loan_burden'].str.replace(',','').str.replace('$','').astype('float')

#df['income'] = df['income'].replace({'\$': '', ',': ''}, regex=True).astype(float)

df['income'].apply(type).value_counts()

df.dtypes

df.columns

df.index

df.isnull().sum()

df.duplicated().sum()

df.income.dtype

# string to int
#df['income'] = df['income'].astype('int')
#df.dtype

"""#trying to use a function that can be reused

This function here give you a general idea of the total and percentage of missing data in each column:
"""

def intitial_eda_checks(df):
    '''
    Takes df
    Checks nulls
    '''
    if df.isnull().sum().sum() > 0:
        mask_total = df.isnull().sum().sort_values(ascending=False) 
        total = mask_total[mask_total > 0]

        mask_percent = df.isnull().mean().sort_values(ascending=False) 
        percent = mask_percent[mask_percent > 0] 

        missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    
        print(f'Total and Percentage of NaN:\n {missing_data}')
    else: 
        print('No NaN found.')

intitial_eda_checks(df)

"""#With specification of the threshold of the missing value percentage, the 
#following function will give you a list of columns that have missing values over that threshold
"""



def view_columns_w_many_nans(df, missing_percent):
    '''
    Checks which columns have over specified percentage of missing values
    Takes df, missing percentage
    Returns columns as a list
    '''
    mask_percent = df.isnull().mean()
    series = mask_percent[mask_percent > missing_percent]
    columns = series.index.to_list()
    print(columns) 
    return columns

"""# Deciding  to drop the columns with too many missing values (over a certain threshold you specify), you can use this function to accomplish the task:"""

def drop_columns_w_many_nans(df, missing_percent):
    '''
    Takes df, missing percentage
    Drops the columns whose missing value is bigger than missing percentage
    Returns df
    '''
    series = view_columns_w_many_nans(df, missing_percent=missing_percent)
    list_of_cols = series.index.to_list()
    df.drop(columns=list_of_cols)
    print(list_of_cols)
    return df

df

df.isnull().sum()

df.duplicated().sum()

#unique values
 
df['income'].unique()

df['spending_per_month'].unique()

df['loan_burden'].unique()

df['major_purchases'].unique()

df.corr()

fig=df['loan_burden'].hist(bins=50)