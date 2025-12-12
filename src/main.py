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

#endregion

#region FUNC IMPORTS
from components.sidebar import *
from utils.Fonctions import *
from pages.tableau import *
from pages.graphique import layout_graphique
# Moved to end to avoid circular import: from pages.back_end_pages.back_end_graphique import *

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
app.layout = html.Div(style={
    'backgroundColor': '#fdf2e9', #'#fae5d3', 
    'position': 'relative', 
    'top': 0, 
    'bottom': 0, 
    'left': 0, 
    'right': 0,
    'min-height': 'auto',  # Assure que la couleur de fond s'étend sur toute la hauteur de la page
    'min-width': 'auto', 
    'color':'black',
    'font-family': 'Arial', 
},children=[
        generate_sidebar(),
        dcc.Loading(
    id="loading",
    type="dot",
    children=[
        dcc.Store(id='active-tab'),]),
        
       html.Table(
        style={'width': '100%', 'borderCollapse': 'collapse'}, # Le tableau prend 50% de la largeur de l'écran
        
        children=[
            # LIGNE 1
            html.Tr([
                html.Td(style={'vertical-align': 'top'},children=[
                    html.Div(id='titre-page'),
                    dcc.Dropdown(
                            id='choix_df',
                            options=[{'label':'Données Brutes','value':'df_brutes'}],value='df_brutes',
                            style={'display':'block','width':'200px','backgroundColor': '#eeeeee', 'color': 'black','border':'none','borderRadius': '10px','textAlign': 'left'}
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
    ),
    layout_graphique,

    ], id='main-content')
#endregion

# Import callbacks after app is fully configured to avoid circular imports
from pages.back_end_pages.back_end_graphique import *
@callback(
    Output('page-content', 'children'),
    Output('titre-page','children'),
    Output('active-tab', 'data'),
    Input('tab-tableau','n_clicks'),
    Input('tab-graphique','n_clicks'),
    Input('tab-maps','n_clicks'),
    Input('tab-fonctions','n_clicks'),
    Input('tab-informations','n_clicks'),
    State('choix_df','value'),
)
def generate_page_content(tableau_click,graphique_click,maps_click,fonctions_click,informations_click,choix):
    newdf=choix_df(choix,global_df_brut,global_df_mean,global_meandf_repared,global_df_fusionnées,global_meandf_fusionnées,global_df_1,global_df_2,global_df_3,global_df_4,global_df_5,global_meandf_1,global_meandf_2,global_meandf_3,global_meandf_4,global_meandf_5)
    match ctx.triggered_id:
        case 'tab-tableau':
            
            return generate_tableau1(newdf,'black','#f9f9f9'),"Page Tableau ",'tableau'
        case 'tab-graphique':
            return None,"Page Graphique",'graphique'
        case 'tab-maps':
            return html.Div(),"Page Maps",'maps'
        case 'tab-fonctions':
            return None,"Page Fonctions",'options'
        case 'tab-informations':
            return html.Div(),"Page Informations",'informations'
        
        case _:
            return html.Div(),"",dash.no_update
#region RUN
if __name__ == '__main__':
    app.run(debug=True)
#endregion

