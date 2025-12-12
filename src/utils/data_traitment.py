"""
#Fonction permettant de sauvegarder les données  
def save_data(data, filename):
    with open(filename + '_settings.json', 'w') as f:#Nous pouvons choisir le nom du fichier de sauvegarde
        json.dump(data, f)#fonction de json pour sauvegarder


#Fonction afin de charger la sauvegarde selon le nom du fichier upload
def load_data(filename):
    with open(filename + '_settings.json', 'r') as f:
        return json.load(f)
"""

import pandas as pd
import pathlib

# Define RAW_DATA_PATH locally to avoid circular imports
BASE_PATH = pathlib.Path(__file__).parent.parent.parent.resolve()
RAW_DATA_PATH = BASE_PATH.joinpath("data").joinpath("raw").resolve()

global_df_brut=global_df_repared=global_df_mean=global_repared_na=global_meandf_decal=global_meandf_repared=global_meandf_repared_na=global_df_fusionnées=global_meandf_fusionnées=global_df_1=global_df_2=global_df_3=global_df_4=global_df_5=global_meandf_1=global_meandf_2=global_meandf_3=global_meandf_4=global_meandf_5=global_fusion_data=None
global_df_brut = pd.read_csv(RAW_DATA_PATH.joinpath("rawdata.csv"),delimiter=';',encoding='utf-8')

