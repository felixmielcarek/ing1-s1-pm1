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
)