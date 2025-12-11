
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
from pages.graphique import *
from pages.informations import *
from utils.data_traitment import global_df_brut,global_df_repared,global_df_mean,global_repared_na,global_meandf_decal,global_meandf_repared,global_meandf_repared_na,global_df_fusionnées,global_meandf_fusionnées,global_df_1,global_df_2,global_df_3,global_df_4,global_df_5,global_meandf_1,global_meandf_2,global_meandf_3,global_meandf_4,global_meandf_5,global_fusion_data
from pages.graphique import *
import Fonctions
@callback(
    Output('page-content', 'children'),
    Output('titre-page','children'),
    Input('tab-tableau','n_clicks'),
    Input('tab-graphique','n_clicks'),
    Input('tab-maps','n_clicks'),
    Input('tab-fonctions','n_clicks'),
    Input('tab-informations','n_clicks'),
    State('choix_df','value'),
)
def generate_page_content(tableau_click,
                          graphique_click,
                          maps_click,
                          fonctions_click,
                          informations_click,choix):
    newdf=Fonctions.choix_df(choix,global_df_brut,global_df_repared,global_df_mean,global_repared_na,global_meandf_decal,global_meandf_repared,global_meandf_repared_na,global_df_fusionnées,global_meandf_fusionnées,global_df_1,global_df_2,global_df_3,global_df_4,global_df_5,global_meandf_1,global_meandf_2,global_meandf_3,global_meandf_4,global_meandf_5,global_fusion_data)
    match ctx.triggered_id:
        case 'tab-tableau':
            return generate_tableau1(global_df_brut,'black','#f9f9f9'),"Page Tableau "
        case 'tab-graphique':
            return affichage_graphique(),"Page Graphique"
        case 'tab-maps':
            return None,"Page Maps"
        case 'tab-fonctions':
            return None,"Page Fonctions"

        
        case _:
            return None,""