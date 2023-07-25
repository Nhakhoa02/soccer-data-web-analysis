import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import dash_table
import plotly.graph_objects as go
from dash import dcc, html, callback, Output, Input
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

dash.register_page(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/Nhakhoa02/soccer-data-web-analysis/main/src/soccer21-22.csv", encoding= "latin")

# Line graph section
line_graph_section = html.Div(
    className="graph-section",
    children=[
        html.H2('Line Graph'),
        html.Div(
            className="dropdowns",
            children=[
                dcc.Dropdown(
                    id='x-axis-dropdown-line',
                    options=[{'label': col, 'value': col} for col in df.columns],
                    value=df.columns[0]
                ),
                dcc.Dropdown(
                    id='y-axis-dropdown-line',
                    options=[{'label': col, 'value': col} for col in df.columns],
                    value=df.columns[1]
                ),
                dcc.Dropdown(
                    id='line-type-dropdown',
                    options=[{'label': 'Line', 'value': 'line'}, {'label': 'Scatter', 'value': 'scatter'}],
                    value='line'
                ),
                dcc.Dropdown(
                    id='line-color-dropdown',
                    options=[{'label': 'Blue', 'value': 'blue'}, {'label': 'Red', 'value': 'red'}],
                    value='blue'
                ),
                dcc.Dropdown(
                    id='line-style-dropdown',
                    options=[{'label': 'Solid', 'value': 'solid'}, {'label': 'Dashed', 'value': 'dash'},
                             {'label': 'Dotted', 'value': 'dot'}, {'label': 'Dashdot', 'value': 'dashdot'}],
                    value='solid'
                )
            ]
        ),
        dcc.Graph(id='line-graph')
    ]
)

#fig 1
custom_fig1 = px.line(x=[8, 16, 14], y=['M Oliver', 'P Tierney', 'D Coote'])
custom_fig1.update_traces(line=dict(dash='dash'))

#fig 2
custom_fig2 = px.line(x = ['Arsenal', 'Leeds', 'Brighton', 'Crystal Palace', 'Southampton', 'Wolves', 'Aston Villa', 'Liverpool', 'West Ham', 'Man City'], y = ['2', '5', '1', '3', '3', '1', '3', '0', '2', '1'])
custom_fig2.update_traces(line =dict(dash='dash'))

#fig3
custom_fig3 = px.line(x = ['Brentdord', 'Man United', 'Burnley', 'Chelsea'], y = [3,8,3,6])
custom_fig3.update_traces(line=dict(dash='dash'))

custom_plot_section = html.Div(
    className="graph-section",
    style={
        'backgroundColor': 'lightgray',
        'color': 'black',
        'padding': '20px',
    },
    children=[
        #fig1_section
        html.H2('Shot on target by the home team when three referees blow the whistle', style={'color': 'black'}),
        
        dcc.Graph(
            figure=custom_fig1
        ),
        html.P(
            "M Oliver is the referee from the United Kingdom of Great Britain and Northern Ireland. P Tierney controlled the home team's match, a match with only 8 shots that the home team brought. The referee from the United Kingdom of Great Britain and Northern Ireland, P Tierney, led the home match with 16 shots, which is quite a surprising and respectable number. And finally, D Coote - the British referee with his control of the game, the home team launched 14 shots during the performance, a pretty great number for the players.",
            style={'color': 'black'}
        ),


        #fig2_section
        html.H2('The number of goals scored by away teams in the first round of matches.', style={'color': 'black'}),
        
        dcc.Graph(
            figure=custom_fig2
        ),
        html.P(
            "Starting with Liverpool's poor performance, zero is the number of goals the team has brought. Followed by an extremely difficult match between the Wolves and Man City brought me 1 goal. Arsenal and West Ham are two teams with the same number of goals in the away teams in the first round of 2 goals. With his shooting, 3 is a great number that Crystal Palace and Southampton have achieved.",
            style={'color': 'black'}
        ),


        #fig3_section
        html.H2('The number of shots by home teams in the first four matches of the 2021-2022 season', style={'color': 'black'}),
        
        dcc.Graph(
            figure=custom_fig3
        ),
        html.P(
            "In the 2021-2022 season, we first came to the home team Brentford; with the game progressing, nothing special and stable, Brentford got himself 3 shots in 4 matches in the first round. Next was the Man United team, a match with continuous shots on the opposing team up to 8 shots. Like Brentford, Burnley, the home team, also brought a stable rhythm to the game when the number of shots was 3. Finally, the Chelsea team had a rather fast pace and brought themselves 6 shots in the round. first season 2021-2022.",
            style={'color': 'black'}
        )


    ]
)



layout = html.Div(
    children= [
        line_graph_section,
        custom_plot_section
    ]
)

# Callback to update the line graph based on dropdown values
@callback(
    Output('line-graph', 'figure'),
    [Input('x-axis-dropdown-line', 'value'),
     Input('y-axis-dropdown-line', 'value'),
     Input('line-type-dropdown', 'value'),
     Input('line-color-dropdown', 'value'),
     Input('line-style-dropdown', 'value')]
)
def update_line_graph(x_axis, y_axis, line_type, line_color, line_style):
    fig = go.Figure()

    if line_type == 'line':
        fig.add_trace(go.Scatter(x=df[x_axis], y=df[y_axis], mode='lines', line_color=line_color, line_dash=line_style))
    elif line_type == 'scatter':
        fig.add_trace(go.Scatter(x=df[x_axis], y=df[y_axis], mode='markers', marker_color=line_color))

    fig.update_layout(title=f'Line Graph: {x_axis} vs {y_axis}')

    return fig
