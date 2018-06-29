import dash_core_components as dcc   
import dash_html_components as html 
from dash.dependencies import Input, Output

from app import app 
import sys
sys.path.append('./apps/')

from components.navbar import navbar

layout = html.Div([
    navbar,
    html.H1('Page 1')

])