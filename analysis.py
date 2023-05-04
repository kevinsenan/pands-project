# analysis.py
# Programming and Scripting Project. To analyse the Fisher's Iris data set using histogram and scatter plots
# author K Donovan

import pandas as pd

# read in the data from the iris.data file as a csv file as that is how the data is presented and assign it to a datafile named df.
df = pd.read_csv('iris.data')
print(df)

