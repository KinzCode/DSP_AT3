import streamlit as st
import pandas as pd
import numpy as np
import src
from dataclasses import dataclass

# @dataclass
# class StreamlitApp(src.text.Text_Column, src.numeric.NumericColumn,
#                    src.data.Dataset, src.datetime.DateColumn)





def data_logic(df, file_name):
    # Render overall information heading
    overall_information = st.header('Overall Information')
    # instantiate data class
    data_inst = src.data.Dataset(file_name, df)
    # get name and render
    data_inst.get_name()
    #file_name_str = data_inst.name
    file_name = st.write(f'**Name of Table:** {data_inst.name}')
    # get number of rows and render
    data_inst.get_n_rows()
    number_rows = st.write(f'**Number of Rows:** {data_inst.rows}')
    # get number of columns and render
    data_inst.get_n_cols()
    number_cols = st.write(f'**Number of Columns:** {data_inst.cols}')
    # get number of duplicated rows and render
    data_inst.get_n_duplicates()
    number_duplicates = st.write(f'**Number of Duplicates:** {data_inst.duplicate}')
    # get number of missing rows and render
    data_inst.get_n_missing()
    number_missing = st.write(f'**Number of Duplicates:** {data_inst.missing}')
    # get list of columns and render
    data_inst.get_cols_list()
    cols_list_heading = st.write(f'**List of Columns:**')
    cols_list_str = st.write(data_inst.cols_list)
    # get cols dtype and render as table
    data_inst.get_cols_dtype()
    dtype_df = pd.DataFrame([data_inst.dataTypeDict]).T
    dtype_df.rename(columns = {0: 'Value'}, inplace = True)
    cols_dtype_df = st.dataframe(data=dtype_df)
    # render slider
    slider = st.slider("Select the number of rows to be displayed",
                       min_value=5,
                       max_value = 50,
                       value = 5)
    # get head_df and render based on slider's values
    data_inst.get_head(slider)
    head_df = st.dataframe(data = data_inst.head)
    
    # get taiL_df and render based on slider's values
    data_inst.get_tail(slider)
    tail_df = st.dataframe(data = data_inst.tail)
    
    # get sample_df and render based on slider's values
    data_inst.get_sample(slider)
    sample_df = st.dataframe(data = data_inst.sample)

    # user mutli select box to choose which text columns converted to datetime
    data_inst.get_text_columns()
    text_columns = data_inst.text_col
    select_box = st.multiselect('Which columns do you want to convert to dates', text_columns)
    
    # get numerical_cols
    data_inst.get_numeric_columns()
    numerical_columns = data_inst.num_col
    return text_columns, numerical_columns
    
    
def numeric_logic(df, numerical_columns):
    for col in df[numerical_columns]:
        numeric_inst = src.numeric.NumericColumn(col, df[col])
        # create subtitle of column name
        numeric_inst.get_name()
        numeric_subtitle = st.subheader(numeric_inst.name)
        # create numeric info
        numeric_inst.get_unique()
        numeric_inst.get_missing()
        numeric_inst.get_zeros()
        numeric_inst.get_negatives()
        numeric_inst.get_mean()
        numeric_inst.get_std()
        numeric_inst.get_min()
        numeric_inst.get_max()
        numeric_inst.get_median()
 
        # create dictionary with labels and values
        col_dict = {'Number of Unique Values':numeric_inst.unique,
                    'Number of Rows with Missing Values': numeric_inst.missing,
                    'Number of Rows with 0': numeric_inst.zeros,
                    'Number of rows with Negative Values': numeric_inst.negatives,
                    'Average Value': numeric_inst.mean,
                    'Standard Deviation Value': numeric_inst.std,
                    'Minimum Value': numeric_inst.min,
                    'Maximuim Value': numeric_inst.max,
                    'Median Value': numeric_inst.median
            }
        
        # parse dict to df and render
        numeric_frame = pd.DataFrame([col_dict]).T
        numeric_frame.rename(columns = {0: 'Value'}, inplace = True)
        numeric_frame_df = st.dataframe(data=numeric_frame)
        # create histogram and render
        numeric_inst.get_histogram()
        numeric_histogram = numeric_inst.histogram
        
        # create dictionary with labels and values
        numeric_inst.get_frequent()
        numeric_inst.frequencie


def text_logic(df, text_columns):
    for col in df[text_columns]:
        text_inst = src.numeric.NumericColumn(col, df[col])
        # get name and render
        text_inst.get_name()
        text_subtitle = st.subheader(text_inst.get_name())
        
        # create text info
        text_inst.get_unique()
        text_inst.get_missing()
        text_inst.get_empty()
        text_inst.get_whitespace()
        text_inst.get_lowercase()
        text_inst.get_uppercase()
        text_inst.get_alphabet()
        text_inst.get_digit()
        text_inst.get_mode()
        
        # create dictionary with labels and values
        col_dict = {'Number of Unique Values': text_inst.unique,
                    'Number of Rows with Missing Values': text_inst.missing,
                    'Number of Empty Rows': text_inst.empty,
                    'Number of Rows with Only Whitespace': text_inst.white,
                    'Number of Rows with Only Lowercases': text_inst.lower,
                    'Number of Rows with Only Uppercases': text_inst.upper,
                    'Number of Rows with Only Alphabet': text_inst.alpha,
                    'Number of Rows with only Digits': text_inst.digit,
                    'Mode Value': text_inst.mode
                    }
        # parse dict to df and render
        text_frame = pd.DataFrame([col_dict]).T
        text_frame.rename(columns = {0: 'Value'}, inplace = True)
        text_frame_df = st.dataframe(data=text_frame)
        
        # plot and render bar chart
        text_inst.get_barchar()
        text_barchart = text_inst.barchart
        
        # get frequencies and render
        text_inst.get_frequent()
        text_frequency = st.dataframe(date = text_inst.frequent)
    return    


def datetime_logic(df):
    # https://stackoverflow.com/questions/17465045/can-pandas-automatically-read-dates-from-a-csv-file
    # loop over dates
    #st.subheader('Information on Dates')
    #date_column = st.write(df)
    for col in df:
        #date_class = src.datetime.DateColumn(col, df)
        subheader = st.subheader(f'Information on {col}')
    return





# # Display Title "Data Explorer Tool"
# St.title('Data Explorer Tool')

# # File uploader
# st.file_uploader('Choose a CSV file')

# # Display header called “Overall Information”
# st.header('1.Overall Information')

# # Display subheader called “Name of Table”
# st.subheader('Name of Table:')

# # Display subheader called “Number of Rows”
# st.subheader('Number of Rows:')

# # Display subheader called “Number of Columns”
# st.subheader('Number of Columns:')

# # Display subheader called “Number of Duplicated Rows”
# st.subheader('Number of Duplicated Rows:')

# # Display subheader called “Number of Rows with Missing Values”
# st.subheader('Number of Rows with Missing Values:')

# # Display subheader called “List of Columns”
# st.subheader('List of Columns:')

# # Display subheader called “Type of Columns”
# st.subheader('Type of Columns:')

# # Display Slider for selecting number of rows to be displayed
# st.slider('Select the number of rows to be displayed',0,50,5 )

# # Display subheader called “Top Rows of Table”
# st.subheader('Top Rows of Table:')

# # Display subheader called “Bottom Rows of Table”
# st.subheader('Bottom Rows of Table:')

# # Display subheader called “Random Sample Rows of Table”
# st.subheader('Random Sample Rows of Table:')

# # Display a multi select box for choosing which text columns will be converted to datetime
# st.multiselect('Which columns do you want to convert to dates', [])

# # Display header called “Numeric Column Information”
# st.header('2.Numeric Column Information')

# # Display name of column as subtitle
# st.subheader(2.0 Field Name:)\n st.subtitle()


# def convert_object_datetime(df):
#     df = df.apply(lambda col: pd.to_datetime(col, errors='ignore') 
#                   if col.dtypes == object 
#                   else col, 
#                   axis=0)
#     return df

def run():
    # web app heading
    st.title('CSV Explorer')
    # upload csv widget - must only accept CSV
    uploaded_file = st.file_uploader("Upload CSV", ['csv'])
    # create logic to forward application
    if uploaded_file is not None:
        # ensure to parse dates as datetime
        df = pd.read_csv(uploaded_file, parse_dates = True)
        # convert object to datetime
        #df = convert_object_datetime(df)
        
        # Apply data_logic here
        text_columns, numerical_columns = data_logic(df, uploaded_file.name)
        
        # Apply text_logic here
        numeric_logic(df, numerical_columns)
        
        # Apply text_logic here
        text_logic(df, text_columns)
        
        # create dateframe
        # date_df = df.select_dtypes(include=[np.datetime64])
        # # Apply datetime_logic here
        # datetime_logic(date_df)



        # Apply
        

    

if __name__ == '__main__':
    run()
    