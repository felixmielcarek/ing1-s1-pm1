from pages.graphique import *
from dash.exceptions import PreventUpdate
from pages.back_end_pages.back_end_graphique import *
import utils.data_traitment as dt
#from utils.data_traitment import *

#region AFFICHAGE DES ELEMENTS SUR LA PAGE FONCTIONS
@callback(
Output('texte_regression','children'),
    Output('rolling_window','style'),
    Output('submit-button','style'),
    Output('colonnes','options'),  
    Output('colonnes','style'),
    Output('profond','style', allow_duplicate=True),
    Output('columns','options'),
    Output('columns','style'),#A voir c'est un drp
    Output('exclure','style'), 
    Output('upload-second-data','style'),
    Output('file-name', 'children', allow_duplicate=True),#21 output
    Output('filtre','style'),
    Output('table-options','style'),

    Output('valider','style'),

    Output('saut8','children'),
    Output('text_df_filtre','children'),

    Output('filtrage_données','options'), 
    Output('filtrage_données','style'),
    Output('condition1','style'),
    Output('submit','style'),
    Output('threshold','style'),

    Output('condition2','style'),
    Output('condition3','style'),
    Output('threshold2','style'),
    Output('threshold3','style'),
    Output('type_fusion','style'),
    Output('fichier_fusionner','style'),
    Output('saut_curve','children'),
    Output('col-rename','style'),
    Output('col-rename','options'),
    Output('submit-rename','style'),
    Output('text-rename','style'),
    Output('comp_colonne','options'),
    Output('comp_colonne','style'),
    Output('condition_colonne','style'),
    Output('solveur_colonne','options'),
    Output('solveur_colonne','style'),
    Output('equation_solveur','style'),
    Output('btn_solveur','style'),
    Output('info_numpy','style'),
    Output('ligne_comp','style'),
    Output('ligne_comp_cond','style'),
    Output('btn_ligne_seuil','style'),
    Output('saut_ligne_comp1','children'),
    Output('saut_ligne_comp2','children'),
    Output('saut_ligne_comp3','children'),
    Output('msg_filtrage_donnees','children'),
    Output('saut_comp','children'),
    Output('check_filtre','style'),

    Output('choix_scinder','style'),
    Output('choix_charniere','style'),
    Output('choix_charniere','options'),
    Output('exp_scission','style'),
 

    Output('validate-button','style'),


    Output('drp_pente','style'),
    Output('drp_pente','options'),
    Output('options_pente','style'),
    Output('btn_pente','style'),
    Output('msg_filtrage_donnees2','children'),
    Output('msg_filtrage_donnees3','children'),

    Output('choix_df_filtrage','style'),
    Output('info_filtre_1','children'), 
    Output('info_filtre_2','children'),
    Output('info_filtre_3','children'),
    Output('saut_filtre_1','children'),
    Output('info_filtre_4','children'), 
    Output('info_choix_df','children'),
    Output('type_mean','style'),

    Input('type_mean','value'),
    Input('y-axis','value'),
    Input('filtre', 'value'),
    Input('active-tab', 'data'),
    Input('exclure','value'),
    Input('choix_df','value'),
   
    State('threshold','value'),
    State('condition1','value'),
    State('filtrage_données','value'),
    State('columns','value'),
    Input('choix_scinder','value'),
    State('condition_colonne','value'),
    State('comp_colonne','value'),
    prevent_initial_call=True

    

)

def pages_fonctions(type_mean,y,value,tab,exclure,choix,threshold,condition1,col,columns,choix_scinder,condition_colonne,comp_colonne):
    if dt.global_df_brut is not None and tab=='options':
        
        pas=0
        df=choix_df(choix,dt.global_df_brut,dt.global_df_mean,dt.global_df_fusionnées,dt.global_meandf_fusionnées,dt.global_df_1,dt.global_df_2,dt.global_df_3,dt.global_df_4,dt.global_df_5,dt.global_meandf_1,dt.global_meandf_2,dt.global_meandf_3,dt.global_meandf_4,dt.global_meandf_5)
        filename=''
        style4={'display':'inline-block','width':'70%','margin':'auto','maring-left':'5px','backgroundColor': couleur_drpbackground, 'color': couleur_text,'borderRadius': '10px','vertical-align':'top','margin-right':'5px'}
        table={'border': '10px solid #fae5d3','width':'90%','margin-left':'8px','margin-left':'0px','position': 'absolute','top': '15%','zIndex': '100'}
           
        if  df is not None :
            if value is None:
                return None,{'display': 'none'},{'display': 'none'}, dash.no_update, {'display': 'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},f"Nom : {filename}",style4,table,{'display':'none'},None,None, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},None,{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},None,None,None,None,None,{'display': 'none'},{'display': 'none'},{'display': 'none'}, dash.no_update,{'display': 'none'},{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},None,None,{'display': 'none'},None,None,None,None,None,None,{'display':'none'}
            match value :
                case 'filtrage_df_données':
                    msg_comp=html.Div([html.Br(),html.Br(),html.Div('Filtrage par colonne')])
                    msg_cond_comp=html.Div([html.Br(),html.Br()])
                    msg_filt_seuil=html.Div([html.Br(),html.Br(),html.Div('Filtrage par valeur seuil',style={'vertical-align':'top','display':'block'})])
                    saut_comp=html.Div([html.Br(),html.Br(),html.Br()])
                    options=[{'label': i, 'value': i} for i in df.columns]#creation de l'option du dropdown en mettant les colonnes de celui ci comme options 

                    style={'fontSize': '15px','display': 'inline-block','width':'80%','vertical-align': 'top-right','margin':'auto','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px'}
                    opt_columns=[{'label': i, 'value': i} for i in df.columns]
                    style_filtrage_horaire_button={ 'display': 'inline-block', 'vertical-align': 'top', 'text-align': 'center','margin':'auto', 'borderRadius': '5px','backgroundColor':couleur_drpbackground, 'color': couleur_text,'border': '2px solid #4b5160'}
                    #unique_times = df['temps'].unique()
                    #return_option_filtrage_horaire=[{'label': str(time), 'value': time} for time in unique_times]
                    
                    show_df={'display': 'inline-block','width':'80%','margin':'auto','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px','margin-left':'0px'}
                    aff1={'margin-bottom': '100px','display': 'inline-block','width':'100%','vertical-align': 'top','margin':'auto','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px'}
                    return None,{'display': 'none'},{'display': 'none'}, dash.no_update, {'display': 'none'},{'display':'none'},opt_columns,aff1,{'display': 'inline-block','margin':'auto'},{'display':'none'},f"Nom du fichier : {filename}",style4,table,{'display':'none'},None,None,options,{'display': 'block','width':'80%','vertical-align': 'top','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px'},{'display': 'inline-block'},{'display': 'inline-block','backgroundColor':couleur_btnbackground, 'color': couleur_text,'border': '2px solid #4b5160'},{'margin-bottom': '100px','display': 'inline-block','width':'65%','vertical-align': 'top','margin':'auto'},{'display':'inline-block'},{'display':'inline-block'},{'margin-bottom': '100px','display': 'inline-block','width':'65%','vertical-align': 'top','margin':'auto'},{'margin-bottom': '100px','display': 'inline-block','width':'65%','vertical-align': 'top','margin':'auto'},{'display':'none'},{'display':'none'},None,{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},options,{'display': 'inline-block','width':'80%','vertical-align': 'top','margin-left':'0px','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px'},{'display':'inline-block'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display': 'none'},{'width':'100%','padding-left': '0px','heigh':'100px','padding-top': '0px','border': '2px solid #1e2130','display':'flex'},{'width':'100%','padding-left': '0px','heigh':'100px','padding-top': '0px','border': '2px solid #1e2130','display':'flex'},{'width':'100%','padding-left': '0px','heigh':'100px','padding-top': '0px','border': '2px solid #1e2130','display':'flex'},msg_comp,msg_cond_comp,None,msg_filt_seuil,saut_comp,{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'}, {'display': 'none'},'Filtrage par valeur seuil','Filtrage par colonne', show_df,'Séléction des points',html.Div([html.Br(),html.Br(),html.Div('Exclusion de colonne(s)')]),html.Div([html.Br(),html.Br(),html.Div('Filtrage horaire')]),html.Br(),html.Div([html.Br(),html.Br(),html.Div('Séléction des jours')]),'Veuillez choisir où vous allez stocker vos données.',{'display': 'none'}
               
                case 'moyenne':
                    opt_colonnes=[{'label': i, 'value': i} for i in df.columns]
                    #df.groupby('CRIT_AIR')['PARC_2024'].transform('mean')
                    return None,{'display': 'none'},{'display': 'inline-block','margin':'auto','backgroundColor':couleur_btnbackground, 'color': couleur_text,'border': '2px solid #4b5160'},opt_colonnes,{'display': 'inline-block','width':'80%','vertical-align': 'top','margin':'auto','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},f"Nom du fichier : {filename}",style4,table,{'display':'none'},None,None, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'} ,{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},None,{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},None,None,None,None,None,{'display': 'none'},{'display': 'none'},{'display': 'none'}, dash.no_update,{'display': 'none'},{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},None,None,{'display': 'none'},None,None,None,None,None,None,{'display': 'inline-block'}# Add ,{'display': 'none'}
                case 'rename':
                    style_rename={'fontSize': '15px','display': 'inline-block','width':'80%','vertical-align': 'top-right','margin':'auto','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px'}
                    style_rename_buton={ 'display': 'inline-block', 'vertical-align': 'top', 'text-align': 'center','margin':'auto', 'borderRadius': '5px','backgroundColor':couleur_btnbackground, 'color':couleur_text,'border': '2px solid #4b5160'}
                    opt_colonnes_rename=[{'label': i, 'value': i} for i in df.columns]
                    return None,{'display': 'none'},{'display': 'none'}, dash.no_update, {'display': 'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},f"Nom du fichier : {filename}",style4,table,{'display':'none'},None,None, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},None,style_rename,opt_colonnes_rename,style_rename_buton,{'display': 'inline-block','margin':'auto','width':'60%'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},None,None,None,None,None,{'display': 'none'},{'display': 'none'},{'display': 'none'}, dash.no_update,{'display': 'none'},{'display':'none'}, dash.no_update, dash.no_update,{'display':'none'},{'display':'none'},None,None,{'display': 'none'},None,None,None,None,None,None,{'display': 'none'}
                case 'scission':
                    if choix_scinder=='charniere':
                        opt_colonnes_scission=[{'label': i, 'value': i} for i in df.columns]
                        drop_scission={'margin-bottom': '100px','display': 'inline-block','width':'80%','vertical-align': 'top','margin':'auto','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px'}
                    else:
                        opt_colonnes_scission= dash.no_update
                        drop_scission={'display':'none'}
                    return None,{'display': 'none'},{'display': 'none'}, dash.no_update, {'display': 'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},f"Nom du fichier : {filename}",style4,table,{'display':'none'},None,None, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},None,{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},html.Br(),html.Br(),None,None,None,{'display':'inline-block'},{'margin-bottom': '100px','display': 'inline-block','width':'80%','vertical-align': 'top','margin':'auto','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px'},drop_scission ,opt_colonnes_scission,{'display': 'inline-block','margin':'auto','backgroundColor':couleur_btnbackground, 'color': couleur_text,'border': '2px solid #4b5160'},{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},None,None,{'display': 'none'},None,None,None,None,None,None,{'display': 'none'}
                            
                case 'fichier':
                    drop10={'margin-bottom': '100px','display': 'inline-block','width':'80%','vertical-align': 'top','margin':'auto','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px'}
                    style12={ 'display': 'inline-block', 'vertical-align': 'top', 'text-align': 'center','margin':'auto', 'borderRadius': '5px','backgroundColor':couleur_btnbackground, 'color': couleur_text,'border': '2px solid #4b5160'}
                    return None,{'display': 'none'},{'display': 'none'}, dash.no_update, {'display': 'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},style12,f"Nom du fichier : {filename}",style4,table,{'display':'none'},None,None, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},None,{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},None,None,None,None,None,{'display': 'none'},{'display': 'none'},{'display': 'none'}, dash.no_update,{'display': 'none'},{'display':'none'}, dash.no_update, dash.no_update,{'display':'none'},{'display':'none'},None,None,{'display': 'none'},None,None,None,None,None,None,{'display': 'none'}
                case 'solveur':
                    opt_solveur=[{'label': i, 'value': i} for i in df.columns]
                    dropsolv={'overflowY':'visible','margin-bottom': '100px','display': 'inline-block','width':'80%','vertical-align': 'top','margin':'auto','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px'}
                    style_formule={'fontSize': '15px','display': 'inline-block','width':'80%','vertical-align': 'top-right','margin':'auto','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px'}
                    style_formule_buton={ 'display': 'inline-block', 'vertical-align': 'top', 'text-align': 'center','margin':'auto', 'borderRadius': '5px','backgroundColor':couleur_btnbackground, 'color': couleur_text,'border': '2px solid #4b5160'}
                    
                    return None,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},f"Nom du fichier : {filename}",style4,table,{'display': 'none'},None,None, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},None,{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},opt_solveur,dropsolv,style_formule,style_formule_buton,{'display':'inline-block'},{'display': 'none'},{'display': 'none'},{'display': 'none'},None,None,None,None,None,{'display': 'none'},{'display': 'none'},{'display': 'none'}, dash.no_update,{'display': 'none'},{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},None,None,{'display': 'none'},None,None,None,None,None,None,{'display': 'none'}
                case 'calcul_pente':
                    opt_colonnes_pente=[{'label': i, 'value': i} for i in df.columns]
                    style_pente_button={ 'display': 'inline-block', 'vertical-align': 'top', 'text-align': 'center','margin':'auto', 'borderRadius': '5px','backgroundColor':couleur_btnbackground, 'color': couleur_text,'border': '2px solid #4b5160'}
                    drop_pente={'margin-bottom': '100px','display': 'inline-block','width':'80%','vertical-align': 'top','margin':'auto','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px'}
                    return None,{'display': 'none'},{'display': 'none'}, dash.no_update, {'display': 'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},f"Nom du fichier : {filename}",style4,table,{'display':'none'},None,None, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},None,{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},None,None,None,None,None,{'display': 'none'},{'display': 'none'},{'display': 'none'}, dash.no_update,{'display': 'none'},{'display':'none'},drop_pente,opt_colonnes_pente,{'display':'inline-block'},style_pente_button,None,None,{'display': 'none'},None,None,None,None,None,None,{'display': 'none'}
                case 'prof':
                    #Il y 0 elements qui sont liées a prof donc a voir
                    return None,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},f"Nom du fichier : {filename}",style4,table,{'display': 'none'},None,None, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},None,{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},None,None,None,None,None,{'display': 'none'},{'display': 'none'},{'display': 'none'}, dash.no_update,{'display': 'none'},{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},None,None,{'display': 'none'},None,None,None,None,None,None,{'display': 'none'}
                case 'fusion_fichier':
                    return None,{'display': 'none'},{'display': 'none'}, dash.no_update, {'display': 'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},f"Nom du fichier : {filename}",style4,table,{'display':'none'},None,None, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'inline-block'},{'display':'inline-block'},None,{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},None,None,None,None,None,{'display': 'none'},{'display': 'none'},{'display': 'none'}, dash.no_update,{'display': 'none'},{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},None,None,{'display': 'none'},None,None,None,None,None,None,{'display': 'none'}
    else:
        return None,{'display': 'none'},{'display': 'none'}, dash.no_update, {'display': 'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},None,None, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},None,{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},{'display': 'none'},None,None,None,None,None,{'display': 'none'},{'display': 'none'},{'display': 'none'}, dash.no_update,{'display': 'none'},{'display':'none'},{'display':'none'}, dash.no_update,{'display':'none'},{'display':'none'},None,None,{'display': 'none'},None,None,None,None,None,None,{'display': 'none'}

#endregion   

#region Fonction renommer les colonnes
@callback(
    Output('rename_col', 'data'), 
    Input('submit-rename','n_clicks'),
    State('col-rename','value'),
    State('text-rename','value'),
    State('choix_df','value'),
    prevent_initial_call=True
)
def rename_colonne(submit,colonne,new_nom,choix):
    ctx = dash.callback_context
    if not ctx.triggered:
        # Aucun bouton n'a été cliqué.
        button_id = 'No clicks yet'
    else:
        # Obtenez l'id du bouton qui a été cliqué.
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id =='submit-rename' and new_nom is not None:

        df=choix_df(choix,dt.global_df_brut,dt.global_df_mean,dt.global_df_fusionnées,dt.global_meandf_fusionnées,dt.global_df_1,dt.global_df_2,dt.global_df_3,dt.global_df_4,dt.global_df_5,dt.global_meandf_1,dt.global_meandf_2,dt.global_meandf_3,dt.global_meandf_4,dt.global_meandf_5)
        if df is not None :
            df.rename(columns={colonne: new_nom}, inplace=True)
            affectation_df(choix,df,dt.global_df_brut,dt.global_df_mean,dt.global_df_fusionnées,dt.global_meandf_fusionnées,dt.global_meandf_1,dt.global_meandf_2,dt.global_meandf_3,dt.global_meandf_4,dt.global_meandf_5, dt.global_df_1, dt.global_df_2, dt.global_df_3, dt.global_df_4, dt.global_df_5)
    else:
        return dash.no_update
    

#region Fonction fusion des fichiers
@callback(
    Output('fichier_fusion','data'),
    Input('fichier_fusionner','contents'),
    Input('fichier_fusionner','filename'),
    Input('filtre','value'),
    Input('type_fusion','value'),
    State('active-tab', 'data'),
    State('choix_df','value'),
    prevent_initial_call=True
    )
def fusion_fichiers(contents,name_fusion,filtre,type_fusion,tab,choix):
    global global_df_fusionnées
    if contents is not None:
        
        if tab=='options' and contents is not None and filtre=='fusion_fichier':
            newdfs=[]               
            df=choix_df(choix,dt.global_df_brut,dt.global_df_mean,dt.global_df_fusionnées,dt.global_meandf_fusionnées,dt.global_df_1,dt.global_df_2,dt.global_df_3,dt.global_df_4,dt.global_df_5,dt.global_meandf_1,dt.global_meandf_2,dt.global_meandf_3,dt.global_meandf_4,dt.global_meandf_5)
            if df is not None and contents is not None:
                if type_fusion=='f_lignes':
                        # Créez une liste de tuples (nom, contenu)
                        contents_with_names = list(zip(name_fusion, contents))
                        # Triez la liste par nom
                        contents_with_names.sort()
                        # Décompressez la liste triée
                        sorted_names, sorted_contents = zip(*contents_with_names)
                        for content, name in zip(sorted_contents, sorted_names):
                            newdf = parse_contents(content,name)
                            newdfs.append(newdf)
                        newdf1 = pd.concat(newdfs)
                        fusion_fichier_df= pd.concat([df, newdf1])
                        fusion_fichier_df['pas'] = fusion_fichier_df['temps'].diff().dt.total_seconds()
                        fusion_fichier_df['temps_secondes_cumulée'] = fusion_fichier_df['pas'].cumsum()
                        fusion_fichier_df['temps_heure_cumulée']=fusion_fichier_df['temps_secondes_cumulée']/3600
                        fusion_fichier_df['Date'] = pd.to_datetime(fusion_fichier_df['Date'],format='mixed')
                        # Convertir la colonne 'Heure' en datetime
                        fusion_fichier_df['Heure'] = pd.to_datetime(fusion_fichier_df['Heure'], format='%H:%M:%S', errors='coerce')
                        
                        # Créer la colonne 'temps_heure_24'
                        fusion_fichier_df['temps_heure_24'] = (fusion_fichier_df['Heure'].dt.hour) + (fusion_fichier_df['Heure'].dt.minute / (60)) + (fusion_fichier_df['Heure'].dt.second/(3600))
                        # Convertir la colonne 'Heure' en datetime.time
                        fusion_fichier_df['Heure'] = fusion_fichier_df['Heure'].dt.time 

                        
                        fusion_fichier_df.iloc[0, fusion_fichier_df.columns.get_loc('pas')] = 0
                        fusion_fichier_df.iloc[0, fusion_fichier_df.columns.get_loc('temps_secondes_cumulée')] = 0
                        fusion_fichier_df.iloc[0, fusion_fichier_df.columns.get_loc('temps_heure_cumulée')] = 0
                        fusion_fichier_df = pd.DataFrame(fusion_fichier_df)
                        global_df_fusionnées=fusion_fichier_df
                        print("\n\n\nValeur de global_df_fusionnées \n",global_df_fusionnées)
                        return True
                if type_fusion=='f_colonnes':
                        # Créez une liste de tuples (nom, contenu)
                        contents_with_names = list(zip(name_fusion, contents))
                        # Triez la liste par nom
                        contents_with_names.sort()
                        # Décompressez la liste triée
                        sorted_names, sorted_contents = zip(*contents_with_names)
                        for i, (content, name) in enumerate(zip(sorted_contents, sorted_names)):
                            newdf = parse_contents(content,name)
                            if (('Date' not in newdf.columns) or ('Heure' not in newdf.columns)):
                                newdf['Heure']=newdf['temps'].dt.strftime('%H:%M:%S')
                                newdf['Date']=newdf['temps'].dt.date
                            newdf['pas'] = newdf['temps'].diff().dt.total_seconds()
                            newdf['temps_secondes_cumulée'] = newdf['pas'].cumsum()
                            newdf['temps_heure_cumulée']=newdf['temps_secondes_cumulée']/3600
                            newdf['Date'] = pd.to_datetime(newdf['Date'],format='mixed')
                            # Convertir la colonne 'Heure' en datetime
                            newdf['Heure'] = pd.to_datetime(newdf['Heure'], format='%H:%M:%S', errors='coerce')
                            
                            # Créer la colonne 'temps_heure_24'
                            newdf['temps_heure_24'] = (newdf['Heure'].dt.hour) + (newdf['Heure'].dt.minute / (60)) + (newdf['Heure'].dt.second/(3600))
                            # Convertir la colonne 'Heure' en datetime.time
                            newdf['Heure'] = newdf['Heure'].dt.time 
                            newdf.iloc[0, newdf.columns.get_loc('pas')] = 0
                            newdf.iloc[0, newdf.columns.get_loc('temps_secondes_cumulée')] = 0
                            newdf.iloc[0, newdf.columns.get_loc('temps_heure_cumulée')] = 0
                            # Utilisez i+2 pour le nom du fichier 
                            newdf.columns = newdf.columns.map(lambda x: x if x == 'temps' else f"{x}_Fichier{i+2}")
                            newdfs.append(newdf)
                        # Concaténez tous les DataFrame le long des colonnes en un seul DataFrame
                        newdf1 = pd.concat(newdfs, axis=1)
                        df = df.reset_index(drop=True)
                        newdf1 = newdf1.reset_index(drop=True)

                        # Concaténez le DataFrame original avec le nouveau DataFrame
                        #fusion_fichier_df = pd.concat([df, newdf1],axis=1,join='outer')
                        fusion_fichier_df = pd.merge(newdf1, df, how='outer')
                        cols_fichier2 = [col for col in fusion_fichier_df.columns if col.endswith(('_Fichier2', '_Fichier3', '_Fichier4'))]

                        #print("\n\n\n\n\n\n\n\n\n\n nom de colonne avec suffixe ", cols_fichier2)

                        # Remplir les valeurs manquantes avant et après l'interpolation
                        fusion_fichier_df[cols_fichier2] = fusion_fichier_df[cols_fichier2].fillna(method='ffill').fillna(method='bfill')
                        fusion_fichier_df[cols_fichier2] = fusion_fichier_df[cols_fichier2].interpolate(method='linear')
                        global_df_fusionnées=fusion_fichier_df
                        return True
                    
        else:
            return dash.no_update
        
#region Fonction Filtrage des données
@callback(
        Output('filtrage_df_ok','data'),
        Output('saut_fcnt_filtrees_btn','children'),
        Input('filtre','value'),
        Input('active-tab', 'data'),
        Input('choix_df','value'),
        Input('submit','n_clicks'),
        State('choix_df_filtrage','value'),
        State('columns', 'value'),
        State('condition2', 'value'),
        State('condition3', 'value'),
        State('threshold2', 'value'),
        State('threshold3', 'value'),
        State('threshold', 'value'),  #
        State('condition1', 'value'),  #
        State('comp_colonne', 'value'),
        State('condition_colonne', 'value'),
        State('columns','value'),
        State('filtrage_temp_heure_debut','value'),
        State('filtrage_temp_heure_fin','value'),


)
def fcnt_Filtrage_des_Données(filtre,tab,choix,submit,choix_newdf, col, condition2, condition3, threshold2, threshold3, threshold1, condition1, comp_colonne, condition_colonne,columns,temps_debut,temps_fin):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    msg=None
    if (button_id=='submit' and choix_newdf is not None):
        df=choix_df(choix,dt.global_df_brut,dt.global_df_mean,dt.global_df_fusionnées,dt.global_meandf_fusionnées,dt.global_df_1,dt.global_df_2,dt.global_df_3,dt.global_df_4,dt.global_df_5,dt.global_meandf_1,dt.global_meandf_2,dt.global_meandf_3,dt.global_meandf_4,dt.global_meandf_5)
        if (col is not None and (condition2 or condition3 or threshold2 or threshold3 or threshold1 or condition1)) or (comp_colonne is not None and condition_colonne is not None):
            df=apply_filters(df, col, [condition1, condition2, condition3], [threshold1, threshold2, threshold3], condition_colonne, comp_colonne)
        
        if columns is not None :
            df=df.drop(columns, axis=1)
        
        if choix_newdf=='choix_df1':
            print("\n\n\n\n\n\n\n  elif choix_newdf=='choix_df1': \n\n\n\n\n")
            dt.global_df_1=df 
            msg='Vous pouvez retrouvez vos données filtrées dans le jeux de données suivant : Données Filtrées 1 '
        elif choix_newdf=='choix_df2':
            dt.global_df_2=df
            msg='Vous pouvez retrouvez vos données filtrées dans le jeux de données suivant : Données Filtrées 2 '
        elif choix_newdf=='choix_df3':
            dt.global_df_3=df
            msg='Vous pouvez retrouvez vos données filtrées dans le jeux de données suivant : Données Filtrées 3 '
        elif choix_newdf=='choix_df4':
            dt.global_df_4=df
            msg='Vous pouvez retrouvez vos données filtrées dans le jeux de données suivant : Données Filtrées 4 '
        elif choix_newdf=='choix_df5':
            dt.global_df_5=df
            msg='Vous pouvez retrouvez vos données filtrées dans le jeux de données suivant : Données Filtrées 5 '
        if msg is not None:
            print("\n\n\n\n\n\n\n  elif msg is not None: \n\n\n\n\n")

            return True,msg
    else:
        return False, None
    
@callback(
    Output('threshold','type'),
    Output('threshold2','type'),
    Output('threshold3','type'),
    Input('threshold','type'),
    Input('threshold2','type'),
    Input('threshold3','type'),
    prevent_initial_call=True 
    )
def changement_type_dccinput(threshold,threshold2,threshold3):
    if threshold.isdigit():
        return 'number',dash.no_update,dash.no_update
    else:
        return 'text',dash.no_update,dash.no_update
    
    if threshold2.isdigit():
        return dash.no_update,'number',dash.no_update
    else:
        return dash.no_update,'text',dash.no_update
    
    if threshold3.isdigit():
        return dash.no_update,dash.no_update,'number'
    else:
        return dash.no_update,dash.no_update,'text'
#endregion
#region Fonction Solveur
@callback(
    Output('column_mapping_text', 'children'),
    Input('filtre', 'value'),
    Input('btn_solveur', 'n_clicks'),
    State('equation_solveur', 'value'),
    Input('solveur_colonne', 'value'),
    State('choix_df', 'value'),

    prevent_initial_call=True
)
def solveur(filtre, submit, equation, colonne_solveur, choix):
    if filtre != 'solveur':
        return dash.no_update

    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if colonne_solveur is not None:
        column_map = {chr(65 + i): col for i, col in enumerate(colonne_solveur)}
        column_mapping_text = html.Div([
            html.P("Correspondances des colonnes :"),
            html.Ul([html.Li(f"{var} = {col}") for var, col in column_map.items()])
        ]) 

    if (button_id == 'btn_solveur') and (colonne_solveur and equation):
        
        df=choix_df(choix,dt.global_df_brut,dt.global_df_mean,dt.global_df_fusionnées,dt.global_meandf_fusionnées,dt.global_df_1,dt.global_df_2,dt.global_df_3,dt.global_df_4,dt.global_df_5,dt.global_meandf_1,dt.global_meandf_2,dt.global_meandf_3,dt.global_meandf_4,dt.global_meandf_5)
        if df is not None:
            if '=' in equation:
                result_column_name, equation = equation.split('=')
                result_column_name = result_column_name.strip()
            else:
                result_column_name = 'Result'

            for var, col in column_map.items():
                equation = equation.replace(var, f'`{col}`')

            # Remplacer les fonctions pandas par leurs résultats
            if 'max' in equation:
                col_name = equation.split('(')[1].split(')')[0].strip('`')
                max_value = df[col_name].max()
                equation = equation.replace(f'max(`{col_name}`)', str(max_value))
            if 'min' in equation:
                col_name = equation.split('(')[1].split(')')[0].strip('`')
                min_value = df[col_name].min()
                equation = equation.replace(f'min(`{col_name}`)', str(min_value))
            if 'mean' in equation:
                col_name = equation.split('(')[1].split(')')[0].strip('`')
                mean_value = df[col_name].mean()
                equation = equation.replace(f'mean(`{col_name}`)', str(mean_value))
            if 'cumsum' in equation:
                col_name = equation.split('(')[1].split(')')[0].strip('`')
                df[result_column_name] = df[col_name].cumsum()
            else:
                local_dict = {'np': np}
                df[result_column_name] = df.eval(equation, engine='python', local_dict=local_dict)

            affectation_df(choix,df,dt.global_df_brut,dt.global_df_mean,dt.global_df_fusionnées,dt.global_meandf_fusionnées,dt.global_meandf_1,dt.global_meandf_2,dt.global_meandf_3,dt.global_meandf_4,dt.global_meandf_5, dt.global_df_1, dt.global_df_2, dt.global_df_3, dt.global_df_4, dt.global_df_5)
    else:
        if colonne_solveur is None:
            column_mapping_text=None
        return column_mapping_text
    
#endregion

#region Fonction scission des fichiers
@callback ( 
    Output('download_F1_scission','data'),
    Output('download_F2_scission','data'),
    Input('check_filtre','value'),
    Input('choix_scinder','value'),
    Input('choix_charniere','value'),
    Input('exp_scission','n_clicks'),

    State('choix_df','value'),
    State('columns','value'),
    State('upload-data','filename'),
    State('condition2','value'),
    State('condition3','value'),
    State('threshold2','value'),
    State('threshold3','value'),
    State('threshold', 'value'),#
    State('condition1', 'value'),#
    State('comp_colonne','value'),
    State('condition_colonne','value'),
    State('avec_condition','value'),
    State('submit', 'n_clicks'),
    State('filtrage_données','value'),
    prevent_initial_call=True

)
def scission(filtre,choix_scinder,choix_charniere,btn_export,choix,columns,filename,condition2,condition3,threshold2,threshold3,threshold1,condition1,comp_colonne,condition_colonne,condition_filtre,submit,col):
    ctx = dash.callback_context
    if not ctx.triggered:
        # Aucun bouton n'a été cliqué.
        button_id = 'No clicks yet'
    else:
        # Obtenez l'id du bouton qui a été cliqué.
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if (button_id=='exp_scission') and (choix_scinder is not None):
       
        df=choix_df(choix,dt.global_df_brut,dt.global_df_mean,dt.global_df_fusionnées,dt.global_meandf_fusionnées,dt.global_df_1,dt.global_df_2,dt.global_df_3,dt.global_df_4,dt.global_df_5,dt.global_meandf_1,dt.global_meandf_2,dt.global_meandf_3,dt.global_meandf_4,dt.global_meandf_5)
   
        if df is not None:
            if filtre=='sans_filtrage':
                df2=df.copy()
            else:
                df2=df.copy()
                if submit is not None:
                    if col is not None: 
                            for i, col_name in enumerate(col):
                                    if col_name is not None:
                                        condition = locals()[f'condition{i+1}']
                                        threshold = locals()[f'threshold{i+1}']
                                        
                                        # Vérifiez si la valeur est numérique
                                        if threshold.replace('.', '', 1).isdigit():
                                            # Convertissez la valeur en float si elle est numérique
                                            threshold = float(threshold)
                                        
                                        if condition == 'gt' and threshold is not None:
                                            df2 = df2[df2[col_name] < threshold] 
                                        elif condition == 'eq' and threshold is not None:
                                            df2 = df2[df2[col_name] != threshold]
                                        elif condition == 'lt' and threshold is not None:
                                            df2 = df2[df2[col_name] > threshold]
                                       
                                        if condition == 'gt' and threshold is not None:
                                            df = df[df2[col_name] > threshold]
                                        elif condition == 'eq' and threshold is not None:
                                            df = df[df2[col_name] == threshold]
                                        elif condition == 'lt' and threshold is not None:
                                            df = df[df2[col_name] < threshold]
                    if condition_colonne=='gt':
                        df2=df2[df2[comp_colonne[0]]<df2[comp_colonne[1]]]
                    elif condition_colonne == 'eq' :
                        df2 = df2[df2[comp_colonne[0]]!=df2[comp_colonne[1]]]
                    elif condition_colonne == 'lt' :
                        df2 = df2[df2[comp_colonne[0]]>df2[comp_colonne[1]] ]
                    
                    if condition_colonne=='gt':
                        df=df[df[comp_colonne[0]]>df[comp_colonne[1]]]
                    elif condition_colonne == 'eq' :
                        df = df[df[comp_colonne[0]]==df[comp_colonne[1]]]
                    elif condition_colonne == 'lt' :
                        df = df[df[comp_colonne[0]]<df[comp_colonne[1]] ]
            if choix_scinder=='col_exclus':
                df3=df2[columns]
                df3['temps']=df2['temps']
                df=df.drop(columns, axis=1)
            else:
                df = df2.loc[:, :choix_charniere].iloc[:, :-1]
                df3 = df2.loc[:, choix_charniere:]
                if 'temps' not in df3.columns:
                    df3['temps']=df2['temps']
            if df3 is not None:
                return dcc.send_data_frame(df.to_csv, "F1_scinder_"+filename, sep=';',index=False),dcc.send_data_frame(df3.to_csv, "F2_scinder_"+filename, sep=';',index=False),
#endregion
#region Fonction Calcul de moyenne
@callback(
    Output('calcul_mean', 'data'),#
    Input('type_mean','value'),
    Input('filtre','value'),
    Input('choix_df','value'),
    Input('submit-button', 'n_clicks'),

    State('colonnes', 'value'), 
    State('rolling_window', 'value'), 
   
    prevent_initial_call=True

)
def df_mean(type_mean,filtre,choix,n_clicks,colonnes,window):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if button_id=='submit-button' and filtre=='moyenne':        
        if (dt.global_df_mean is None) or (dt.global_meandf_fusionnées is None ) or (dt.global_meandf_1 is None ) or (dt.global_meandf_2 is None ) or (dt.global_meandf_3 is None ) or (dt.global_meandf_4 is None ) or (dt.global_meandf_5 is None ): 
            newdf=choix_df(choix,dt.global_df_brut,dt.global_df_mean,dt.global_df_fusionnées,dt.global_meandf_fusionnées,dt.global_df_1,dt.global_df_2,dt.global_df_3,dt.global_df_4,dt.global_df_5,dt.global_meandf_1,dt.global_meandf_2,dt.global_meandf_3,dt.global_meandf_4,dt.global_meandf_5)
        if dt.global_df_mean is not None and choix =='DF_Brut':
            newdf=dt.global_df_mean          

        if (dt.global_meandf_fusionnées is not None) and (choix=='df_fusionnées'):
            newdf=dt.global_meandf_fusionnées
       
        if dt.global_meandf_1 is not None and (choix=='df_1'):
            newdf=dt.global_meandf_1
        if dt.global_meandf_2 is not None and (choix=='df_2'):
            newdf=dt.global_meandf_2
        if dt.global_meandf_3 is not None and (choix=='df_3'):
            newdf=dt.global_meandf_3
        if dt.global_meandf_4 is not None and (choix=='df_4'):
            newdf=dt.global_meandf_4
        if dt.global_meandf_5 is not None and (choix=='df_5'):
            newdf=dt.global_meandf_5

        if newdf is not None: 
            if type_mean=='mean_cum':
                for col in colonnes:
                    newdf[col + '.mean_cum'] = newdf[col].expanding().mean()
                match choix:
                    case 'df_brutes' | 'df_mean':
                        print("\n\n\n\n\n\n\n\n\n\n\n\n match choix: case 'DF_Brut' | 'df_mean':\n\n\n\n\n\n")
                        dt.global_df_mean = newdf
                        print("\n\n\n\n\n\n\n\n\n\n\n\n match choix: case 'DF_Brut' | 'df_mean':\n\n\n\n\n\n",dt.global_df_mean.head())
                    case 'meandf_fusionnées' | 'df_fusionnées':
                        dt.global_meandf_fusionnées = newdf
                    case 'meandf_filtrees' | 'df_filtrees':
                        dt.global_meandf_filtrees = newdf
                    case 'meandf_filtrees' | 'df_1':
                        dt.global_meandf_1 = newdf
                    case 'meandf_filtrees' | 'df_2':
                        dt.global_meandf_2 = newdf
                    case 'meandf_filtrees' | 'df_3':
                        dt.global_meandf_3 = newdf
                    case 'meandf_4' | 'df_4':
                        dt.global_meandf_4 = newdf
                    case 'meandf_5' | 'df_5':
                        dt.global_meandf_5 = newdf
                return True
               
    else:
        return False

#endregion

#region Fonction Profondeur
@callback(
    Output('choixreference','options'),  
    Output('choixreference','style'),  
    Output('selected_color','data'),
    Output('submit-color','style'),
    Output('my-color-picker-1','style'),
    Output('clear-color','style'),
    Output('saut8','children',allow_duplicate=True),

    Output('color-palette', 'children'),
    Output('palette_defaut','style'),
    Output('palette_defaut','value'),

    State('palette_defaut','value'),
    Input('clear-color','n_clicks'),
    Input('filtre','value'),
    Input('active-tab', 'data'),
    Input('choix_df','value'),
    Input('profond','value'), 
    State('my-color-picker-1','value'),
    Input('submit-color','n_clicks'),
    prevent_initial_call=True
    )   
def reference(palette_defaut,clear,filtre,tab,choix,value,color,button):
    global color_selec
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if filtre=='prof':
        df=choix_df(choix,dt.global_df_brut,dt.global_df_mean,dt.global_df_fusionnées,dt.global_meandf_fusionnées,dt.global_df_1,dt.global_df_2,dt.global_df_3,dt.global_df_4,dt.global_df_5,dt.global_meandf_1,dt.global_meandf_2,dt.global_meandf_3,dt.global_meandf_4,dt.global_meandf_5)

        option=[{'label': i, 'value': i} for i in df.columns]
        if color is not None:
            if button_id == 'submit-color':
               color_selec.append(color)
        
        if palette_defaut is not None:
           if palette_defaut == 'temperature':
                color_selec = [{'hex': '#3138e7', 'rgb': {'r': 49, 'g': 56, 'b': 231, 'a': 1}}, {'hex': '#e9280b', 'rgb': {'r': 233, 'g': 40, 'b': 11, 'a': 1}}]  # bleu, rouge
           elif palette_defaut == 'temps':
                color_selec = [{'hex': '#0b0808', 'rgb': {'r': 11, 'g': 8, 'b': 8, 'a': 1}}, {'hex': '#3138e7', 'rgb': {'r': 49, 'g': 56, 'b': 231, 'a': 1}}, {'hex': '#fa8342', 'rgb': {'r': 250, 'g': 131, 'b': 66, 'a': 1}}, {'hex': '#e9280b', 'rgb': {'r': 233, 'g': 40, 'b': 11, 'a': 1}}, {'hex': '#0b0808', 'rgb': {'r': 11, 'g': 8, 'b': 8, 'a': 1}}]  # noir, bleu, orange, rouge, noir
           elif palette_defaut == 'autre':
                color_selec = [{'hex': '#636261', 'rgb': {'r': 99, 'g': 98, 'b': 97, 'a': 1}}, {'hex': '#0b0808', 'rgb': {'r': 11, 'g': 8, 'b': 8, 'a': 1}}]  # gris, fnoir
        if button_id == 'clear-color':
            if color_selec is not None:
                color_selec.pop()
            if palette_defaut is not None :
                return  dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,None
    else:
        return dash.no_update,{'display': 'none'},dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},None,None,{'display':'none'},dash.no_update
    
    if tab=='options' and color_selec is not None and df is not None:
        color_palette = html.Div([
            html.Div(style={'background-color': c['hex'], 'height': '50px', 'width': '50px', 'border': '1px solid white'}) for c in color_selec
            ], style={'display': 'flex'})

        return option, {'margin-bottom': '100px','display': 'inline-block','width':'80%','vertical-align': 'top','margin':'auto','backgroundColor': couleur_drpbackground, 'color': couleur_text,'border':'none','borderRadius': '10px'},color_selec,{'display':'inline-block','backgroundColor':couleur_btnbackground,'color': couleur_text,'border': '2px solid #4b5160','height': '30px', 'width': '130px', 'borderRadius': '5px'},{'display':'inline-block'},{'display':'inline-block','backgroundColor':couleur_btnbackground,'color': couleur_text,'border': '2px solid #4b5160','height': '30px', 'width': '130px', 'borderRadius': '5px'},html.Br(),color_palette,{'display':'inline-block'},dash.no_update
    elif (tab!='options'):
        return dash.no_update,{'display': 'none'},dash.no_update,{'display':'none'},{'display':'none'},{'display':'none'},None,None,{'display':'none'},dash.no_update

#endregion
#region Fonction Calcul de pente
@callback(
    Output('ok_pente','children'),
    Input('filtre','value'),
    Input('drp_pente', 'value'),
    Input('options_pente', 'value'),
    Input('btn_pente','n_clicks'),
    State('choix_df','value'),
    prevent_initial_call=True

)
def apply_pente_variation(filtre,selected_column, options, btn, choix):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if filtre !='calcul_pente':
        return None

    if button_id == 'btn_pente':
        if selected_column is not None:
           
            df=choix_df(choix,dt.global_df_brut,dt.global_df_mean,dt.global_df_fusionnées,dt.global_meandf_fusionnées,dt.global_df_1,dt.global_df_2,dt.global_df_3,dt.global_df_4,dt.global_df_5,dt.global_meandf_1,dt.global_meandf_2,dt.global_meandf_3,dt.global_meandf_4,dt.global_meandf_5)

            x_vals = df['temps_heure_24'].values  
            y_vals = df[selected_column].values

            if len(y_vals) > 1 and len(x_vals) > 1:
                #Xn-Xn-1
                pente = [(y_vals[i+1] - y_vals[i]) for i in range(len(y_vals) - 1)]
                pente.append(pente[-1])  # Pour garder la même longueur

                if 'ABS' in options:
                    pente = np.abs(pente)
                if 'LIMIT' in options:
                    max_pente = max(pente)
                    if max_pente != 0:
                        pente = [p / max_pente for p in pente]


                df[selected_column + '_Pente'] = pente
                affectation_df(choix,df,dt.global_df_brut,dt.global_df_mean,dt.global_df_fusionnées,dt.global_meandf_fusionnées,dt.global_meandf_1,dt.global_meandf_2,dt.global_meandf_3,dt.global_meandf_4,dt.global_meandf_5,dt.global_df_1,dt.global_df_2,dt.global_df_3,dt.global_df_4,dt.global_df_5)  
            else:    
                return None
    else:
        return None

#endregion