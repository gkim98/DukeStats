import pandas as pd
import dash_core_components as dcc   
import dash_html_components as html 
import plotly.graph_objs as go  
from dash.dependencies import Input, Output 
from datetime import datetime

from app import app


opp_df = pd.read_csv('..\..\DukeWebsite\data\data\opponents-sorted.csv')
# dataframe used for win data over the season
wins_df = opp_df.groupby(['season', 'date']).mean()

# dropdown options
season_options = [{
    'label': year,
    'value': year
} for year in opp_df['season'].unique()]


team_bar_graph = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(id='season-dropdown',
                options=season_options,
                value=[1991, 1992, 2001],
                multi=True)
        ], style={'width': '80%'}),
        
        dcc.Graph(id='team-graph',
            figure=dict(
            data=[],
            layout=go.Layout(title='default')
        ), config={'displayModeBar': False})
    ], style={'width':'60%'})
])

# graph for win totals
@app.callback(Output('team-graph', 'figure'),
    [Input('season-dropdown', 'value')])
def update_win_graph(seasons):
    if isinstance(seasons, int) : seasons = [seasons]

    traces = []

    # total games played line
    traces.append(go.Scatter(
        x=[0, 38],
        y=[0, 38],
        line=dict(dash='dash'),
        name='Games Played'
    ))

    for year in seasons:
        df = get_wins_df(year)
        x = df.index
        y = df['wins']
        trace = go.Scatter(
            x=x,
            y=y,
            name=year,
            mode='line',
            marker=dict(opacity=0.6)
        )
        traces.append(trace)

    fig=dict(
        data=traces,
        layout=go.Layout(
            xaxis=dict(
                title='games played',
                showgrid=False
            ),
            yaxis=dict(
                title='wins',
                showgrid=False
            )
        )
    )

    return fig











# processes data for win totals
def get_wins_df(year):
    df_slice = wins_df.xs(int(year), axis=0, level=0)
    df = df_slice.reset_index()
    df['date'] = convert_to_datetime(df['date'])
    df.sort_values(by='date')

    # keeps track of overall wins
    wins = []
    wins.append(0)
    for i in range(1, len(df.index)):
        if df['differential'][i] < 0 : wins.append(wins[i-1])
        else : wins.append(wins[i-1] + 1)
    df['wins'] = wins

    return df






# converts dates into datetimes
def convert_to_datetime(dates):
    return dates.map(full_date)

def full_date(date):
    index = date.find('/', date.find('/') + 1)
    year_prefix = '20' if int(date[index+1:])<50 else '19'
    full_date = date[:index+1] + year_prefix + date[index+1:]
    return datetime.strptime(full_date, '%m/%d/%Y')