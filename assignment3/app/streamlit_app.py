
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

# Display Title "Data Explorer Tool"
St.title('Data Explorer Tool')

# File uploader
st.file_uploader('Choose a CSV file')

# Display header called “Overall Information”
st.header('1.Overall Information')

# Display subheader called “Name of Table”
st.subheader('Name of Table:')

# Display subheader called “Number of Rows”
st.subheader('Number of Rows:')

# Display subheader called “Number of Columns”
st.subheader('Number of Columns:')

# Display subheader called “Number of Duplicated Rows”
st.subheader('Number of Duplicated Rows:')

# Display subheader called “Number of Rows with Missing Values”
st.subheader('Number of Rows with Missing Values:')

# Display subheader called “List of Columns”
st.subheader('List of Columns:')

# Display subheader called “Type of Columns”
st.subheader('Type of Columns:')

# Display Slider for selecting number of rows to be displayed
st.slider('Select the number of rows to be displayed',0,50,5 )

# Display subheader called “Top Rows of Table”
st.subheader('Top Rows of Table:')

# Display subheader called “Bottom Rows of Table”
st.subheader('Bottom Rows of Table:')

# Display subheader called “Random Sample Rows of Table”
st.subheader('Random Sample Rows of Table:')

# Display a multi select box for choosing which text columns will be converted to datetime
st.multiselect('Which columns do you want to convert to dates', [])

# Display header called “Numeric Column Information”
st.header('2.Numeric Column Information')

# Display name of column as subtitle
st.subheader(2.0 Field Name:)\n st.subtitle()


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
    