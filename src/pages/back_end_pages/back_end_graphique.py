from dash import Input, Output, State, callback, ctx
import dash
from dash import dcc, html, no_update
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.optimize import curve_fit
from scipy.special import factorial
import base64
import utils.Fonctions as Fonctions
from utils.Fonctions import choix_df
from utils.data_traitment import *

# Dictionnaire des fonctions
fitting_functions = {
    'Linear': Fonctions.linear,
    'Cauchy': Fonctions.cauchy,
    'Cubic': Fonctions.cubic,
    'Damped Function': Fonctions.damped,
    'Damped Oscillator': Fonctions.damped_oscillator,
    'Exponential': Fonctions.exponential,
    'Gaussian': Fonctions.gaussian,
    'Inverse': Fonctions.inverse,
    'Logistic': Fonctions.logistic,
    'Lorentzian': Fonctions.lorentzian,
    'Natural Log': Fonctions.natural_log,
    'Oscillator': Fonctions.oscillator,
    'Poisson': Fonctions.poisson,
    'Power Law': Fonctions.power_law,
    'Power Law with Offsets': Fonctions.power_law_offset,
    'Quadratic': Fonctions.quadratic,
    'Quartic': Fonctions.Quartic,
    'Stokes Law': Fonctions.stokes_law,
    'Two Slit Interference': Fonctions.two_slit_interference,
    'Courbe moyennée 24h': Fonctions.smooth_y_values,
}
#region DROPDWON AXES
@callback(
    Output('y-axis', 'style', allow_duplicate=True),
    Output('y2-axis', 'style', allow_duplicate=True),
    Input('y-axis', 'value'),
    Input('y2-axis', 'value'),
    prevent_initial_call=True
)
def taille_auto_axes(val_y, valy2):
    # Initialisation des styles par défaut
    style_y = {'overflowY': 'visible', 'heigh': '70px', 'vertical-align': 'center', 'display': 'inline-block', 'width': '90%', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}
    style_y2 = {'overflowY': 'visible', 'heigh': '70px', 'vertical-align': 'right', 'display': 'inline-block', 'width': '90%', 'backgroundColor': '#eeeeee', 'color': 'black', 'border': 'none', 'borderRadius': '10px'}

    # Logique pour y-axis
    if val_y is not None and len(val_y) >= 4:
        style_y['heigh'] = 'auto'
        style_y['width'] = 'auto'

    # Logique pour y2-axis
    if valy2 is not None and len(valy2) >= 4:
        style_y2['heigh'] = 'auto'
        style_y2['width'] = 'auto'

    return style_y, style_y2

#App.callback qui gere l'affectation des valeurs par defaut des axes y et y secondaire 
@callback(
     Output('y-axis','value',allow_duplicate=True),#Il faut mettre allow_duplicate=True pour pouvoir avoir plusieurs output avec des memes variables 
     Output('y2-axis','value',allow_duplicate=True),
     Output('x-axis','options',allow_duplicate=True),
     Output('x-axis', 'value',allow_duplicate=True),
     Input('active-tab', 'data'),
     Input('choix_df','value'),
     Input('filtre','value'),
     Input('Regression', 'value'),
     Input('fusion','value'),
     State('y-axis','value'),
     State('y2-axis','value'),
     State('x-axis','value'),
     prevent_initial_call=True
     
     )
def value_axe(tab,choix,filtre,regression,fusion,y_value,y2_value,x_axis):
    if tab=='graphique':

        df=choix_df(choix,global_df_brut,global_df_mean,global_meandf_repared,global_df_fusionnées,global_meandf_fusionnées,global_df_1,global_df_2,global_df_3,global_df_4,global_df_5,global_meandf_1,global_meandf_2,global_meandf_3,global_meandf_4,global_meandf_5)

        if len(df.columns)<4:
            #print('\n\n\n\n\n CEST PLUS PETIT')
            y_value=[df.columns[0],df.columns[1]]
            y2_value=[df.columns[1],df.columns[0]]
            x_value=df.columns[1]
            return y_value,y2_value,dash.no_update,x_value
    
        if df is not None and ((y_value and y2_value and x_axis) is None): #Si  la variable df n'est pas nul mais que y et y 2 sont nul alors on leur attribue des valeurs par defauts 
            #print('\n\n\n\n\n if df is not None and (((y_value and y2_value and x_axis) is None) and ')

            #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n MAUVAIS IF POUR LES VALUES \n\n\n\n\n\n\n\n\n")   
            y_value=[df.columns[7],df.columns[8]]
            y2_value=[df.columns[6],df.columns[5]]
            x_value=[df.columns[1]]
            return y_value,y2_value,dash.no_update,x_value
           
       
        if regression=='Reg_avec' :
            #print("\n\n Pas probleme")
            
            x_axis_options=[{'label': i, 'value': i} for i in df.columns]
                        
            return y_value,y2_value,x_axis_options,dash.no_update
        else:
            x_axis_options=[{'label': i, 'value': i} for i in df.columns]
            return y_value,y2_value,x_axis_options,dash.no_update
            

    if tab!='graphique' :
            return dash.no_update,dash.no_update,dash.no_update,dash.no_update
    
@callback(
    Output('x-axis','options'),
    Output('x-axis','style'),
    Output('y-axis','options'),
    Output('y-axis','style'),
    Output('y2-axis','options'),
    Output('y2-axis','style'),
    Output('text_x_axis','children'),
    Output('text_y_axis','children'),
    Output('text_y2_axis','children'),
    Output('log_x','style'),
    Output('log_y','style'),
    Output('log_y2','style'),
    Output('all_selec','style'),
    Input('active-tab', 'data'),
    Input('choix_df','value'),#Recuperation du choix si DF_Brut ou DF_decaler
    
    
)
def choix_des_axes(tab,choix):
    if tab!='graphique':
        return dash.no_update,{'display': 'none'}, dash.no_update,{'display': 'none'}, dash.no_update,{'display': 'none'},None,None,None,{'display':'none'},{'display':'none'},{'display':'none'},{'display': 'none'}#,{'display': 'none'},{'display': 'none'}
    else :
        print(" \n\n\n\n\n Je suis dans graphique !!!! \n\n")
        if global_df_brut is not None:
            
            df=choix_df(choix,global_df_brut,global_df_mean,global_meandf_repared,global_df_fusionnées,global_meandf_fusionnées,global_df_1,global_df_2,global_df_3,global_df_4,global_df_5,global_meandf_1,global_meandf_2,global_meandf_3,global_meandf_4,global_meandf_5)
            
            style_button={ 'display': 'inline-block', 'vertical-align': 'right', 'text-align': 'center','margin-left':'3%', 'borderRadius': '5px','backgroundColor':'#eeeeee', 'color': 'black','border': '2px solid #4b5160'}

            x_axis_options=[{'label': i, 'value': i} for i in df.columns]
            x_axis_style={'heigh':'auto','vertical-align':'left','vertical-align':'left','display': 'inline-block', 'width': '90%','backgroundColor': '#eeeeee', 'color': 'black','border':'none','borderRadius': '10px'}
            #x_axis_value='temps'
            y_axis_style={'heigh':'70px','overflowY':'visible','vertical-align':'center','display': 'inline-block', 'width': '90%','backgroundColor': '#eeeeee', 'color': 'black','border':'none','borderRadius': '10px'}
            y_axis_options=[{'label': i, 'value': i} for i in df.columns]
            y2_axis_style={'heigh':'70px','overflowY':'visible','vertical-align':'right','display': 'inline-block', 'width': '90%','backgroundColor': '#eeeeee', 'color': 'black','border':'none','borderRadius': '10px'}
            print(" \n\n\n\n\n Je suis AVANT le if tab== graphique \n\n",tab)
            return x_axis_options,x_axis_style, y_axis_options,y_axis_style, y_axis_options,y2_axis_style,"Axe x","Axe de gauche","Axe de droite",{'display':'inline-block'},{'display':'inline-block'},{'display':'inline-block'},style_button#, f"{'Axe des x'}", f"{'Axe des y'}", f"{'Axes des y secondaire'}"
    
#endregion 

#Callback permettant d'afficher ou non les slider pour la clarter des points, de la taille des points et de la police.Mais aussi du graphique vierge
@callback(
 Output('graph','style'),
 Output('options_graph_largeur','children'),
 Output('options_graph_hauteur','children'),
 Output('unité_x','children'),
 Output('unité_y','children'),
 Output('unité_y2','children'),
 
 Output('x-axis-unit','style',allow_duplicate=True),
 Output('y-axis-unit','style',allow_duplicate=True),
 Output('y2-axis-unit','style',allow_duplicate=True),
 Output('width-input','style'),
 Output('height-input','style'),
 Output('affichage_slider_point','style'),
 
 Output('titre_graphique','style'),
 Output('texte_titre_graph','children'),
 
 Input('graph','style'),
 Input('x-axis','value'),
 Input('y-axis','value'),
 Input('type_graph','value'),#recuperation du choix de type de graphique
 Input('active-tab', 'data'),
 prevent_initial_call=True

 )

def slider(style,x,y,value,tab):
    if tab=='graphique' and global_df_brut is not None:
        opt_l=[
        html.Br(),
        html.Label('Largeur :'), ]
        opt_h=[html.Br(), html.Label('Hauteur :')]
        #graph_style={'margin-left':'100px'} 
        graph_style={'display':'inline-block','margin-left':'100px'} 
        text_graph=[html.Br(), 
        html.Label('Titre du graphique :'),]
        if value=='dot':
            axe= {'display':'inline-block','width':'70%'} #Dans ce if les slider s'afficheront car nuage de point a ete selectionner
        else:
            axe= {'display':'none'} #Dans ce if les slider s'afficheront car nuage de point a ete selectionner
        return graph_style,opt_l,opt_h,"Unité : ","Unité : ","Unité : ",{'display':'inline-block','margin-left':'5px'},{'display':'inline-block'},{'display':'inline-block'},{'display':'inline-block'},{'display':'inline-block'},axe,{'display':'inline-block'},text_graph
    if tab!='graphique' or ((x and y is None) or global_df_brut is None):
        graph_style={'display':'none'}
    return graph_style,None,None,None,None,None,{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'},None


@callback(
    Output('y-axis', 'value', allow_duplicate=True),
    Input('all_selec', 'n_clicks'),
    Input('y-axis', 'value'),
    Input('x-axis', 'value'),
    State('choix_df', 'value'),
    Input('fusion', 'value'),

    prevent_initial_call=True
)
def select_all_options(n_clicks, y_axis, x_axis, choix, fusion):
    ctx = dash.callback_context
    if not ctx.triggered:
        # Aucun bouton n'a été cliqué.
        button_id = 'No clicks yet'
    else:
        # Obtenez l'id du bouton qui a été cliqué.
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == 'all_selec':

        df=choix_df(choix,global_df_brut,global_df_mean,global_meandf_repared,global_df_fusionnées,global_meandf_fusionnées,global_df_1,global_df_2,global_df_3,global_df_4,global_df_5,global_meandf_1,global_meandf_2,global_meandf_3,global_meandf_4,global_meandf_5)
        if x_axis is not None:
            # Récupère toutes les valeurs des colonnes
            all_values = df.columns.tolist()

            # Filtre les valeurs déjà sélectionnées par l'autre dropdown
            dropdown1_values = y_axis or []
            dropdown1_selectable = [val for val in all_values if val not in x_axis]

            return dropdown1_selectable
    else:
        return dash.no_update

#Appcallback qui gere l'ajout des courbes au graphique 
@callback(
    Output('graph', 'figure'),
    Output('stock_curve_fitting','data'),
    Input('log_x','value'),
    Input('log_y','value'),
    Input('log_y2','value'),
    Input('type_bar','value'),
    Input('x-axis-unit', 'value'),
    Input('y-axis-unit', 'value'),
    Input('y2-axis-unit', 'value'),

    Input('width-input', 'value'),
    Input('height-input', 'value'),
    Input('active-tab', 'data'),
    Input('avec_condition','value'),
    Input('submit', 'n_clicks'),
    Input('choixreference','value'),
    Input('profond','value'),
    Input('exclure','value'),
    Input('columns','value'),
    Input('type_graph','value'),
    Input('points', 'value'),
    Input('choix_df', 'value'),
    Input('x-axis', 'value'),
    Input('y-axis', 'value'),
    Input('y2-axis', 'value'),
    Input('point-size-slider', 'value'),
    Input('point-opacity-slider', 'value'),
    Input('font-size-slider', 'value'),
    Input('Regression', 'value'),
    Input('fusion','value'),
    Input('type_curve_fitting','value'),
    State('graph', 'relayoutData'),
    State('threshold', 'value'),#
    State('condition1', 'value'),#
    Input('selected_color','data'),
    State('condition2','value'),

    State('condition3','value'),

    State('threshold2','value'),

    State('threshold3','value'),
    Input('titre_graphique','value'),
    State('threshold','type'),
    State('threshold2','type'),
    State('threshold3','type'),
    State('comp_colonne','value'),
    State('condition_colonne','value'),
    prevent_initial_call=True

)
def update_graph(log_x,log_y,log_y2,type_bar, x_unit, y_unit, y2_unit, width, height, tab, condition_filtre, submit, reference, profondeur, exclure, columns, graph, value, choix, x_axis, y_axis, y2_axis, point_size, point_opacity, font_size, regression, fusion, fitting_function, relayoutData, threshold1, condition1, selected_color, condition2, condition3, threshold2, threshold3, titre_graphique, type_threshold, type_threshold2, type_threshold3, comp_colonne, condition_colonne):
    if x_unit is None:
        x_unit = ''
    if y_unit is None:
        y_unit = ''
    if y2_unit is None:
        y2_unit = ''
    
    if tab != 'graphique':
        return no_update, no_update
    
    filtered_df = choix_df(choix,global_df_brut,global_df_mean,global_meandf_repared,global_df_fusionnées,global_meandf_fusionnées,global_df_1,global_df_2,global_df_3,global_df_4,global_df_5,global_meandf_1,global_meandf_2,global_meandf_3,global_meandf_4,global_meandf_5)

    #filtered_df = global_df_brut
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    #filtered_df=filtered_df.compute()  
    if graph == 'dot':
        if profondeur == 'Prof_avec':
            color_palette = [color['hex'] for color in selected_color]
            category_codes = filtered_df[reference].astype('category').cat.codes
            category_labels = filtered_df[reference].astype('category').cat.categories
            
            if filtered_df[reference].dtype == 'float64':
                tickvals = None
                ticktext = None
            else:
                tickvals = list(range(len(category_labels)))
                ticktext = category_labels
            
            discrete_colorscale = []
            if type_bar == 'degrade':
                type_col = color_palette
            else:
                for i, color in enumerate(color_palette):
                    discrete_colorscale.append([i / len(color_palette), color])
                    discrete_colorscale.append([(i + 1) / len(color_palette), color])
                type_col = discrete_colorscale
            
            fig.add_trace(
                go.Scatter(
                    x=filtered_df[x_axis],
                    y=filtered_df[y_axis[0]],
                    mode='markers',
                    name='Profondeur ' + y_axis[0],
                    marker=dict(
                        size=point_size,
                        color=category_codes,
                        colorscale=type_col,
                        opacity=point_opacity,
                        colorbar=dict(
                            title=reference,
                            titleside='right',
                            titlefont=dict(size=14, family='Arial, sans-serif'),
                            x=1.05,
                            xanchor='left',
                            y=0.7,
                            yanchor='top',
                            lenmode='fraction',
                            len=0.8,
                            thickness=20,
                            orientation='v',
                            tickvals=tickvals,
                            ticktext=ticktext
                        )
                    )
                )
            )
        
        for y in y_axis:
            visibility = 'legendonly' if y == y_axis[0] and profondeur == 'Prof_avec' else True
            fig.add_trace(
                go.Scatter(x=filtered_df[x_axis], y=filtered_df[y], name=y, mode='markers', marker=dict(size=point_size, opacity=point_opacity), visible=visibility),
                secondary_y=False,
            )
        
        for y2 in y2_axis:
            fig.add_trace(
                go.Scatter(x=filtered_df[x_axis], y=filtered_df[y2], name=y2, mode='markers', marker=dict(size=point_size, opacity=point_opacity)),
                secondary_y=True,
            )
    
    elif graph == 'line':
        for y in y_axis:
            fig.add_trace(
                go.Scatter(x=filtered_df[x_axis], y=filtered_df[y], name=y),
                secondary_y=False,
            )
        
        for y2 in y2_axis:
            fig.add_trace(
                go.Scatter(x=filtered_df[x_axis], y=filtered_df[y2], name=y2),
                secondary_y=True,
            )
    elif graph=='histo':
        for y in y_axis:
            fig.add_trace(
                go.Bar(x=filtered_df[x_axis], y=filtered_df[y], name=y),
                secondary_y=False,
            )

        # Ajout des histogrammes pour y2_axis
        for y2 in y2_axis:
            fig.add_trace(
                go.Bar(x=filtered_df[x_axis], y=filtered_df[y2], name=y2),
                secondary_y=True,
            )
    if regression == 'Reg_avec':
        x_data = filtered_df[x_axis]
        y_data = filtered_df[y_axis[0]]
        mask = ~np.isnan(x_data) & ~np.isnan(y_data)
        x_data = x_data[mask]
        y_data = y_data[mask]
        
        if fitting_function == 'Courbe moyennée 24h':
            x_fit, y_fit = Fonctions.smooth_y_values(filtered_df, x_axis, y_axis[0])
            fig.add_trace(
                go.Scatter(x=x_fit, y=y_fit, name=f'Regression {y_axis[0]}: ', mode='lines', line=dict(color='black', width=3)),
                secondary_y=False,
            )
            equation = None
            fitting_df = None
        else:
            popt, _ = curve_fit(fitting_functions[fitting_function], x_data, y_data)
            y_fit = fitting_functions[fitting_function](x_data, *popt)
            equation = Fonctions.choix_equation(fitting_function, *popt)
            fitting_df = pd.DataFrame({f"{fitting_function}_{y_axis[0]}": y_fit.tolist()})
            
            # Vérifiez l'existence de la colonne 'informations'
            if 'informations' not in fitting_df.columns:
                fitting_df['informations'] = None  # Crée la colonne si elle n'existe pas
            
            fitting_df.loc[0, 'informations'] = equation
            for i in range(len(popt)):
                fitting_df.loc[i + 1, 'informations'] = f'c{i+1}={popt[i]}'
            fitting_df.loc[len(popt) + 1, 'informations'] = f'r2={Fonctions.calculate_r_squared(x_data, y_data, fitting_functions[fitting_function], popt)}'
            if x_data is not ( 'Date' or 'Heure' or 'pas' or 'temps_secondes_cumulée' or 'temps_heure_cumulée' or 'temps_heure_24'):
                # Supposons que x_fit et y_fit sont deux listes de même longueur
                x_data, y_fit = zip(*sorted(zip(x_data, y_fit)))

            fig.add_trace(
                go.Scatter(x=x_data, y=y_fit, name=f'Regression {y_axis[0]}: ', mode='lines', line=dict(color='black', width=3)),
                secondary_y=False,
            )
        
        fig.add_annotation(
            x=0.05,
            y=1,
            xref="paper",
            yref="paper",
            text=equation,
            showarrow=False,
            font=dict(size=16, color="#000000"),
            bgcolor="#ffffff",
            bordercolor="#c7c7c7",
            borderwidth=2,
            borderpad=4,
            opacity=0.8
        )
    
    fig.layout.plot_bgcolor = '#FFFFFF'
    fig.layout.paper_bgcolor = '#FFFFFF'
    if 'log' in log_x:
        val_log_x = 'log'
    else:
        val_log_x = None

    if 'log' in log_y:
        val_log_y = 'log'
    else:
        val_log_y = None

    if 'log' in log_y2:
        val_log_y2 = 'log'
    else:
        val_log_y2 = None

    if graph == 'dot':
        fig.update_xaxes(type=val_log_x,title_text=f"{x_axis} [{x_unit}]", zerolinecolor='black', zeroline=True, showgrid=True, gridwidth=1, gridcolor='gray', title_font={'size': font_size})
        fig.update_yaxes(type=val_log_y,showgrid=True, gridwidth=1, zerolinecolor='black', zeroline=True, gridcolor='gray', title_text=f"[{y_unit}]", title_font={'size': font_size})
        fig.update_yaxes(type=val_log_y2,showgrid=True, gridwidth=1, zerolinecolor='black', zeroline=True, gridcolor='gray', title_text=f"[{y2_unit}]", title_font={'size': font_size}, secondary_y=True)
    else:
        fig.update_xaxes(type=val_log_x,title_text=f"{x_axis} [{x_unit}]", showgrid=True, zerolinecolor='black', gridwidth=1, gridcolor='gray')
        fig.update_yaxes(type=val_log_y,showgrid=True, gridwidth=1, zerolinecolor='black', zeroline=True, gridcolor='gray', title_text=f"[{y_unit}]")
        fig.update_yaxes(type=val_log_y2,showgrid=True, gridwidth=1, zerolinecolor='black', zeroline=True, gridcolor='gray', title_text=f"[{y2_unit}]", secondary_y=True)
    
    fig.update_layout(
        width=width,
        height=height,
        title=titre_graphique,
        title_x=0.5,
        title_y=0.95,
        title_font=dict(family='Arial, sans-serif', size=20, color='black')
    )
    
    if relayoutData:
        if 'xaxis.range[0]' in relayoutData and 'xaxis.range[1]' in relayoutData:
            fig['layout']['xaxis']['range'] = [relayoutData['xaxis.range[0]'], relayoutData['xaxis.range[1]']]
        if 'yaxis.range[0]' in relayoutData and 'yaxis.range[1]' in relayoutData:
            fig['layout']['yaxis']['range'] = [relayoutData['yaxis.range[0]'], relayoutData['yaxis.range[1]']]
        if 'yaxis2.range[0]' in relayoutData and 'yaxis2.range[1]' in relayoutData:
            fig['layout']['yaxis2']['range'] = [relayoutData['yaxis2.range[0]'], relayoutData['yaxis2.range[1]']]
    
    if regression == 'Reg_avec' and fitting_df is not None:
        fitting_df = fitting_df.astype(str)
        #fitting_df =fitting_df.compute()
        return fig, base64.b64encode(fitting_df.to_parquet()).decode()
        
    return fig, no_update


@callback(
    Output('Regression','style'),
    Output('profond','style'),
    Output('type_graph','style',allow_duplicate=True),
    Output('file-name', 'children'),
    Output('avec_condition','style'),
    
    Input('y-axis','value'),
    State('upload-data', 'filename'),
    prevent_initial_call=True
)
def filtre_graphique(y, filename):
    
    if global_df_brut is not None:
        if y == 'prof':
            return {'display': 'block'}, {'display': 'block'}, {'display': 'inline-block','margin':'top-right','margin-right':'10px'}, f"Nom du fichier : {filename}", {'display':'inline-block'}
        elif y == 'filtrage':
            return {'display': 'block'}, {'display': 'none'}, {'display': 'inline-block','margin':'top-right','margin-right':'10px'}, f"Nom du fichier : {filename}", {'display':'inline-block'}
        else:
            return {'display': 'block'}, {'display': 'none'}, {'display': 'inline-block','margin':'top-right','margin-right':'10px'}, f"Nom du fichier : {filename}", {'display':'inline-block'}
    
    return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update


#Callback gerant le stockage des unités et la taille du graphique
@callback(
 Output('store-units', 'data'),
 Output('x-axis-unit', 'value'),
 Output('y-axis-unit', 'value'),
 Output('y2-axis-unit', 'value'),
 Output('width-input', 'value'),
 Output('height-input', 'value'),
 Output('point-size-slide', 'value'),
 Output('point-opacity-slider', 'value'),
 Output('font-size-slider', 'value'),
 Input('point-size-slide', 'value'),
 Input('point-opacity-slider', 'value'),
 Input('font-size-slider', 'value'),
 Input('width-input', 'value'),
 Input('height-input', 'value'),
 Input('x-axis-unit', 'value'),
 Input('y-axis-unit', 'value'),
 Input('y2-axis-unit', 'value'),
 Input('active-tab', 'data'),
 State('store-units', 'data'),
 prevent_initial_call=True
)
def manage_units(taille_point, opac_point, taille_police, width_input, height_input, x_unit, y_unit, y2_unit, tab, units_data):
 # Mise à jour des unités et des tailles
    updated_units = {
    'x_unit': x_unit, 'y_unit': y_unit, 'y2_unit': y2_unit,
    'width_input': width_input, 'height_input': height_input,
    'taille_point': taille_point, 'opac_point': opac_point, 'taille_police': taille_police
    }

 # Si l'onglet n'est pas 'tab-2', retourner les valeurs stockées
    if tab != 'graphique' and units_data is not None:
        return updated_units, units_data.get('x_unit', ''), units_data.get('y_unit', ''), units_data.get('y2_unit', ''), units_data.get('width_input', ''), units_data.get('height_input', ''), units_data.get('taille_point', ''), units_data.get('opac_point', ''), units_data.get('taille_police', '')

 # Si l'onglet est 'tab-2' ou si les données sont None, ne faites aucune mise à jour
    return updated_units, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

# Fonctions d'ajustement
def linear(x, a, b):
    return a * x + b

def cauchy(x, A, B, C):
    return A + B / x**2 + C

def cubic(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

def damped(x, a, b, d):
    return a * np.exp(-b * x) + d

def damped_oscillator(x, A0, b, omega, delta, C):
    return A0 * np.exp(-b * x) * np.sin(omega * x + delta) + C

def exponential(x, a, b, c):
    return a * np.exp(b * x) + c

def gaussian(x, A0, x0, sigma, C):
    return A0 * np.exp(- (x - x0)**2 / (2 * sigma**2)) + C

def inverse(x, a, b):
    return a + b / x

def logistic(x, A, B, C):
    return A / (1 + np.exp(-B * (x - C)))

def lorentzian(x, A, omega0, beta, C):
    return (A * np.sqrt((omega0**2 - x**2)**2 + 4 * x**2 * beta**2)) + C

def natural_log(x, a, b):
    return a * np.log(x * b)

def oscillator(x, A0, k, delta, C):
    return A0 * np.sin(k * x + delta) + C

def poisson(x, a, mu):
    return a * np.exp(-mu) * (mu**x / factorial(x))

def power_law(x, a, b):
    return a * x**b

def power_law_offset(x, A, B, x0, C):
    return A * (x - x0)**B + C

def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

def Quartic (x,a,b,c,d,e):
    return a*x**4+b*x**3+c*x**2+d*x+e

def stokes_law(x, k0, a0, K1):
    return (k0 / (18 * a0)) * x**2 * (1 - 2.1 * x / K1)

def two_slit_interference(x, A, k1, k2, x0, C):
    return A * np.sinc(k1 * (x - x0) / np.pi)**2 * np.cos(k2 * (x - x0))**2 + C

def smooth_y_values(df, x_column, y_column, window_size=9):
    sorted_df = df.sort_values(by=x_column)
    smoothed_y = sorted_df[y_column].rolling(window=window_size, center=True).mean()
    return sorted_df[x_column], smoothed_y

# Ejemplo de función de cálculo del R²
def calculate_r_squared(x, y, func, popt):
    residuals = y - func(x, *popt)
    ss_res = sum(residuals**2)
    ss_tot = sum((y - y.mean())**2)
    return 1 - (ss_res / ss_tot)

# Dictionnaire des fonctions
fitting_functions = {
    'Linear': linear,
    'Cauchy': cauchy,
    'Cubic': cubic,
    'Damped Function': damped,
    'Damped Oscillator': damped_oscillator,
    'Exponential': exponential,
    'Gaussian': gaussian,
    'Inverse': inverse,
    'Logistic': logistic,
    'Lorentzian': lorentzian,
    'Natural Log': natural_log,
    'Oscillator': oscillator,
    'Two Slit Interference': two_slit_interference,
    'Courbe moyennée 24h': smooth_y_values,
}

def create_scatter_trace(x, y, name, mode='markers', secondary_y=False, **kwargs):
    """
    Crée une trace Scatter pour un graphique Plotly.
    """
    return go.Scatter(x=x, y=y, name=name, mode=mode, **kwargs), secondary_y

def add_regression_trace(fig, x_data, y_data, fitting_function, y_axis_name):
    """
    Ajoute une courbe de régression au graphique.
    """
    mask = ~np.isnan(x_data) & ~np.isnan(y_data)
    x_data = x_data[mask]
    y_data = y_data[mask]
    
    popt, _ = curve_fit(fitting_function, x_data, y_data)
    y_fit = fitting_function(x_data, *popt)
    
    equation = f"Regression {y_axis_name}: y = {popt[0]:.2f}x + {popt[1]:.2f}"
    fig.add_trace(go.Scatter(x=x_data, y=y_fit, name=equation, mode='lines', line=dict(color='black', width=3)))
    
    return equation

#Fonctions permettant de savoir quel equation afficher
def choix_equation(fitting_function, *popt):
    match fitting_function:
        case 'Linear':
            return "y = {:.2e}x + {:.2e}".format(*popt)
        case 'Cauchy':
            return "y = {:.2e}+{:.2e}/x^2 + {:.2e}/x^4".format(*popt)
        case 'Cubic':
            return "y = {:.2e} * x^3 + {:.2e} * x^2 + {:.2e} * x + {:.2e}".format(*popt)
        
        case 'Damped Function':
            return "y = {:.2e}e^(-{:.2e}x) + {:.2e}".format(*popt)
        
        case 'Damped Oscillator':
            return "y = {:.2e}e^(-{:.2e}x) * sin({:.2e} * x+{:.2e}) + {:.2e}".format(*popt)
        
        case 'Exponential':
            return "y = {:.2e}e^({:.2e}x)+{:.2e}".format(*popt)
        
        case 'Gaussian':
            return "y = {:.2e}e^(-(x - {:.2e})^2 / (2 * {:.2e}^2))+{:.2e}".format(*popt)
        
        case 'Inverse':
            return "y = {:.2e} / ({:.2e} + x )".format(*popt)
        
        case 'Logistic':
            return "y = {:.2e} / (1 + {:.2e}e^(-{:.2e}x))".format(*popt)
        
        case 'Lorentzian':
            A, omega0, beta, C = popt
            return "y = {:.2e} * sqrt((({:.2e}^2 - x^2)^2 + 4 * x^2 * {:.2e}^2)) + {:.2e}".format(A, omega0, beta, C)

        
        case 'Natural Log':
            return "y = {:.2e} * ln( x * {:.2e} )".format(*popt)
        
        case 'Oscillator':
            return "y = {:.2e} * sin(2π * {:.2e} * x + {:.2e})+{:.2e}".format(*popt)
        
        case 'Poisson':
            return "y = {:.2e} * e^(-{:.2e}) * ({:.2e})^x / x!".format(popt[0], popt[1], popt[1])
        
        case 'Power Law':
            return "y = {:.2e} * x^{:.2e}".format(*popt)
        
        case 'Power Law with Offsets':
            return "y = {:.2e} * (x - {:.2e})^{:.2e} + {:.2e}".format(*popt)
        
        case 'Quadratic':
            return "y = {:.2e}x^2 + {:.2e}x + {:.2e}".format(*popt)
        case'Quartic':
            return "y = {:.2e}x^4+{:.2e}x^3 +{:.2e}x^2 + {:.2e}x + {:.2e}".format(*popt)

        case 'Stokes Law':
            k0, a0, K1 = popt
            return "y = ({:.2e} / (18 * {:.2e})) * x^2 * (1 - 2.1 * x / {:.2e})".format(k0, a0, K1)

        
        case 'Two Slit Interference':
            val_x0 = popt[3]
            formatted_val_x0 = "{:.2e}".format(val_x0)
            return "y = {:.2e} * sinc^2({:.2e} * (x - {}) / π) * cos^2({:.2e} * (x - {:.2e})) + {:.2e}".format(popt[0], popt[1], formatted_val_x0, popt[2], val_x0, popt[4])
