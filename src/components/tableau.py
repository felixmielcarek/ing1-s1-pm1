
def Tableau(df,couleur_text,couleur_background):
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
                'backgroundColor': couleur_background,
                'color': couleur_text,

            },
            {
                'if': {'row_index': 'even'},
                'backgroundColor': couleur_background,
                'color': couleur_text,
            },
        ],
        style_header={
            'backgroundColor': couleur_background,
            'color': couleur_text
        },
        style_table={'overflowX': 'auto'},
        style_cell={'width': 'auto'},
    )
    
    # Créer le tableau Dash avec les données du DataFrame
    df_table = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'name': i, 'id': i} for i in df.columns],
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': couleur_background,
            'color': couleur_text,
            'width':'100%',
        },
        {
            'if': {'row_index': 'even'},
            'backgroundColor': couleur_background,
            'color': couleur_text,
            'width':'100%',
        },

    ],
    style_header={
        'backgroundColor': couleur_background,
        'color': couleur_text
    },   
    style_table={'overflowX': 'auto', 'overflowY': 'auto', 'maxHeight': '300px', 'width': '100%'}, 
    fixed_rows={'headers': True, 'data': 0},
    style_cell={'width': 'auto', 'minWidth': '200px'},  
    )


    # Retourner les deux tableaux dans une Div, avec une ligne de rupture entre eux
    return html.Div([df_table, html.Br(),html.Br(), summary_table])
    