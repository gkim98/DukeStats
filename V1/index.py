import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output

from app import app 
from apps import players, team

# testing
import apps


app.layout = html.Div([
    # represents URL bar, doesn't do anything
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), 
                [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/players':
        return players.layout
    elif pathname == '/team':
        return team.layout
    else:
        return players.layout


if __name__ == '__main__':
    app.run_server()

    