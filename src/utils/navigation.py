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

dcc.Store(id='active-tab', data='tableau'),

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