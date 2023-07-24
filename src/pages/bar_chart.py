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

df = pd.read_csv('src/assets/soccer21-22.csv')

# Define the available options for X and Y axes
x_options = [{'label': col, 'value': col} for col in df.columns]
y_options = [{'label': 'Count', 'value': 'count'}, {'label': 'Sum', 'value': 'sum'}, {'label': 'Average', 'value': 'mean'}]

# Bar chart section
bar_chart_section = html.Div(
    className="bar-chart-section",
    children=[
        html.H2('Bar Chart'),
        html.Div(
            className="dropdowns",
            children=[
                dcc.Dropdown(
                    id='x-axis-dropdown',
                    options=x_options,
                    value=x_options[0]['value']
                ),
                dcc.Dropdown(
                    id='y-axis-dropdown',
                    options=y_options,
                    value=y_options[0]['value']
                ),
                dcc.RangeSlider(
                    id='range-slider',
                    min=0,
                    max=len(df),
                    value=[0, len(df)],
                    marks={0: 'Start', len(df): 'End'}
                )
            ]
        ),
        dcc.Graph(id='bar-chart')
    ]
)

data2 = df.iloc[21:30, :]
data3 = df.iloc[41:50, :]
data4 = df.iloc[51:60, :]


#fig 1
custom_fig1 = go.Figure(data=[
    go.Bar(x=data2['HomeTeam'], y=data2['HS'])
])

custom_fig1.update_layout(
    title='Home Team Shots',
    xaxis=dict(title='HomeTeam'),
    yaxis=dict(title='Shots'),
    xaxis_tickangle=-90
)

#fig 2
custom_fig2 = go.Figure(data=[
    go.Bar(x = data3['AwayTeam'],y = data3['FTAG'])
])

custom_fig2.update_layout(
    title='Away Team Goals',
    xaxis=dict(title='AwayTeam'),
    yaxis=dict(title='Goals'),
    xaxis_tickangle=-90
)

#fig3
custom_fig3 = go.Figure(data=[
    go.Bar(x = data4['HomeTeam'],y = data4['HST'])
])

custom_fig3.update_layout(
    title='Home Team Shots On Target',
    xaxis=dict(title='HomeTeam'),
    yaxis=dict(title='Shots on Target'),
    xaxis_tickangle=-90
)

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
                             
                    &nbsp;&nbsp;&nbsp;&nbsp;The bar graph depicts the amount of shots taken by the home teams in the third round of the 2021-2022 season. Overall, Liverpool had the most shots, while Aston Villa had the fewest from the nine named teams: Aston Villa, Brighton, Newcastle, Norwich, West Ham, Liverpool, Burnley, Tottenham, and Wolves.
                    
                    &nbsp;&nbsp;&nbsp;&nbsp;As can be seen from the table, Liverpool's total shots almost reached a peak at 24 shots to the goals in the third round. Brighton, Norwich and West Ham show the exact same number of 14 shots made by each team's players. Meanwhile, Tottenham and Wolves have slightly increased shots, 15 shots to the goal in the third round of the 2021-2022 season.
                    
                    &nbsp;&nbsp;&nbsp;&nbsp;In another hand, Aston Villa in the third round played unsuccessfully with only 7 shots made. Similarly, Newcastle only made 9 shots. However, Burnley in the third round showed more shots than the two others with 13 shots made.
                    
                    &nbsp;&nbsp;&nbsp;&nbsp;In conclusion, Liverpool had a good performance in the third round of the 2021-2022 season with 24 shots taken while Aston Villa only had 7 shots taken.
                ''')
            ],
            style = {'color': 'black'}
        ),



        #fig2_section
        html.H2('The number of goals in all matches of the away teams in the 5th round of the 2021-2022 season', style={'color': 'black'}),
        
        dcc.Graph(
            figure=custom_fig2
        ),
        html.Div(
            [
                dcc.Markdown('''
                             
                    &nbsp;&nbsp;&nbsp;&nbsp;The bar chart depicts the percentage of shots that make up the goals of the away teams in the fifth round of the 2021-2022 season. Overall, Watford and Chelsea are the two teams with the most goals in this round and there are three teams that have not scored at all: Crystal Palace, Southampton and Everton. 
                             
                    &nbsp;&nbsp;&nbsp;&nbsp;As can be seen from the table, Watford and Chelsea are 2 teams out of 9 away teams that have scored the most goals in the fifth round of the 2021-2022 season with a rate of shots in each match of 2.9%. Likewise, Brentford and Man United also have a high rate of shots with 2.0%.
                             
                    &nbsp;&nbsp;&nbsp;&nbsp;On the other hand, Crystal Palace, Southampton and Everton, on the other hand, did not fare well in the fifth round of the 2021-2022 season, with 0% scored. Go with it, Arsenal and Leicester had only 1% rate of scoring. 
                             
                    &nbsp;&nbsp;&nbsp;&nbsp;In conclusion, Watford and Chelsea scored most goals in round 5 of the 21-22 season. Therefore, Crystal Palace, Southampton and Everton players didn’t score any goals for their teams.

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
                    &nbsp;&nbsp;&nbsp;&nbsp;The bar chart illustrates the number of successful shots on goal of the home teams in the sixth round of the 2021-2022 season. Arsenal had the most accurate shots on target overall, while Crystal Palace had the least accurate shots on target.

                    &nbsp;&nbsp;&nbsp;&nbsp;As can be seen from the table, Arsenal is one of the nine teams with the most shots on goal, with exactly 24 shots. Second place was Southampton with 6 shots on target in the 6th round of the tournament. Likewise, Leeds and Leicester also have 5 exactly shots on target. 
                             
                    &nbsp;&nbsp;&nbsp;&nbsp;On the other hand, Crystal Palace is the team with the least number of hits, 3 shots. Meanwhile, Man United, Everton, Watford, and Brentford are the remaining four teams with similar total shots and a hit rate of four shots.
                             
                    &nbsp;&nbsp;&nbsp;&nbsp;In conclusion, Arsenal holds the record with 7 shots on target in the sixth round of the 21-22 season. However, Crystal Palace only got 3 shots on target.

                ''')
            ],
            style = {'color': 'black'}
        ),


    ]
)

layout = html.Div(
    children=[
        bar_chart_section,
        custom_plot_section
    ]
)

# Callback to update the bar chart based on dropdown and range slider values
@callback(
    dash.dependencies.Output('bar-chart', 'figure'),
    [dash.dependencies.Input('x-axis-dropdown', 'value'),
     dash.dependencies.Input('y-axis-dropdown', 'value'),
     dash.dependencies.Input('range-slider', 'value')]
)
def update_bar_chart(x_axis, y_axis, range_value):
    start, end = range_value
    subset_df = df.iloc[start:end]

    if y_axis == 'count':
        y_data = subset_df[x_axis].value_counts()
    elif y_axis == 'sum':
        y_data = subset_df.groupby(x_axis).sum()
    else:  # y_axis == 'mean'
        y_data = subset_df.groupby(x_axis).mean()

    fig = go.Figure(data=go.Bar(x=y_data.index, y=y_data))
    fig.update_layout(
        title=f'Bar Chart ({x_axis} vs {y_axis})',
        xaxis_title=x_axis,
        yaxis_title=y_axis
    )

    return fig

