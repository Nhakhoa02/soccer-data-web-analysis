import dash
import dash_bootstrap_components as dbc
import pandas as pd
import dash_table
import plotly.graph_objects as go
from dash import dcc, html, callback, Output, Input
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

dash.register_page(__name__)

file_path = 'soccer21-22.csv'
df = pd.read_csv("soccer21-22.csv")

# Define the available options for X and Y axes
x_options = [{'label': col, 'value': col} for col in df.columns]
y_options = [{'label': 'Count', 'value': 'count'}, {'label': 'Sum', 'value': 'sum'}, {'label': 'Average', 'value': 'mean'}]

data6 = df.iloc[91:100, :]
data7 = df.iloc[111:120, :]
data8 = df.iloc[140:149, :]

#fig1
custom_fig1 = px.scatter(data6, x='HomeTeam', y='HF', color='AF')

#fig2
custom_fig2 = px.scatter(data7, x='HomeTeam', y='HC', color='AC')

#fig3
custom_fig3 = px.scatter(data8, x = 'HomeTeam', y = 'HTHG', color = 'HTAG')

custom_plot_section = html.Div(
    className="graph-section",
    style={
        'backgroundColor': 'lightgray',
        'color': 'black',
        'padding': '20px',
    },
    children=[
        #fig1_section
        html.H2('The number of shots of the home teams in the third round of the 2021-2022 season', style={'color': 'black'}),
        
        dcc.Graph(
            figure=custom_fig1
        ),
        html.Div(
            [
                dcc.Markdown('''
                             
                    &nbsp;&nbsp;&nbsp;&nbsp;The diagram above shows the number of fouls made by the home teams within 10 seasons of 2021-2022. Looking at the chart, we can see that Watford. Watford has the most fouls in the round with 16 while Aston villa is last in statistics with about 3 fouls. 

                    &nbsp;&nbsp;&nbsp;&nbsp;Going into the details, we can see that in this round, NewCastle and Norwich have the same number of errors with the same 14. The same situation can also be seen in Burnley and Aston Villa with approximately the same 5 fouls. Moreover, this round recorded a relatively high number of fouls with 5 teams having the number of fouls greater than or equal to 10, for example Wolves, Man City, Tottenham, Newcastle, Norwich, Watford.

                ''')
            ],
            style = {'color': 'black'}
        ),



        #fig2_section
        html.H2('The number of goals in all matches of the away teams in the 5th round of the 2021-2022 season', style={'color': 'black'}),
        
        dcc.Graph(
            figure = custom_fig2
        ),
        html.Div(
            [
                dcc.Markdown('''
                             
                    &nbsp;&nbsp;&nbsp;&nbsp;The diagram above shows the number of corners taken by the home teams in the 12th round of the 2021-2022 season. Looking at the chart, we can witness that Watford has the most number of corners in the round with 9 times while Burnley has the least amount of corners with about 3 times. 

                    &nbsp;&nbsp;&nbsp;&nbsp;Going into details, Wolves and Man City have the same number of corners with 7 times. Similarly, Aston Villa and Norwich also have the same number of original penalties with 5 times. The number of corners is also high with 4 teams having more than 5 corners in this round such as Liverpool, Man City, Wolves and Newcastle. Meanwhile, two teams had corners less than 5 

                             
                ''')
            ],
            style = {'color': 'black'}
        ),


        #fig3_section
        html.H2('The number of shots on target of the home teams in the 6th round of the 2021-2022 season', style={'color': 'black'}),
        
        dcc.Graph(
            figure=custom_fig3
        ),
        html.Div(
            [
                dcc.Markdown('''
                             
                    &nbsp;&nbsp;&nbsp;&nbsp;The chart above shows the number of goals scored in the first half of the first half of the home team in the 15th round of the 2021-2022 season. Looking at the graph, we can see that there is a distinct difference. There are two separate groups. A group of 5 teams including Newcastle, Southampton, Leeds, Norwich and Tottenham scored 1 goal in the first half of the first half. In the opposite direction, 4 teams including Wolves, Man United, Everton, and Watford have not scored in this period of time.
                             
                ''')
            ],
            style = {'color': 'black'}
        ),


    ]
)

# Scatter plot section
scatter_plot_section = html.Div(
    className="graph-section",
    children=[
        html.H2('Scatter Plot'),
        html.Div(
            className="dropdowns",
            children=[
                dcc.Dropdown(
                    id='x-axis-dropdown-scatter',
                    options=x_options,
                    value=x_options[0]['value']
                ),
                dcc.Dropdown(
                    id='y-axis-dropdown-scatter',
                    options=x_options,
                    value=x_options[1]['value']
                ),
                dcc.RangeSlider(
                    id='range-slider-scatter',
                    min=0,
                    max=len(df),
                    value=[0, len(df)],
                    marks={0: 'Start', len(df): 'End'}
                )
            ]
        ),
        dcc.Graph(id='scatter-plot')
    ]
)

layout = html.Div(
    children=[
        scatter_plot_section,
        custom_plot_section
    ]
)

# Callback to update the scatter plot based on dropdown and range slider values
@callback(
    dash.dependencies.Output('scatter-plot', 'figure'),
    [dash.dependencies.Input('x-axis-dropdown-scatter', 'value'),
     dash.dependencies.Input('y-axis-dropdown-scatter', 'value'),
     dash.dependencies.Input('range-slider-scatter', 'value')]
)
def update_scatter_plot(x_axis, y_axis, range_value):
    start, end = range_value
    subset_df = df.iloc[start:end]

    fig = go.Figure(data=go.Scatter(x=subset_df[x_axis], y=subset_df[y_axis], mode='markers'))
    fig.update_layout(
        title=f'Scatter Plot ({x_axis} vs {y_axis})',
        xaxis_title=x_axis,
        yaxis_title=y_axis
    )

    return fig