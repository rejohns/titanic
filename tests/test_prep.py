"""test_prep.py

Tests the functions from prep.py
"""
from unittest import TestCase, main
import random
import pandas as pd

import prep

class TestNormalize(TestCase):

    def test_normalize_range(self):
        """Normalize returns values between 1 and 0"""
        data = {'vals': [random.uniform(-1000000, 1000000) for i in range(1000)]}
        df = pd.DataFrame(data, columns=['vals'])
        df = prep._normalize(df, 'vals')
        if df['n(vals)'].min() < 0:
            self.fail("Normalized column returned a value below 0.")
        if df['n(vals)'].max() > 1:
            self.fail("Normalized column returned a value above 1.")

    def test_normalize_vals(self):
        """Normalize a simple column"""
        data = {'vals': [i for i in range(11)]}
        df = pd.DataFrame(data, columns=['vals'])
        df = prep._normalize(df, 'vals')
        expected_data = {'vals': [i for i in range(11)],
                         'n(vals)': [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1]}
        expected_result = pd.DataFrame(expected_data,
                                       columns=['vals', 'n(vals)'])
        self.assertTrue(df.equals(expected_result))

    def test_minval_normalize(self):
        """Normalize with a minimum value argument"""
        data = {'vals': [5, 6, 7, 8, 10]}
        df = pd.DataFrame(data, columns=['vals'])
        df = prep._normalize(df, 'vals', min_val=0)
        expected_data = {'vals': [5, 6, 7, 8, 10],
                         'n(vals)': [.5, .6, .7, .8, 1]}
        expected_result = pd.DataFrame(expected_data,
                                       columns=['vals', 'n(vals)'])
        self.assertTrue(df.equals(expected_result))

    def test_maxval_normalize(self):
        """Normalize with a maximum value argument"""
        data = {'vals': [0, 1, 2, 6, 3]}
        df = pd.DataFrame(data, columns=['vals'])
        df = prep._normalize(df, 'vals', max_val=10)
        expected_data = {'vals': [0, 1, 2, 6, 3],
                         'n(vals)': [0, .1, .2, .6, .3]}
        expected_result = pd.DataFrame(expected_data,
                                       columns=['vals', 'n(vals)'])
        self.assertTrue(df.equals(expected_result))

    def test_minval_maxval_normalize(self):
        """Normalize with a minimum and maximum value argument"""
        data = {'vals': [23, 86, 24, 97, 45]}
        df = pd.DataFrame(data, columns=['vals'])
        df = prep._normalize(df, 'vals', min_val=0, max_val=100)
        expected_data = {'vals': [23, 86, 24, 97, 45],
                         'n(vals)': [.23, .86, .24, .97, .45]}
        expected_result = pd.DataFrame(expected_data,
                                       columns=['vals', 'n(vals)'])
        self.assertTrue(df.equals(expected_result))


class TestDummy(TestCase):

    def test_dummy(self):
        """Dummy variables successfullly created"""
        data = {'sex': ['m', 'm', 'f', 'f', 'm', 't']}
        df = pd.DataFrame(data, columns=['sex'])
        df = prep._dummy(df, 'sex')
        expected_data = {'sex': ['m', 'm', 'f', 'f', 'm', 't'],
                         'f': [0, 0, 1, 1, 0, 0],
                         'm': [1, 1, 0, 0, 1, 0],
                         't': [0, 0, 0, 0, 0, 1]}
        expected_result = pd.DataFrame(expected_data,
                                       columns=['sex', 'f', 'm', 't'])
        self.assertTrue(df.equals(expected_result))

    def test_invalid_column(self):
        """Error triggered before overwriting a column"""
        data = {'sex': ['m', 'm', 'f', 'f', 'm', 't'],
                'm': [1, 1, 0, 0, 1, 0]}
        df = pd.DataFrame(data, columns=['sex', 'm'])
        try:
            df = prep._dummy(df, 'sex')
        except KeyError as detail:
            self.assertIn("A column for value m already exists.", str(detail))
        else:
            self.fail("No error was raised")
        

if __name__ == '__main__':
	main()
