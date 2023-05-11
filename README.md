# pands-project
Python Project ATU Data Analytics Course
The Iris Dataset
The Iris dataset is a multivariate dataset which means there is more than one variable in the dataset, Ronald Fisher first created it in 1936, he was a Statistician from the UK. This dataset has data on Iris flowers, specifically the Iris setosa, Iris versicolor, and the Iris virginica. The data is used to show the characteristics of length and width of sepals and of the petals.
It was created to help with the identification of the three species of Iris in the dataset , which ,as will be shown, can be tricky.

This dataset is highly regarded and is used to help users understand concepts in data exploration, machine learning, and data visualization. It also helps to demonstrate a lot of concepts in data science. The user can analyse different areas of the dataset, such as data distribution, correlations between the different features, and to show when there is data that doesn't fit into the normal pattern, known as outliers.

#layout of document
0 is sepal length, 1 is sepal width, 2 is petal length, 3 is petal width

The histogram consists of several bar charts grouped together. These bar charts are made up from different data and gives the reader a pictorial representation of the data to show which values occur the most in a set of data.
A normal spread of data will look like the shape of a bell, hence the name “bell shaped” curve.

 ![image](https://github.com/kevinsenan/pands-project/assets/125194484/9dbfa69f-0e6e-4779-8ff7-a3d32d84a484)


4 histograms together on one plot
In the graph below, we can see a comparison of the data. The Sepal length shows a variance in the distribution whereas the sepal width is skewed to the left showing a distinct differenc ein one set of data. The petal length has a distinct outlier on the left side and while the petal width has some degree of commonality, again, there is a distinct outlier on the left side. This could show that we have a way of distinguishing at least one of the flowers.

pands-project\Histogram all four.png

To improve on the comparison, I can use a scatter plot. This will plot each data point on a graph and depending on how close the datapoints are grouped, we can see if there is overlap or any data points that show up as distinct.

In the first Scatter Plot, I am plotting the Sepal Length Iris-setosa is red, Iris-virginica is green and Iris-versicolor is blue. I can see that the Iris-setosa is placed separately to the other plots which shows a distinct difference between the flowers, whereas the other two colours are pretty much mixed together albeit with some differences at either end of the data limits. This would show to me that the sepal length would be a good start to distinguishing the Iris-setosa from the other flowers.


Virginica and versicolor have a significant crossover while setosa is distinct

2 and 3 petal length and width by flower
Virginica and versicolor have a crossover at the higher end of versicolor and the lower end of virginica whereas again setosa is distinct at the lower end of the scale

CORRELATION?
BOXPLOTS
The spread of the sepal and petal lengths and widths

Grouped by Iris 
0 is sepal length, top left
1 is sepal width, top right
2 is petal length, bottom left shows significant differences and 
3 is petal width bottom right

Singular grouped by Iris

Four individual box plot graphs

One big graph with all four on and a legend

![Alt text](Boxplot%20comparison.png)


REFERENCES:
[1] https://www.geeksforgeeks.org/how-to-read-csv-file-with-pandas-without-header/
[2] https://www.geeksforgeeks.org/how-to-add-header-row-to-a-pandas-dataframe/ 
[3] Python Data Analysis with Iris Dataset | Data Science, plotting & graphing, https://www.youtube.com/watch?v=02BFXhPQWHQ
[4] https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.plotting.boxplot.html
[5] https://stackoverflow.com/questions/47528955 adding-a-legend-to-a-matplotlib-boxplot-with-multiple-plots-on-same-axes
[6] https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_string.html
