import dash_html_components as html 
import dash_core_components as dcc   


# permanent variables
url_paths = ['/home', '/players', '/team']
page_names = ['Home', 'Players', 'Team']
navbar_color = '#001A57'

# styling for a link in the nav bar
link_style = dict(
    width='100px',
    backgroundColor=navbar_color,
    textAlign='center',
    color='white',
    display='inline-block',
    border='0.5px solid black',
    padding='10px 5px 10px 5px',
    borderRadius='10px',
    opacity='0.6'
)

# create links for nav bar
links = []
for i in range(len(url_paths)):
    link = html.Div([
        dcc.Link(page_names[i], href=url_paths[i])
    ], style=link_style, className='link')
    links.append(link)


navbar = html.Div(
    links,
    style=dict(
        fontFamily='arial',
        marginBottom='100px'
    )
)