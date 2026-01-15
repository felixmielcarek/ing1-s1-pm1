from dash import html, dcc
import dash_bootstrap_components as dbc

# Layout pour la page carte
layout_map = html.Div(id='table-map', style={'display': 'none'}, children=[
    html.Div([
        html.H2("Carte Choroplèthe des Communes", style={
            'textAlign': 'center',
            'color': '#333',
            'marginBottom': '20px',
            'marginTop': '20px'
        }),
        
        # Options de visualisation
        html.Div([
            html.Label("Colonne pour la visualisation:", 
                      style={'fontWeight': 'bold', 'marginRight': '10px'}),
            dcc.Dropdown(
                id='map-color-column',
                placeholder='Sélectionner une colonne numérique...',
                style={'width': '300px', 'display': 'inline-block', 'marginRight': '20px'}
            ),
            html.Label("Groupement:", 
                      style={'fontWeight': 'bold', 'marginRight': '10px'}),
            dcc.Dropdown(
                id='map-groupby-column',
                options=[
                    {'label': 'Somme', 'value': 'sum'},
                    {'label': 'Moyenne', 'value': 'mean'},
                    {'label': 'Compte', 'value': 'count'},
                    {'label': 'Maximum', 'value': 'max'},
                    {'label': 'Minimum', 'value': 'min'}
                ],
                value='sum',
                style={'width': '150px', 'display': 'inline-block'}
            ),
        ], style={'marginBottom': '20px', 'textAlign': 'center'}),
        
        # Conteneur pour la carte Plotly
        dcc.Graph(
            id='choropleth-map',
            style={
                'height': '700px',
            },
            config={'displayModeBar': True, 'scrollZoom': True}
        ),
        
        # Informations sur les données
        html.Div(id='map-info', style={
            'marginTop': '20px',
            'padding': '15px',
            'backgroundColor': '#f8f9fa',
            'borderRadius': '5px',
            'textAlign': 'center'
        })
    ], style={
        'padding': '20px',
        'backgroundColor': 'white',
        'borderRadius': '10px',
        'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
    })
])
