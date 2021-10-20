import streamlit as st
import pandas as pd
import numpy as np
from numeric import NumericColumn
#from data import DataSet
#from datetime import DateColumn
from text import TextColumn



def data_logic(df):
    st.write(df)
    st.header('Overall Information')


def datetime_logic(df):
    # create df for only date coluns
    # date_df = df.select_dtypes(include=[np.datetime64])
    # loop over dates
    # for col in date_df:
    #     date_col = DateColumn(col, date_df[col])
    #     st.subheader(f'Information on {col}')
    return

def numeric_logic(df):
    return

def text_logic(df):
    return



def run():
    # web app heading
    st.title('CSV Explorer')
    # upload csv widget - must only accept CSV
    uploaded_file = st.file_uploader("Upload CSV", ['csv'])
    # create logic to forward application
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        # Apply data_logic here
        data_logic(df)
        # Apply numeric_logic here
        numeric_logic(df)
        # Apply text_logic here
        text_logic(df)
        # Apply datetime_logic here
        datetime_logic(df)
        # Apply
        

if __name__ == '__main__':
    run()
    