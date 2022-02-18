
from dash import  dcc, html, dash
import pandas as pd
import plotly.express as px



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('C://Users//Anand//Desktop//dataviz/bestsellers_amazon.csv')

print(df.head(10))

print(df.isnull().sum())
print(df.describe())
print(df.info())
print (f"Total number of rows : {df.shape[0]}\nTotal number of columns : {df.shape[1]}")


fig1=px.histogram(df,x='User Rating',barmode="group",nbins=40,)

fig2=px.histogram(x=df['Genre'],color=df['Genre'])


import plotly.figure_factory as ff
import numpy as np
np.random.seed(40)
x=df['User Rating']
group_labels = ['User rating']
fig3 = ff.create_distplot([x],group_labels,bin_size=0.1)


fig4=px.histogram(y=df['Price'],x=df['Genre'],color=df['Genre'])



fig5=px.histogram(y=df['User Rating'],x=df['Genre'],color=df['Genre'])




fig6=px.histogram(df['Price'])



x=df['Genre'].value_counts()
fig7=px.pie( values=[x[0],x[1]], names=['Non Fiction','Fiction'], title='Population of European continent')

import plotly.graph_objects as go


fig8= go.Figure()
fig8.add_trace(go.Bar(x=df['Year'],y=df['User Rating'],name='Genre',marker_color='indianred'))
fig8.add_trace(go.Bar(x=df['Year'],y=df['User Rating'],name='Genre',marker_color='lightsalmon'))
# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig8.update_layout(barmode='group', xaxis_tickangle=-45)


fig9=px.scatter(df['Reviews'],df['Price'],color=df['Genre'])


app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.H2(children='User Rating'),
        html.Div(children='''
            Bar Chart (Total Score)
        '''),
        dcc.Graph(
            id='graph1',
            figure=fig1
        ),
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H2(children='Genre'),
        html.Div(children='''
             Bar Chart (Total Score)
         '''),
        dcc.Graph(
            id='graph2',
            figure=fig2
        ),
    ]),
    html.Div([
        html.H2(children='User Rating'),
        html.Div(children='''
             Bar Chart (Total Score)
         '''),
        dcc.Graph(
            id='graph3',
            figure=fig3
        ),
    ]),
    html.Div([
        html.H2(children='Price based on fiction and non fiction'),
        html.Div(children='''
             Bar Chart (Total Score)
         '''),
        dcc.Graph(
            id='graph4',
            figure=fig4
        ),
    ]),
    html.Div([
        html.H2(children='user rating based on fiction and non fiction'),
        html.Div(children='''
             Bar Chart (Total Score)
         '''),
        dcc.Graph(
            id='graph5',
            figure=fig5
        ),
    ]),
    html.Div([
        html.H2(children='Price'),
        html.Div(children='''
             Bar Chart (Total Score)
         '''),
        dcc.Graph(
            id='graph6',
            figure=fig6
        ),
    ]),
    html.Div([
        html.H2(children='Count of Genre'),
        html.Div(children='''
             Bar Chart (Total Score)
         '''),
        dcc.Graph(
            id='graph7',
            figure=fig7
        ),
    ]),
    html.Div([
        html.H2(children='User Rating based on year'),
        html.Div(children='''
             Bar Chart (Total Score)
         '''),
        dcc.Graph(
            id='graph8',
            figure=fig8
        ),
    ]),
    html.Div([
        html.H2(children='User Rating based on Price'),
        html.Div(children='''
             Bar Chart (Total Score)
         '''),
        dcc.Graph(
            id='graph9',
            figure=fig9
        ),
    ]),

])

if __name__ == '__main__':
    app.run_server(debug=True)

