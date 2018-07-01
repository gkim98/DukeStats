import dash_core_components as dcc   
import dash_html_components as html 
from dash.dependencies import Input, Output

from app import app 
import sys
sys.path.append('./apps/')

from components.navbar import navbar
from components.team_graphs import team_bar_graph

layout = html.Div([
    navbar,
    team_bar_graph

])