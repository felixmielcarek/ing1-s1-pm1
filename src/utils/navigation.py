
"""
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
)

"""

from dash import Input, Output, callback, ctx
from pages.tableau import *
from pages.informations import *

@callback(
    Output('page-content', 'children'),

    Input('tab-tableau','n_clicks'),
    Input('tab-graphique','n_clicks'),
    Input('tab-maps','n_clicks'),
    Input('tab-fonctions','n_clicks'),
    Input('tab-informations','n_clicks')
)
def generate_page_content(tableau_click,
                          graphique_click,
                          maps_click,
                          fonctions_click,
                          informations_click):
    match ctx.triggered_id:
        case 'tab-tableau':
            return generate_tableau_page()
        case 'tab-graphique':
            return generate_tableau_page()
        case 'tab-maps':
            return generate_tableau_page()
        case 'tab-fonctions':
            return generate_tableau_page()
        case 'tab-informations':
            return generate_informations_page()
        
        case _:
            return generate_tableau_page()