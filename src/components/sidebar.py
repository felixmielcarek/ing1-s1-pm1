import dash.html as html

def generate_sidebar_item(icon_classname, title, div_id):
    return html.Div(
        [
            html.Div(className='sidebar-icon bi ' + icon_classname),
            html.Span(title, className='sidebar-text')
        ], 
        id = div_id, 
        className='sidebar-item', 
        n_clicks=0
    )

def generate_sidebar():
    return html.Div(
        id='sidebar',
        className='fs-2',
        children=[
            generate_sidebar_item('bi-table', 'Tableau', 'tab-tableau'),
            generate_sidebar_item('bi-graph-up', 'Graphique', 'tab-graphique'),
            generate_sidebar_item('bi-map', 'Maps', 'tab-maps'),
            generate_sidebar_item('bi-gear', 'Fonctions', 'tab-fonctions'),
            generate_sidebar_item('bi-download', 'Exporter le fichier', 'tab-exporter'),
            generate_sidebar_item('bi-info-circle', 'Informations', 'tab-informations')
        ]
    )