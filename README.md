# pands-project
Python Project ATU Data Analytics Course
The Iris Dataset
The Iris dataset is a multivariate dataset which means there is more than one variable in the dataset, Ronald Fisher first created it in 1936, he was a Statistician from the UK. This dataset has data on Iris flowers, specifically the Iris setosa, Iris versicolor, and the Iris virginica. The data is used to show the characteristics of length and width of sepals and of the petals.
It was created to help with the identification of the three species of Iris in the dataset , which ,as will be shown, can be tricky.

This dataset is highly regarded and is used to help users understand concepts in data exploration, machine learning, and data visualization. It also helps to demonstrate a lot of concepts in data science. The user can analyse different areas of the dataset, such as data distribution, correlations between the different features, and to show when there is data that doesn't fit into the normal pattern, known as outliers. [1]

The histogram consists of several bar charts grouped together [2]. These bar charts are made up from different data and gives the reader a pictorial representation of the data to show which values occur the most in a set of data.
A normal spread of data will look like the shape of a bell, hence the name “bell shaped” curve.

 ![image](https://github.com/kevinsenan/pands-project/assets/125194484/9dbfa69f-0e6e-4779-8ff7-a3d32d84a484)



In the graph below, we can see a comparison of the data [1]. The Sepal length shows a variance in the distribution whereas the sepal width is skewed to the left showing a distinct differenc ein one set of data. The petal length has a distinct outlier on the left side and while the petal width has some degree of commonality, again, there is a distinct outlier on the left side. This could show that we have a way of distinguishing at least one of the flowers. [3]

![Histogram all four](https://github.com/kevinsenan/pands-project/assets/125194484/a3f9cc8d-b8a9-4d3c-b501-354f008c89f7)


To improve on the comparison, I can use a scatter plot [4]. This will plot each data point on a graph and depending on how close the datapoints are grouped, we can see if there is overlap or any data points that show up as distinct.

In the first Scatter Plot, I am plotting the Sepal Length and Width where Iris-setosa is red, Iris-virginica is green and Iris-versicolor is blue. I can see that the Iris-setosa is placed separately to the other plots which shows a distinct difference between the flowers, whereas the other two colours are pretty much mixed together albeit with some differences at either end of the data limits. This would show to me that the sepal would be a good start to distinguishing the Iris-setosa from the other flowers.

![Scatter Sepal](https://github.com/kevinsenan/pands-project/assets/125194484/0d47a1ad-f06f-49ff-a06c-1f6549bbdbfe)

In the next scatter plot petal length and width are displayed. Again I can see the red plots are distinct and not mixed at all with the other plots , this leads me to the conclusion that the Iris-setosa is more distinct than the other two flowers.
Virginica and versicolor have a crossover at the higher end but versicolor does show some distinct plots at the lower end of the chart

![Scatter Petal](https://github.com/kevinsenan/pands-project/assets/125194484/a4d064df-e6f1-4935-a4e4-f79088305c09)


Another form of visual display is the boxplot [5]. In this graph, I can represent the data as a rectangular box with lines extending vertically. The extent of the lines shows the span of the data. In this plot we also see some small circles, these denote the outliers (or data which is outside of the general range of the data). The line horizontally through the rectangular box is the mean value of the data.[6]
we can see the sepal lengths and widths from the three types of flower are not clearly distinguishable, there is a marked difference between the petal length and width on the Iris-setosa compared to the others.
In the graph, they are in groups of 3 from left to right. The sepal data is on the left half and the petal data is on the right. It can easily be seen that the sepal data is all in close enough proximity whihc would suggest that the sepals on all three types of flower would not make the flowers easily distinguishable from each other although the Iris-setosa would seem to have sepal lengths less than the others. When we look at the petal data, the Iris-setosa is clearly on its own and this would suggest it is easy to distinguish this variety from the other two. If comparing the other two, I could possibly say the Iris-virginica would have bigger petals and the likelihood of identifying that flower against the Iris-versicolor using that as a comparison would make me correct more times than not.


![Alt text](Boxplot%20comparison.png)

NOTE
To run the program, open a command (cmd) window on your pc, type cd (to change directory but do not press enter) go to the folder it is saved in, drag and drop the folder into the cmd window where you typed cd, it should populate the directory structure automatically, now hit enter to change to the directory. Then type python analysis.py to run the program.

REFERENCES:
[1] https://www.geeksforgeeks.org/data-analysis-tutorial/

[2] https://www.geeksforgeeks.org/interpretations-of-histogram/ 

[3] https://chartio.com/learn/charts/histogram-complete-guide/

[4] https://www.geeksforgeeks.org/scatter-plot-using-plotly-in-python/

[5] https://www.geeksforgeeks.org/box-plot/

[6] https://www.simplypsychology.org/boxplots.html

