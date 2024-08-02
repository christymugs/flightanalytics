# app.py
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv('flights_data.csv')

app = dash.Dash(__name__)

def generate_chart(df):
    fig = px.line(df, x='departure', y='status', title='Flight Status Over Time')
    return fig

app.layout = html.Div(children=[
    html.H1(children='Flight Data Analytics'),
    dcc.Graph(id='flight-status-chart', figure=generate_chart(df))
])

if __name__ == '__main__':
    app.run_server(debug=True)
