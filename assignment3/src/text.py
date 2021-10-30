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
        self.name = str(self.col_name)
        return None

    def get_unique(self):
        """
        Return number of unique values for selected column
        """
        self.unique = str(len(pd.unique(self.serie)))
        return None

    def get_missing(self):
        """
        Return number of missing values for selected column
        """
        self.missing = str(self.serie.isnull().sum())
        return None
    def get_empty(self):
        """
        Return number of rows with empty string for selected column
        """
        self.empty = str(self.serie.isna().sum())
        return None

    def get_whitespace(self):
        """
        Return number of rows with only whitespaces for selected column
        """
        self.white = str(len(self.serie.loc[self.serie.isnull()]))
        return None

    def get_lowercase(self):
        """
        Return number of rows with only lower case characters for selected column
        """
        self.lower = str(len(self.serie[self.serie.apply(lambda x: True if x.islower() else False)]))
        return None

    def get_uppercase(self):
        """
        Return number of rows with only upper case characters for selected column
        """
        self.upper = str(len(self.serie[self.serie.apply(lambda x: True if x.isupper() else False)]))
        return None

    def get_alphabet(self):
        """
        Return number of rows with only alphabet characters for selected column
        """
        self.alpha = str(len(self.serie[self.serie.apply(lambda x: True if x.isalpha() else False)]))
        return None

    def get_digit(self):
        """
        Return number of rows with only numbers as characters for selected column
        """
        self.digit = str(len(self.serie[self.serie.apply(lambda x: True if x.isdigit() else False)]))
        return None

    def get_mode(self):
        """
        Return the mode value for selected column
        """
        self.mode = str(self.serie.mode())
        
        return None

    def get_barchart(self):
        """
        Return the generated bar chart for selected column
        """
        occurences = pd.DataFrame(self.serie.value_counts())
        self.barchart = st.bar_chart(occurences)
        return None

    def get_frequent(self):
        """
        Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
        """
        occurences = pd.DataFrame(self.serie.value_counts()).reset_index()
        percentage = pd.DataFrame(self.serie.value_counts(normalize = True)).reset_index()
        
        self.frequency = occurences.merge(percentage, on = 'index', how = 'left')
        self.frequency.rename(columns = { self.frequency.columns[0]: 'value',
                                          self.frequency.columns[1]: 'occurance',
                                          self.frequency.columns[2]: 'precentage'},
                                inplace = True)
        return None