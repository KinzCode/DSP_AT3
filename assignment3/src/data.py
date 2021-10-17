# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import numpy as np
from pathlib import Path

file_path =
rows = st.slider('Select the number of rows to be displayed', 0, 50, 5)


@dataclass
class Dataset:
    name: str
    df: pd.DataFrame

    def get_name(self):
        """
    Return filename of loaded dataset
    """

        self.name = Path(file_path).stem
        return None

    def get_n_rows(self):
        """
      Return number of rows of loaded dataset
    """
        self.rows = df.shape[0]
        return None

    def get_n_cols(self):
        """
      Return number of columns of loaded dataset
    """
        self.cols = df.shape[1]
        return None

    def get_cols_list(self):
        """
      Return list column names of loaded dataset
    """
        self.cols_list = df.columns.tolist()

        return None

    def get_cols_dtype(self):
        """
      Return dictionary with column name as keys and data type as values
    """
        self.dataTypeDict = dict(df.dtypes)

        return None

    def get_n_duplicates(self):
        """
      Return number of duplicated rows of loaded dataset
    """
        return None

    def get_n_missing(self):
        """
      Return number of rows with missing values of loaded dataset
    """
        self.missing = sum(df.apply(lambda x: sum(x.isnull().values), axis=1) > 0)
        return None

    def get_head(self, n=5):
        """
      Return Pandas Dataframe with top rows of loaded dataset
    """

        self.head = df.head(rows)
        return None

    def get_tail(self, n=5):
        """
      Return Pandas Dataframe with bottom rows of loaded dataset
    """
        self.tail = df.tail(rows)
        return None

    def get_sample(self, n=5):
        """
      Return Pandas Dataframe with random sampled rows of loaded dataset
    """
        self.sample = df.sample(rows)
        return None

    def get_numeric_columns(self):
        """
      Return list column names of numeric type from loaded dataset
    """
        return None

    def get_text_columns(self):
        """
      Return list column names of text type from loaded dataset
    """
        return None

    def get_date_columns(self):
        """
      Return list column names of datetime type from loaded dataset
    """
        return None
