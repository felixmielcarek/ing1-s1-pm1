@app.callback(
    Output('x-axis','style'),
    Output('y-axis','style'),
    Output('y2-axis','style'),
    Output('text_x_axis','style'),
    Output('text_y_axis','style'),
    Output('text_y2_axis','style'),
    Output('unité_x','style'),
    Output('unité_y','style'),
    Output('unité_y2','style'),
    Output('x-axis-unit','style'),
    Output('y-axis-unit','style'),
    Output('y2-axis-unit','style'),
    Output('type_graph','style'),
    Output('x-axis','options'),
    Output('y-axis','options'),
    Output('y2-axis','options'),
    Input('active-tab','data')
)
def update_elements_graphique(tab):
    global df
    if tab=='graphique':
        options=[{'label': col, 'value': col} for col in df.columns]
        style={'vertical-align': 'left', 'display': 'inline-block', 'width': '50%'}
        return style,{'vertical-align': 'center', 'display': 'inline-block', 'width': '60%'}, {'vertical-align': 'right', 'display': 'inline-block', 'width': '60%'}, {'display': 'inline-block'}, {'display': 'inline-block'}, {'display': 'inline-block'}, {'display': 'inline-block', 'margin-left': '15px'}, {'display': 'inline-block', 'margin-left': '20px'}, {'display': 'inline-block', 'margin-left': '20px'}, {'display': 'inline-block'}, {'display': 'inline-block'}, {'display': 'inline-block'}, {'display':'block'}, options, options, options
    else:
        return {'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},dash.no_update,dash.no_update,dash.no_update 

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

# Exemple de fonction de calcul du R²
def calculate_r_squared(x, y, func, popt):
    residuals = y - func(x, *popt)
    ss_res = sum(residuals**2)
    ss_tot = sum((y - y.mean())**2)
    return 1 - (ss_res / ss_tot)

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

def create_scatter_trace(x, y, name, mode='markers', secondary_y=False, **kwargs):
    """
    Crée une trace Scatter pour un graphique Plotly.
    """
    return go.Scatter(x=x, y=y, name=name, mode=mode, **kwargs), secondary_y

def add_regression_trace(fig, x_data, y_data, fitting_function, y_axis_name):
    """
    Ajoute une courbe de régression au graphique.
    """
    mask = ~np.isnan(x_data) & ~np.isnan(y_data)
    x_data = x_data[mask]
    y_data = y_data[mask]
    
    popt, _ = curve_fit(fitting_function, x_data, y_data)
    y_fit = fitting_function(x_data, *popt)
    
    equation = f"Regression {y_axis_name}: y = {popt[0]:.2f}x + {popt[1]:.2f}"
    fig.add_trace(go.Scatter(x=x_data, y=y_fit, name=equation, mode='lines', line=dict(color='black', width=3)))
    
    return equation

#Fonctions permettant de savoir quel equation afficher
def choix_equation(fitting_function, *popt):
    match fitting_function:
        case 'Linear':
            return "y = {:.2e}x + {:.2e}".format(*popt)
        case 'Cauchy':
            return "y = {:.2e}+{:.2e}/x^2 + {:.2e}/x^4".format(*popt)
        case 'Cubic':
            return "y = {:.2e} * x^3 + {:.2e} * x^2 + {:.2e} * x + {:.2e}".format(*popt)
        
        case 'Damped Function':
            return "y = {:.2e}e^(-{:.2e}x) + {:.2e}".format(*popt)
        
        case 'Damped Oscillator':
            return "y = {:.2e}e^(-{:.2e}x) * sin({:.2e} * x+{:.2e}) + {:.2e}".format(*popt)
        
        case 'Exponential':
            return "y = {:.2e}e^({:.2e}x)+{:.2e}".format(*popt)
        
        case 'Gaussian':
            return "y = {:.2e}e^(-(x - {:.2e})^2 / (2 * {:.2e}^2))+{:.2e}".format(*popt)
        
        case 'Inverse':
            return "y = {:.2e} / ({:.2e} + x )".format(*popt)
        
        case 'Logistic':
            return "y = {:.2e} / (1 + {:.2e}e^(-{:.2e}x))".format(*popt)
        
        case 'Lorentzian':
            A, omega0, beta, C = popt
            return "y = {:.2e} * sqrt((({:.2e}^2 - x^2)^2 + 4 * x^2 * {:.2e}^2)) + {:.2e}".format(A, omega0, beta, C)

        
        case 'Natural Log':
            return "y = {:.2e} * ln( x * {:.2e} )".format(*popt)
        
        case 'Oscillator':
            return "y = {:.2e} * sin(2π * {:.2e} * x + {:.2e})+{:.2e}".format(*popt)
        
        case 'Poisson':
            return "y = {:.2e} * e^(-{:.2e}) * ({:.2e})^x / x!".format(popt[0], popt[1], popt[1])
        
        case 'Power Law':
            return "y = {:.2e} * x^{:.2e}".format(*popt)
        
        case 'Power Law with Offsets':
            return "y = {:.2e} * (x - {:.2e})^{:.2e} + {:.2e}".format(*popt)
        
        case 'Quadratic':
            return "y = {:.2e}x^2 + {:.2e}x + {:.2e}".format(*popt)
        case'Quartic':
            return "y = {:.2e}x^4+{:.2e}x^3 +{:.2e}x^2 + {:.2e}x + {:.2e}".format(*popt)

        case 'Stokes Law':
            k0, a0, K1 = popt
            return "y = ({:.2e} / (18 * {:.2e})) * x^2 * (1 - 2.1 * x / {:.2e})".format(k0, a0, K1)

        
        case 'Two Slit Interference':
            val_x0 = popt[3]
            formatted_val_x0 = "{:.2e}".format(val_x0)
            return "y = {:.2e} * sinc^2({:.2e} * (x - {}) / π) * cos^2({:.2e} * (x - {:.2e})) + {:.2e}".format(popt[0], popt[1], formatted_val_x0, popt[2], val_x0, popt[4])




graphique_layout = html.Table(id='table-graph',children=[
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






