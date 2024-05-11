'''
Function: EDA

Description: This function explore the dataset and it's characteristics

Developer: The Dadeline Doers

Date: 16 April,2024

'''

# import external libs
import numpy as np

def EDA(df):
    print("===== Shape =====")
    print(df.shape, end="\n\n")
    
    print('-'*80)

    print("===== Columns =====")
    print(df.columns, end="\n\n")
    
    print('-'*80)

    numerical_cols = df.select_dtypes(include=[np.number]).columns
    print("===== Numerical Columns =====")
    print(numerical_cols, end="\n\n")
    
    print('-'*80)

    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    print("===== Categorical Columns =====")
    print(categorical_cols, end="\n\n")
    
    print('-'*80)

    print("===== Info =====")
    print(df.info(), end="\n\n")
    
    print('-'*80)

    print("===== Description =====")
    print(df.describe(), end="\n\n")
    
    print('-'*80)

    print("===== Head =====")
    print(df.head(), end="\n\n")
    
    print('-'*80)

    print("===== Null values =====")
    print(df.isnull().sum(), end="\n\n")
