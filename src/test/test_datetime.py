import pandas as pd
import numpy as np
import unittest

import sys
sys.path.append('../')

from src.datetime import DateColumn



class TestGetName(unittest.TestCase):
    def test_get_name_success(self):
        # Create sample df
        rng = pd.date_range('2015-02-24', periods=5, freq='T')
        df = pd.DataFrame({ 'Date': rng, 'Val': np.random.randn(len(rng))})
        
        date_inst = DateColumn('Date', df['Date'])
        date_inst.get_name()
        
        self.assertEqual('Date', date_inst.name)


class TestGetUnique(unittest.TestCase):
    def test_get_unique(self):
        # Create sample df
        rng = pd.date_range('2015-02-24', periods=5, freq='T')
        df = pd.DataFrame({ 'Date': rng, 'Val': np.random.randn(len(rng))})
        
        date_inst = DateColumn('Date', df['Date'])
        date_inst.get_unique()
        
        self.assertEqual('5', date_inst.unique)
        
class TestGetMissing(unittest.TestCase):
    def test_get_missing(self):
        # Create sample df
        rng = pd.date_range('2015-02-24', periods=5, freq='T')
        df = pd.DataFrame({ 'Date': rng, 'Val': np.random.randn(len(rng))})
        
        date_inst = DateColumn('Date', df['Date'])
        date_inst.get_missing()
        
        self.assertEqual('0', date_inst.missing)

class TestGetWeekend(unittest.TestCase):
    def test_get_weekend(self):
        # Create sample df
        df = pd.DataFrame({'Date': ['6/11/2021', '7/11/2021', '8/11/2021'],
               'value': [2, 3, 4]})
        
        df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
        
        
        date_inst = DateColumn('Date', df['Date'])
        date_inst.get_weekend()
        
        self.assertEqual('2', date_inst.weekend)
        
# class TestGetWeekday(unittest.TestCase):
#     def test_get_weekday(self):
#         # Create sample df
#         # Create sample df
#         df = pd.DataFrame({'Date': ['6/11/2021', '7/11/2021', '8/11/2021'],
#                    'value': [2, 3, 4]})
        
#         date_inst = DateColumn('Date', df['Date'])
#         date_inst.get_weekday()
        
#         self.assertEqual('1', date_inst.weekday)
        





        
if __name__ == '__main__':
    unittest.main()  
  