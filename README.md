# Class 103

Code to display given data in -
1. Tabular Form
2. Line Graph
3. Bar Graph
4. Scatter Plot 

<p>
  Used Libraries - 
  <br><b>Pandas</b><br>
  https://pandas.pydata.org/docs/
  <br><b>Plotly Express</b><br>
  https://plotly.com/python/plotly-express/
  
<p>
  First read file -> file = pandas.read_csv(<i>file path</i>)
  <br><b>Tabular Form</b> -> print(file)
  <br><b>Bar Graph</b> -> plotly.express.bar(file, x, y)
  <br><b>Line Graph</b> -> plotly.express.line(file, x, y, color, title)
  <br><b>Scatter Plot</b> -> plotly.express.scatter(file, x, y, size, color, title)
