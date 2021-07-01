# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import sqlite3
import sqlalchemy

USER = ''
cnx = sqlite3.connect('db.sqlite')
df = pd.read_sql_query("SELECT * FROM class_table", cnx)
cnx.close()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#############
# import flask
#
# server = flask.Flask(__name__)
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets,external_scripts=external_scripts, server=server)
#################
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Button('CV Ranking', id='btn-nclicks-1', n_clicks=0),
    html.Button('Scatter Plot', id='btn-nclicks-2', n_clicks=0),
    html.Button('Button 3', id='btn-nclicks-3', n_clicks=0),
    html.Div(id='container-button-timestamp')
])

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')

fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Name, df.Age, df.Salary, df.Location,df.Mail,df.Profession,df.Class],
               fill_color='lavender',
               align='left'))
])

fig.update_layout(title = 'CVs Ranking')

fig1 = go.Figure(data=go.Scatter(
    x = df['Age'],
    y = df['Salary'],
    text = df['Name'],
    mode='markers',
    marker=dict(
        size=16,
        color=df['Salary'], #set color equal to a variable
        colorscale='Viridis', # one of plotly colorscales
        showscale=True
    )
))

fig1.update_layout(title = 'CVs Ranking', xaxis_title="Age",yaxis_title="Salary")

done= html.Div([
    dcc.Graph(figure=fig)
])

done1 = html.Div([
    dcc.Graph(figure=fig1)
])


@app.callback(Output('container-button-timestamp', 'children'),
              Input('btn-nclicks-1', 'n_clicks'),
              Input('btn-nclicks-2', 'n_clicks'),
              Input('btn-nclicks-3', 'n_clicks'))
def displayClick(btn1, btn2, btn3):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'btn-nclicks-1' in changed_id:
        msg = 'Button 1 was most recently clicked'
        return done
    elif 'btn-nclicks-2' in changed_id:
        msg = 'Button 2 was most recently clicked'
        return done1
    elif 'btn-nclicks-3' in changed_id:
        msg = 'Button 3 was most recently clicked'
    else:
        msg = 'None of the buttons have been clicked yet'
    return html.Div(msg)

if __name__ == '__main__':
    app.run_server(host='localhost',port='4000',debug=True)


# import tornado.ioloop
# import tornado.web
#
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")
#
# def make_app():
#     return tornado.web.Application([
#         (r"/", MainHandler),
#     ])
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(4000)
#     tornado.ioloop.IOLoop.current().start()
