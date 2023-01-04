from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

all_options = {
    'Regresja': ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide'],
    'Klasyfikacja': ['density', 'sulphates', 'alcohol', 'quality']
}

df = pd.read_csv('\\Users\\pawellopatynski\\Desktop\\Studia\\PAD\\cw 6\\winequelity.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(html.Tr([html.Th(col) for col in dataframe.columns])),
        html.Tbody([
            html.Tr([html.Td(dataframe.iloc[i][col]) for col in dataframe.columns])
            for i in range(min(len(dataframe), max_rows))
        ])
    ])


app.layout = html.Div([
    html.H4(children='Wine quality'),
    generate_table(df),
    html.Br(),
    html.Label('Typ wykresu: '),
    dcc.RadioItems(['Regresja', 'Klasyfikacja'],
                   'Regresja',
                   id = 'chart-radio'),
    html.Br(),
    html.Label('Zmienna: '),
    dcc.RadioItems(id='variable-radio'),
    dcc.Graph(id='graph')
])


@app.callback(
    Output('variable-radio', 'options'),
    Input('chart-radio', 'value'))

def set_variables_options(selected_option):
    return [{'label': i, 'value': i} for i in all_options[selected_option]]


@app.callback(
    Output('variable-radio', 'value'),
    Input('variable-radio', 'options'))

def set_variables_value(available_options):
    return available_options[0]['value']

@app.callback(
    Output('graph', 'figure'),
    Input('variable-radio', 'value'),
    Input('chart-radio', 'value'))

def update_graph(variable, chart):

    if chart == 'Klasyfikacja':
        fig = px.scatter(x=df['target'],
                         y=df[variable],
                         labels={"x": "target",
                                 "y": variable},
                         width=750,
                         height=1000)

        fig.update_layout(margin={'l': 50,
                                  'b': 50,
                                  't': 15,
                                  'r': 0},
                          hovermode='closest')
        return fig

    else:
        fig = px.scatter(x=df['pH'],
                         y=df[variable],
                         labels={"x": "pH",
                                 "y": variable},
                         width=1000,
                         height=400)

        fig.update_layout(margin={'l': 50,
                                  'b': 50,
                                  't': 15,
                                  'r': 0},
                          hovermode='closest')
        return fig

if __name__ == '__main__':
    app.run_server(debug=True)