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
        col = [random.uniform(-1000000, 1000000) for i in range(1000)]
        ncol = prep._normalize(col)
        if min(ncol) < 0:
            self.fail("Normalized column returned a value below 0.")
        if max(ncol) > 1:
            self.fail("Normalized column returned a value above 1.")

    def test_normalize_vals(self):
        """Normalize a simple column"""
        col = [i for i in range(11)]
        ncol = prep._normalize(col)
        self.assertEqual(ncol, [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1])

    def test_minval_normalize(self):
        """Normalize with a minimum value argument"""
        col = [5, 6, 7, 8, 10]
        ncol = prep._normalize(col, min_val=0)
        self.assertEqual(ncol, [.5, .6, .7, .8, 1])

    def test_maxval_normalize(self):
        """Normalize with a maximum value argument"""
        col = [0, 1, 2, 6, 3]
        ncol = prep._normalize(col, max_val=10)
        self.assertEqual(ncol, [0, .1, .2, .6, .3])

    def test_minval_maxval_normalize(self):
        """Normalize with a minimum and maximum value argument"""
        col = [23, 86, 24, 97, 45]
        ncol = prep._normalize(col, min_val=0, max_val=100)
        self.assertEqual(ncol, [.23, .86, .24, .97, .45])


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
        self.assertEqual(df.equals(expected_result), True)

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
