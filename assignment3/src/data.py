# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import numpy as np


@dataclass
class Dataset:
    name: str
    df: pd.DataFrame
  
    
    def get_name(self):
      """
      Return filename of loaded dataset
      """
      self.name = self.name
      return None
  
    def get_n_rows(self):
      """
        Return number of rows of loaded dataset
      """
      self.rows = self.df.shape[0]
      return None
  
    def get_n_cols(self):
      """
        Return number of columns of loaded dataset
      """
      self.cols = self.df.shape[1]
      return None
  
    def get_cols_list(self):
      """
        Return list column names of loaded dataset
      """
      self.cols_list = self.df.columns.tolist()
  
      return None
  
    def get_cols_dtype(self):
      """
        Return dictionary with column name as keys and data type as values
      """
      #self.dataTypeDict = self.df.dtypes.to_dict()
      self.dataTypeDict = self.df.dtypes.apply(lambda x: x.name).to_dict()
  
      return None
  
    def get_n_duplicates(self):
      """
        Return number of duplicated rows of loaded dataset
      """
      self.duplicate = len(set(self.df)- set(self.df.duplicated(keep='first')))
      return None
  
    def get_n_missing(self):
      """
        Return number of rows with missing values of loaded dataset
      """
      self.missing = self.df.isnull().any(axis=1).sum()
      return None
  
    def get_head(self, n=5):
      """
        Return Pandas Dataframe with top rows of loaded dataset
      """
  
      self.head = self.df.head(n)
      return None
  
    def get_tail(self, n=5):
      """
        Return Pandas Dataframe with bottom rows of loaded dataset
      """
      self.tail = self.df.tail(n)
      return None
  
    def get_sample(self, n=5):
      """
        Return Pandas Dataframe with random sampled rows of loaded dataset
      """
      self.sample = self.df.sample(n)
      return None
  
    def get_numeric_columns(self):
      """
        Return list column names of numeric type from loaded dataset
      """
      self.num_col = list(self.df.select_dtypes(include='number').columns)
      return None
  
    def get_text_columns(self):
      """
        Return list column names of text type from loaded dataset
      """
      self.text_col = list(self.df.select_dtypes(include='object').columns)
      return None
  
    def get_date_columns(self):
      """
        Return list column names of datetime type from loaded dataset
      """
      self.date_col = list(self.df.select_dtypes(include='datetime').columns)
      return None

