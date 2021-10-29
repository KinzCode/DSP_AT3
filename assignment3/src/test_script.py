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

for col in df:
    print(enumerate(col)[0])

# data_inst = src.data.Dataset('pin', df)
# # data_inst.get_text_columns()
# # data_inst.get_numeric_columns()

# # x = data_inst.text_col
# # y = data_inst.num_col

# # text_inst = src.text.TextColumn('BlueCorner', df['BlueCorner'])
# # text_inst.get_mode()
# # a = text_inst.mode

# def convert_object_datetime(df):
#     df = df.apply(lambda col: pd.to_datetime(col, errors='ignore') 
#                   if col.dtypes == object 
#                   else col, 
#                   axis=0)
#     return df

# df = convert_object_datetime(df)

# date_inst = src.datetime.DateColumn('pin', df['UploadTimeStamp'])
# date_inst.get_unique()
# date_inst.get_missing()
# date_inst.get_weekend()
# date_inst.get_weekday()
# date_inst.get_future()
# date_inst.get_empty_1900()
# date_inst.get_empty_1970()
# date_inst.get_min()
# date_inst.get_max()

# # create dictionary with labels and values
# col_dict = {'Number of Unique Values': date_inst.unique,
#             'Number of Rows with Missing Values': date_inst.missing,
#             'Number of Weekend Dates': date_inst.weekend,
#             'Number of Weekday Dates': date_inst.weekday,
#             'Number of Dates in Future': date_inst.future,
#             'Number of Rows with 1900-01-01': date_inst.empty_1900,
#             'Number of Rows with 1970-01-01': date_inst.empty_1970,
#             'Minimum Value': date_inst.min,
#             'Maximum Value': date_inst.max
#             }


# # parse dict to df and render
# date_frame = pd.DataFrame([col_dict]).transpose()
# date_frame.rename(columns = {0: 'Value'}, inplace = True)



# @dataclass
# class StreamlitApp(src.text.TextColumn, src.numeric.NumericColumn,src.data.Dataset, src.datetime.DateColumn):
        
#     def data_logic(self, df, file_name):
#         # Render overall information heading
#         overall_information = st.header('Overall Information')
#         # instantiate data class
#         data_inst = src.data.Dataset(file_name, self.df)
#         # get name and render
#         data_inst.get_name()
#         #file_name_str = data_inst.name
#         file_name = st.write(f'**Name of Table:** {data_inst.data_name}')
#             # get number of rows and render
#             # data_inst.get_n_rows()
#             # number_rows = st.write(f'**Number of Rows:** {data_inst.rows}')
#             # # get number of columns and render
#             # data_inst.get_n_cols()
#             # number_cols = st.write(f'**Number of Columns:** {data_inst.cols}')
#             # get number of duplicated rows and render
#             # data_inst.get_n_duplicates()
#             # number_duplicates = st.write(f'**Number of Duplicates:** {data_inst.duplicate}')
#             # # get number of missing rows and render
#             # data_inst.get_n_missing()
#             # number_missing = st.write(f'**Number of Duplicates:** {data_inst.missing}')
#             # # get list of columns and render
#             # data_inst.get_cols_list()
#             # cols_list_heading = st.write(f'**List of Columns:**')
#             # cols_list_str = st.write(data_inst.cols_list)
#             # # get cols dtype and render as table
#             # data_inst.get_cols_dtype()
#             # dtype_df = pd.DataFrame([data_inst.dataTypeDict]).T
#             # dtype_df.rename(columns = {0: 'Value'}, inplace = True)
#             # cols_dtype_df = st.dataframe(data=dtype_df)
#             # # render slider
#             # slider = st.slider("Select the number of rows to be displayed",
#             #                     min_value=5,
#             #                     max_value = 50,
#             #                     value = 5)
#             # # get head_df and render based on slider's values
#             # data_inst.get_head(slider)
#             # head_df = st.dataframe(data = data_inst.head)
            
#             # # get taiL_df and render based on slider's values
#             # data_inst.get_tail(slider)
#             # tail_df = st.dataframe(data = data_inst.tail)
            
#             # # get sample_df and render based on slider's values
#             # data_inst.get_sample(slider)
#             # sample_df = st.dataframe(data = data_inst.sample)

#             # # user mutli select box to choose which text columns converted to datetime
#             # data_inst.get_text_columns()
#             # text_columns = data_inst.text_col
#             # datetime_columns = st.multiselect('Which columns do you want to convert to dates', text_columns)
#             # # get numerical_cols
#             # data_inst.get_numeric_columns()
#             # numerical_columns = data_inst.num_col
#             # return text_columns, numerical_columns, datetime_columns
    
    
#     def main(self):
#         # web app heading
#         st.title('CSV Explorer')
#         # upload csv widget - must only accept CSV
#         self.uploaded_file = st.file_uploader("Upload CSV", ['csv'])
#         # create logic to forward application
#         if self.uploaded_file is not None:
#             # ensure to parse dates as datetime
#             self.df = pd.read_csv(self.uploaded_file, parse_dates = True)
#             text_columns, numerical_columns, datetime_columns = self.data_logic(self.df, self.uploaded_file.name)
#         return None

