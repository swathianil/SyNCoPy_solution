# SyNCoPy_solution
The current repository consists of two solutions to the SyNCoPy code challenge

# Run
To run each method, run the corresponding *.py file and pass the datafile as an argument:

    python3 method1.py production_table  # method 1
    python3 method2.py production_table  # method 2

Note: Run from the directory where production_table is located

Alternatively, the code can be run in a python environment by importing the module as follows:

    from method1 import checksum_calc
    checksum = checksum_calc('production_table')

or
    from method2 import checksum_calc
    checksum = checksum_calc('production_table')

The function returns the checksum value

# Output
The checksum value will be saved in a numpy file in the current directory. Two sample output files are provided using the included datafile 'production_table':

production_table_checksum_m1.npy

production_table_checksum_m2.npy

# Test
The methods_test.py file include a test function for both solutions. A file 'test_data' has been included to support this functionality.
