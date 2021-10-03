import pandas as pd
import plotly.express as pe
df = pd.read_csv('covid.csv')
graph = pe.scatter(df, x = 'date', y = 'cases', color = 'country')
graph.show()