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
        return self.name

    def get_unique(self):
        """
        Return number of unique values for selected column
        """
        self.unique = len(pd.unique(self.serie))
        return self.unique

    def get_missing(self):
        """
        Return number of missing values for selected column
        """
        self.missing = self.serie.isnull().sum()
        return self.missing

    def get_empty(self):
        """
        Return number of rows with empty string for selected column
        """
        self.empty = self.serie.isna().sum()
        return self.empty

    def get_whitespace(self):
        """
        Return number of rows with only whitespaces for selected column
        """
        self.white = len(self.serie.loc[self.serie.isnull()])
        return self.white

    def get_lowercase(self):
        """
        Return number of rows with only lower case characters for selected column
        """
        self.lower = len(self.serie[self.serie.apply(lambda x: True if x.islower() else False)])
        return self.lower

    def get_uppercase(self):
        """
        Return number of rows with only upper case characters for selected column
        """
        self.upper = len(self.serie[self.serie.apply(lambda x: True if x.isupper() else False)])
        return self.upper

    def get_alphabet(self):
        """
        Return number of rows with only alphabet characters for selected column
        """
        self.alpha = len(self.serie[self.serie.apply(lambda x: True if x.isalpha() else False)])
        return self.alpha

    def get_digit(self):
        """
        Return number of rows with only numbers as characters for selected column
        """
        self.digit = len(self.serie[self.serie.apply(lambda x: True if x.isdigit() else False)])
        return self.digit

    def get_mode(self):
        """
        Return the mode value for selected column
        """
        self.mode = self.serie.mode()
        
        if len(self.mode) > 1:
            self.mode =  max(set(self.serie), key=self.serie.count)
        return 

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
        occurences = pd.DataFrame(self.serie.value_counts()).reset_index()
        percentage = pd.DataFrame(self.serie.value_counts(normalize = True)).reset_index()
        
        self.frequency = occurences.merge(percentage, on = 'index', how = 'left')
        self.frequency.rename(columns = { self.frequencie.columns[0]: 'value',
                                          self.frequencie.columns[1]: 'occurance',
                                          self.frequencie.columns[2]: 'precentage'},
                                inplace = True)
        return