
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

from pages.fonctions import *
from utils.data_traitment import global_df_brut,global_df_repared,global_df_mean,global_repared_na,global_meandf_decal,global_meandf_repared,global_meandf_repared_na,global_df_fusionnées,global_meandf_fusionnées,global_df_1,global_df_2,global_df_3,global_df_4,global_df_5,global_meandf_1,global_meandf_2,global_meandf_3,global_meandf_4,global_meandf_5,global_fusion_data

from pages.graphique import *
from utils.Fonctions import choix_df


