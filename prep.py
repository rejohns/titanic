"""prep.py

Cleans and prepares the input data to be used by the model to train or predict
the Titanic survivors.

Input Data and relevant transformations:
`pclass` is the ticket class (1st, 2nd, or 3rd), which should be transformed
into two dummy variables.
`sex` should be transformed into a dummy variable
`age` should be normalized
`sibsp` should be normalized
`parch` should be normalized
`ticket` is an ID variable that is not relevant for the model
`fare` should be normalized
`cabin` [[[potentially relevant, but not sure how to deal with this just yet]]]
`embarked` [[[not sure if relevant]]]

If the `survival` data is present (for training), then this will be output as a
second vector.  Any non-relevant data columns will not be output.
"""
import pandas as pd
import numpy as np

def _validate_file(path):
    """Validate the format of the input data"""
    pass

def _dummy(dataFrame, column):
    """Returns a data fram with dummy variables from a column of categories

    The first row of the output matrix will be the value for each dummy
    category.
    """
    categories = sorted(list(set(dataFrame[column])))
    for category in categories:
        if category in dataFrame.columns:
            raise KeyError("A column for value {} already exists."
                           .format(category))
        dataFrame[category] = np.where(dataFrame[column] == category, 1, 0)
    return dataFrame

def _normalize(dataFrame, column, min_val=None, max_val=None):
    """Normalizes a column of data

    If no min and max values are given, then the data is normalized based off
    of the min and max from the sample data.
    """
    if min_val is None:
        min_val = dataFrame[column].min()
    if max_val is None:
        max_val = dataFrame[column].max()
    dataFrame['n({})'.format(column)] = (
        (dataFrame[column] - min_val) / (max_val - min_val)
        )
    return dataFrame

def parse_data(path):
    """Cleans and prepares the data to be used in the  model"""
    pass
