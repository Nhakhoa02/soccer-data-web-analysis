import dash
import dash_bootstrap_components as dbc
import pandas as pd
import dash_table
import plotly.graph_objects as go
from dash import dcc, html, callback, Output, Input
import numpy as np
import matplotlib.pyplot as plt

dash.register_page(__name__)

file_path = 'soccer21-22.csv'
df = pd.read_csv(file_path)

# Define the available options for X axis
x_options = [{'label': col, 'value': col} for col in df.columns]

data13 = df.iloc[333:342, ]
data14 = df.iloc[322:332, ]
data15 = df.iloc[316:321, ]

#fig1
mycolor_fig1 = data13['HomeTeam']

custom_fig1 = go.Figure(data=go.Pie(
    labels=data13['HomeTeam'], 
    values=data13['HST'],                             
    marker=dict(colors=mycolor_fig1), 
    textinfo='percent', 
))

#fig2
mycolor_fig2 = data13['HomeTeam']

custom_fig2 = go.Figure(data=go.Pie(
    labels=data14['HomeTeam'], 
    values=data14['HS'],                            
    marker=dict(colors=mycolor_fig2), 
    textinfo='percent', 
))

#fig3
mycolor_fig3 = data15['HomeTeam']

custom_fig3 = go.Figure(data=go.Pie(
    labels=data15['AwayTeam'], 
    values=data15['AST'],                            
    marker=dict(colors=mycolor_fig3), 
    textinfo='percent', 
))

custom_plot_section = html.Div(
    className="graph-section",
    style={
        'backgroundColor': 'lightgray',
        'color': 'black',
        'padding': '20px',
    },
    children=[
        #fig1_section
        html.H2('The number of shots on target of the home teams in the 31st round of buying 2021-2022', style={'color': 'black'}),
        
        dcc.Graph(
            figure=custom_fig1
        ),
        html.Div(
            [
                dcc.Markdown('''
                             
                    &nbsp;&nbsp;&nbsp;&nbsp;The given chart illustrates data on the goals scored by various home teams in the 31st football season (2021-2022). The aim of this report is to highlight the comparative performance of these teams based on the recorded number of goals.
 
                    &nbsp;&nbsp;&nbsp;&nbsp;The chart shows a clear distinction in the goal tally amongst the teams. Tottenham scored the most goals with 21.9, followed by Aston Villa with 18.8. Manchester United and Everton also performed well, scoring 15.6 and 12.5 goals respectively. Southampton and West Ham tied, with each scoring 9.4 goals. 

                    &nbsp;&nbsp;&nbsp;&nbsp;On the other end of the spectrum, Watford, Wolves, and Leeds initially scored fewer goals, each only attaining a tally of 3.1. However, Leeds made a significant improvement in the latter half of the season, doubling their goal count to 6.2. 

                    &nbsp;&nbsp;&nbsp;&nbsp;In conclusion, the chart displays a considerable variation in home team performance during the 31st football season. The data suggests that there is potential for improvement, as seen in Leeds, and also emphasizes the role of effective strategies and player abilities in scoring goals. Future investigations could focus on factors such as player statistics, team strategies, and coaching influences on overall team performance. 

                ''')
            ],
            style = {'color': 'black'}
        ),



        #fig2_section
        html.H2('The number of shots of the home teams in the 30th round buy 2021-2022', style={'color': 'black'}),
        
        dcc.Graph(
            figure=custom_fig2
        ),
        html.Div(
            [
                dcc.Markdown('''
                             
                    &nbsp;&nbsp;&nbsp;&nbsp;The pie chart demonstrates data on the percentage of goals scored by different home teams in the 30th football season (2021-2022). The teams include Norwich, Manchester City, Leicester, Manchester United, Crystal Palace, Liverpool, Chelsea, Burnley, Brighton, and Brentford. 

                    &nbsp;&nbsp;&nbsp;&nbsp;The chart shows a marked disparity in the goal-scoring percentages amongst the teams. Chelsea had the highest percentage, contributing 19.3% of the total goals, followed by Manchester City with 15.6%. Liverpool and Crystal Palace also performed well, scoring 13.3% and 12.6% of the goals respectively. Brentford and Burnley also had decent performances, with percentages of 11.1% and 10.4% respectively. 

                    &nbsp;&nbsp;&nbsp;&nbsp;On the other hand, some teams had a lower contribution to the total goals. Norwich and Leicester shared an equal percentage of 3.7%, while Manchester United and Brighton scored slightly higher percentages of 4.4% and 5.9% respectively. 

                    &nbsp;&nbsp;&nbsp;&nbsp;In conclusion, the chart provides a vivid representation of the varied performance levels of home teams in terms of goal-scoring percentages during the 30th football season. This analysis provides valuable insights for future football analytics and performance improvement strategies.


                ''')
            ],
            style = {'color': 'black'}
        ),


        #fig3_section
        html.H2('The number of shots on target of the away teams in the 29th round buy 2021-2022', style={'color': 'black'}),
        
        dcc.Graph(
            figure=custom_fig3
        ),
        html.Div(
            [
                dcc.Markdown('''
                    &nbsp;&nbsp;&nbsp;&nbsp;The given pie chart shows information about the goal scoring percentages of different home teams during the 29th football season (2021-2022). The teams under scrutiny are Arsenal, Southampton, Brighton, Crystal Palace, and Leicester. 

                    &nbsp;&nbsp;&nbsp;&nbsp;As can be seen from the chart, there is a wide disparity in the percentages of goals scored by these teams. Arsenal secured the top spot, accounting for 30.8% of the total goals scored. Southampton and Leicester also exhibited solid performances, each contributing 23.1% to the overall goals. Crystal Palace scored 15.4% of the total goals, whereas Brighton trailed with a contribution of only 7.7%. 

                    &nbsp;&nbsp;&nbsp;&nbsp;To conclude, the chart presents a comprehensive view of the varied performance levels of the home teams in terms of goal scoring percentages during the 29th football season. This data-driven analysis can potentially inform future football analytics and strategic planning aimed at improving team performance. 


                ''')
            ],
            style = {'color': 'black'}
        ),


    ]
)

# Pie plot section
pie_plot_section = html.Div(
    className="graph-section",
    children=[
        html.H2('Pie Plot'),
        html.Div(
            className="dropdowns",
            children=[
                dcc.Dropdown(
                    id='x-axis-dropdown-pie',
                    options=x_options,
                    value=x_options[0]['value']
                ),
            ]
        ),
        dcc.Graph(id='pie-plot')
    ]
)

layout = html.Div(
    children= [
        pie_plot_section,
        custom_plot_section
    ]
)


# Callback to update the pie plot based on dropdown value
@callback(
    dash.dependencies.Output('pie-plot', 'figure'),
    [dash.dependencies.Input('x-axis-dropdown-pie', 'value')]
)
def update_pie_plot(x_axis):
    x_data = df[x_axis].value_counts()

    fig = go.Figure(data=go.Pie(labels=x_data.index, values=x_data))
    fig.update_layout(
        title=f'Pie Plot ({x_axis})'
    )

    return fig
