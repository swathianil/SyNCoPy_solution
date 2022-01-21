# Import packages
import sys
import os
import pandas as pd
import numpy as np

# Import functions to test
from method1 import checksum_calc as c1
from method2 import checksum_calc as c2

# Test function
def test_answer(rawdata1, rawdata2):
    assert c1(rawdata1) == 130.
    assert c2(rawdata2) == 130.

# Test
if __name__ == '__main__':
    # File location
    dirloc = str(os.getcwd()) + "/"  # current directory
    filename = 'test_data'
    # Load data
    rawdata1 = np.loadtxt(dirloc + filename)  # 2d array
    rawdata2 = pd.read_table(dirloc + filename,delimiter="\t",header=None)  # dataframe
    test_answer(rawdata1, rawdata2)