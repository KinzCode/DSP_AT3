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

# col = 'BookieMatchNo'


# numeric_inst = src.numeric.NumericColumn(col, df[col])
# numeric_inst.get_unique()
# numeric_inst.get_missing()
# numeric_inst.get_zeros()
# numeric_inst.get_negatives()
# numeric_inst.get_mean()
# numeric_inst.get_std()
# numeric_inst.get_min()
# numeric_inst.get_max()
# numeric_inst.get_median()
# ## create column headings list

# col_dict = {'Number of Unique Values':numeric_inst.unique,
#             'Number of Rows with Missing Values': numeric_inst.missing,
#             'Number of Rows with 0': numeric_inst.zeros,
#             'Number of rows with Negative Values': numeric_inst.negatives,
#             'Average Value': numeric_inst.mean,
#             'Standard Deviation Value': numeric_inst.std,
#             'Minimum Value': numeric_inst.min,
#             'Maximuim Value': numeric_inst.max,
#             'Median Value': numeric_inst.median
#     }


# # col_list = ['Number of Unique Values',
# #             'Number of Rows with Missing Values',
# #             'Number of Rows with 0',
# #             'Number of rows with Negative Values',
# #             'Average Value',
# #             'Standard Deviation Value',
# #             'Minimum Value',
# #             'Maximuim Value',
# #             'Median Value']
# # data_list = [numeric_inst.unique,
# #              numeric_inst.missing,
# #              numeric_inst.zeros,
# #              numeric_inst.negatives,
# #              numeric_inst.mean,
# #              numeric_inst.std,
# #              numeric_inst.min,
# #              numeric_inst.max,
# #              numeric_inst.median]

# numeric_frame = pd.DataFrame([col_dict]).T

hist_values = np.histogram(df['RedCornerOdds'],
                                bins=50,
                                range=(0,50)
                                )

z = pd.DataFrame(df['RedCornerOdds'].value_counts()).reset_index()
b = pd.DataFrame(df['RedCornerOdds'].value_counts(normalize = True)).reset_index()

z = z.merge(b, on = 'index', how = 'left')