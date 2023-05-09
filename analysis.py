# analysis.py
# Programming and Scripting Project. To analyse the Fisher's Iris data set using histogram and scatter plots
# author K Donovan

import pandas as pd
import matplotlib.pyplot as plt

#assigning the name of the data set file iris.data to the variable filename
Iris_Dataset = 'iris.data'
# read in the data from the iris.data file as a csv file as that 
# is how the data is presented. Assign it to a datafile named df. 
# Header is set to None to ensure the first line 
# of data isn't ignored as a header.
df = pd.read_csv(Iris_Dataset, header=None)
#As the dataset had no column headers, I have to insert them into the dataset. 
# I am using 0 to 3 for the numerical columns to make it easier for me later in the program.
df.set_axis([0, 1, 2, 3, "Iris"], axis=1,inplace=True)
# saving the list of correct column names in a list called headers. 
headers = ["sepal length", "sepal width", "petal length", "petal width"]
# To get an idea of the data, we use the command describe 
# to show the statistical information and using print to display it.
print(df.describe())
#I can now plot a histogram of all the values adding labels using the headers list
plt.hist([df[0], df[1], df[2], df[3]], label=[headers[0], headers[1], headers[2], headers[3]])
plt.legend()
plt.savefig("Histogram")
#plt.show()
#plot a scatter plots for the sepals and petals
colour = {'Iris-setosa':'red', 'Iris-virginica':'green', 'Iris-versicolor':'blue'}
plt.scatter(df[0], df[1], c=df['Iris'].map(colour))
plt.xlabel(headers[0])
plt.ylabel(headers[1])
plt.title('Scatter Plot for Fishers Iris Data set showing sepal length and width')
plt.savefig("Scatter Sepal")
#plt.show()
plt.scatter(df[2], df[3], c=df['Iris'].map(colour))
plt.xlabel(headers[2])
plt.ylabel(headers[3])
plt.title('Scatter Plot for Fishers Iris Data set showing petal length and width')
plt.savefig("Scatter Petal")
#plt.show()
#show data correlation in a table form
print(df.corr())
#show boxplots of data to show the range of data for each of the attributes of all the flowers
plt.boxplot([df[0], df[1], df[2], df[3]])
plt.savefig("Boxplot all flowers")
#plt.show()
#show boxplots of data to show the range of data for each of the attributes of each flower separately
df.boxplot(column=[0], by=['Iris'])
plt.savefig("Boxplot column 0")
#plt.show()
# Show all the boxplots on one graph. Define a function called set_colour and pass in the variable bp. 
# The boxes showing data from column 0 in the list will be coloured blue, column 1 red, column 3 green.
def set_colour(plot):
    plt.setp(plot['boxes'][0], color='blue')
    plt.setp(plot['boxes'][1], color='red')
    plt.setp(plot['boxes'][2], color='green')
#To show the plots individually, the data from the four columns are assigned to lists by header name 
# and then split into flower type
fig, ax = plt.subplots()
Sepal_Length = [df[0][df.Iris == 'Iris-setosa'], df[0][df.Iris == 'Iris-virginica'], df[0][df.Iris == 'Iris-versicolor']]
Sepal_Width = [df[1][df.Iris == 'Iris-setosa'], df[1][df.Iris == 'Iris-virginica'], df[1][df.Iris == 'Iris-versicolor']]
Petal_Length = [df[2][df.Iris == 'Iris-setosa'], df[2][df.Iris == 'Iris-virginica'], df[2][df.Iris == 'Iris-versicolor']]
Petal_Width = [df[3][df.Iris == 'Iris-setosa'], df[3][df.Iris == 'Iris-virginica'], df[3][df.Iris == 'Iris-versicolor']]
#The variable plot is assigned the data for each column, the positions on the x axis are defined by the positions list
#and the width of the boxes is defined by the variable widths. 
# The colour is then defined by the function set_colour.
plot = plt.boxplot(Sepal_Length, positions = [1, 2, 3], widths = 0.7)
set_colour(plot)
plot = plt.boxplot(Sepal_Width, positions = [5, 6, 7], widths = 0.7)
set_colour(plot)
plot = plt.boxplot(Petal_Length, positions = [9, 10, 11], widths = 0.7)
set_colour(plot)
plot = plt.boxplot(Petal_Width, positions = [13, 14, 15], widths = 0.7)
set_colour(plot)
#The labels on the x axis are spaced out as defined by the set_xticks, this is the point on the x axis 
#the label should be set, with the labels being taken from the headers list.
ax.set_xticks([2, 6, 10, 14])
ax.set_xticklabels(headers)
ax.set_title('Boxplots by Iris')
#Adding a legend to the plot
ax.legend([plot["boxes"][0], plot["boxes"][1], plot["boxes"][2]], ['Iris-setosa', 'Iris-virginica', 'Iris-versicolor'], loc='upper right')
#Save the plot to a file
plt.savefig("Boxplot comparison")
#plt.show()
#Open a file and write the data to it. I had to convert the dataframe back to a string 
# to write to the file.
filename = "test.txt"
with open(filename, 'wt') as f:
    f.write(df.to_string())
