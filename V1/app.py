"""
    DON'T TOUCH
"""

import dash  

app = dash.Dash()
server = app.server 
app.config.suppress_callback_exceptions=True 

# removes undo button
app.css.append_css({
    'external_url': (
        'https://rawgit.com/gkim98/DukeStats/master/styling/app.css'
    )
})
