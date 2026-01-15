from dash import Input, Output, callback, State
import dash
import utils.data_traitment as dt
from utils.Fonctions import choix_df
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
import pathlib

# Variable globale pour stocker le GeoJSON
_cached_geojson = None

# Chemin vers le fichier GeoJSON local
BASE_PATH = pathlib.Path(__file__).parent.parent.parent.parent.resolve()
GEOJSON_PATH = BASE_PATH.joinpath("data").joinpath("raw").joinpath("communes.json")

def get_france_geojson():
    """
    Charge le fichier GeoJSON des communes françaises depuis data/raw/communes.json
    """
    global _cached_geojson
    
    if _cached_geojson is not None:
        return _cached_geojson
    
    try:
        # Charger le fichier GeoJSON local
        with open(GEOJSON_PATH, 'r', encoding='utf-8') as f:
            _cached_geojson = json.load(f)
            print(f"GeoJSON chargé avec succès depuis {GEOJSON_PATH}")
            return _cached_geojson
    except FileNotFoundError:
        print(f"Erreur: Le fichier {GEOJSON_PATH} n'existe pas")
    except json.JSONDecodeError as e:
        print(f"Erreur de décodage JSON: {e}")
    except Exception as e:
        print(f"Erreur lors du chargement du GeoJSON: {e}")
    
    return None

def create_choropleth_map(df, color_column=None, groupby_func='sum'):
    """
    Crée une carte choroplèthe Plotly avec les données du DataFrame
    """
    if df is None or df.empty:
        # Retourner une figure vide
        fig = go.Figure()
        fig.update_layout(
            title="Aucune donnée disponible",
            height=700
        )
        return fig
    
    # Vérifier les colonnes nécessaires
    if 'COMMUNE_CODE' not in df.columns or 'COMMUNE_NOM' not in df.columns:
        fig = go.Figure()
        fig.update_layout(
            title="Les colonnes COMMUNE_CODE et COMMUNE_NOM sont requises",
            height=700
        )
        return fig
    
    # Préparer les données agrégées par commune
    if color_column and color_column in df.columns:
        # Grouper les données par commune
        agg_dict = {color_column: groupby_func}
        df_grouped = df.groupby(['COMMUNE_CODE', 'COMMUNE_NOM']).agg(agg_dict).reset_index()
        df_grouped.columns = ['COMMUNE_CODE', 'COMMUNE_NOM', 'Valeur']
    else:
        # Si pas de colonne, compter les lignes par commune
        df_grouped = df.groupby(['COMMUNE_CODE', 'COMMUNE_NOM']).size().reset_index(name='Valeur')
    
    # Récupérer le GeoJSON
    geojson = get_france_geojson()
    
    if geojson is None:
        fig = go.Figure()
        fig.update_layout(
            title="Impossible de charger les données géographiques",
            height=700
        )
        return fig
    
    # Créer la carte choroplèthe
    fig = px.choropleth_mapbox(
        df_grouped,
        geojson=geojson,
        locations='COMMUNE_CODE',
        featureidkey="properties.code",
        color='Valeur',
        color_continuous_scale="Viridis",
        mapbox_style="carto-positron",
        zoom=8,
        center={"lat": 48.6, "lon": 3.0},
        opacity=0.6,
        labels={'Valeur': color_column if color_column else 'Nombre'},
        hover_name='COMMUNE_NOM',
        hover_data={'COMMUNE_CODE': True, 'Valeur': ':.2f'}
    )
    
    fig.update_layout(
        margin={"r": 0, "t": 30, "l": 0, "b": 0},
        height=700,
        title={
            'text': f"Carte des communes - {color_column if color_column else 'Nombre par commune'}",
            'x': 0.5,
            'xanchor': 'center'
        }
    )
    
    return fig

# Callback pour gérer l'affichage de la page carte
@callback(
    Output('table-map', 'style'),
    Input('active-tab', 'data'),
    prevent_initial_call=True
)
def display_map_page(tab):
    """
    Affiche ou cache la table de la page carte selon l'onglet actif
    """
    if tab == 'maps':
        return {
            'border': '10px solid #fae5d3',
            'width': '90%',
            'margin-left': '8px',
            'position': 'absolute',
            'top': '15%',
            'zIndex': '100',
            'display': 'block'
        }
    else:
        return {'display': 'none'}

@callback(
    Output('map-color-column', 'options'),
    Input('choix_df', 'value'),
    prevent_initial_call=False
)
def update_map_columns(choix):
    """
    Met à jour les colonnes disponibles pour la carte
    """
    df = choix_df(
        choix,
        dt.global_df_brut,
        dt.global_df_mean,
        dt.global_df_fusionnées,
        dt.global_meandf_fusionnées,
        dt.global_df_1,
        dt.global_df_2,
        dt.global_df_3,
        dt.global_df_4,
        dt.global_df_5,
        dt.global_meandf_1,
        dt.global_meandf_2,
        dt.global_meandf_3,
        dt.global_meandf_4,
        dt.global_meandf_5
    )
    
    if df is not None:
        # Filtrer les colonnes numériques pour la visualisation
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        return [{'label': col, 'value': col} for col in numeric_cols]
    
    return []

@callback(
    Output('choropleth-map', 'figure'),
    Output('map-info', 'children'),
    Input('choix_df', 'value'),
    Input('map-color-column', 'value'),
    Input('map-groupby-column', 'value'),
    Input('active-tab', 'data'),
    prevent_initial_call=False
)
def update_map(choix, color_column, groupby_func, tab):
    """
    Met à jour la carte choroplèthe Plotly avec les données sélectionnées
    """
    if tab != 'maps':
        return dash.no_update, dash.no_update
    
    df = choix_df(
        choix,
        dt.global_df_brut,
        dt.global_df_mean,
        dt.global_df_fusionnées,
        dt.global_meandf_fusionnées,
        dt.global_df_1,
        dt.global_df_2,
        dt.global_df_3,
        dt.global_df_4,
        dt.global_df_5,
        dt.global_meandf_1,
        dt.global_meandf_2,
        dt.global_meandf_3,
        dt.global_meandf_4,
        dt.global_meandf_5
    )
    
    if df is None or df.empty:
        empty_fig = go.Figure()
        empty_fig.update_layout(title="Aucune donnée disponible", height=700)
        return empty_fig, "Aucune donnée à afficher"
    
    # Créer la carte
    fig = create_choropleth_map(df, color_column, groupby_func or 'sum')
    
    # Créer le message d'information
    total_rows = len(df)
    unique_communes = df['COMMUNE_CODE'].nunique() if 'COMMUNE_CODE' in df.columns else 0
    
    info_msg = f"Total de {total_rows} lignes | {unique_communes} communes uniques dans les données"
    
    return fig, info_msg
