import pandas as pd
import unittest

import sys

sys.path.append('../')

from src.data import Dataset


class TestDataSet(unittest.TestCase):
    def test_get_name(self):
        df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7]})

        instantiated_data = Dataset('a', df)
        instantiated_data.get_name()
        result = instantiated_data.name
        self.assertEqual(result, 'a')

    def test_get_n_rows(self):
        df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7]})

        instantiated_data = Dataset('a', df)
        instantiated_data.get_n_rows()
        result = instantiated_data.rows
        self.assertEqual(result, 7)

    def test_get_n_cols(self):
        df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7]})

        instantiated_data = Dataset('a', df)
        instantiated_data.get_n_cols()
        result = instantiated_data.cols
        self.assertEqual(result, 1)

    def test_get_cols_list(self):
        df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7]})

        instantiated_data = Dataset('a', df)
        instantiated_data.get_cols_list()
        result = instantiated_data.cols_list
        self.assertEqual(result, ['a'])

    def test_get_cols_dtype(self):
        df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7]})

        instantiated_data = Dataset('a', df)
        instantiated_data.get_cols_dtype()
        result = instantiated_data.dataTypeDict
        self.assertEqual(result, {'a': 'int64'})

    def test_n_duplicates(self):
        df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7, 7]})

        instantiated_data = Dataset('a', df)
        instantiated_data.get_n_duplicates()
        result = instantiated_data.duplicate
        self.assertEqual(result, 1)

    def test_n_missing(self):
        df = pd.DataFrame({'a': [1, 2, 3, None, 5, 6, 7, 7]})

        instantiated_data = Dataset('a', df)
        instantiated_data.get_n_missing()
        result = instantiated_data.missing

        self.assertAlmostEqual(result, 1)

    def test_head(self):
        df = pd.DataFrame({'a': [1, 2, 3, None, 5, 6, 7, 7]})

        instantiated_data = Dataset('a', df)
        instantiated_data.get_head()
        result = instantiated_data.head

        self.assertAlmostEqual(result['a'][2], 3)

    def test_tail(self):
        df = pd.DataFrame({'a': [1, 2, 3, None, 5, 6, 7, 7]})

        instantiated_data = Dataset('a', df)
        instantiated_data.get_tail()
        result = instantiated_data.tail
        result.reset_index(drop=True, inplace=True)

        self.assertAlmostEqual(result['a'][1], 5)

    def test_sample(self):
        df = pd.DataFrame({'a': [1, 1, 1, 1, 1, 1, 1, 1]})

        instantiated_data = Dataset('a', df)
        instantiated_data.get_sample()
        result = instantiated_data.sample
        result.reset_index(drop=True, inplace=True)

        self.assertAlmostEqual(result['a'][3], 1)

    def test_numeric_columns(self):
        df = pd.DataFrame({'a': [1, 1, 1, 1, 1, 1, 1, 1],
                           'b': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']})

        instantiated_data = Dataset('a', df)
        instantiated_data.get_numeric_columns()
        result = instantiated_data.num_col

        self.assertAlmostEqual(result, ['a'])

    def test_text_columns(self):
        df = pd.DataFrame({'a': ['a', 'b', 'c'],
                           'b': ['a', 'b', 'c']})

        instantiated_data = Dataset('a', df)
        instantiated_data.get_text_columns()
        result = instantiated_data.text_col

        self.assertAlmostEqual(result, ['a', 'b'])

    def test_date_columns(self):
        df = pd.DataFrame({'a': ['a', 'b', 'c'],
                           'b': ['a', 'b', 'c'],
                           'Date': ['6/11/2021', '7/11/2021', '8/11/2021']})

        df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")

        instantiated_data = Dataset('a', df)
        instantiated_data.get_date_columns()
        result = instantiated_data.date_col

        self.assertAlmostEqual(result, ['Date'])


if __name__ == '__main__':
    unittest.main()
