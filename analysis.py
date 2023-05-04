# analysis.py
# Programming and Scripting Project. To analyse the Fisher's Iris data set using histogram and scatter plots
# author K Donovan

import pandas as pd

# read in the data from the iris.data file as a csv file 
# as that is how the data is presented and assign it to a datafile 
# named df. Header is set to None to ensure the first line 
# of data isn't ignored as a header.
df = pd.read_csv('iris.data', header=None)
#test print to be removed
print(df)

