
from dash import Input, Output, callback, ctx
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

def affichage_graphique():
    return html.Table(id='table-graph',children=[
                html.Tr([ 
                    html.Td([
        html.Div([
            html.Div([ 
                
                dcc.ConfirmDialog(#Pop-up pour indiquer que le fichier charger ne possede pas de colonne temps 
               id='manque_temporel',
               
           ),
          
                html.Div(id='mondal_message'),
                html.Div(id='message_Na_popup'),
                                  

                  html.Div(id='file-name'),#html.Div qui afficheras le nom du fichiers charger 
                  
                  #html.Div(id='text_df'),
                  html.Br(),
                  html.Div([dcc.Dropdown( #Dropdown qui affichera toutes les types de données utilisable
                      id='choix_df_drp',
                      options=[{'label': 'Données Brut', 'value': 'DF_Brut'}],value='DF_Brut',style={'display':'none','width':'120%','vertical-align': 'top-right','margin':'auto','backgroundColor': '#eeeeee', 'color': 'black','border':'none','borderRadius': '10px'}
                  ),],style={'display':'flex'}),
                  
                  html.Div(id='options_graph_largeur'),
                  dcc.Input(id='width-input', type='number', value=1300,min=800,max=2000,step=10,style={'display':'none'}),#Zone de texte pour la largeur du graphique
                  html.Div(id='options_graph_hauteur'),

                  dcc.Input(id='height-input', type='number',value=700,min=500,max=1000,step=10,style={'display':'none'}),#Zone de texte pour la hauteur du graphique
                  html.Div(id='texte_titre_graph'),
                  dcc.Input(id='titre_graphique', type='text',style={'display':'none'}),#Zone de texte pour le nom du graphique
                  html.Br(),
                  html.Div(id='saut_curve'),
                  dcc.Dropdown(
                        id='type_curve_fitting',
                        options=[{'label': i, 'value': i} for i in fitting_functions.keys()],
                        style={'display':'none','width':'80%','backgroundColor': '#eeeeee', 'color': 'black','border':'none','borderRadius': '10px'},
                  ),
                  dcc.RadioItems(
                      id='Regression',#Ce RadioItems permets d'appliquer une Regression ou non a notre graphique sa valeur par defaut est Sans Regression
                      options=[
                          {'label': 'Curve fitting', 'value': 'Reg_avec'},{'label': 'Sans curve fitting', 'value': 'Reg_sans'}
                      ],
                      value='Reg_sans',inline=True,style={'width':'80%','display': 'none'}
                  ),
                  dcc.RadioItems(#Choix / RadioItems permettant de choisir si on veux notre graphique avec de la profondeur ou non sa valeur par defaut est Prof_sans 
                      id='profond',
                      options=[
                          {'label': 'Avec Profondeur', 'value': 'Prof_avec'},{'label': 'Sans Profondeur', 'value': 'Prof_sans'}
                      ],
                      value='Prof_sans',inline=True,style={'width':'80%','display': 'none'}
                  ),
                  html.Br(),
                  dcc.RadioItems(#Choix / RadioItems permettant de choisir si on veux notre graphique avec de la profondeur ou non sa valeur par defaut est Prof_sans 
                      id='type_bar',
                      options=[
                          {'label': 'Couleur dégradé', 'value': 'degrade'},{'label': 'Couleur fixe', 'value': 'fixe'}
                      ],
                      value='degrade',inline=True,style={'width':'80%','display': 'none'}
                  ),
                  
                  html.Br(),
                  dcc.RadioItems(#Permet de choisir quel type de graphique soit lineaire soit nuage de point sa valeur par defaut est lineaire pour faciliter le 1er affichage 
                      id='type_graph',
                      options=[
                          {'label': 'Linéaire', 'value': 'line'},{'label': 'Nuage de point', 'value': 'dot'},{'label': 'Histogramme', 'value': 'histo'}                   
                      ],
                      value='line',inline=True,style={'display': 'none'}
                  ),
                  dcc.RadioItems(#RadioItems gerant l'utilisation ou non du filtrage des données 
                      id='avec_condition',
                      options=[
                          {'label': 'Filtrage actif', 'value': 'actif'},
                          {'label': 'Filtrage inactif', 'value': 'desactive'},
                          ],
                      value='desactive',
                      inline=True,style={'display':'none'}
                      ),
                    html.Div(id='affichage_slider_point',children=[#Slideur pour regler la taille des points , clarté et la taille de la police lorsque le graph est en mode nuage de point
                         html.Label('Taille des points'),
                         dcc.Slider(
                             id='point-size-slider',
                             min=5,
                             max=20,
                             step=2,
                             value=7,
                         ),
                         html.Label('Clarté des points'),
                         dcc.Slider(
                             id='point-opacity-slider',
                             min=0.1,
                             max=1,
                             step=0.2,
                             value=0.5,
                         ),
                         html.Label('Taille de la police'),
                         dcc.Slider(
                             id='font-size-slider',
                             min=10,
                             max=30,
                             step=5,
                             value=15,
                         ),
                         
                     ],style={'display':'none','margin':'auto','width':'100%'}),
                    html.Div(id='info_option',style={'display':'inline-block','margin-left':'3px'}),

                   ],style={'display': 'inline-block','vertical-align':'top-left', 'width': '100%','margin-top':'10px','margin-left':'60px'} ),

                    html.Td([ #Deuxieme colonne du tableau pour bien repartir les elements
                        html.Table(id='table-graph_2',children=[ 
                                     html.Tr([ 
                                         html.Td([     
                                             html.Div([ 
                                                    html.Div([
                                                     html.Div(id='text_x_axis',style={'display':'inline-block'}),
                                                     
                                                     html.Div(id='unité_x',style={'display':'inline-block','margin-left':'15px'}), dcc.Input(id='x-axis-unit', type='text',style={'display':'none'}),
                                                     
                                                     #ce dropdown permet de selectionner notre colonne pour l'axe des x ce dropdown est a choix unique et les options on les feras dans un app.callback
                                                     dcc.Dropdown(id='x-axis',placeholder="Axe X",style= {'vertical-align':'left','vertical-align':'left','display': 'none', 'width': '50%'}),
                                                    dcc.Checklist(
                                                                id='log_x',
                                                                options=[
                                                                    {'label': 'Échelle log ', 'value': 'log'},
                                                                ],
                                                                value=[],style={'display':'none'}
                                                            ),
                                                 ],style={'display': 'inline-block','vertical-align':'top-left', 'width': '30%'} ),
                                                 
                                                    html.Div([
                                                     html.Div(id='text_y_axis',style={'display':'inline-block'}),
                                                     html.Div(id='unité_y',style={'display':'inline-block','margin-left':'20px'}),
                                                     dcc.Input(id='y-axis-unit', type='text',style={'display':'none'}),
                                                   dcc.Dropdown(id='y-axis',placeholder="Axes Y primaire",multi=True,style={'vertical-align':'center','display': 'none', 'width': '70%'}),
                                                    dcc.Checklist(
                                                                id='log_y',
                                                                options=[
                                                                    {'label': 'Échelle log ', 'value': 'log'},
                                                                ],
                                                                value=[],style={'display':'none'}
                                                            ),
                                                   html.Button('Tout sélectionner', id='all_selec',style={'display':'none'}),
                                                 ],style={'height':'60px','display': 'inline-block','vertical-align':'top-center', 'width': '30%','margin-left':'50px'}),
                                                
                                                    html.Div([
                                                     html.Br(),
                                                     html.Div(id='text_y2_axis',style={'display':'inline-block'}),
                                                     html.Div(id='unité_y2',style={'display':'inline-block','margin-left':'20px'}),
                                                     dcc.Input(id='y2-axis-unit', type='text',style={'display':'none'}),
                                                     #ce dropdown permet de selectionner nos colonnes pour l'axe des y secondaire ce dropdown est a choix mutliple et les options on les feras dans un app.callback
                                                     dcc.Dropdown(id='y2-axis',placeholder="Axes Y secondaire",multi=True,style= {'overflowY': 'auto','vertical-align':'right','display': 'none', 'width': '70%'}),
                                                    dcc.Checklist(
                                                                id='log_y2',
                                                                options=[
                                                                    {'label': 'Échelle log', 'value': 'log'},
                                                                ],
                                                                value=[],style={'display':'none'}
                                                            ),
                                                 ],style={'height':'60px','display': 'inline-block','vertical-align':'right', 'width': '30%','margin-left':'50px'}),
                                                 ],style={'display': 'inline-block','margin-left':'120px','vertical-align': 'top'}
                                                 ),]),]),
                                     html.Tr([html.Td([dcc.Graph(id='graph',config={'scrollZoom': True},style={'height': '800px','width': '100%','display':'none'}),]),#☻Affichage de notre graphique 
                     ],style={'display':'flex'}), ],style={'display':'inline-block'}),
])
     
    ], style={'display': 'flex'}),]),]),], style={'width':'40%','margin-left':'8px','display': 'inline-block'}), #1e2130

