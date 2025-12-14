from pages.graphique import *
from pages.back_end_pages.back_end_graphique import *
@callback(
            Output('rolling_window', 'style'),
            Output('submit-button', 'style'), 
            Output('colonnes', 'options'),
            Output('colonnes', 'style'),
            Output('date-picker2', 'style'), 
            Output('Regression', 'style'), 
            Output('profond', 'style'),
            Output('points', 'style'), 
            Output('columns', 'options'), 
            Output('columns', 'style'),
            Output('exclure', 'style'),
            Output('type_graph', 'style'),
            Output('upload-second-data', 'style'),
            Output('constructeur', 'style'),
            Output('file-name', 'children'),
            Output('file', 'children'), 
            Output('version', 'style'),
            Output('filtre', 'style'),
            Output('table-options', 'style'),
            Output('time-shift-input', 'style'),
            Output('apply-button', 'style'),
            Output('puissances_elec', 'style'), 
            Output('puissances_therm', 'style'), 
            Output('valider', 'style'), 
            Output('saut1', 'children'), 
            Output('saut2', 'children'),
            Output('choix_temp', 'style'),
            Output('choix_tdp_ch', 'style'),
            Output('pelec', 'style'), 
            Output('qpac', 'style'), 
            Output('ptherm', 'style'), 
            Output('type_lois_deau', 'style'),
            Output('choix_cop', 'style'), 
            Output('filtrage_données', 'options'), 
            Output('filtrage_données', 'style'), 
            Output('condition1', 'style'),
            Output('submit', 'style'),
            Output('threshold', 'style'), 
            Output('avec_condition', 'style'),
            Output('filtrage_lois_deau_pelec', 'style'), 
            Output('filtrage_lois_deau_qpac', 'style'),
            Output('condition2', 'style'),
            Output('condition3', 'style'),
            Output('threshold3', 'style'), 
            Output('type_fusion', 'style'),
            Output('fichier_fusionner', 'style'), 
            Output('type_curve_fitting', 'style'),
            Output('saut_curve', 'children'), 
            Output('col-rename', 'options'),
            Output('submit-rename', 'style'), 
            Output('text-rename', 'style'), 
            Output('comp_colonne', 'options'), 
            Output('comp_colonne', 'style'),
            Output('condition_colonne', 'style'), 
            Output('solveur_colonne', 'options'), 
            Output('solveur_colonne', 'style'),
            Output('equation_solveur', 'style'), 
            Output('btn_solveur', 'style'), 
            Output('info_numpy', 'style'), 
            Output('ligne_comp', 'style'),
            Output('ligne_comp_cond', 'style'),
            Output('btn_ligne_seuil', 'style'),
            Output('saut_ligne_comp1', 'children'),
            Output('saut_ligne_comp2', 'children'),
            Output('saut_ligne_comp3', 'children'),
            Output('saut_comp', 'children'),
            Output('check_filtre', 'style'),
            Output('choix_scinder', 'style'),
            Output('choix_charniere', 'style'),
            Output('choix_charniere', 'options'),
            Output('exp_scission', 'style'), 
            Output('function-file-dropdown', 'style'),
            Output('function-dropdown', 'style'),
            Output('columns-dropdown', 'style'),
            Output('validate-button', 'style'),
            Output('columns-dropdown', 'options'),
            Output('drp_pente', 'style'),
            Output('drp_pente', 'options'),
            Output('btn_pente', 'style'),
            Output('msg_filtrage_donnees2', 'children'), 
            Output('msg_filtrage_donnees3', 'children'),
            Output('condi1', 'options'),
            Output('condi2', 'options'),
            Output('condi3', 'options'), 
            Output('condi4', 'options'),
            Output('condi5', 'options'),
            Output('condi6', 'style'), 
            Output('param1', 'style'),
            Output('param2', 'style'),
            Output('param3', 'style'), 
            Output('param4', 'style'), 
            Output('param5', 'style'),
            Output('type_bar', 'style'),
            Output('vs_code_fcnt', 'style'),
            Output('choix_PAC', 'style'),
            Output('type_capteur_temperature', 'style'),
            Output('temperature_int', 'style'), 
            Output('temperature_sortie', 'style'),
            Output('tqv', 'style'),
            Output('saut_tqv_pelec', 'children'),
            Output('qv', 'style'),
            Output('temperature_int', 'options'), 
            Output('choix_temp_rosee', 'style'),
            Output('choix_temp_rosee', 'options'),
            Output('filtrage_temp_heure_fin', 'style'),
            Output('filtrage_temp_heure_debut', 'options'),
            Output('filtrage_temp_heure_fin', 'options'), 
            Output('choix_df_filtrage', 'style'), 
            Output('info_filtre_1', 'children'),
            Output('info_filtre_2', 'children'),
            Output('info_filtre_3', 'children'),
            Output('saut_filtre_1', 'children'),
            Output('info_filtre_4', 'children'),
            Output('info_choix_df', 'children'),
            Output('type_capteur_hygro', 'style'),
            Output('type_capteur_pelec', 'style'), 
            Output('type_capteur_pression', 'style'),
            Output('type_capteur_debit', 'style'), 
            Output('temperature_air_sec_entre', 'options'),
            Output('temperature_air_sec_entre', 'style'),
            Output('temperature_air_sec_sortie', 'options'),
            Output('temperature_air_sec_sortie', 'style'),
            Output('temperature_rosee_int', 'options'),
            Output('temperature_rosee_int', 'style'),
            Output('temperature_rosee_sortie', 'options'),
            Output('temperature_rosee_sortie', 'style'),
            Input('type_mean', 'value'), 
            Input('filtre', 'value'), 
            Input('active-tab', 'data'),
            Input('choix_df_drp', 'value'),
            Input('fusion', 'value'),
            State('upload-data', 'filename'),
            State('pas', 'data'),
            State('threshold', 'value'),
            State('condition1', 'value'), 
            State('filtrage_données', 'value'), 
            State('columns', 'value'),
            Input('choix_scinder', 'value'),
            State('condition_colonne', 'value'),
            State('comp_colonne', 'value'),
            Input('active-tab', 'data')
            )
def filtre_tab3_et_tab2(type_mean, value, choix, fusion, filename, pas, choix_scinder,tab):
    if tab=='fonctions':
        style4={'display':'inline-block','width':'70%','margin':'auto','maring-left':'5px','backgroundColor': '#eeeeee', 'color': 'black','borderRadius': '10px','vertical-align':'top','margin-right':'5px'}
        table={'border': '10px solid #fae5d3','width':'140%','margin-left':'8px'}
    else:
        style4={'display':'none'}
        table={'display':'none'}
    if (global_df_brut is not None) and tab=='fonctions':
        df = choix_df(choix,global_df_brut,global_df_mean,global_meandf_repared,global_df_fusionnées,global_meandf_fusionnées,global_df_1,global_df_2,global_df_3,global_df_4,global_df_5,global_meandf_1,global_meandf_2,global_meandf_3,global_meandf_4,global_meandf_5)
        if df is not None and value is not None:
            match value:
                case 'filtrage_df_données':
                    msg_comp = html.Div([html.Br(), html.Br(), html.Div('Filtrage par colonne')])
                    msg_cond_comp = html.Div([html.Br(), html.Br()])
                    msg_filt_seuil = html.Div([html.Br(), html.Br(), html.Div('Filtrage par valeur seuil', style={'vertical-align': 'top', 'display': 'block'})])
                    saut_comp = html.Div([html.Br(), html.Br(), html.Br()])
                    options = [{'label': i, 'value': i} for i in df.columns]
                    style = {'fontSize': '15px', 'display': 'inline-block', 'width': '80%', 'vertical-align': 'top-right', 'margin': 'auto', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}
                    opt_columns = [{'label': i, 'value': i} for i in df.columns]
                    unique_times = df['temps'].unique()
                    return_option_filtrage_horaire = [{'label': str(time), 'value': time} for time in unique_times]
                    show_df = {'display': 'inline-block', 'width': '80%', 'margin': 'auto', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px', 'margin-left': '0px'}
                    aff1 = {'margin-bottom': '100px', 'display': 'inline-block', 'width': '100%', 'vertical-align': 'top', 'margin': 'auto', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}
                    return ({'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, style, {'display': 'none'}, {'display': 'none'}, {'display': 'block'}, opt_columns, aff1, {'display': 'inline-block', 'margin': 'auto'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, f'Nom du fichier : {filename}', f'Pas d acquisition : {pas} s', {'display': 'inline-block'}, style4, table, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, options, {'display': 'block', 'width': '80%', 'vertical-align': 'top', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}, {'display': 'inline-block'}, {'display': 'inline-block', 'backgroundColor': '#fae5d3', 'color': 'black', 'border': '2px solid #4b5160'}, {'margin-bottom': '100px', 'display': 'inline-block', 'width': '65%', 'vertical-align': 'top', 'margin': 'auto'}, {'display': 'none', 'width': '100%', 'vertical-align': 'top', 'margin': 'auto'}, {'display': 'none'}, {'display': 'none'}, {'display': 'inline-block'}, {'display': 'inline-block'}, {'margin-bottom': '100px', 'display': 'inline-block', 'width': '65%', 'vertical-align': 'top', 'margin': 'auto'}, {'margin-bottom': '100px', 'display': 'inline-block', 'width': '65%', 'vertical-align': 'top', 'margin': 'auto'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, options, {'display': 'inline-block', 'width': '80%', 'vertical-align': 'top', 'margin-left': '0px', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}, {'display': 'inline-block'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'width': '100%', 'padding-left': '0px', 'heigh': '100px', 'padding-top': '0px', 'border': '2px solid #1e2130', 'display': 'flex'}, {'width': '100%', 'padding-left': '0px', 'heigh': '100px', 'padding-top': '0px', 'border': '2px solid #1e2130', 'display': 'flex'}, {'width': '100%', 'padding-left': '0px', 'heigh': '100px', 'padding-top': '0px', 'border': '2px solid #1e2130', 'display': 'flex'}, msg_comp, msg_cond_comp, msg_filt_seuil, saut_comp, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, 'Filtrage par valeur seuil', 'Filtrage par colonne', {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, html.Br(), {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'overflowY': 'visible', 'vertical-align': 'right', 'display': 'inline-block', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px', 'width': '90%'}, {'overflowY': 'visible', 'width': '90%', 'vertical-align': 'right', 'display': 'inline-block', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}, return_option_filtrage_horaire, return_option_filtrage_horaire, show_df, 'Séléction des points', html.Div([html.Br(), html.Br(), html.Div('Exclusion de colonne(s)')]), html.Div([html.Br(), html.Br(), html.Div('Filtrage horaire')]), html.Br(), html.Div([html.Br(), html.Br(), html.Div('Séléction des jours')]), 'Veuillez choisir où vous allez stocker vos données.', {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'})
                case 'moyenne':
                    opt_colonnes = [{'label': i, 'value': i} for i in df.columns]
                    if type_mean == 'mean_g':
                        return ({'display': 'inline-block', 'margin': 'auto', 'width': '60%'}, {'display': 'inline-block', 'margin': 'auto', 'backgroundColor': '#fae5d3', 'color': 'black', 'border': '2px solid #4b5160'}, opt_colonnes, {'display': 'inline-block', 'width': '80%', 'vertical-align': 'top', 'margin': 'auto', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, f'Nom du fichier : {filename}', f'Pas d acquisition : {pas} s', {'display': 'inline-block'}, style4, table, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, dash.no_update, {'display': 'none'}, None, None, None, None, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'})
                    if type_mean != 'mean_g':
                        return ({'display': 'none'}, {'display': 'inline-block', 'margin': 'auto', 'backgroundColor': '#fae5d3', 'color': 'black', 'border': '2px solid #4b5160'}, opt_colonnes, {'display': 'inline-block', 'width': '80%', 'vertical-align': 'top', 'margin': 'auto', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, f'Nom du fichier : {filename}', f'Pas d acquisition : {pas} s ', {'display': 'inline-block'}, style4, table, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, dash.no_update, {'display': 'none'}, None, None, None, None, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'})
                case 'rename':
                    style_rename = {'fontSize': '15px', 'display': 'inline-block', 'width': '80%', 'vertical-align': 'top-right', 'margin': 'auto', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}
                    style_rename_buton = {'display': 'inline-block', 'vertical-align': 'top', 'text-align': 'center', 'margin': 'auto', 'borderRadius': '5px', 'backgroundColor': '#fae5d3', 'color': 'black', 'border': '2px solid #4b5160'}
                    opt_colonnes_rename = [{'label': i, 'value': i} for i in df.columns]
                    return ({'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, f'Nom du fichier : {filename}', f'Pas d acquisition : {pas} s', {'display': 'inline-block'}, style4, table, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, style_rename, opt_colonnes_rename, style_rename_buton, {'display': 'inline-block', 'margin': 'auto', 'width': '60%'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, dash.no_update, {'display': 'none'}, None, None, None, None, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, None)
                case 'scission':
                    if choix_scinder == 'charniere':
                        opt_colonnes_scission = [{'label': i, 'value': i} for i in df.columns]
                        drop_scission = {'margin-bottom': '100px', 'display': 'inline-block', 'width': '80%', 'vertical-align': 'top', 'margin': 'auto', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}
                    else:
                        opt_colonnes_scission = dash.no_update
                        drop_scission = {'display': 'none'}
                    return ({'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, f'Nom du fichier : {filename}', f'Pas d acquisition : {pas} s', {'display': 'inline-block'}, style4, table, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, html.Br(), html.Br(), None, None, {'display': 'inline-block'}, {'margin-bottom': '100px', 'display': 'inline-block', 'width': '80%', 'vertical-align': 'top', 'margin': 'auto', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}, drop_scission, opt_colonnes_scission, {'display': 'inline-block', 'margin': 'auto', 'backgroundColor': '#fae5d3', 'color': 'black', 'border': '2px solid #4b5160'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, dash.no_update, {'display': 'none'}, None, None, None, None, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, {'display': 'none'})
                case 'fichier':
                    drop10 = {'margin-bottom': '100px', 'display': 'inline-block', 'width': '80%', 'vertical-align': 'top', 'margin': 'auto', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}
                    style12 = {'display': 'inline-block', 'vertical-align': 'top', 'text-align': 'center', 'margin': 'auto', 'borderRadius': '5px', 'backgroundColor': '#fae5d3', 'color': 'black', 'border': '2px solid #4b5160'}
                    return ({'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, style12, drop10, f'Nom du fichier : {filename}', f'Pas d acquisition : {pas} s', {'display': 'inline-block'}, style4, table, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, dash.no_update, {'display': 'none'}, None, None, None, None, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, {'display': 'none'})
                case 'solveur':
                    opt_solveur = [{'label': i, 'value': i} for i in df.columns]
                    dropsolv = {'overflowY': 'visible', 'margin-bottom': '100px', 'display': 'inline-block', 'width': '80%', 'vertical-align': 'top', 'margin': 'auto', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}
                    style_formule = {'fontSize': '15px', 'display': 'inline-block', 'width': '80%', 'vertical-align': 'top-right', 'margin': 'auto', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}
                    style_formule_buton = {'display': 'inline-block', 'vertical-align': 'top', 'text-align': 'center', 'margin': 'auto', 'borderRadius': '5px', 'backgroundColor': '#fae5d3', 'color': 'black', 'border': '2px solid #4b5160'}
                    return ({'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, f'Nom du fichier : {filename}', f'Pas d acquisition : {pas} s', {'display': 'inline-block'}, style4, table, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, opt_solveur, dropsolv, style_formule, style_formule_buton, {'display': 'inline-block'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, dash.no_update, {'display': 'none'}, None, None, None, None, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'})
                case 'fcnt_extern':
                    opt_colonnes_fcnt = [{'label': i, 'value': i} for i in df.columns]
                    saut_fcnt = html.Br()
                    dropfcnt = {'overflowY': 'visible', 'margin-bottom': '100px', 'display': 'inline-block', 'width': '80%', 'vertical-align': 'top', 'margin': 'auto', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}
                    style_fcnt_button = {'display': 'inline-block', 'vertical-align': 'top', 'text-align': 'center', 'margin': 'auto', 'borderRadius': '5px', 'backgroundColor': '#fae5d3', 'color': 'black', 'border': '2px solid #4b5160'}
                    return ({'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, f'Nom du fichier : {filename}', f'Pas d acquisition : {pas} s', {'display': 'inline-block'}, style4, table, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, saut_fcnt, saut_fcnt, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, saut_fcnt, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, dropfcnt, dropfcnt, dropfcnt, style_fcnt_button, opt_colonnes_fcnt, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, style_fcnt_button, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, dash.no_update, {'display': 'none'}, None, None, None, None, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, {'display': 'none'})
                case 'fusion_fichier':
                    return ({'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, f'Nom du fichier : {filename}', f'Pas d acquisition : {pas} s', {'display': 'inline-block'}, style4, table, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'inline-block'}, {'display': 'inline-block'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, dash.no_update, {'display': 'none'}, None, None, None, None, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, [], {'display': 'none'}, {'display': 'none'})
                case 'prof':
                    return ({'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, dash.no_update, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, f'Nom du fichier : {filename}', f'Pas d acquisition : {pas} s', {'display': 'inline-block'}, style4, table, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, None, None, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'})
   