import streamlit as st
from dataclasses import dataclass
import pandas as pd
import numpy as np
import altair as alt

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
    self.unique = len(self.serie.unique())
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
    self.zeros = 0
    for i in self.serie.values:
        if i ==0:
          self.zeros += 1
    return None

  def get_negatives(self):
    """
    Return number of negative values for selected column
    """
    self.negatives = 0
    for n in self.serie.values:  
        if n < 0: 
          self.negatives += 1
 
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
    
    df = pd.DataFrame(self.serie)
    chart = alt.Chart(df).mark_bar().encode(
        alt.X(f'{self.serie.name}', bin = alt.Bin(maxbins=50)),
        y='count()',)
    
    self.histogram = st.altair_chart(chart)

    return None

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    
    occurrences = pd.DataFrame(self.serie.value_counts().reset_index())
    if len(occurrences) > 20:
        occurrences = occurrences[:20]
    
    percentage = pd.DataFrame(self.serie.value_counts(normalize = True)).reset_index()
    
    self.frequency = occurrences.merge(percentage, on = 'index', how = 'left')
    self.frequency.rename(columns = { self.frequency.columns[0]: 'value',
                                      self.frequency.columns[1]: 'occurance',
                                      self.frequency.columns[2]: 'precentage'},
                            inplace = True)
    
    return None