#Librairie crée par Micael FEBRAS FRAGOSO CARMONA

import dash 
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import json
from scipy.special import factorial
import dash
from dash import html,dcc,dash_table
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import json
import numpy as np
import dash_daq as daq
from dash.exceptions import PreventUpdate
from scipy.special import factorial
import os

app_layout=html.Div(style={
    'backgroundColor': couleur_background, #'#fae5d3', 
    'position': 'relative', 
    'top': 0, 
    'bottom': 0, 
    'left': 0, 
    'right': 0,
    'min-height': '10000px',  # Assure que la couleur de fond s'étend sur toute la hauteur de la page
    'min-width': 'auto', 
    'color':couleur_text,
    'font-family': 'Arial', 
},
children=[# Definition du layout affichage principale
#Création des differents onglets
    # Sidebar avec onglets       

   html.Div([    
               
    ], style={'width': '50%', 'display': 'inline-block', 'vertical-align': 'top'}),
    html.Div([

       #Permet de crée deux bouttons pour switch entre le data frame originel et celui décalé par défaut le choix est sur data frame originel grace a "value='DF_Brut'"
    ], style={'width': '50%', 'display': 'inline-block', 'vertical-align': 'top-right', 'text-align': 'right'}),
    html.Div(id='output-table', style={'margin': 'auto', 'width': '95%'}),#Affichage du Tableau 
     #],style={'display':'inline-block'}),#La roue qui tourne

    html.Pre(id='output-container'),
    html.Div(id='sliders2',style={'margin-left':'15px','margin-right':'15px'}),
    html.Div(id='output-container-slider',style={'margin-left':'15px','margin-right':'15px'}),

    
   ])