
import sys
sys.path.append('../')
from text import *

import unittest


class MyClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("====> start class")

        col_name = 'BlueCorner'
        df = pd.read_csv('pinnacle_odds_sample.csv')
        serie = df[col_name]
        cls.textColumn = TextColumn(col_name, serie)

    @classmethod
    def tearDownClass(cls):
        print("====> end class")

    def test_get_name(self):
        """
          Return name of selected column
        """
        name = self.textColumn.get_name()
        # self.assertEqual(name, 'TotalsLine')

    def test_get_unique(self):
        """
          Return number of unique values for selected column
        """
        unique = self.textColumn.get_unique()
        print(unique)
        # self.assertEqual(unique, 42)

    def test_get_missing(self):
        """
        Return number of missing values for selected column
        """
        self.missing = self.textColumn.get_missing()
        # self.assertEqual(self.missing, 29)

    def test_get_empty(self):
        """
         Return number of rows with empty string for selected column
        """
        self.empty = self.textColumn.get_empty()
        # self.assertEqual(self.empty, 29)

    def test_get_whitespace(self):
        """
         Return number of rows with only whitespaces for selected column
         """
        self.empty = self.textColumn.get_whitespace()
        # self.assertEqual(self.empty, 29)

    def test_get_lowercase(self):
        """
        Return number of rows with only lower case characters for selected column
        """
        self.empty = self.textColumn.get_lowercase()
        # self.assertEqual(self.empty, 0)

    def test_get_uppercase(self):
        """
        Return number of rows with only upper case characters for selected column
        """
        self.empty = self.textColumn.get_uppercase()
        # self.assertEqual(self.empty, 0)

    def test_get_isalpha(self):
        """
        Return number of rows with only alphabet characters for selected column
        """
        self.empty = self.textColumn.get_alphabet()
        # self.assertEqual(self.empty, 0)

    def test_get_digit(self):
        """
        Return number of rows with only numbers as characters for selected column
        """
        self.empty = self.textColumn.get_digit()
        # self.assertEqual(self.empty, 0)

    def test_get_mode(self):
        """
        Return the mode value for selected column
        """
        self.mode = self.textColumn.get_mode()
        # self.assertEqual(self.mode, 0)

    def test_get_frequent(self):
        """
        Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
        """
        self.get_frequent = self.textColumn.get_frequent()
        # self.assertEqual(self.get_frequent, 0)


if __name__ == '__main__':
    unittest.main()

