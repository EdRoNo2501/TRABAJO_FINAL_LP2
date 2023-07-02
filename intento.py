import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
from flask import Flask
import plotly.graph_objects as go


# Cargar los datos
bueno = pd.read_csv("dolar_bueno.csv")
malo = pd.read_csv("dolar_malo.csv")

# Crear la aplicación de Dash
app = dash.Dash()

# Definir el diseño de la aplicación
app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-descripcion', children=[
        dcc.Tab(label='Descripción del proyecto', value='tab-descripcion'),
        dcc.Tab(label='Clasificacion de noticias sobre el dolar', value='tab-noticias'),
        dcc.Tab(label='Indicadores economicos', value='tab-indicadores'),
        dcc.Tab(label='Distritos-Precios', value='tab-prueba') ]),
    html.Div(id='content')])

# Función para mostrar el contenido correspondiente a cada pestaña
@app.callback(
    dash.dependencies.Output('content', 'children'),
    [dash.dependencies.Input('tabs', 'value')]
)
def render_content(tab):
    if tab == 'tab-descripcion':
        return html.Div([
            html.H2('Descripción del proyecto')
        ])
    
    elif tab == 'tab-noticias':
        return html.Div([
            html.H2('Noticias'),
            html.H3('Noticias positivas para el sol'),
            
            dcc.Graph(
                figure=go.Figure(data=[go.Table(
                    header=dict(values=list(bueno.columns),
                                fill_color='paleturquoise',
                                align='left'),
                    cells=dict(values=[bueno['TITULO'], bueno['FECHA'], bueno['URL']],
                               fill_color='lavender',
                               align='left'))
                ])
            ),
            html.H3('Noticias negativas para el sol'),            
            dcc.Graph(
                figure=go.Figure(data=[go.Table(
                    header=dict(values=list(malo.columns),
                                fill_color='paleturquoise',
                                align='left'),
                    cells=dict(values=[malo['TITULO'], malo['FECHA'], malo['URL']],
                               fill_color='lavender',
                               align='left'))
                ])
            )
        ])
    elif tab == 'tab-indicadores':
        return html.Div([
            html.H2('Indicadores'),
            html.H3('Inflacion'),
            html.H3('Soles VS Dolares'),
        ])
    elif tab == 'tab-prueba':
        return html.Div([
            html.H2('Distritos'),
            html.H3('Promedios'),
            html.H3('Maximo'),
            html.H3('Minimo'),
        ])
    
    
if __name__ == '__main__':
    app.run_server()
    


