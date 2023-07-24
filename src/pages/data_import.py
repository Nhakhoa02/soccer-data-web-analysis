import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import dash_table
import plotly.graph_objects as go

# Initialize the Dash app
dash.register_page(__name__, path='/', name='Home') # '/' is home page

# Define the DataFrame as a global variable
file_path = 'soccer21-22.csv'
df = pd.read_csv("soccer21-22.csv")

# Data Import Section
sample_data = html.Div(
    className="sample-data",
    children=[
        html.H1('Soccer Data', className="text-center"),
        html.Div(
            className="scroll-table",
            style={'height': '400px', 'overflowY': 'scroll'},
            children=dash_table.DataTable(
                id='data-table',
                columns=[{'name': col, 'id': col} for col in df.columns],
                data=df.to_dict('records'),
                style_data={
                    'whiteSpace': 'normal',
                    'height': 'auto'
                },
                style_table={'overflowX': 'scroll'},
            )
        )
    ]
)

# Define the layout of the app
layout = html.Div(
    children=[
        html.Div(
            children=[
               sample_data,
                # Add other sections here
            ]
        )
    ]
)


