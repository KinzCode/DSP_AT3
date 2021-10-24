# numeric
import streamlit as st
from dataclasses import dataclass
import pandas as pd



@dataclass
class NumericColumn:
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
    self.unique = self.serie.nunique()
    return None

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    self.missing = self.serie.isna().sum()
    return None

  def get_zeros(self):
    """
    Return number of occurrence of 0 value for selected column
    """
    zeros = 0
    for i in self.serie.values:
        if i ==0:
          zeros += 1
    print(zeros)
    return None

  def get_negatives(self):
    """
    Return number of negative values for selected column
    """
    negatives = 0
    for n in self.serie.values:  
        if n < 0: 
          negatives += 1
    print(negatives)
    return None

  def get_mean(self):
    """
    Return the average value for selected column
    """
    self.mean = self.serie.mean()
    return None

  def get_std(self):
    """
    Return the standard deviation value for selected column
    """
    self.std = self.serie.std()
    return None
  
  def get_min(self):
    """
    Return the minimum value for selected column
    """
    self.min = self.serie.min()
    return None

  def get_max(self):
    """
    Return the maximum value for selected column
    """
    self.max = self.serie.max()
    return None

  def get_median(self):
    """
    Return the median value for selected column
    """
    self.median = self.serie.median()
    return None

  def get_histogram(self):
    """
    Return the generated histogram for selected column
    """
    self.histogram = st.hist(self.serie)
    return None

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    self.occurences = pd.DataFrame(self.serie.value_counts()) 
    self.percentage = pd.DataFrame(self.serie.value_counts(normalize = True))
    return None
