import pandas as pd
import plotly.express as px

#Tabular From
df = pd.read_csv("/Users/drpoojayadav/Downloads/class 103/sa/csv files/line_chart.csv")
# OR
# data = ["Morrissey", "Marr", "Lennon", "McCartney" ]
# df = pd.DataFrame(data, #parameters)
# print(df)


#Line Graph
fig = px.line(df, x = "Year", y = "Per capita income", color = "Country", title = "Per Capita Income")
# fig.show()


#Bar Graph 
#reading data from csv file
graph = pd.read_csv("/Users/drpoojayadav/Downloads/class 103/sa/csv files/data.csv")
graph_img = px.bar(graph, x = "Country", y = "InternetUsers")
#graph_img.show()


#Scatter Plot
data = pd.read_csv('/Users/drpoojayadav/Downloads/class 103/sa/csv files/data.csv')
data_img = px.scatter(data, x = "Population", y = "Per capita", size = "Percentage", color = "Country", size_max = 60)
#data_img.show()