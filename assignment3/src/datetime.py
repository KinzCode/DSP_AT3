# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class DateColumn:
  col_name: str
  serie: pd.Series
  
  def get_name(self):
    """
    Return name of selected column
    """
    # get column name. Column is passed as string into class
    self.name = self.col_name
    return None

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    # get unique values in series then take length of array
    self.unique = len(pd.unique(self.serie))
    return None

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    # filter series for only n/a values then take length
    self.missing = len(self.serie.loc[self.serie.isnull()])
    print(self.missing)
    return None

  def get_weekend(self):
    """
    Return number of occurrence of days falling during weekend (Saturday and Sunday)
    """
    # get length of series and subract set of weekdays to get weekends
    self.weekend = len(set(self.serie) - set(self.serie.dt.weekday))
    return None

  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    # use pandas functions to get weekdays
    self.weekday = len(self.serie.dt.weekday)

    return None
  
  def get_future(self):
    """
    Return number of cases with future dates (after today)
    """
    # get todays date and filter for greater than today and take length
    self.future = len(self.serie.loc[self.serie > pd.to_datetime("today")])
    return None

  def get_empty_1900(self):
    """
    Return number of occurrence of 1900-01-01 value
    """
    # filter array for dates only of 1900-01-01 and take length
    self.empty_1900 = len(self.serie.loc[self.serie == '1900-01-01'])
    return None

  def get_empty_1970(self):
    """
    Return number of occurrence of 1970-01-01 value
    """
    # filter for dates only of 1970-01-01 and take length
    self.empty_1970 = len(self.serie.loc[self.serie == '1970-01-01'])
    return None

  def get_min(self):
    """
    Return the minimum date
    """
    # get lowest date with min
    self.min = self.serie.min()
    return None

  def get_max(self):
    """
    Return the maximum date 
    """
    # get largest date with max
    self.max = self.serie.max()
    return None

  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    # create basic bar chart on series with streamlit
    self.barchart = st.bar_chart(self.serie)

    return None

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    # create frequencies dataframe
    self.frequent = pd.DataFrame(self.serie.value_counts())
    return None

