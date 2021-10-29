# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:09:43 2021

@author: KinzCode
"""

import streamlit as st
import pandas as pd
import numpy as np
import src

df = pd.read_csv('pinnacle_odds_sample.csv')

data_inst = src.data.Dataset('pin', df)
# data_inst.get_text_columns()
# data_inst.get_numeric_columns()

# x = data_inst.text_col
# y = data_inst.num_col

# text_inst = src.text.TextColumn('BlueCorner', df['BlueCorner'])
# text_inst.get_mode()
# a = text_inst.mode

def convert_object_datetime(df):
    df = df.apply(lambda col: pd.to_datetime(col, errors='ignore') 
                  if col.dtypes == object 
                  else col, 
                  axis=0)
    return df

df = convert_object_datetime(df)

date_inst = src.datetime.DateColumn('pin', df['UploadTimeStamp'])
date_inst.get_unique()
date_inst.get_missing()
date_inst.get_weekend()
date_inst.get_weekday()
date_inst.get_future()
date_inst.get_empty_1900()
date_inst.get_empty_1970()
date_inst.get_min()
date_inst.get_max()

# create dictionary with labels and values
col_dict = {'Number of Unique Values': date_inst.unique,
            'Number of Rows with Missing Values': date_inst.missing,
            'Number of Weekend Dates': date_inst.weekend,
            'Number of Weekday Dates': date_inst.weekday,
            'Number of Dates in Future': date_inst.future,
            'Number of Rows with 1900-01-01': date_inst.empty_1900,
            'Number of Rows with 1970-01-01': date_inst.empty_1970,
            'Minimum Value': date_inst.min,
            'Maximum Value': date_inst.max
            }


# parse dict to df and render
date_frame = pd.DataFrame([col_dict]).transpose()
date_frame.rename(columns = {0: 'Value'}, inplace = True)