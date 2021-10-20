# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class TextColumn:
  col_name: str
  serie: pd.Series
  
  def get_name(self):
    """
    Return name of selected column
    """
    self.name = self.col_name
    return None

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    self.unique = len(pd.unique(self.serie))
    return None

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    self.missing = len(self.serie.loc[self.serie.isnull()])
    print(self.missing)
    return None

  def get_empty(self):
    """
    Return number of rows with empty string for selected column
    """
    self.empty = len(self.serie.loc[self.serie.isnan()])
    print(self.empty)
    return None

  def get_whitespace(self):
    """
    Return number of rows with only whitespaces for selected column
    """
    self.white = len(self.serie.loc[self.serie.isspace()])
    print(self.white)
    return None

  def get_lowercase(self):
    """
    Return number of rows with only lower case characters for selected column
    """
    self.lower = len(self.serie.loc[self.serie.islower()])
    print(self.lower)
    return None

  def get_uppercase(self):
    """
    Return number of rows with only upper case characters for selected column
    """
    self.upper = len(self.serie.loc[self.serie.isupper()])
    print(self.upper)
    return None
  
  def get_alphabet(self):
    """
    Return number of rows with only alphabet characters for selected column
    """
    self.alpha = len(self.serie.loc[self.serie.isalpha()])
    print(self.alpha)
    return None

  def get_digit(self):
    """
    Return number of rows with only numbers as characters for selected column
    """
    self.digit = len(self.serie.loc[self.serie.isdigit()])
    print(self.digit)
    return None

  def get_mode(self):
    """
    Return the mode value for selected column
    """
    self.mode = self.serie.mode()
    return None


  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    self.barchart = st.bar_chart(self.serie)
    return None

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    self.frequent = pd.DataFrame(self.serie.value_counts())
    return None