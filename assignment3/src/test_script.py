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
data_inst.get_text_columns()
data_inst.get_numeric_columns()

x = data_inst.text_col
y = data_inst.num_col

text_inst = src.text.TextColumn('BlueCorner', df['BlueCorner'])
text_inst.get_mode()
a = text_inst.mode