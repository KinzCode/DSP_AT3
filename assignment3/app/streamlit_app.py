import streamlit as st
import pandas as pd
import numpy as np
import src



def render_data_get_name(data_inst):
    """
    get name from DataSet class and render to app
    """
    # get name and render
    data_inst.get_name()
    file_name = st.write(f'**Name of Table:** {data_inst.name}')

def render_data_get_n_rows(data_inst):
    """ 
    get number of rows from Dataset class and render to app
    """
    # get number of rows and render
    data_inst.get_n_rows()
    number_rows = st.write(f'**Number of Rows:** {data_inst.rows}')
    
def render_data_get_n_cols(data_inst):
    """ 
    get number of columns from Dataset class and render to app
    """
    # get number of columns and render
    data_inst.get_n_cols()
    number_cols = st.write(f'**Number of Columns:** {data_inst.cols}')
    

def render_data_get_n_duplicates(data_inst):
    """ 
    get number of duplicated rows from Dataset class and render to app
    """
    # get number of duplicated rows and render
    data_inst.get_n_duplicates()
    number_duplicates = st.write(f'**Number of Duplicates:** {data_inst.duplicate}')

def render_data_get_n_missing(data_inst):
    """ 
    get number of rows with missing values from Dataset class and render to app
    """
    # get number of missing rows and render
    data_inst.get_n_missing()
    number_missing = st.write(f'**Number of Duplicates:** {data_inst.missing}')

def render_data_get_cols_list(data_inst):
    """ 
    get list of column names from Dataset class and render to app
    """
    # get list of columns and render
    data_inst.get_cols_list()
    cols_list_heading = st.write(f'**List of Columns:**')
    #data_inst.cols_list
    cols_list_str = st.write(', '.join(data_inst.cols_list))

def render_data_get_cols_dtype(data_inst):
    """ 
    get list of cols dtype from Dataset class and render to app
    """ 
    # get cols dtype and render as table
    cols_type_heading = st.write('**Type of Columns**')
    data_inst.get_cols_dtype()
    dtype_df = pd.DataFrame([data_inst.dataTypeDict]).T
    dtype_df.rename(columns = {0: 'Value'}, inplace = True)
    cols_dtype_df = st.dataframe(data=dtype_df)

def render_data_slider():
    """ 
    create & return slider object of min_value = 5 & max_value = 50 with
    default 5.
    """
    # render slider
    slider = st.slider("Select the number of rows to be displayed",
                        min_value=5,
                        max_value = 50,
                        value = 5)
    return slider
    
def render_data_get_head(data_inst, slider):
    """ 
    get head of df from Dataset class and render to app
    """
    top_rows_heading = st.write('**Top Rows of Table**')
    # get head_df and render based on slider's values
    data_inst.get_head(slider)
    head_df = st.dataframe(data = data_inst.head)

def render_data_get_tail(data_inst, slider):
    """ 
    get tail of df from Dataset class and render to app
    """
    bottom_rows_heading = st.write('**Bottom Rows of Table**')
    # get taiL_df and render based on slider's values
    data_inst.get_tail(slider)
    tail_df = st.dataframe(data = data_inst.tail)
    
    
def render_data_get_sample(data_inst, slider):
    """ 
    get random sample of df from Dataset class and render to app
    """
    random_rows_heading = st.write('**Random Sample Rows of Table**')
    # get sample_df and render based on slider's values
    data_inst.get_sample(slider)
    sample_df = st.dataframe(data = data_inst.sample)

def render_data_select_box(data_inst):
    """ 
    get text_col from Dataset class and render as multiselect box to app
    """
    # user mutli select box to choose which text columns converted to datetime
    data_inst.get_text_columns()
    text_columns = data_inst.text_col
    datetime_columns = st.multiselect('Which columns do you want to convert to dates', text_columns)
    return text_columns, datetime_columns
    
def data_logic(df, file_name):
    """ 
    Function holding the logic rendering data.py
    """
    # Render overall information heading
    overall_information = st.header('1. Overall Information')
    
    # instantiate data class
    data_inst = src.data.Dataset(file_name, df)
    
    # render components
    render_data_get_name(data_inst)
    render_data_get_n_rows(data_inst)
    render_data_get_n_cols(data_inst)
    render_data_get_n_duplicates(data_inst)
    render_data_get_n_missing(data_inst)
    render_data_get_cols_list(data_inst)
    render_data_get_cols_dtype(data_inst)
    
    # render & return slider
    slider = render_data_slider()
    
    # render head,tail,random
    render_data_get_head(data_inst, slider)
    render_data_get_tail(data_inst, slider)
    render_data_get_sample(data_inst, slider)

    #render select box and create text & datetime column lists
    text_columns, datetime_columns = render_data_select_box(data_inst)

    # get numerical_cols
    data_inst.get_numeric_columns()
    numerical_columns = data_inst.num_col
    
    return text_columns, numerical_columns, datetime_columns
    
    

def render_numeric_subtitle(numeric_inst, index):
    """ 
    get name from NumericColumn class and render to app
    """
    # create subtitle of column name
    numeric_inst.get_name()
    numeric_subtitle = st.subheader(f'2.{index} Field Name: {numeric_inst.name}')    

def render_numeric_information_df(numeric_inst):
    """ 
    get descriptive data from NumericColumn class and render to app
    """ 
    
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
 

def render_numeric_histogram(numeric_inst):
    """ 
    get histogram from NumericColumn class and render to app
    """
    numeric_histogram_heading = st.write('**Histogram**')
    # create histogram and render
    numeric_inst.get_histogram()
    numeric_histogram = numeric_inst.histogram


def render_numeric_frequency_table(numeric_inst):
    """ 
    get frequency df from NumericColumn class and render to app
    """
    numeric_frequency_heading = st.write('**Most Frequent Values**')
    # create dictionary with labels and values
    numeric_inst.get_frequent()
    numeric_frequency = st.dataframe(data = numeric_inst.frequency)
    

def numeric_logic(df, numerical_columns):
    for col in enumerate(df[numerical_columns]):
        # instnatiate NumericColumn class
        numeric_inst = src.numeric.NumericColumn(col[1], df[col[1]])
        
        # render subtitle
        render_numeric_subtitle(numeric_inst, col[0])
        # render information df
        render_numeric_information_df(numeric_inst)
        # render histogram
        render_numeric_histogram(numeric_inst)
        # render frequency df
        render_numeric_frequency_table(numeric_inst)


def render_text_subheader(text_inst, index):
    """ 
    get name from TextColumn class and render to app
    """
    # get name and render
    text_inst.get_name()
    text_subtitle = st.subheader(f'3.{index} Field Name: {text_inst.name}')

def render_text_information_df(text_inst):
    """ 
    get descriptive data from TextColumn class and render to app
    """
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
    
    # create provision for mode
    if len(text_inst.mode) > 1:
        text_inst.mode = "No singular value"
    
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
        

def render_text_barchart(text_inst):
    """ 
    get barchart from TextColumn class and render to app
    """
    text_barchart_heading = st.write('**Bar Chart**')
    # plot and render bar chart
    text_inst.get_barchart()
    text_barchart = text_inst.barchart
      
def render_text_frequency_df(text_inst):
    """ 
    get frequency df from TextColumn class and render to app
    """
    text_frequency_heading = st.write('**Most Frequent Values**')
    # get frequencies and render
    text_inst.get_frequent()
    text_frequency = st.dataframe(data = text_inst.frequency)
  
def text_logic(df, text_columns):
    """ 
    Need to include mode
    
    """
    for col in enumerate(df[text_columns]):
        # instantiate class
        text_inst = src.text.TextColumn(col[1], df[col[1]])
        # render subheading
        render_text_subheader(text_inst, col[0])
        # render text information df
        render_text_information_df(text_inst)
        # render text barchart
        render_text_barchart(text_inst)
        # render frequency df
        render_text_frequency_df(text_inst)
        
def render_datetime_subheading(date_inst, index):
    """ 
    get name from DateColumn class and render to app
    """
    date_inst.get_name()
    date_subheader = st.subheader(f'4.{index} Field Name: {date_inst.name}')
    
def render_datetime_information_df(date_inst):
    """ 
    get information df from DateColumn class and render to app
    """
    # create date info
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
    date_frame_df = st.dataframe(data=date_frame)

def render_datetime_barchart(date_inst):
    """ 
    get barchart from DateColumn class and render to app
    """
    # plot and render bar chart
    date_inst.get_barchart()
    date_barchart = date_inst.barchart
    
def render_datetime_frequency_df(date_inst):
    """ 
    get frequency df from DateColumn class and render to app
    """
    #get frequencies and render
    date_inst.get_frequent()
    date_frequency = st.dataframe(data = date_inst.frequency)

def convert_object_datetime(df):
    """ 
    Convert date objects to datetime format
    """
    df = df.apply(lambda col: pd.to_datetime(col, errors='ignore') 
                  if col.dtypes == object 
                  else col, 
                  axis=0)
    return df

def datetime_logic(df, datetime_columns):
    """
    INSERT DOCSTRING
    """
    #convert text date times to datetimes
    df = convert_object_datetime(df)
    
    for col in enumerate(df[datetime_columns]):
        date_inst = src.datetime.DateColumn(col[1], df[col[1]])
        # render datetime subheading
        render_datetime_subheading(date_inst, col[0])
        # render information df
        render_datetime_information_df(date_inst)
        # render datetime barchart
        render_datetime_barchart(date_inst)
        # render datetime frequency df
        render_datetime_frequency_df(date_inst)
     
def main():
    # web app heading
    st.title('Data Explorer Tool')
    # upload csv widget - must only accept CSV
    uploaded_file = st.file_uploader("Upload CSV", ['csv'])
    # create logic to forward application
    if uploaded_file is not None:
        # ensure to parse dates as datetime
        df = pd.read_csv(uploaded_file, parse_dates = True)
        
        # Apply data_logic here
        text_columns, numerical_columns, datetime_columns = data_logic(df, uploaded_file.name)
        # Apply text_logic here
        numeric_logic(df, numerical_columns)
        # Apply text_logic here
        text_logic(df, text_columns)
        #Apply datetime_logic here
        datetime_logic(df, datetime_columns)


if __name__ == '__main__':
    main()
    