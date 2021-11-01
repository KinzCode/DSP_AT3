import pandas as pd
import numpy as np
import unittest

import sys
sys.path.append('../')

from datetime import DateColumn


class TestGetName(unittest.TestCase):
    def test_get_name_success(self):
        # Create sample df
        rng = pd.date_range('2015-02-24', periods=5, freq='T')
        df = pd.DataFrame({ 'Date': rng, 'Val': np.random.randn(len(rng))})
        
        date_inst = DateColumn('Date', df)
        date_inst.get_name()
        
        self.assertEqual('Date', date_inst.name)


    
# class TestGetUnique(unittest.TestCase):
#     def test_get_unique(self):
#         # Create sample df
#         rng = pd.date_range('2015-02-24', periods=5, freq='T')
#         df = pd.DataFrame({ 'Date': rng, 'Val': np.random.randn(len(rng))})
        
#         date_inst = DateColumn('Date', df)
#         date_inst.get_unique()
        
#         self.assertEqual('5', date_inst.unique)
        
# class TestGetMissing(unittest.TestCase):
#     def test_get_missing(self):
#         # Create sample df
#         rng = pd.date_range('2015-02-24', periods=5, freq='T')
#         df = pd.DataFrame({ 'Date': rng, 'Val': np.random.randn(len(rng))})
        
#         date_inst = DateColumn('Date', df)
#         date_inst.get_missing()
        
#         self.assertEqual('0', date_inst.missing)

# class TestGetWeekend(unittest.TestCase):
#     def test_get_weekend(self):
#         # Create sample df
#         rng = pd.date_range('2015-02-24', periods=5, freq='T')
#         df = pd.DataFrame({ 'Date': rng, 'Val': np.random.randn(len(rng))})
        
#         date_inst = DateColumn('Date', df)
#         date_inst.get_weekend()
        
#         self.assertEqual('5', date_inst.weekend)
        
# class TestGetWeekday(unittest.TestCase):
#     def test_get_weekday(self):
#         # Create sample df
#         rng = pd.date_range('2015-02-24', periods=5, freq='T')
#         df = pd.DataFrame({ 'Date': rng, 'Val': np.random.randn(len(rng))})
        
#         date_inst = DateColumn('Date', df)
#         date_inst.get_weekday()
        
#         self.assertEqual('0', date_inst.weekday)
        

        
        
        
    