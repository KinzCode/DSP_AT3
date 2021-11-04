import unittest
import pandas as pd
import streamlit as st

import sys

sys.path.append('../')

from src.text import TextColumn


class MyClass(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        data = pd.Series(['DSP', 'Shangqing', 'Navid', None, 'DSP', " "])
        test_column_name = "Text_Column"
        self.text = TextColumn(test_column_name, data)

    @classmethod
    def tearDownClass(cls):
        print("====> end class")

    def test_get_name(self):
        self.text.get_name()
        self.assertEqual(self.text.name, "Text_Column")

    def test_get_unique(self):
        self.text.get_unique()
        self.assertEqual(self.text.unique, '5')

    def test_get_missing(self):
        self.text.get_missing()
        self.assertEqual(self.text.missing, '1')

    def test_get_empty(self):
        self.text.get_empty()
        self.assertEqual(self.text.empty, '1')

    def test_get_whitespace(self):
        self.text.get_whitespace()
        self.assertEqual(self.text.white, '1')

    def test_get_lowercase(self):
        self.text.get_lowercase()
        self.assertEqual(self.text.lower, '0')

    def test_get_uppercase(self):
        self.text.get_uppercase()
        self.assertEqual(self.text.upper, '2')

    def test_get_isalpha(self):
        self.text.get_alphabet()
        self.assertEqual(self.text.alpha, '5')

    def test_get_digit(self):
        self.text.get_digit()
        self.assertEqual(self.text.digit, '0')

    def test_get_mode(self):
        self.text.get_mode()
        self.assertEqual(self.text.mode, 'DSP')

    def test_get_barchart(self):
        data = pd.Series(['DSP', 'Shangqing', 'Navid', None, 'DSP', " "])
        test_barchart = st.bar_chart(data.value_counts())

        self.text.get_barchart()
        self.assertEqual(self.text.barchart, test_barchart)

    def test_get_frequent(self):
        self.text.get_frequent()
        self.assertEqual(self.text.frequency['value'][0], 'DSP')


if __name__ == '__main__':
    unittest.main()
