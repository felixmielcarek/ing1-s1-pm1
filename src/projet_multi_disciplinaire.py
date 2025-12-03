#Projet multi disciplinaire

import dash 
import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, ctx
from dash import html,dcc,dash_table
import requests
from io import StringIO
from front_end import app_layout
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
url =r"C:\Users\micae\Desktop\Projet multisciplinaire\Projet multisciplinaire CODE\ing1-s1-pm1\Data\Donnees-sur-le-parc-de-vehicules-au-niveau-communal.2025-09.csv" #"https://data.statistiques.developpement-durable.gouv.fr/dido/api/v1/datafiles/1582861b-e042-4490-9161-6429d8229703/csv?COMMUNE_CODE=startsWith%3A77"

df = pd.read_csv(url,delimiter=';',encoding='utf-8')

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
app.layout = app_layout


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