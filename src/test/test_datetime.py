import pandas as pd
import numpy as np
import unittest
import streamlit as st

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
        df = pd.DataFrame({'Date': ['6/11/2021', '7/11/2021', '9/11/2021'],
                   'value': [2, 3, 4]})
        

        df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
        
        date_inst = DateColumn('Date', df['Date'])
        date_inst.get_weekend()
        
        self.assertEqual('2', date_inst.weekend)
        
class TestGetWeekday(unittest.TestCase):
    def test_get_weekday(self):
        # Create sample df
        df = pd.DataFrame({'Date': ['6/11/2021', '7/11/2021', '8/11/2021'],
                    'value': [2, 3, 4]})
        df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
        
        date_inst = DateColumn('Date', df['Date'])
        date_inst.get_weekday()
        
        self.assertEqual('1', date_inst.weekday)
        

class TestGetFuture(unittest.TestCase):
    def test_get_future(self):
        # Create sample df
        df = pd.DataFrame({'Date': ['6/11/2021', '7/11/2021', '8/11/2021'],
                    'value': [2, 3, 4]})
        df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
        
        date_inst = DateColumn('Date', df['Date'])
        date_inst.get_future()

        
        self.assertEqual('3', date_inst.future)  

class TestGetEmpty1900(unittest.TestCase):
    def test_get_empty_1900(self):
        # Create sample df
        df = pd.DataFrame({'Date': ['1900-01-01', '1900-01-01' ,'2021-01-02']})
        df['Date'] = pd.to_datetime(df['Date'], format="%Y/%m/%d")
        
        date_inst = DateColumn('Date', df['Date'])
        date_inst.get_empty_1900()
        
        self.assertEqual('2', date_inst.empty_1900)  

class TestGetEmpty1970(unittest.TestCase):
    def test_get_empty_1970(self):
        # Create sample df
        df = pd.DataFrame({'Date': ['1970-01-01', '1900-01-01' ,'2021-01-02']})
        df['Date'] = pd.to_datetime(df['Date'], format="%Y/%m/%d")
        
        date_inst = DateColumn('Date', df['Date'])
        date_inst.get_empty_1970()
        
        self.assertEqual('1', date_inst.empty_1970)
        
class TestGetMin(unittest.TestCase):
    def test_get_min(self):
        # Create sample df
        df = pd.DataFrame({'Date': ['6/11/2021', '7/11/2021', '8/11/2021']})
        df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
        
        date_inst = DateColumn('Date', df['Date'])
        date_inst.get_min()
        
        self.assertEqual('2021-11-06 00:00:00', date_inst.min)
        
class TestGetMax(unittest.TestCase):
    def test_get_max(self):
        # Create sample df
        df = pd.DataFrame({'Date': ['6/11/2021', '7/11/2021', '8/11/2021']})
        df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
        
        date_inst = DateColumn('Date', df['Date'])
        date_inst.get_max()
        
        self.assertEqual('2021-11-08 00:00:00', date_inst.max)

class TestGetBarchart(unittest.TestCase):
    def test_get_barchart(self):
        df = pd.DataFrame({'Date': ['6/11/2021', '7/11/2021', '8/11/2021']})
        df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y") 
        
        result = st.bar_chart(df['Date'].value_counts())
        
        date_inst = DateColumn('Date', df['Date'])
        date_inst.get_barchart()
        
        self.assertEqual(result, date_inst.barchart)

class TestGetFrequent(unittest.TestCase):
    def test_get_frequent(self):
        df = pd.DataFrame({'Date': ['6/11/2021','7/11/2021','8/11/2021', '8/11/2021']})
        df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
        
        
        date_inst = DateColumn('Date', df['Date'])
        date_inst.get_frequent()
        
        self.assertEqual(2, date_inst.frequency['occurance'][0])
        
        
if __name__ == '__main__':
    unittest.main()  
  