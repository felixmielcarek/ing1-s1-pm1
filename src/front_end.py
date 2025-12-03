
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

# Styles CSS pour la bulle et la fenêtre de chat
styles_chatbot = {
    'chat-icon': {
        'position': 'fixed',
        'bottom': '20px',
        'right': '20px',
        'width': '50px',
        'height': '50px',
        'background-color': '#0078FF',
        'color': 'white',
        'border-radius': '50%',
        'display': 'flex',
        'align-items': 'center',
        'justify-content': 'center',
        'cursor': 'pointer',
        'box-shadow': '0px 4px 10px rgba(0, 0, 0, 0.2)',
    },
    'chat-window': {
        'position': 'fixed',
        'bottom': '80px',
        'right': '20px',
        'width': '500px',
        'height': '600px',
        'background-color': 'white',
        'border-radius': '10px',
        'box-shadow': '0px 4px 10px rgba(0, 0, 0, 0.2)',
        'display': 'none',  # Caché par défaut
        'flex-direction': 'column',
        'padding': '10px',
    },
    'chat-header': {
        'font-weight': 'bold',
        'border-bottom': '1px solid #ccc',
        'padding-bottom': '5px',
        'margin-bottom': '10px',
    },
    'chat-messages': {
        'flex-grow': '1',
        'overflow-y': 'auto',
        'margin-bottom': '10px',
    },
    'chat-input-container': {
        'display': 'flex',
    },
    'chat-input': {
        'flex-grow': '1',
        'padding': '5px',
        'border': '1px solid #ccc',
        'border-radius': '5px',
    },
    'chat-send-button': {
        'margin-left': '10px',
        'padding': '5px 10px',
        'background-color': '#0078FF',
        'color': 'white',
        'border': 'none',
        'border-radius': '5px',
        'cursor': 'pointer',
    },
}



message = """
Fonctions de Racine et Puissance
- **sqrt(x)** : Calcule la racine carrée de chaque élément de l'array.
- **cbrt(x)** : Calcule la racine cubique de chaque élément.
- **power(x, y)** : Élève chaque élément de x à la puissance y.

Fonctions Exponentielles et Logarithmiques
- **exp(x)** : Calcule l’exponentielle de chaque élément.
- **expm1(x)** : Calcule exp(x) - 1 pour chaque élément.
- **log(x)** : Calcule le logarithme naturel de chaque élément.
- **log10(x)** : Calcule le logarithme en base 10.
- **log2(x)** : Calcule le logarithme en base 2.
- **log1p(x)** : Calcule log(1 + x) pour chaque élément.

Fonctions Trigonométriques
- **sin(x)** : Calcule le sinus de chaque élément.
- **cos(x)** : Calcule le cosinus de chaque élément.
- **tan(x)** : Calcule la tangente de chaque élément.
- **arcsin(x)** : Calcule l’arc sinus (inverse du sinus).
- **arccos(x)** : Calcule l’arc cosinus (inverse du cosinus).
- **arctan(x)** : Calcule l’arc tangente (inverse de la tangente).

Fonctions Hyperboliques
- **sinh(x)** : Calcule le sinus hyperbolique de chaque élément.
- **cosh(x)** : Calcule le cosinus hyperbolique.
- **tanh(x)** : Calcule la tangente hyperbolique.
- **arcsinh(x)** : Calcule l’arc sinus hyperbolique (inverse du sinus hyperbolique).
- **arccosh(x)** : Calcule l’arc cosinus hyperbolique (inverse du cosinus hyperbolique).
- **arctanh(x)** : Calcule l’arc tangente hyperbolique (inverse de la tangente hyperbolique).

Fonctions de calcul
- **cumsum(x)** : Somme cumulée.
- **min(x)** : Minimum.
- **max(x)** : Maximum.
- **mean(x)** : Moyenne.
"""
# Fonctions d'ajustement
def linear(x, a, b):
    return a * x + b

def cauchy(x, A, B, C):
    return A + B / x**2 + C / x**4

def cubic(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

def damped(x, a, b, d):
    return a * np.exp(-b * x) + d

def damped_oscillator(x, A0, b, omega, delta, C):
    return A0 * np.exp(-b * x) * np.sin(omega * x + delta) + C

def exponential(x, a, b, c):
    return a * np.exp(b * x) + c

def gaussian(x, A0, x0, sigma, C):
    return A0 * np.exp(- (x - x0)**2 / (2 * sigma**2)) + C

def inverse(x, a, b):
    return a + b / x

def logistic(x, A, B, C):
    return A / (1 + np.exp(-B * (x - C)))

def lorentzian(x, A, omega0, beta, C):
    return (A * np.sqrt((omega0**2 - x**2)**2 + 4 * x**2 * beta**2)) + C

def natural_log(x, a, b):
    return a * np.log(x * b)

def oscillator(x, A0, k, delta, C):
    return A0 * np.sin(k * x + delta) + C

def poisson(x, a, mu):
    return a * np.exp(-mu) * (mu**x / factorial(x))

def power_law(x, a, b):
    return a * x**b

def power_law_offset(x, A, B, x0, C):
    return A * (x - x0)**B + C

def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

def Quartic (x,a,b,c,d,e):
    return a*x**4+b*x**3+c*x**2+d*x+e

def stokes_law(x, k0, a0, K1):
    return (k0 / (18 * a0)) * x**2 * (1 - 2.1 * x / K1)

def two_slit_interference(x, A, k1, k2, x0, C):
    return A * np.sinc(k1 * (x - x0) / np.pi)**2 * np.cos(k2 * (x - x0))**2 + C

def smooth_y_values(df, x_column, y_column, window_size=9):
    sorted_df = df.sort_values(by=x_column)
    smoothed_y = sorted_df[y_column].rolling(window=window_size, center=True).mean()
    return sorted_df[x_column], smoothed_y



#Apparance de l'application
couleur_background='#fdf2e9'
couleur_drpbackground='#eeeeee'
couleur_btnbackground='#fae5d3'
couleur_text='black'

 
 
# Dictionnaire des fonctions
fitting_functions = {
    'Linear': linear,
    'Cauchy': cauchy,
    'Cubic': cubic,
    'Damped Function': damped,
    'Damped Oscillator': damped_oscillator,
    'Exponential': exponential,
    'Gaussian': gaussian,
    'Inverse': inverse,
    'Logistic': logistic,
    'Lorentzian': lorentzian,
    'Natural Log': natural_log,
    'Oscillator': oscillator,
    'Poisson': poisson,
    'Power Law': power_law,
    'Power Law with Offsets': power_law_offset,
    'Quadratic': quadratic,
    'Quartic':Quartic,
    'Stokes Law': stokes_law,
    'Two Slit Interference': two_slit_interference,
    'Courbe moyennée 24h': smooth_y_values,
}

#Message pour le bouton Aide 
modal = dbc.Modal(
    [
        dbc.ModalHeader("Aide",style={'backgroundColor':couleur_background, 'color':couleur_text}),
        dbc.ModalBody(
            [dcc.Markdown('''
                ## Utilité

                Cet outil de visualisation et d’analyse de données permet de représenter les données issues des essais PAC (ou autre type de données) sous forme de graphique ou de tableaux, et de les traiter à l’aide de diverses fonctions. 
                ### Fonctionnement

            '''),
                  
                       
                        html.Br(),
                        
                        html.Br(),
                        html.A("Calcul de moyenne",id="text_moyenneglissante",className="mb-3"),
                        dbc.Collapse(
                            dcc.Markdown('''
                                L’utilisateur peut choisir une ou plusieurs colonnes dans « Sélection ». 
                                Dans Option/validation, il peut choisir 3 types de moyenne, moyenne glissante, moyenne cumulée ou moyenne horaire. 
                                Les colonnes moyennées sont ajoutées à un nouveau jeu de données avec un suffixe "moyennées" . 
                                En fonction du type de moyenne sélectionner les colonnes seront intitulées « nom de la colonne "_mean_glissante", " nom de la colonne _mean_cum" et " nom de la colonne _mean_horaire ". 
                                
                                Calcule d'une moyenne glissante : 
                                Préciser la plage de temps glissante. 
                                
                                Calcule d'une moyenne horaire : 
                                Le calcule se fait au termes de la periode. 



                             '''
                                ),
                            
                            id="text_moyenneg",
                            ),
                            
                            html.Br(),
                            html.A("Profondeur",id="text_profondeur",className="mb-3"),
                            dbc.Collapse(
                                dcc.Markdown('''
                                     
                                   Associe une palette de couleurs aux données d'une colonne choisie. 
                                    Le menu déroulant permet de choisir la colonne de référence. 
                                    Pour ajouter une couleur à la palette, cliquer sur la couleur et sur « Valider ». 
                                    Il est possible de supprimer la derniere couleur sélectionnée en cliquant sur " Clear". 
                                    Par défaut, 3 palettes sont déjà créées : 
                                    -	Température ( bleu et rouge) 
                                    -	Heure de la journée (minuit à minuit)  ( noir , bleu , orange, rouge et noir ) 
                                    -	Autres données ( gris , noir) 
                                    
                                    L’utilisateur peut ensuite retourner dans l’onglet "Graphique". 
                                    Dans la partie gauche un nouvel élément permet d’activer ou non la profondeur sur la 1er colonne sélectionner en axe y primaire. 
                                    
                                                 '''                                  
                               ),
                                
                                id="text_prof",
                                ),
                            html.Br(),
                           
                            html.A(" Régression Linéaire ", id="reg_lin_button", className="mb-3"),
                            dbc.Collapse(
                                dcc.Markdown('''
                                                                            
                                      Il est possible de l'activer ou non en choisissant "Avec régression" dans l'onglet Graphique, la régression se fait sur la 1re colonne y primaire. 
                                      Lorsque cette fonction est activée les seules colonnes temporelles utilisables en axe des x sont "temps_heure_24" ou "temps_heure_cumulée". 
                            
                     '''),
                                id="text_regression_lineaire",
                            ),
                            html.Br(),
                            html.A("Exclusion de(s) colonne(s)",id="text_exclusion",className="mb-3"),
                            dbc.Collapse(
                                dcc.Markdown('''
                                             En sélectionnant "Filtrage", un menu déroulant permet de sélectionner les colonnes à supprimer.                                          
                                        '''                                  
                               ),
                                
                                id="text_exclu",
                                ),

                            html.Br(),
                            html.A("Filtrage des données",id="text_filtrage",className="mb-3"),
                            dbc.Collapse(
                                dcc.Markdown('''
                                      Sélectionnez jusqu'à 3 colonnes de références dans la section 'Sélection'. Pour chaque colonne sélectionnée, vous devez indiquer leur valeur seuil et le type de filtre. 
                                      Pour valider le (s) filtrage (s), cliquer sur « Valider ». Pour activer ou désactiver ce filtrage, il faut se rendre dans l’onglet "Graphique"... 
                                       
                                           '''                                  
                               ),
                                
                                id="text_filtre",
                                ),
                            html.Br(),

                               
                          
            ],style={'backgroundColor':couleur_background, 'color': couleur_text}
        ),
        dbc.ModalFooter(
            dbc.Button("Fermer", id="close", className="ml-auto"),style={'backgroundColor':couleur_background, 'color': couleur_text}
        ),
    ],
    id="modal",
    size="fullscreen",#“sm”, “lg”, “xl” et “fullscreen”.
    style={
        'backgroundColor':couleur_background, # Couleur de fond du bouton
        'color': couleur_text, # Couleur du texte du bouton
        'border': '2px solid #4b5160' # Supprime la bordure par défaut du bouton
    }
)

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
       html.Div(
        id='sidebar',
        children=[
                             
                html.Div(
                    id='sidebar-content',
                    children=[
                        html.Div([
                            html.I(className='bi bi-table'),
                            html.Span('Tableau', className='sidebar-text')
                        ], id='tab-tableau', className='sidebar-link', n_clicks=0),
                        html.Div([
                            html.I(className='bi bi-graph-up'),
                            html.Span('Graphique', className='sidebar-text')
                        ], id='tab-graphique', className='sidebar-link', n_clicks=0),
                        html.Div([
                            html.I(className='bi bi-map'),
                            html.Span('Maps', className='sidebar-text')
                        ], id='tab-maps', className='sidebar-link', n_clicks=0),
                        html.Div([
                            html.I(className='bi bi-gear'),
                            html.Span('Fonctions', className='sidebar-text')
                        ], id='tab-fonctions', className='sidebar-link', n_clicks=0),
                        html.Div([
                            html.I(className='bi bi-download'),
                            html.Span('Exporter le fichier', className='sidebar-text')
                        ], id='tab-exporter', className='sidebar-link', n_clicks=0),
                        html.Div([
                            html.I(className='bi bi-info-circle'),
                            html.Span('Informations', className='sidebar-text')
                        ], id='tab-informations', className='sidebar-link', n_clicks=0),
                    ],
                    className='sidebar-content'
                ),
            
            

        ],
        className='sidebar'
    ),
        dcc.Store(id='active-tab', data='tableau'),

        dcc.Loading(
        id="loading",
        type="dot",
        children=[
            
            dcc.Store(id='stock_curve_fitting'),
           
            dcc.Store(id='selected_color'),
            dcc.Store(id='alert-displayed'),
            dcc.Store(id='alert-displayed_NA'),
            dcc.Store(id='col_na'),
            dcc.Store(id='df_ok'),
            dcc.Store(id='pas'),
        
            dcc.Store(id='store-units'),
            dcc.Store(id='shifted-data'),
            
            dcc.Store(id='add-fichier'),
            dcc.Store(id='stock_temp_ext'),
            dcc.Store(id='stock_tdep'),
            dcc.Store(id='manque_temporel_data'),
            dcc.Store(id='calcul_energie'),
            dcc.Store(id='calcul_coolprop'),
            dcc.Store(id='calcul_fcnt_utilisateur'),
            dcc.Store(id='calcul_incertitude'),
            dcc.Store(id='output_regen'),
            dcc.Store(id='output_regen_na'),
            dcc.Store(id='calcul_mean'),
            dcc.Store(id='rename_col'),
            dcc.Store(id='fichier_fusion'),
            dcc.Store(id='df_cop_loi_deau'),
            dcc.Store(id='filtrage_df_ok'),
            
        ]
    ),
           
   html.Div([ 
            html.Table(id='table-graph',children=[
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
                      options=[{'label': 'Données Brut', 'value': 'DF_Brut'}],value='DF_Brut',style={'display':'none','width':'120%','vertical-align': 'top-right','margin':'auto','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px'}
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
                        style={'display':'none','width':'80%','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px'},
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
        
                    


        html.Br(),#Permet de faire des sauts de lignes
        html.Div([
            html.Table(id='table-options',children=[ #Tableau visible dans l'onglet Options
                html.Tr([ 
                    html.Td([
                        html.Th('Fonction', style={'width': '30%','text-align':'center','font-size':'17px','vertical-align':'center'}),#Titre de la 1er colonne 
                    ],style={'width': '20%','border': '1px solid #fae5d3'}),
                    html.Td([
                        html.Th('Sélection', style={'width': '30%','text-align':'center','font-size':'17px','vertical-align':'center'})#Titre de la 2eme colonne 
                    ],style={'width': '20%','border': '1px solid #fae5d3'}),
                    html.Td([
                      html.Th('Option/Validation',style={'width': '30%','text-align':'center','font-size':'17px','vertical-align':'center'})  #Titre de la 3eme colonne 
                    ],style={'width': '20%','border': '1px solid #fae5d3'}),
                ]),
                html.Tr([#Le html.Tr permet de crée une ligne 
                    html.Td([#Le html.Td permet de crée une colonne
                        dcc.Dropdown(#♪Dropdown qui permet de choisir notre fonction
                            id='filtre',
                           options = [
                               
                                {'label':'Filtrage des données', 'value':'filtrage_df_données'},
                                {'label':'Sélection de l année', 'value':'selec_annee'},
                                {'label': 'Renommer colonne', 'value': 'rename'},
                                {'label': 'Solveur', 'value': 'solveur'},
                                {'label': 'Scission', 'value': 'scission'},
                                {'label': 'Calcul de pente/variation', 'value': 'calcul_pente'},
                                {'label': 'Calcul de moyenne', 'value': 'moyenne'},
                                {'label': 'Profondeur', 'value': 'prof'},
                                
                                {'label': 'Fonctions utilisateurs', 'value': 'fcnt_extern'},
                                

                            ],
                            placeholder="Paramètres et fonctions",#Quand le dropdown est vide ce message s'affiche dedans
                            style={'display': 'none','vertical-align':'top','maring-left':'5px'}
                        ),],style={'width':'40%','heigh':'20px','border': '1px solid #1e2130','padding-left': '8px','padding-top': '2px'}),
                    html.Td([
                        dcc.Dropdown(id='drp_pente', placeholder='Sélectionnez une colonne', style={'display':'none'}),
                        dcc.Dropdown(id='function-file-dropdown', placeholder='Sélectionnez un fichier chargé', style={'display':'none'}),
                        dcc.Dropdown(id='choixreference',style={'display': 'none'}),#Colonne reference pour la profondeur
                        dcc.Dropdown(id='colonnes', multi=True, style={'display':'none'}),#Choix des colonnes pour calculer une moyenne
                        dcc.Dropdown(id='col-rename', multi=False, style={'width':'100%','display': 'none'}), #Choix de colonne pour renommer
                        dcc.Dropdown(id='solveur_colonne',style={'display': 'none'},multi=True),#Colonne reference pour la profondeur
                        

                                                             
                        
                        dcc.Dropdown(id='function-dropdown', placeholder='Sélectionnez une fonction du fichier chargé', style={'display':'none'}),                    

                    
                    dcc.Dropdown(id='choix_scinder',
                                 options=[  
                                    {'label': 'Charnière', 'value': 'charniere'},
                                 ],style={'display':'none'}
                                 
                                 ),
                    
                    dcc.Dropdown(id='choix_charniere',style={'display':'none'}),
                    
                    html.Div(id='saut_fcnt_filtrees_drp'),
                    #Filtrage de données
                    html.Div(id='info_filtre_1'),
                    html.Div(id='info_filtre_2'),
                dcc.Dropdown(id='columns',multi=True,style={'display':'none'}),#Selectionner quel colonne on veut exclure de notre data frame
                html.Div(id='info_filtre_4'),
                dcc.Dropdown(id='date-picker2', multi=True, style={'width':'100%','display': 'none'}), #Choix de ou des jours 
                
                html.Div(id='info_filtre_3'),

                dcc.Dropdown(id='filtrage_temp_heure_debut', placeholder='Entrez le debut du filtrage horaire', style={'overflowY':'visible','vertical-align':'right','display': 'none','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px','width':'90%'}),
                html.Div(id='saut_filtre_1'),

                dcc.Dropdown(id='filtrage_temp_heure_fin', placeholder='Entrez la fin du filtrage horaire', style={'overflowY':'visible','vertical-align':'right','display': 'none','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px','width':'90%'}),
                html.Div(id='msg_filtrage_donnees',style={'vertical-align':'top','display':'flex'}),
                

                dcc.Dropdown(id='filtrage_données', style={'display':'none'},multi=True),#Colonnes de reference pour la fonctio Filtrage de données
                html.Div(id='saut_ligne_comp1'),

                html.Td(id='ligne_comp',children=[dcc.Dropdown(id='comp_colonne',style={'display': 'none','width':'100%','vertical-align':'top','maring-left':'5px'},multi=True),]),
                    html.Td(id='drp_col_filtrees',children=[
                            html.Div(id='msg_col_filtrees'),
                             dcc.Dropdown(id='fcnt_drp_filtrees',multi=True, placeholder='Sélectionnez une/des colonne(s)', style={'display':'none'}),
                             ]),
                    

                    ],style={'width':'30%','heigh':'20px','border': '1px solid #1e2130', 'padding-left': '8px'}),
                    html.Td([
                           html.Button('Ouvrir le code par défaut', id='vs_code_fcnt',style={'display':'none'}),

                         dcc.Input(#zone de texte permettant de rentrer la valeur de seuille pour notre filtrage de donnée
                        id='equation_solveur', type='text', placeholder='Nom de colonne = votre formule',style={'display':'none'}
                    ),
                    dcc.Checklist(
                            id='options_pente',
                            options=[
                                {'label': 'Valeur absolue', 'value': 'ABS'},
                                {'label': 'Normaliser les pics à 1', 'value': 'LIMIT'}
                            ],
                            value=[]
                        ),
                    html.Div(id='info_choix_df'),
                    dcc.Dropdown(id='choix_df_filtrage',options=[
                        {'label':'Choix Data Frame 1','value':'choix_df1'},
                        {'label':'Choix Data Frame 2','value':'choix_df2'},
                        {'label':'Choix Data Frame 3','value':'choix_df3'},
                        {'label':'Choix Data Frame 4','value':'choix_df4'},
                        {'label':'Choix Data Frame 5','value':'choix_df5'},
                    ],style={'display':'none'}),
                    html.Button('Calculer', id='btn_solveur', n_clicks=0), 
                    html.Button('Valider', id='validate-button',style={'display':'none'}),
                    
                    
                    
                    
                    html.Div(id='info_numpy', children=[
                                dcc.Markdown(message,style={'font-size': '13px'})
                            ]),
                    html.Div(id='ok_pente'),
                    html.Div(id='texte_regression'),
                    html.Button('Calculer', id='btn_pente', n_clicks=0),
                                               
                        
                        html.Div(id='saut16'),
                                               
                daq.ColorPicker(#Element permettant de choisir notre couleur pour la fonction Profondeur
                            id='my-color-picker-1',
                            label='Color Picker',
                            style={'display':'none'}
                        ),
                dcc.RadioItems(#RadioItems permets d'avoir des bouttons a choix, qui ceux unique on doit faire 1 choix sur les differentes proposition
                    id='palette_defaut',#Identifiant de ce dcc.RadioItems
                    options=[#Options correspond aux choix qu'on pourras faire avec ce RadioItems, meme principe que pour les dropdown
                        {'label': 'Temperature', 'value': 'temperature'},
                        {'label': 'Heure de la journée (minuit à minuit)', 'value': 'temps'},
                        {'label': 'Autres données', 'value': 'autre'}
                    ], 
                    inline=False, style={'width':'100%','display': 'none'}#l'options inline permets d'avoir les bouttons de choix a la suite 
                ), 
                        html.Div(id='color-palette'),
                        html.Div(id='saut_comp'),
                        html.Div(id='msg_filtrage_donnees2',style={'vertical-align':'top','display':'flex'}),

                        dcc.Input(#zone de texte permettant de rentrer la valeur de seuille pour notre filtrage de donnée
                        id='threshold',
                        #type='number',
                        placeholder='Entrez une valeur de seuil',style={'display':'none'}
                    ),
                        dcc.RadioItems(#Ce RadioItems correspond au choix d'appliquer un filtrage sur nos données
                            id='condition1',
                            options=[
                                {'label': 'Supérieur', 'value': 'gt'},
                                {'label': 'Égal', 'value': 'eq'},
                                {'label': 'Inférieur', 'value': 'lt'}
                                ],
                            inline=True,style={'display':'none'}#Le style={'display':'none'} permet de ne pas afficher de base ce RadioItems pour l'afficher qu'a une certaine condition par exemple ici il s'afficheras que quand on selectionneras filtrage dans le menu 'filtre' et pour l'afficher on change le display:none en display: block ou inline-block
                            ),
                        dcc.Input(#zone de texte permettant de rentrer la valeur de seuille pour notre filtrage de donnée
                        id='threshold2',
                        #type='number',
                        placeholder='Entrez une valeur de seuil',style={'display':'none'}
                    ),
                        dcc.RadioItems(#Ce RadioItems correspond au choix d'appliquer un filtrage sur nos données
                            id='condition2',
                            options=[
                                {'label': 'Supérieur', 'value': 'gt'},
                                {'label': 'Égal', 'value': 'eq'},
                                {'label': 'Inférieur', 'value': 'lt'}
                                ],
                            inline=True,style={'display':'none'}#Le style={'display':'none'} permet de ne pas afficher de base ce RadioItems pour l'afficher qu'a une certaine condition par exemple ici il s'afficheras que quand on selectionneras filtrage dans le menu 'filtre' et pour l'afficher on change le display:none en display: block ou inline-block
                            ),
                        dcc.Input(#zone de texte permettant de rentrer la valeur de seuille pour notre filtrage de donnée
                        id='threshold3',
                        #type='number',
                        placeholder='Entrez une valeur de seuil',style={'display':'none'}
                    ),
                        dcc.RadioItems(#Ce RadioItems correspond au choix d'appliquer un filtrage sur nos données
                            id='condition3',
                            options=[
                                {'label': 'Supérieur', 'value': 'gt'},
                                {'label': 'Égal', 'value': 'eq'},
                                {'label': 'Inférieur', 'value': 'lt'}
                                ],
                            inline=True,style={'display':'none'}#Le style={'display':'none'} permet de ne pas afficher de base ce RadioItems pour l'afficher qu'a une certaine condition par exemple ici il s'afficheras que quand on selectionneras filtrage dans le menu 'filtre' et pour l'afficher on change le display:none en display: block ou inline-block
                            ),
                        
                        
                        
                        dcc.RadioItems(#Permet de choisir quel type de moyenne utilisé
                            id='type_mean',
                            options=[
                                {'label': 'Moyenne glissante', 'value': 'mean_g'},{'label': 'Moyenne cumulée', 'value': 'mean_cum'},{'label': 'Moyenne horaire', 'value': 'mean_horaire'}
                            ],
                            value='mean_g',inline=True,
                            style={'display': 'none'}
                        ),
                        html.Div(id='saut8'),
                        dcc.Input(id='text-rename', type='text', placeholder='Nouveau nom de colonne'),

                        html.Button('Soumettre', id='submit-rename', n_clicks=0,style={'display':'none'}),#boutton pour valider notre saisie du nouveau nom de la colonne

                        html.Button('Valider Couleur', id='submit-color', n_clicks=0,style={'display':'none'}),#boutton pour valider notre saisie sur la valeur de couleur
                        html.Button('Clear Couleur', id='clear-color', n_clicks=0,style={'display':'none'}),#boutton pour supprimer la couleur

                        html.Div(id='information_reg_et_prof'),
                        html.Div(id='text_df_filtre'),
                          

                       
                        dcc.RadioItems(# Permet de choisir si on veux exclure des données ou non sa valeur par defaut est filtrage_off
                            id='exclure', 
                            options=[
                                {'label': 'Filtrage', 'value': 'filtrage_on'},{'label': 'Sans Filtrage', 'value': 'filtrage_off'}
                            ],
                            value='filtrage_off',inline=True,
                            style={'display': 'none'}
                        ),
                        
                        
                        
                        html.Button('Valider les puissances', id='valider', style={ 'display': 'none'}),


                        dcc.Input(id='moyenne', type='text', placeholder='Entrez une moyenne glissante', style={'display': 'none'}),#Zone de texte pour ecrire sur combien de temps on veut notre moyenne glissante
                        html.Button('Appliquer la moyenne', id='button2', style={'display': 'none'}),#Boutton pour valide notre moyenne glissante
                        dcc.Input(
                            id='rolling_window',
                            type='text',
                            placeholder='Taille de la fenêtre (ex: 00:30:00 )',style={'display': 'none'}
                       ),
                        html.Button('Appliquer la moyenne', id='submit-button', n_clicks=0,style={'display': 'none'}),
                        dcc.RadioItems(id='check_filtre',
                                options=[
                                    {'label': 'Avec Filtrage', 'value': 'avec_filtrage'},
                                    {'label': 'Sans filtrage', 'value': 'sans_filtrage'},
                                ],value='sans_filtrage', style={'display':'none'}
                            ),
                        html.Div(id='saut_ligne_comp2'),
                        html.Button('Exporter', id='exp_scission', style={'display': 'none'}),#Button pour valider notre saisie
                        html.Div(id='msg_filtrage_donnees3',style={'vertical-align':'top','display':'flex'}),

                        
                        html.Div(id='saut_fcnt_filtrees_btn'),

                         html.Td(id='btn_col_filtrees',children=[
                            html.Div(id='df_filtrees_text'),

                            html.Button('Valider', id='ok_fcnt_filtrees', n_clicks=0,style={'display':'none'}),
                            ]),#boutton pour supprimer la couleur
                         html.Td(id='ligne_comp_cond',children=[
                              dcc.RadioItems(#Ce RadioItems correspond au choix d'appliquer un filtrage sur nos données
                            id='condition_colonne',
                            options=[
                                {'label': 'Supérieur', 'value': 'gt'},
                                {'label': 'Égal', 'value': 'eq'},
                                {'label': 'Inférieur', 'value': 'lt'}
                                ],
                            inline=True,style={'display':'none'}#Le style={'display':'none'} permet de ne pas afficher de base ce RadioItems pour l'afficher qu'a une certaine condition par exemple ici il s'afficheras que quand on selectionneras filtrage dans le menu 'filtre' et pour l'afficher on change le display:none en display: block ou inline-block
                            ),],style={'display':'none','marginBottom':'5px'}),
                        html.Div(id='saut_ligne_comp3'),

                        html.Td(id='btn_ligne_seuil',children=[

                            html.Button('Valider le filtrage', id='submit', n_clicks=0,style={'display':'none'}),#boutton pour valider notre saisie sur la valeur de seuil

                        ],style={'display':'none','marginBottom':'5px'}),
                        ],style={'heigh':'20px','border': '1px solid #1e2130','width':'40%', 'padding-left': '8px'}),
                
                ],style={'padding-top': '0px'},),
               
            ], style={'border': '10px solid #fae5d3','width':'140%','display':'none','margin-left':'8px'}),
        ], style={'display': 'block','width':'140%','margin-left':'50px'}),#, 'justify-content': 'space-between'}),

               
    ], style={'width': '50%', 'display': 'inline-block', 'vertical-align': 'top'}),
    html.Div([
        modal,
       
        
        dcc.Download(id="download"),
        dcc.Download(id="download_F1_scission"),
        dcc.Download(id="download_F2_scission"),

        html.Br(),
        dcc.RadioItems(#Permet de choisir quel type de graphique soit lineaire soit nuage de point sa valeur par defaut est lineaire pour faciliter le 1er affichage 
            id='fusion',
            options=[
                {'label': 'Fichiers non fusionner', 'value': 'f_fusion'},{'label': 'Fichiers fusionner', 'value': 't_fusion'}                
            ],
            value='f_fusion',inline=True,style={'display': 'none'}
        ),

        dcc.Download(id="download_df"),
       #Permet de crée deux bouttons pour switch entre le data frame originel et celui décalé par défaut le choix est sur data frame originel grace a "value='DF_Brut'"
    ], style={'width': '50%', 'display': 'inline-block', 'vertical-align': 'top-right', 'text-align': 'right'}),
    html.Div(id='output-table', style={'margin': 'auto', 'width': '95%'}),#Affichage du Tableau 
     #],style={'display':'inline-block'}),#La roue qui tourne

    html.Pre(id='output-container'),
    html.Div(id='slider-temp',style={'margin-left':'15px','margin-right':'15px'}),
    html.Div(id='sliders2',style={'margin-left':'15px','margin-right':'15px'}),
    html.Div(id='output-container-slider',style={'margin-left':'15px','margin-right':'15px'}),

    # Icône du chatbot
    html.Div(id='chat-icon', children='🤖', style=styles_chatbot['chat-icon']),
    # Fenêtre de chat
    html.Div(id='chat-window', style=styles_chatbot['chat-window'], children=[
        html.Div("Chatbot", style=styles_chatbot['chat-header']),
        html.Div(id='chat-messages1'),
        html.Div([
            dcc.Markdown(id='chat-messages'),
        ], style=styles_chatbot['chat-messages']),

        html.Div(style=styles_chatbot['chat-input-container'], children=[
            dcc.Input(id='chat-input', type='text', placeholder='Écrivez un message...', style=styles_chatbot['chat-input']),
            html.Button('Envoyer', id='chat-send-button',n_clicks=0, style=styles_chatbot['chat-send-button']),
        ]),
    ])
   ])