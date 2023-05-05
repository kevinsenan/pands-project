# analysis.py
# Programming and Scripting Project. To analyse the Fisher's Iris data set using histogram and scatter plots
# author K Donovan

import pandas as pd
import matplotlib.pyplot as plt

#assigning the name iris.data to the variable filename
filename = 'iris.data'
# read in the data from the iris.data file as a csv file as that 
# is how the data is presented. Assign it to a datafile named df. 
# Header is set to None to ensure the first line 
# of data isn't ignored as a header.
df = pd.read_csv(filename, header=None)
#As the dataset had no column headers, I have to insert them into the dataset. 
# I am using 0 to 4 for the numerical columns to make it easier for me but I am 
df.set_axis([0, 1, 2, 3, "Iris"], axis=1,inplace=True)
# saving the list of correct column names in a list called headers. 
headers = ["sepal length", "sepal width", "petal length", "petal width"]
# To get an idea of the data, we use the command describe 
# to show the statistical information using print.
print(df.describe())
#I can now plot a histogram of all the values adding labels using the headers list
plt.hist([df[0], df[1], df[2], df[3]], label=[headers[0], headers[1], headers[2], headers[3]])
plt.legend()
plt.show()         