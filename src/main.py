#region LIB IMPORTS
import dash
import dash_bootstrap_components as dbc
import pathlib
from dash import dcc, html

import dash
from dash import html,dcc,dash_table
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import html, dcc, Output, Input,State, ctx
import numpy as np
from dash import no_update
from scipy.optimize import curve_fit
from scipy.special import factorial
import os
import importlib.util
import subprocess
import re
import inspect

import shutil
import sys

import glob
import pandas as pd

import  utils.Fonctions
#endregion

#region FUNC IMPORTS
from components.sidebar import *
from utils.navigation import *
from pages.back_end_pages.back_end_graphique import *

#endregion



#region APP CONFIG
app = dash.Dash(
    __name__, 
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=[dbc.themes.BOOTSTRAP,"https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css"]
) 
app.title="Parc automobile Francais"

server = app.server
app.config.suppress_callback_exceptions = True
#endregion

#region PATH
BASE_PATH = pathlib.Path(__file__).parent.parent.resolve()
RAW_DATA_PATH = BASE_PATH.joinpath("data").joinpath("raw").resolve()
#endregion

#region APP LAYOUT
app.layout = html.Div(
    [
        generate_sidebar(),
        html.Table(
        style={'width': '100%', 'borderCollapse': 'collapse'}, # Le tableau prend 50% de la largeur de l'écran
        
        children=[
            # LIGNE 1
            html.Tr([
                html.Td(style={'vertical-align': 'top'},children=[
                    html.H1(id='titre-page'),
                    dcc.Dropdown(
                        id='choix_df',
                        options=[{'label':'Données Brutes','value':'df_brutes'}],
                        style={'display':'block','width':'130px','backgroundColor': '#eeeeee', 'color': 'black','border':'none','borderRadius': '10px','textAlign': 'left'}
                    ),
                    
                ])
        ]),
            
            # LIGNE 2
            html.Tr([
                html.Td([
                    html.Div(id='page-content',style={'margin':'auto'}),
                ])
            ]),
            
                    
        ]
    )
        
        
    ], id='main-content')
#enregion

#region RUN
if __name__ == '__main__':
    app.run(debug=True)
#endregion

