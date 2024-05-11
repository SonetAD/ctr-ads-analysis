
'''
Title- main file

Description: This is the main file that run all external functions and create the arguments for them like dataframe and so on.

Developer: Team Deadline Doers

Date: 15 April,2024
'''

#import external libs
import pandas as pd
from yaspin import yaspin

# import custom functions
from eda import EDA
from graph import draw_graph
from train_model import train_model

# Load the data set

chunk_size=1000

chunks=[]

target_col='label'
inp_col='his_app_size'

with yaspin(text='Reading Dataset...',color='yellow'):
    for chunk in pd.read_csv('train_data.csv',chunksize=chunk_size,sep='|',usecols= lambda x: x in [target_col,inp_col]):
        chunks.append(chunk)


# Creatig dataframe

with yaspin(text='Creating Dataframe...',color='yellow'):
    df=pd.concat(chunks,ignore_index=True)


# eda
EDA(df)

# drawing graph
with yaspin(text='Drawing Graph...',color='yellow'):
    draw_graph(df, inp_col, target_col, "Click Through Rate based on App Size", {'Yes': 'blue', 'No': 'red'})


# train model


with yaspin(text='Training Model with Machine Learning...',color='yellow'):
    train_model(df,target_col,inp_col)





