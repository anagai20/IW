from dash import html, dcc
from dash.dependencies import Input, Output
from pages import create_lbw_race_page, payment_page,weight_gain_page,prenatal_care_page

from app import app

server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
   if pathname == '/payment':
      return payment_page()
   if pathname == '/weight_gain':
      return weight_gain_page()
   if pathname == '/prenatal_care':
      return prenatal_care_page()
   else:
      return create_lbw_race_page()


if __name__ == '__main__':
    app.run_server(debug=True)