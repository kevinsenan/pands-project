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
# I am using 0 to 3 for the numerical columns to make it easier for me.
df.set_axis([0, 1, 2, 3, "Iris"], axis=1,inplace=True)
# saving the list of correct column names in a list called headers. 
headers = ["sepal length", "sepal width", "petal length", "petal width"]
# To get an idea of the data, we use the command describe 
# to show the statistical information and using print to display it.
print(df.describe())
#I can now plot a histogram of all the values adding labels using the headers list
plt.hist([df[0], df[1], df[2], df[3]], label=[headers[0], headers[1], headers[2], headers[3]])
plt.legend()
plt.show()
#plot a scatter plots for the sepals and petals
colour = {'Iris-setosa':'red', 'Iris-virginica':'green', 'Iris-versicolor':'blue'}
plt.scatter(df[0], df[1], c=df['Iris'].map(colour))
plt.xlabel(headers[0])
plt.ylabel(headers[1])
plt.title('Scatter Plot for Fishers Iris Data set showing sepal length and width')
plt.show()
plt.scatter(df[2], df[3], c=df['Iris'].map(colour))
plt.xlabel(headers[2])
plt.ylabel(headers[3])
plt.title('Scatter Plot for Fishers Iris Data set showing petal length and width')
plt.show()
#show data correlation in a table form
print(df.corr())
#show boxplots of data to show the range of data for each of the attributes of all the flowers
plt.boxplot([df[0], df[1], df[2], df[3]])
plt.show()
#show boxplots of data to show the range of data for each of the attributes of each flower separately
df.boxplot(column=[0], by=['Iris'])
plt.show()
#
'''
fig, ax = plt.subplots(2, 2, figsize=(8, 6))
A = [df[0][df.Iris == 'Iris-setosa'], df[0][df.Iris == 'Iris-virginica'], df[0][df.Iris == 'Iris-versicolor']]
B = [df[1][df.Iris == 'Iris-setosa'], df[1][df.Iris == 'Iris-virginica'], df[1][df.Iris == 'Iris-versicolor']]
C = [df[2][df.Iris == 'Iris-setosa'], df[2][df.Iris == 'Iris-virginica'], df[2][df.Iris == 'Iris-versicolor']]
D = [df[3][df.Iris == 'Iris-setosa'], df[3][df.Iris == 'Iris-virginica'], df[3][df.Iris == 'Iris-versicolor']]
ax[0, 0].boxplot(A, widths = 0.7)
ax[0, 0].set_title(headers[0])
ax[0, 1].boxplot(B, widths = 0.7)
ax[0, 1].set_title(headers[1])
ax[1, 0].boxplot(C, widths = 0.7)
ax[1, 0].set_title(headers[2])
ax[1, 1].boxplot(D, widths = 0.7)
ax[1, 1].set_title(headers[3])
plt.show()
'''
# trying to show all the boxplots on one graph
def set_colour(bp):
    plt.setp(bp['boxes'][0], color='blue')
    plt.setp(bp['boxes'][1], color='red')
    plt.setp(bp['boxes'][2], color='green')

A = [df[0][df.Iris == 'Iris-setosa'], df[0][df.Iris == 'Iris-virginica'], df[0][df.Iris == 'Iris-versicolor']]
B = [df[1][df.Iris == 'Iris-setosa'], df[1][df.Iris == 'Iris-virginica'], df[1][df.Iris == 'Iris-versicolor']]
C = [df[2][df.Iris == 'Iris-setosa'], df[2][df.Iris == 'Iris-virginica'], df[2][df.Iris == 'Iris-versicolor']]
D = [df[3][df.Iris == 'Iris-setosa'], df[3][df.Iris == 'Iris-virginica'], df[3][df.Iris == 'Iris-versicolor']]

bp = plt.boxplot(A, 0, '', positions = [1, 2, 3], widths = 0.7)
set_colour(bp)
bp = plt.boxplot(B, 0, '', positions = [5, 6, 7], widths = 0.7)
set_colour(bp)
bp = plt.boxplot(C, 0, '', positions = [9, 10, 11], widths = 0.7)
set_colour(bp)
bp = plt.boxplot(D, 0, '', positions = [13, 14, 15], widths = 0.7)
set_colour(bp)

ax = plt.axes()
ax.set_xticks([2, 6, 10, 14])
ax.set_xticklabels(headers)
plt.show()

filename = "test.txt"
with open(filename, 'wt') as f:
    f.write("Kevin is an arse")