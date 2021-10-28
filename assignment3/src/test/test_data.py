# To be filled by students
import unittest
from data import Dataset
import pandas as pd


class TestDataSet(unittest.TestCase):
    def test_get_name(self):
        df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7]})

        instantiated_data = Dataset('Run the test', df)
        instantiated_data.get_name()
        result = instantiated_data.name
        self.assertEqual(result, 'Run the test')

    def test_get_n_rows(self):
        df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7]})

        instantiated_data = Dataset('Run the test', df)
        instantiated_data.get_n_rows()
        result = instantiated_data.rows
        self.assertEqual(result, 7)

    def test_get_n_cols(self):
        df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7]})

        instantiated_data = Dataset('Run the test', df)
        instantiated_data.get_n_cols()
        result = instantiated_data.cols
        self.assertEqual(result, 1)

    def test_get_cols_list(self):
        df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7]})

        instantiated_data = Dataset('Run the test', df)
        instantiated_data.get_cols_list()
        result = instantiated_data.list
        self.assertEqual(result, ['a'])

    def test_get_cols_dtype(self):
        df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7]})

        instantiated_data = Dataset('Run the test', df)
        instantiated_data.get_cols_dtype()
        result = instantiated_data.dtype
        self.assertEqual(result, {'a':'int'})


    def get_n_duplicates(self):
        df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7, 7]})

        instantiated_data = Dataset('Run the test', df)
        instantiated_data.get_n_duplicates()
        result = instantiated_data.duplicates
        self.assertEqual(result, 1)



