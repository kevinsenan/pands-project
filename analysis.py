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
#plot the histograms of each data set and save them as files
plt.hist(df[0])
plt.title('sepal length')
plt.savefig("Histogram sepal length")
plt.show()
plt.hist(df[1])
plt.title('sepal width')
plt.savefig("Histogram sepal width")
plt.show()
plt.hist(df[2])
plt.title('petal length')
plt.savefig("Histogram petal length")
plt.show()
plt.hist(df[3])
plt.title('petal width')
plt.savefig("Histogram petal width")
plt.show()
#Show all four histograms on one diagram to assist in comparison. I am using the variables fig and ax with the function plt.subplots() because the function returns a tuple containing a figure and axes objects. [7]
fig, ax=plt.subplots(2, 2, figsize=(8, 4))
ax[0,0].hist(df[0])
ax[0,1].hist(df[1])
ax[1,0].hist(df[2])
ax[1,1].hist(df[3])
ax[0,0].set_title(headers[0])
ax[0,1].set_title(headers[1])
ax[1,0].set_title(headers[2])
ax[1,1].set_title(headers[3])
plt.savefig("Histogram all four")
plt.show()
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

# Show all the boxplots on one graph. Define a function called colour and pass in the variable plot. 
# The boxes showing data from column 0 in the list will be coloured blue, column 1 red, column 3 green.
def colour(plot):
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
# The colour is then defined by the function colour.
plot = plt.boxplot(Sepal_Length, positions = [1, 2, 3], widths = 0.7)
colour(plot)
plot = plt.boxplot(Sepal_Width, positions = [5, 6, 7], widths = 0.7)
colour(plot)
plot = plt.boxplot(Petal_Length, positions = [9, 10, 11], widths = 0.7)
colour(plot)
plot = plt.boxplot(Petal_Width, positions = [13, 14, 15], widths = 0.7)
colour(plot)
#The labels on the x axis are spaced out as defined by the set_xticks, this is the point on the x axis 
#the label should be set, with the labels being taken from the headers list.
ax.set_xticks([2, 6, 10, 14])
ax.set_xticklabels(headers)
ax.set_title('Boxplots by Iris')
#Adding a legend to the plot
ax.legend([plot["boxes"][0], plot["boxes"][1], plot["boxes"][2]], ['Iris-setosa', 'Iris-virginica', 'Iris-versicolor'], loc='upper right')
#Save the plot to a file
plt.savefig("Boxplot comparison")
# To get an idea of the data, we use the command describe 
# to show the statistical information and using print to display it for potential use.
print(df.describe())
#show data correlation in a table form for potential use 
print(df.corr())
#Open a file and write the data to it. I had to convert the dataframe back to a string 
# to write to the file.
filename = "data.txt"
with open(filename, 'wt') as f:
    f.write(df.to_string())
