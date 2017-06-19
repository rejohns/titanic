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

def _validate_file(path):
    """Validate the format of the input data"""
    pass

def _dummy(column):
    """Returns columns of dummy variables from a column of categories"""
    pass

def _normalize(column, min_val=None, max_val=None):
    """Normalizes a column of data

    If no min and max values are given, then the data is normalized based off
    of the min and max from the sample data.
    """
    if min_val is None:
        min_val = min(column)
    if max_val is None:
        max_val = max(column)
    column = [float(val) for val in column]
    column = [(val - min_val) / (max_val - min_val) for val in column]
    return column

def parse_data(path):
    """Cleans and prepares the data to be used in the  model"""
    pass
