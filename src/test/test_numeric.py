import pandas as pd
import unittest
from numeric import NumericColumn

class TestNumericColumn(unittest.TestCase):

    def setUp(self):
        data = pd.Series([-1, -1, -1.5, None, 0, 2, 1, 3, 4.25, 5.25, 100, None])
        test_column_name = "A_Test_Column"
        self.column = NumericColumn(col_name=test_column_name, serie=data)

        self.column.get_name()
        self.column.get_unique()
        self.column.get_missing()
        self.column.get_zeros()
        self.column.get_negatives()
        self.column.get_mean()
        self.column.get_std()
        self.column.get_min()
        self.column.get_max()
        self.column.get_median()

        """"
        Because all methods -- get_name(), get_unique(), and so on -- from Numeric.py end with "return None", 
        so in test methods below, when calling these methods in text-book format, results are actually "None"; 
        so, the expected results generated are "None", causing "failed" test outcomes. Therefore, instead of
        calling the methods to get the value, the attributes should be called - i.e. attributes from NumericColumn 
        Class, such as name, unique, missing...

        But calling these attibutes alone still did not work, because the machine does not recognise these 
        attributes yet (name, unique ...). So, I needed to let the machine recognise these attributes, by calling
        the methods at the initialisation stage of the test - i.e. setUp() - to set up the attributes...

        """

    def tearDown(self):
        del self.column
    
    def test_get_name(self):
        self.assertEqual(self.column.name, "A_Test_Column")

    def test_get_unique(self):
        self.assertEqual(self.column.unique, 10)

    def test_get_missing(self):
        self.assertEqual(self.column.missing, 2)

    # def test_get_zeros(self):
    #     self.assertEqual(self.column.zeros, 1)

    # def test_get_negatives(self):
    #     self.assertEqual(self.column.negatives, 3)

    # def test_get_mean(self):
    #     self.assertEqual(self.column.mean, 11.2)

    # def test_get_std(self):
    #     self.assertEqual(round(self.column.std, 2), 31.29)

    # def test_get_min(self):
    #     self.assertEqual(self.column.min, -1.5)

    # def test_get_max(self):
    #     self.assertEqual(self.column.max, 100)

    # def test_get_median(self):
    #     self.assertEqual(self.column.median, 1.5)


if __name__ == '__main__':
    unittest.main()# To be filled by students