import dash
import dash_bootstrap_components as dbc
import pandas as pd
import dash_table
import plotly.graph_objects as go
from dash import dcc, html, callback, Output, Input

dash.register_page(__name__)

file_path = 'C:/Users/Admin/Desktop/New folder (2)/soccer21-22.csv'
df = pd.read_csv(file_path)

data9 = df.iloc[371:380, :]
data10 = df.iloc[359:366, ] 
data11 = df.iloc[353:358, ]
data12 = df.iloc[343:352, ]

#fig1
custom_fig1 = go.Figure(data=go.Bar(
    x=data9['HomeTeam'],
    y=data9['HF'],
    width=1,  
    marker_color='yellow'
))

custom_fig1.update_layout(
    xaxis_title='HomeTeam',
    yaxis_title='HF',
    title='Total Yellow cards of AwayTeam in Round 35',
    xaxis_tickangle=-90
)

#fig2
custom_fig2 = go.Figure(data=go.Bar(
    x=data10['HomeTeam'],
    y=data10['HF'],
    width=1,  
    marker_color='yellow'
))

custom_fig2.update_layout(
    xaxis_title='HomeTeam',
    yaxis_title='HF',
    title='Total Fouls of Home Team in Round 34',
    xaxis_tickangle=-90
)

#fig3
custom_fig3 = go.Figure(data=go.Bar(
    x=data11['AwayTeam'],
    y=data11['AR'],
    width=1,  
    marker_color='blue'
))

custom_fig3.update_layout(
    xaxis_title='AwayTeam',
    yaxis_title='AR',
    title='Total Red cards of Away Team in Round 33',
    xaxis_tickangle=-90
)

#fig4
custom_fig4 = go.Figure(data=go.Bar(
    x=data12['HomeTeam'],
    y=data12['HC'],
    width=1,  
    marker_color='green'
))

custom_fig4.update_layout(
    xaxis_title='HomeTeam',
    yaxis_title='HC',
    title='Total Corners of Home Team in Round 32',
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
        html.H2('Statistics of the number of yellow cards that the away teams have received in the 35th round of the 2021-2022 season', style={'color': 'black'}),
        
        dcc.Graph(
            figure=custom_fig1
        ),
        html.Div(
            [
                dcc.Markdown('''
                             
                    &nbsp;&nbsp;&nbsp;&nbsp;The histogram statistics the number of yellow cards that the away teams including Brentford, Brighton, Burnley, Chelsea, Crystal Palace, Leicester, Liverpool, Man City, and Norwich must receive in the 35th round of the 2021 - 2022 season. Overall, there is a noticeable discrepancy between the required amount of yellow cards for each club. When we examine the specifics, we can find that Norwich holds the top spot on the list with 13 yellow cards, followed by Crystal Palace in second place with 12 yellow cards. Man City, as opposed to the other two clubs, must receive the fewest amount of yellow cards, only five. The fact that Brighton and Chelsea both have 9 yellow cards is a coincidence.

                ''')
            ],
            style = {'color': 'black'}
        ),



        #fig2_section
        html.H2('Statistics of the number of fouls that the home teams have made in the 34th round of the 2021-2022 season', style={'color': 'black'}),
        
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
        html.H2('Statistics of the number of red cards that the away teams have received in the 33rd round of the 2021-2022 season', style={'color': 'black'}),
        
        dcc.Graph(
            figure=custom_fig3
        ),
        html.Div(
            [
                dcc.Markdown('''
                             
                    &nbsp;&nbsp;&nbsp;&nbsp;The histogram statistics the number of red cards that the away teams including Chelsea, Norwich, Everton, Man City, and Arsenal had to receive in the 33rd round of the 2021 - 2022 season. In general, the number of teams receiving cards is not the same. Going into details, Arsenal is the only away team to receive a red card in this round with one card.
                             
                ''')
            ],
            style = {'color': 'black'}
        ),

        #fig4_section
        html.H2('Statistics of the number of corners taken by the home teams in the 32nd round of the 2021-2022 season', style={'color': 'black'}),
        
        dcc.Graph(
            figure=custom_fig4
        ),
        html.Div(
            [
                dcc.Markdown('''
                             
                    &nbsp;&nbsp;&nbsp;&nbsp;The histogram statistics the number of corners that the home teams including Burnley, Chelsea, Crystal Palace, Brighton, Liverpool, Arsenal, Leicester, Norwich, and Man City have taken in the 32nd round of the 2021-2022 season. In general, there is a clear difference in the number of corners between the teams. Going into details, we can see that Liverpool is the team that takes the most corners with more than 10 times. Following are two teams Chelsea and Norwich with 9 corners and divided in 2nd place. Contrary to the above three teams, Burnley is the team that has taken the fewest corners with 4 times. More specifically, in this statistic, there are three teams with the same number of corners taken: Crystal Palace, Arsenal, and Man City with 8 times.
                             
                ''')
            ],
            style = {'color': 'black'}
        ),


    ]
)

# Histogram plot section
histogram_section = html.Div(
    className="graph-section",
    children=[
        html.H2('Histogram Plot'),
        html.Div(
            className="dropdowns",
            children=[
                dcc.Dropdown(
                    id='x-axis-dropdown-hist',
                    options=[{'label': col, 'value': col} for col in df.columns],
                    value=df.columns[0]
                ),
                dcc.Dropdown(
                    id='hist-bins-dropdown',
                    options=[
                        {'label': '10', 'value': 10},
                        {'label': '20', 'value': 20},
                        {'label': '30', 'value': 30}
                    ],
                    value=10
                ),
                dcc.Dropdown(
                    id='hist-color-dropdown',
                    options=[{'label': 'Blue', 'value': 'blue'}, {'label': 'Red', 'value': 'red'}],
                    value='blue'
                )
            ]
        ),
        dcc.Graph(id='histogram-plot')
    ]
)

layout = html.Div(
    children=[
        histogram_section,
        custom_plot_section
    ]
)

# Callback to update the histogram plot based on dropdown values
@callback(
    Output('histogram-plot', 'figure'),
    [Input('x-axis-dropdown-hist', 'value'),
     Input('hist-bins-dropdown', 'value'),
     Input('hist-color-dropdown', 'value')]
)
def update_histogram_plot(x_axis, num_bins, hist_color):
    data = df[x_axis]
    fig = go.Figure(data=[go.Histogram(x=data, nbinsx=num_bins, marker_color=hist_color)])

    fig.update_layout(title=f'Histogram Plot: {x_axis}', xaxis_title=x_axis, yaxis_title='Count')

    return fig
