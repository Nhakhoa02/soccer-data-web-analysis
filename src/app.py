import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB])
server = app.server

sidebar = dbc.Nav(
    [
        dbc.NavLink(
            [
                html.Div(page["name"], className="ms-2"),
            ],
            href=page["path"],
            active="exact",
        )
        for page in dash.page_registry.values()
    ],
    vertical=True,
    pills=True,
    className="bg-light",
)

app.layout = html.Div(
    style={
        'background-image': 'url("/assets/igOxsl.gif")',
        'background-repeat': 'no-repeat',
        'background-size': 'cover',

    },
    children=[
        dcc.Store(id='uploaded-data', data={}),
        html.Div(
            style={
                'backgroundColor': 'rgba(255, 255, 255, 0.8)',
                'padding': '20px',
                'text-align': 'center',
            },
            children=[
                html.H1(
                    "Premier League Status Season 2021-2022",
                    style={
                        'font-size': '36px',
                    }
                )
            ]
        ),

        html.Hr(),

        html.Div(
            style={
                'display': 'flex',
                'flex-direction': 'row',
            },
            children=[
                html.Div(
                    style={
                        'flex': '1',
                        'backgroundColor': 'rgba(255, 255, 255, 0.8)',
                        'padding': '20px',
                    },
                    children=[sidebar]
                ),

                html.Div(
                    style={
                        'flex': '4',
                        'backgroundColor': 'rgba(255, 255, 255, 0.8)',
                        'padding': '20px',
                    },
                    children=[dash.page_container]
                )
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
