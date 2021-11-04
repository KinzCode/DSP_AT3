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


serie = df['BookieMatchNo']
test = serie[np.isfinite(serie)]

num = src.numeric.NumericColumn("Test", serie)
num.get_histogram()

x = num.histogram

