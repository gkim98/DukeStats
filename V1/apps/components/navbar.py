import dash_html_components as html 
import dash_core_components as dcc   


# permanent variables
url_paths = ['/players', '/team']
page_names = ['Players', 'Team']
navbar_color = 'rgb(50, 99, 205)'

# styling for a link in the nav bar
link_style = {
    'width': '100px',
    'backgroundColor': navbar_color,
    'textAlign': 'center',
    'color': 'white',
    'display': 'inline-block',
    'border': '1px solid black',
    'padding': '5px 0px 5px 0px'
}

# create links for nav bar
links = []
for i in range(len(url_paths)):
    link = html.Div([
        dcc.Link(page_names[i], href=url_paths[i])
    ], style=link_style)
    links.append(link)


navbar = html.Div(
    links,
    style={
        'fontFamily': 'arial',
        'marginBottom': '100px'
    }
)