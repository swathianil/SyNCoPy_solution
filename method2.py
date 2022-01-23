# Import packages
import sys
import os
import pandas as pd
import numpy as np

def data_wrangler(dirloc,filename):
    # Load data
    rawdata = pd.read_table(dirloc + filename,delimiter="\t",header=None)  # dataframe

    #datatype = rawdata.dtype
    return rawdata

def checksum_calc(rawdata):

    # Split odd and even rows into two dataframes
    odd_r = rawdata.iloc[::2]
    even_r = rawdata.iloc[1::2]
    
    # Row-wise operations
    odd_op = np.multiply(odd_r.min(axis=1), odd_r.max(axis=1))
    even_op = np.subtract(even_r.max(axis=1), even_r.min(axis=1))

    checksum = odd_op.sum() + even_op.sum()
    return checksum

# Save data
def datasave(checksum,filename):
    np.save(filename + "_" + "checksum_m2.npy", checksum)

if __name__ == '__main__':    
    # File location
    dirloc = str(os.getcwd()) + "/"  # current directory
    filename = sys.argv[1]  # filename accepted as argument
    rawdata = data_wrangler(dirloc,filename)
    # Call checksum_calc()
    checksum = checksum_calc(rawdata)
    datasave(checksum,filename)
