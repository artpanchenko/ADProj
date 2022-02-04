import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output

# Load data
df = pd.read_csv('data/stockdata2.csv', index_col=0, parse_dates=True)
dataset = pd.read_csv('data/HRDataset_v14.csv')
df.index = pd.to_datetime(df['Date'])

# Initialise the app
app = dash.Dash(__name__)

# Define the app
app.layout = html.Div()
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)