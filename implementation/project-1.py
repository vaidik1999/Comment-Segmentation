import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H3(children='Comment segmantation'),

    html.Div(children='''
        Amazon mobile data sentiment .
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'positive'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'negative'},
            ],
            'layout': {
                'title': 'Sentiment Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
