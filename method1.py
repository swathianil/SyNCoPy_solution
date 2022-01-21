# Import packages
import sys
import os
import pandas as pd
import numpy as np


def data_wrangler(dirloc,filename):
    # Load data
    rawdata = np.loadtxt(dirloc + filename)  # 2d array

    #datatype = rawdata.dtype
    return rawdata


def checksum_calc(rawdata):
    
    checker_list = []
    counter = 1
    for row in rawdata:
        minima = np.min(row)
        maxima = np.max(row)
        if counter % 2 == 0:  # Even rows
            checker = np.subtract(maxima, minima)
        else:  # Odd rows
            checker = np.multiply(maxima, minima)
        checker_list.append(checker)  # contains row-wise operation output
        counter += 1
    checksum = np.sum(checker_list)
    return checksum

# Save data
def datasave(checksum,filename):
    np.save(filename + "_" + "checksum_m1.npy", checksum)


if __name__ == '__main__':    
    # File location
    dirloc = str(os.getcwd()) + "/"  # current directory
    filename = sys.argv[1]  # filename accepted as argument
    rawdata = data_wrangler(dirloc,filename)
    # Call checksum_calc()
    checksum = checksum_calc(rawdata)
    datasave(checksum,filename)
