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


serie = df['BlueCornerOdds']

n = 5
x = df['BlueCornerOdds'].value_counts().loc[lambda x: np.cumsum(x) < 20]