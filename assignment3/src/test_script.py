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


text_inst = src.text.TextColumn('cool', df['RedCorner'])
# text_inst.get_alphabet()

# print(text_inst.alpha)

text_inst.get_mode()
text_inst.mode
print(text_inst.mode)