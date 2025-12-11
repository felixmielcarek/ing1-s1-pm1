#Librairie crée par Micael FEBRAS FRAGOSO CARMONA

import dash
import dash_bootstrap_components as dbc
import pathlib
from dash import dcc, html

import dash
from dash import html,dcc,dash_table
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import html, dcc, Output, Input,State, ctx
import numpy as np
from dash import no_update
from scipy.optimize import curve_fit
from scipy.special import factorial
import os
import importlib.util
import subprocess
import re
import inspect

import shutil
import sys

import glob
import pandas as pd

import  utils.Fonctions



def Tableau(df,couleur_text,couleur_background):
    if df is None:
        return None
   # Calculer le résumé statistique et arrondir à 2 chiffres après la virgule
    summary = df.describe().round(2)
    # Ajouter une colonne pour expliquer chaque ligne
    summary['Description'] = {
        'count': 'Nombre total de valeurs',
        'mean': 'Moyenne des valeurs',
        'std': 'Écart type des valeurs',
        'min': 'Valeur minimale',
        '25%': '1/4 quart',
        '50%': '2/4 (médiane)',
        '75%': '3/4 quartile',
        'max': 'Valeur maximale'
    }


    # Réorganiser les colonnes pour que 'Description' soit la première colonne
    summary = summary[['Description'] + [col for col in summary.columns if col != 'Description']]
    # Convertir le résumé en format dictionnaire pour Dash DataTable
    summary_dict = summary.reset_index().to_dict('records')
    # Créer le tableau Dash avec les données du résumé
    summary_table = dash_table.DataTable(
        data=summary_dict,
        columns=[{'name': i, 'id': i} for i in summary.columns],
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': couleur_background,
                'color': couleur_text,

            },
            {
                'if': {'row_index': 'even'},
                'backgroundColor': couleur_background,
                'color': couleur_text,
            },
        ],
        style_header={
            'backgroundColor': couleur_background,
            'color': couleur_text
        },
        style_table={'overflowX': 'auto'},
        style_cell={'width': 'auto'},
    )
    
    # Créer le tableau Dash avec les données du DataFrame
    df_table = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'name': i, 'id': i} for i in df.columns],
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': couleur_background,
            'color': couleur_text,
            'width':'100%',
        },
        {
            'if': {'row_index': 'even'},
            'backgroundColor': couleur_background,
            'color': couleur_text,
            'width':'100%',
        },

    ],
    style_header={
        'backgroundColor': couleur_background,
        'color': couleur_text
    },   
    style_table={'overflowX': 'auto', 'overflowY': 'auto', 'maxHeight': '300px', 'width': '100%'}, 
    fixed_rows={'headers': True, 'data': 0},
    style_cell={'width': 'auto', 'minWidth': '200px'},  
)


    # Retourner les deux tableaux dans une Div, avec une ligne de rupture entre eux
    return html.Div([df_table, html.Br(),html.Br(), summary_table])
    

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

def initialiser_variables_globales():
    global global_df_brut
    global global_df_repared 
    global global_df_mean  
    global global_repared_na  
    global global_meandf_decal  
    global global_meandf_repared  
    global global_meandf_repared_na 
    global global_df_fusionnées 
    global global_meandf_fusionnées
    global global_df_1 
    global global_df_2 
    global global_df_3 
    global global_df_4 
    global global_df_5 
    global global_meandf_1  
    global global_meandf_2 
    global global_meandf_3  
    global global_meandf_4  
    global global_meandf_5 
    global global_fusion_data 
    



# Exemple de fonction de calcul du R²
def calculate_r_squared(x, y, func, popt):
    residuals = y - func(x, *popt)
    ss_res = sum(residuals**2)
    ss_tot = sum((y - y.mean())**2)
    return 1 - (ss_res / ss_tot)

# Fonctions d'ajustement
def linear(x, a, b):
    return a * x + b

def cauchy(x, A, B, C):
    return A + B / x**2 + C / x**4

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

#Fonction permettant de sauvegarder les données  
def save_data(data, filename):
    with open(filename + '_settings.json', 'w') as f:#Nous pouvons choisir le nom du fichier de sauvegarde
        json.dump(data, f)#fonction de json pour sauvegarder


#Fonction afin de charger la sauvegarde selon le nom du fichier upload
def load_data(filename):
    with open(filename + '_settings.json', 'r') as f:
        return json.load(f)

def affectation_df(choix,df,global_df_brut,global_df_repared,global_df_loisdeau,global_df_decal,global_df_filtrees,global_df_mean,global_meandf_filtrees,global_repared_na,global_meandf_decal,global_meandf_repared,global_meandf_repared_na,global_df_fusionnées,global_meandf_fusionnées,global_meandf_1,global_meandf_2,global_meandf_3,global_meandf_4,global_meandf_5,global_df_1,global_df_2,global_df_3,global_df_4,global_df_5):
    match choix :
        case 'DF_Brut': 
            global_df_brut=df
        
        case 'df_fusionnées' if df is not None: 
            global_df_fusionnées=df
        case 'df_mean' if df is not None:
            global_df_mean=df
                
        case 'meandf_filtrees':
            global_meandf_filtrees=df
        case 'df_filtrees':
            global_df_filtrees=df
        case 'df_1':
            global_df_1=df
        case 'df_2':
            global_df_2=df

        case 'df_3':
            global_df_3=df

        case 'df_4':
            global_df_4=df

        case 'df_5':
            global_df_5=df

        case 'meandf_1':
            global_meandf_1=df

        case 'meandf_2':
            global_meandf_2=df

        case 'meandf_3':
            global_meandf_3=df

        case 'meandf_4':
           global_meandf_4=df

        case 'meandf_5':
            global_meandf_5=df


 

#Fonction permettant de recrée les données manquantes temporel
def interpolate(df,mask,pas,ordre):
    ordre=int(ordre)
    for i in mask[mask].index:
        diff = df.loc[i, 'pas']
        start = df.loc[i-1, 'temps']
        while diff > pas: #Recreation des lignes manquantes
            start = start + pd.Timedelta(seconds=pas)
            diff -= pas
            df.loc[df.index.max() + 1] = {'temps': start}
    df = df.sort_values('temps').reset_index(drop=True)
    # Compléter les NaN avec la fonction interpolate option polynomiale
    for col in df.columns:
        if df[col].dtype == np.number:
            df[col] = df[col].interpolate(method='polynomial', order=ordre)
    return df

#Fonction permettant de choisir quel data frame utiliser
def choix_df(choix,global_df_brut,global_df_repared,global_df_mean,global_repared_na,global_meandf_decal,global_meandf_repared,global_meandf_repared_na,global_df_fusionnées,global_meandf_fusionnées,global_df_1,global_df_2,global_df_3,global_df_4,global_df_5,global_meandf_1,global_meandf_2,global_meandf_3,global_meandf_4,global_meandf_5,global_fusion_data):
    match choix:
        case 'DF_Brut':
            df = global_df_brut

        
        case 'df_mean':
            df = global_df_mean
        
        case 'meandf_repared':
            df = global_meandf_repared
        
        case 'df_fusionnées' :
            df = global_df_fusionnées
        
        case 'meandf_fusionnées':
            df = global_meandf_fusionnées
               
        case 'df_filtrees':
            df = global_df_filtrees
        
        case 'meandf_filtrees':
            df = global_meandf_filtrees

        case 'df_1':
            df=global_df_1

        case 'df_2':
            df=global_df_2

        case 'df_3':
            df=global_df_3

        case 'df_4':
            df=global_df_4

        case 'df_5':
            df=global_df_5

        case 'meandf_1':
            df=global_meandf_1

        case 'meandf_2':
            df=global_meandf_2

        case 'meandf_3':
            df=global_meandf_3

        case 'meandf_4':
            df=global_meandf_4

        case 'meandf_5':
            df=global_meandf_5

   
    #df = dd.DataFrame(df)
    #df = df.repartition(npartitions=desired_number_of_partitions)
    return df

def create_scatter_trace(x, y, name, mode='markers', secondary_y=False, **kwargs):
    """
    Crée une trace Scatter pour un graphique Plotly.
    """
    return go.Scatter(x=x, y=y, name=name, mode=mode, **kwargs), secondary_y

def apply_filters(df, col, conditions, thresholds, condition_colonne, comp_colonne):
    """
    Applique les filtres sur le DataFrame.
    """
    filtered_df = df.copy()
    
    if col is not None and conditions is not None and thresholds is not None:
        for col_name, condition, threshold in zip(col, conditions, thresholds):
            if col_name is not None and condition is not None and threshold is not None:
                if isinstance(threshold, str) and threshold.replace('.', '', 1).isdigit():
                    threshold = float(threshold)
                
                if condition == 'gt':
                    filtered_df = filtered_df[filtered_df[col_name] > threshold]
                elif condition == 'eq':
                    filtered_df = filtered_df[filtered_df[col_name] == threshold]
                elif condition == 'lt':
                    filtered_df = filtered_df[filtered_df[col_name] < threshold]
    
    if condition_colonne is not None and comp_colonne is not None and len(comp_colonne) == 2:
        if condition_colonne == 'gt':
            filtered_df = filtered_df[filtered_df[comp_colonne[0]] > filtered_df[comp_colonne[1]]]
        elif condition_colonne == 'eq':
            filtered_df = filtered_df[filtered_df[comp_colonne[0]] == filtered_df[comp_colonne[1]]]
        elif condition_colonne == 'lt':
            filtered_df = filtered_df[filtered_df[comp_colonne[0]] < filtered_df[comp_colonne[1]]]
    
    return filtered_df

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