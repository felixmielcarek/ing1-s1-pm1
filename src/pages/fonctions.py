from dash import Input, Output, State, callback, ctx
import dash
from dash import dcc, html, no_update
import numpy as np
import pandas as pd
import dash_daq as daq
def affectation_df(choix,df,global_df_brut,global_df_repared,global_df_loisdeau,global_df_decal,global_df_filtrees,global_df_mean,global_meandf_filtrees,global_repared_na,global_meandf_decal,global_meandf_repared,global_meandf_repared_na,global_df_fusionnées,global_meandf_fusionnées,global_meandf_1,global_meandf_2,global_meandf_3,global_meandf_4,global_meandf_5,global_df_1,global_df_2,global_df_3,global_df_4,global_df_5):
    match choix :
        case 'DF_Brut': 
            global_df_brut=df
        
        case 'df_fusionnées' if df is not None: 
            global_df_fusionnées=df
        case 'df_mean' if df is not None:
            global_df_mean=df
                
        case 'meandf_filtrees':
            global_meandf_filtrees=df
        case 'df_filtrees':
            global_df_filtrees=df
        case 'df_1':
            global_df_1=df
        case 'df_2':
            global_df_2=df

        case 'df_3':
            global_df_3=df

        case 'df_4':
            global_df_4=df

        case 'df_5':
            global_df_5=df

        case 'meandf_1':
            global_meandf_1=df

        case 'meandf_2':
            global_meandf_2=df

        case 'meandf_3':
            global_meandf_3=df

        case 'meandf_4':
           global_meandf_4=df

        case 'meandf_5':
            global_meandf_5=df

#Fonction permettant de recrée les données manquantes temporel
def interpolate(df,mask,pas,ordre):
    ordre=int(ordre)
    for i in mask[mask].index:
        diff = df.loc[i, 'pas']
        start = df.loc[i-1, 'temps']
        while diff > pas: #Recreation des lignes manquantes
            start = start + pd.Timedelta(seconds=pas)
            diff -= pas
            df.loc[df.index.max() + 1] = {'temps': start}
    df = df.sort_values('temps').reset_index(drop=True)
    # Compléter les NaN avec la fonction interpolate option polynomiale
    for col in df.columns:
        if df[col].dtype == np.number:
            df[col] = df[col].interpolate(method='polynomial', order=ordre)
    return df

def apply_filters(df, col, conditions, thresholds, condition_colonne, comp_colonne):
    """
    Applique les filtres sur le DataFrame.
    """
    filtered_df = df.copy()
    
    if col is not None and conditions is not None and thresholds is not None:
        for col_name, condition, threshold in zip(col, conditions, thresholds):
            if col_name is not None and condition is not None and threshold is not None:
                if isinstance(threshold, str) and threshold.replace('.', '', 1).isdigit():
                    threshold = float(threshold)
                
                if condition == 'gt':
                    filtered_df = filtered_df[filtered_df[col_name] > threshold]
                elif condition == 'eq':
                    filtered_df = filtered_df[filtered_df[col_name] == threshold]
                elif condition == 'lt':
                    filtered_df = filtered_df[filtered_df[col_name] < threshold]
    
    if condition_colonne is not None and comp_colonne is not None and len(comp_colonne) == 2:
        if condition_colonne == 'gt':
            filtered_df = filtered_df[filtered_df[comp_colonne[0]] > filtered_df[comp_colonne[1]]]
        elif condition_colonne == 'eq':
            filtered_df = filtered_df[filtered_df[comp_colonne[0]] == filtered_df[comp_colonne[1]]]
        elif condition_colonne == 'lt':
            filtered_df = filtered_df[filtered_df[comp_colonne[0]] < filtered_df[comp_colonne[1]]]
    
    return filtered_df

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

layout_fonctions = html.Div([
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

                dcc.Dropdown(id='filtrage_temp_heure_debut', placeholder='Entrez le debut du filtrage horaire', style={'overflowY':'visible','vertical-align':'right','display': 'none','backgroundColor': '#eeeeee', 'color': 'black','border':'none','borderRadius': '10px','width':'90%'}),
                html.Div(id='saut_filtre_1'),

                dcc.Dropdown(id='filtrage_temp_heure_fin', placeholder='Entrez la fin du filtrage horaire', style={'overflowY':'visible','vertical-align':'right','display': 'none','backgroundColor': '#eeeeee', 'color': 'black','border':'none','borderRadius': '10px','width':'90%'}),
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