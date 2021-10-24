# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 20:48:50 2021

@author: KinzCode
"""
import pandas as pd
import numpy as np
from data import Dataset

#dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
df = pd.read_csv('pinnacle_odds_sample.csv')


# df = df.apply(lambda col: pd.to_datetime(col, errors='ignore') 
#               if col.dtypes == object 
#               else col, 
#               axis=0)

# date_df = df.select_dtypes(include=[np.datetime64])

data_inst = Dataset('cool', df)
data_inst.get_n_rows()
x = data_inst.name
rows = data_inst.rows

data_inst.get_cols_dtype()
new = data_inst.dataTypeDict

