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
from pages.fonctions import layout_fonctions
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
    'color':'black',
    'font-family': 'Arial', 
    'min-height': '1000px',
    'min-width': '1000px',
    
},children=[
        generate_sidebar(),
        dcc.Loading(
    id="loading",
    type="dot",
    children=[
        dcc.Store(id='active-tab'),
         dcc.Store(id='stock_curve_fitting'),
           
        dcc.Store(id='selected_color'),
        dcc.Store(id='alert-displayed'),
        dcc.Store(id='alert-displayed_NA'),
        dcc.Store(id='col_na'),
        dcc.Store(id='df_ok'),
            
        dcc.Store(id='store-units'),
                
        dcc.Store(id='add-fichier'),
        dcc.Store(id='stock_temp_ext'),
        dcc.Store(id='stock_tdep'),
        dcc.Store(id='manque_temporel_data'),
       
        dcc.Store(id='output_regen'),
        dcc.Store(id='output_regen_na'),
        dcc.Store(id='calcul_mean'),
        dcc.Store(id='rename_col'),
        dcc.Store(id='fichier_fusion'),
        
        dcc.Store(id='filtrage_df_ok'),
        
        
        ]),
            
            html.Table(
        style={'width': '100%', 'borderCollapse': 'collapse','margin-left':'5%'}, # Le tableau prend 50% de la largeur de l'écran
        
        children=[
            # LIGNE 1
            html.Tr([
                html.Td(style={'vertical-align': 'top'},children=[
                   
                     dcc.Dropdown(
                            id='choix_df',
                            options=[{'label':'Données Brutes','value':'df_brutes'}],value='df_brutes',
                            style={'display':'block','height':'40px','width':'200px','backgroundColor': '#eeeeee', 'color': 'black','border':'none','borderRadius': '10px','textAlign': 'left','margin-left':'0%'}
                        ),
                                        
                ])
        ]),
            
            # LIGNE 2
            html.Tr([
                html.Td(style={'vertical-align': 'top','margin-top':'5%'},children=[
                    html.Div(id='page-content',style={'overflowX':'auto'}),
                        
                    layout_graphique,
                    layout_fonctions,

                    
                ])
            ]),
            
                    
        ]
    ),
       
     

    ], id='main-content')
#endregion

# Import callbacks after app is fully configured to avoid circular imports
from pages.back_end_pages.back_end_graphique import *
from pages.back_end_pages.back_end_fonctions import *
@callback(
    Output('page-content', 'children'),
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
            
            return generate_tableau3(newdf,'black','#fdf2e9'),'tableau'
        case 'tab-graphique':
            return None,'graphique'
        case 'tab-maps':
            return None,'maps'
        case 'tab-fonctions':
            return None,'options'
                
        case _:
            return None,dash.no_update
#region Gestion des options de DataFrame       
@callback(
    Output('choix_df_drp','options'),
    Input('filtrage_df_ok','data'),
    Input('fichier_fusion','data'),
    Input('output_regen','data'),
    Input('calcul_mean','data'),
    Input('df_cop_loi_deau','data'),
    Input('output_regen_na','data'), 
    State('alert-displayed', 'data'),  
    prevent_initial_call=True
)
def choix_df_drp(filtrage_df_ok,fichier_fusion,output_regen,calcul_mean,df_cop_loi_deau,output_regen_na,alert_displayed):
    if options is None:
        options = []
    if global_df_brut is not None:
        options.append({'label':'Données Brut','value':'DF_Brut'})
        
    if global_df_repared is not None: 
        options.append({'label':'Données régénérées en ligne ','value':'df_repared'})

    if global_df_mean is not None:
        options.append({'label':'Données brut moyennées','value':'df_mean'})
        
    if (global_df_fusionnées is not None):
        options.append({'label':'Données fusionnées','value':'df_fusionnées'})
        
    if (global_meandf_fusionnées is not None):
        options.append({'label':'Données fusionnées moyennées','value':'meandf_fusionnées'})
    
    if global_df_1 is not None:
        options.append({'label':'Données Filtrées 1','value':'df_1'})
        
    if global_df_2 is not None:
        options.append({'label':'Données Filtrées 2','value':'df_2'})
    
    if global_df_3 is not None :
        options.append({'label':'Données Filtrées 3','value':'df_3'})
    
    if global_df_4 is not None :
        options.append({'label':'Données Filtrées 4','value':'df_4'})

    if global_df_5 is not None:
        options.append({'label':'Données Filtrées 5','value':'df_5'})

    if global_meandf_1 is not None:
        options.append({'label':'Données Filtrées 1 moyennées','value':'meandf_1'})
        
    if global_meandf_2 is not None:
        options.append({'label':'Données Filtrées 2 moyennées','value':'meandf_2'})
    
    if global_meandf_3 is not None :
        options.append({'label':'Données Filtrées 3 moyennées','value':'meandf_3'})
    
    if global_meandf_4 is not None:
        options.append({'label':'Données Filtrées 4 moyennées','value':'meandf_4'})
        
    if global_meandf_5 is not None:
        options.append({'label':'Données Filtrées 5 moyennées','value':'meandf_5'})
          
    return options
#endregion
#region RUN
if __name__ == '__main__':
    app.run(debug=True)
#endregion

