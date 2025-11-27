#Projet multi disciplinaire

import dash 
import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, ctx
from dash import html,dcc,dash_table
import requests
from io import StringIO
css_code="""
<style>
.sidebar {
    width: 50px;
    height: 100vh; 
    background-color: #f8f9fa;
    position: fixed;
    transition: width 0.3s;
    overflow: hidden;
    z-index: 1000;
}

.sidebar:hover{
    width: 200px;
}
.sidebar-link {
    display: flex;
    align-items: center;
    padding: 10px;
    margin-bottom: 10px; 
    text-decoration: none;
    color: #000;
    cursor: pointer;
    width: 100%;
    border-left: 4px solid transparent;
    transition: all 0.3s;
    font-size: 24px;
}

.sidebar-link:hover{
    background-color: #e9ecef;
}
.sidebar-text{
    display: none;
    margin-left: 10px;
    white-space: nowrap;
    font-size: 16px;
}
.sidebar:hover .sidebar-text{
    display: inline;
    font-size: 16px;
}
.main-content{
    margin-left: 50px;
    padding: 20px;
    transition: margin-left 0.3s;
}
.sidebar:hover ~ .main-content{
    margin-left: 200px;
}
.sidebar-link.active{
    background-color: #dee2e6;
    border-left: 4pw solid #007bff;
    font-weight :bold;
}
</style>
"""
url ="https://data.statistiques.developpement-durable.gouv.fr/dido/api/v1/datafiles/1582861b-e042-4490-9161-6429d8229703/csv?COMMUNE_CODE=startsWith%3A77"
response = requests.get(url)
csv_data = StringIO(response.text)
df = pd.read_csv(csv_data,delimiter=';',encoding='utf-8')

#Fonction permmettant d'afficher le Tableau et le summary   
def Tableau(df):
    if df is None:
        return None
   # Calculer le résumé statistique et arrondir à 2 chiffres après la virgule
    summary = df.describe().round(2)
    # Ajouter une colonne pour expliquer chaque ligne
    summary['Description'] = {
        'count': 'Nombre total de valeurs',
        'mean': 'Moyenne des valeurs',
        'std': 'Écart type des valeurs',
        'min': 'Valeur minimale',
        '25%': '1/4 quart',
        '50%': '2/4 (médiane)',
        '75%': '3/4 quartile',
        'max': 'Valeur maximale'
    }


    # Réorganiser les colonnes pour que 'Description' soit la première colonne
    summary = summary[['Description'] + [col for col in summary.columns if col != 'Description']]
    # Convertir le résumé en format dictionnaire pour Dash DataTable
    summary_dict = summary.reset_index().to_dict('records')
    # Créer le tableau Dash avec les données du résumé
    summary_table = dash_table.DataTable(
        data=summary_dict,
        columns=[{'name': i, 'id': i} for i in summary.columns],
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#fdf2e9',
                'color': 'black',

            },
            {
                'if': {'row_index': 'even'},
                'backgroundColor': '#fdf2e9',
                'color': 'black',
            },
        ],
        style_header={
            'backgroundColor': '#fdf2e9',
            'color': 'black'
        },
        style_table={'overflowX': 'auto'},
        style_cell={'width': 'auto'},


    )
    if 'temps' in df.columns :
        cols = ['temps', 'Date','Heure'] + [col for col in df.columns if col not in ['temps', 'Date','Heure']]
        df = df[cols]
    # Créer le tableau Dash avec les données du DataFrame
    df_table = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'name': i, 'id': i} for i in df.columns],
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': '#fdf2e9',
            'color': 'black',
            'width':'100%',
        },
        {
            'if': {'row_index': 'even'},
            'backgroundColor': '#fdf2e9',
            'color': 'black',
            'width':'100%',
        },

    ],
    style_header={
        'backgroundColor': '#fdf2e9',
        'color': 'black'
    },   
    style_table={'overflowX': 'auto', 'overflowY': 'auto', 'maxHeight': '300px', 'width': '100%'}, 
    fixed_rows={'headers': True, 'data': 0},
    style_cell={'width': 'auto', 'minWidth': '200px'},  
)


    # Retourner les deux tableaux dans une Div, avec une ligne de rupture entre eux
    return html.Div([df_table, html.Br(),html.Br(), summary_table])

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP,"https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css"])#Création du site en precisant qu'on ne veut pas de message d'erreur avec " suppress_callback_exceptions=True"
app.title="Parc automobile Francais"
app.index_string=f"""
    <!DOCTYPE html>
        <html>
            <head>
                {{%metas%}}
                <title>Parc automobile Francais</title>
                {{%favicon%}}
                {{%css%}}
                {css_code}
            </head>
            <body>
                {{%app_entry%}}
                <footer>
                    {{%config%}}
                    {{%scripts%}}
                    {{%renderer%}}
                </footer>
            </body>
        </html>
"""
app.layout = html.Div(
    style={
        'backgroundColor': '#fdf2e9',
        'position': 'relative',
        'top': 0,
        'bottom': 0,
        'left': 0,
        'right': 0,
        'min-height': '10000px',
        'min-width': 'auto',
        'color': 'black',
        'font-family': 'Arial'
    },
    children=[
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
        dcc.Store(id='active-tab'),
        dcc.Dropdown(id='dataframe-drp',options={'label':'DataFrame Brut','value':'df_brut'},value='df_brut',style={'display':'inline-block','width':'120%','vertical-align': 'top-right','margin':'auto','backgroundColor': '#e7e7f4', 'color': 'black','border':'none','borderRadius': '10px'}),
        html.Table(
            children=[
                # Première ligne
                html.Tr([
                    html.Td([]),  # Partie supérieure gauche vide
                    html.Td([
                        html.Div(id='affichage_element'),
                        html.Table(
                            id='table-graph_2',
                            children=[
                                html.Div([
                                    html.Div([
                                        html.Div(id='text_x_axis', children=["Choissisez votre axe x"], style={'display': 'inline-block'}),
                                        html.Div(id='unité_x', children=["Choissisez votre unité x"], style={'display': 'inline-block', 'margin-left': '15px'}),
                                        dcc.Input(id='x-axis-unit', type='text', style={'display': 'none'}),
                                        dcc.Dropdown(id='x-axis', placeholder="Axe X", style={'vertical-align': 'left', 'display': 'none', 'width': '50%'})
                                    ], style={'display': 'inline-block', 'vertical-align': 'top-left', 'width': '30%'}),
                                    html.Div([
                                        html.Div(id='text_y_axis', children=["Choissisez votre axe y"], style={'display': 'inline-block'}),
                                        html.Div(id='unité_y', children=["Choissisez votre unité y"], style={'display': 'inline-block', 'margin-left': '20px'}),
                                        dcc.Input(id='y-axis-unit', type='text', style={'display': 'none'}),
                                        dcc.Dropdown(id='y-axis', placeholder="Axes Y primaire", multi=True, style={'vertical-align': 'center', 'display': 'none', 'width': '60%'})
                                    ], style={'display': 'inline-block', 'vertical-align': 'top-center', 'width': '30%', 'margin-left': '50px'}),
                                    html.Div([
                                        html.Br(),
                                        html.Div(id='text_y2_axis', children=["Choissisez votre axe y2"], style={'display': 'inline-block'}),
                                        html.Div(id='unité_y2', children=["Choissisez votre unité y2"], style={'display': 'inline-block', 'margin-left': '20px'}),
                                        dcc.Input(id='y2-axis-unit', type='text', style={'display': 'none'}),
                                        dcc.Dropdown(id='y2-axis', placeholder="Axes Y secondaire", multi=True, style={'overflowY': 'auto', 'vertical-align': 'right', 'display': 'none', 'width': '60%'})
                                    ], style={'display': 'inline-block', 'vertical-align': 'right', 'width': '30%', 'margin-left': '50px'}),
                                ], style={'display': 'inline-block', 'margin-left': '120px', 'vertical-align': 'top'})
                            ],
                            style={"display": 'none', 'margin': 'auto', 'width': '100%'}
                        )
                    ])
                ]),
                # Deuxième ligne
                html.Tr([
                    html.Td([
                        dcc.RadioItems(
                            id='type_graph',
                            options=[
                                {'label': 'Linéaire', 'value': 'line'},
                                {'label': 'Nuage de point', 'value': 'dot'},
                                {'label': 'Histogramme', 'value': 'bar'}
                            ],
                            value='line',
                            inline=True,
                            style={'display': 'none'}
                        ),
                        html.Div(
                            id='affichage_slider_point',
                            children=[
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
                            ],
                            style={'display': 'none', 'margin': 'auto', 'width': '100%'}
                        )
                    ])
                ])
            ],
            style={
                "width": "100%",
                "borderCollapse": "collapse",
                "margin-left": "60px",
                "display": "flex",
            }
        )
    ]
)

@app.callback(
    Output('active-tab','data'),
    Input('tab-tableau','n_clicks'),
    Input('tab-graphique','n_clicks'),
    Input('tab-maps','n_clicks'),
    Input('tab-fonctions','n_clicks'),
    Input('tab-informations','n_clicks'),
)
def flag_onglets(n1,n2,n3,n4,n5):
    if ctx.triggered_id is not None:
        return ctx.triggered_id.replace('tab-','')
    return 'tableau'

@app.callback(
    Output('affichage_element','children'),
    Output('affichage_slider_point','style'),
    Output('table-graph_2','style'),
    Input('active-tab','data')
)
def affichage_onglet(tab):
    global df
    if tab=='tableau':
        return Tableau(df),{'display':'none'},{'display':'none'}
    elif tab=='graphique':
        return None,{"display":'block','margin':'auto','width':'100%'},{'display':'block'}
    elif tab=='maps':
        return dash.no_update,{'display':'none'},{'display':'none'}
    elif tab=='informations':
        return dash.no_update,{'display':'none'},{'display':'none'}
    elif tab=='fonctions':
        return dash.no_update,{'display':'none'},{'display':'none'}

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
if __name__ == '__main__':
    app.run(debug=True)