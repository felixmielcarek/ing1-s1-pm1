# Parc Automobile Français - Dashboard Interactif

## Vue d'ensemble

Ce projet est une application web interactive développée en Python permettant l'exploration, l'analyse et la visualisation des données du parc automobile français au niveau communal. Le dashboard offre des capacités avancées de traitement de données, de visualisation graphique et cartographique, ainsi que des outils d'export pour faciliter l'analyse approfondie du secteur automobile français.

**Technologie principale :** Dash (framework web Python pour la création de dashboards interactifs)

**Auteurs :** Félix MIELCAREK et Micael FEBRAS FRAGOSO CARMONA

**Licence :** MIT

---

## Table des matières

1. [User Guide](#user-guide)
2. [Data](#data)
3. [Developer Guide](#developer-guide)
4. [Rapport d'Analyse](#rapport-danalyse)
5. [Architecture et Flux de Données](#architecture-et-flux-de-données)
6. [Copyright et Déclaration d'Originalité](#copyright-et-déclaration-doriginalité)

---

## User Guide

### Installation et Déploiement

#### Prérequis

- **Python 3.8+** (testé avec Python 3.9 et 3.10)
- **pip** (gestionnaire de paquets Python)
- **Git** (optionnel, pour cloner le dépôt)

#### Étape 1 : Cloner ou télécharger le projet

```bash
# Avec Git
git clone <url-du-repository>
cd ing1-s1-pm1

# Ou télécharger et extraire le fichier ZIP
```

#### Étape 2 : Créer et activer un environnement virtuel

**Sur Windows (PowerShell) :**
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Sur macOS/Linux :**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Étape 3 : Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Dépendances principales :
- dash >= 2.0
- dash-bootstrap-components >= 1.0
- pandas >= 1.0
- plotly >= 5.0
- numpy >= 1.0
- scipy >= 1.0
- pyarrow >= 10.0
- chardet >= 4.0

#### Étape 4 : Lancer l'application

Depuis la racine du projet :

```bash
python src/main.py
```

L'application s'ouvrira automatiquement dans votre navigateur par défaut à l'adresse `http://127.0.0.1:8050/`

### Utilisation du Dashboard

Le dashboard est structuré autour d'une barre de navigation latérale qui fournit accès aux fonctionnalités principales :

#### 1. **Tableau** 
- Affiche les données brutes ou transformées sous forme de tableau interactif
- Permet la visualisation rapide des données chargées
- Affiche les statistiques descriptives (moyenne, écart-type, min, max, quartiles)

#### 2. **Graphique**
- Visualisation de données sous forme de graphiques personnalisables
- Types de graphiques disponibles : courbes, points, histogrammes, boîtes à moustaches
- Sélection d'axes X et Y
- Axes Y secondaires pour visualiser plusieurs séries
- Options d'échelle logarithmique pour chaque axe
- **Curve Fitting avancé** : ajustement des données à 20+ modèles mathématiques (linéaire, exponentiel, gaussien, oscillateur, etc.)
- Export des courbes d'ajustement

#### 3. **Maps (Cartes Choroplèthes)**
- Visualisation géographique des données par commune
- Filtres interactifs (carburant, Crit'Air, statut, groupe, catégorie)
- Sélection de colonnes numériques pour la coloration
- Agrégation par commune (somme, moyenne, compte, min, max)
- Données géospatiales basées sur GeoJSON

#### 4. **Fonctions (Outils Avancés)**
Ensemble complet d'outils de manipulation de données :

- **Filtrage des données** : Créer des filtres complexes avec conditions multiples
- **Renommer les colonnes** : Modifier les noms de colonnes pour plus de clarté
- **Solveur** : Créer de nouvelles colonnes avec des formules NumPy personnalisées
- **Scission de données** : Diviser le DataFrame en utilisant une colonne "charnière"
- **Calcul de pente/variation** : Analyser les variations temporelles ou spatiales
- **Calcul de moyenne** : Agrégation des données par groupes
- **Profondeur** : Calculer des statistiques par rapport à une colonne de référence
- **Fusionner des fichiers** : Combiner plusieurs fichiers de données

#### 5. **Exporter le fichier**
- Télécharger les données traitées au format CSV
- Exporte le DataFrame actif avec tous les traitements appliqués

### Gestion des Fichiers

- **Chargement** : Cliquez sur l'icône de téléchargement pour charger des fichiers CSV ou Excel
- **Formats supportés** : CSV (tous délimiteurs) et XLSX
- **Détection automatique** : Détection du délimiteur et de l'encodage
- **Multiple fichiers** : Chargez jusqu'à 5 fichiers simultanément et basculez entre eux

### Raccourcis et Conseils d'Utilisation

- Utilisez les dropdowns pour sélectionner rapidement des axes ou des colonnes
- Les sliders permettent d'ajuster la largeur et la hauteur des graphiques
- Les checkboxes permettent des options comme la normalisation ou la valeur absolue
- Utilisez l'export pour sauvegarder vos analyses intermédiaires

---

## Data

### Sources de Données

Les données utilisées dans ce projet proviennent des sources officielles suivantes :

#### 1. **Données du Parc Automobile Communal (2025)**

**Fichier :** `data/Donnees-sur-le-parc-de-vehicules-au-niveau-communal.2025-09.csv`

**Source :** Ministère de la Transition Écologique et Cohésion des Territoires (MTECT)  
Base de données : Statistiques sur le développement durable  
URL source : https://data.statistiques.developpement-durable.gouv.fr

**Mise à jour :** Septembre 2025

**Description :**  
Dataset comprehensive sur le parc automobile français par commune, incluant :
- Codes et noms des communes
- Classification des véhicules (catégorie, groupe)
- Énergie/Carburant (essence, diesel, électrique, hybride, etc.)
- Normes environnementales (Crit'Air)
- Statut des véhicules (circulant, non-circulant)
- Nombre de véhicules par catégorie

**Granularité :** Niveau communal  
**Période couverte :** Données actualisées au 30 septembre 2025

#### 2. **Données Géospatiales (GeoJSON)**

**Fichier :** `data/raw/communes.json`

**Format :** GeoJSON (RFC 7946)

**Description :**  
Contient les géométries des communes françaises avec les codes INSEE pour l'appariement avec les données du parc automobile.

**Structure :**
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "code": "75056",
        "nom": "Paris"
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [...]
      }
    }
  ]
}
```

### Dictionnaire des Colonnes Principales

| Colonne | Type | Description |
|---------|------|-------------|
| `COMMUNE_CODE` | String | Code INSEE de la commune (ex: "75056") |
| `COMMUNE_NOM` | String | Nom officiel de la commune |
| `CARBURANT` | String | Type de carburant (Essence, Diesel, Électrique, Hybride, etc.) |
| `CRITAIR` | String | Classe environnementale (0-5, non-défini) |
| `STATUT` | String | Circulant/Non-circulant |
| `GROUPE` | String | Groupe de véhicules (VP, VUL, etc.) |
| `CATEGORIE` | String | Catégorie détaillée |
| `NOMBRE` | Integer | Nombre de véhicules |

### Stockage et Organisation

```
data/
├── Donnees-sur-le-parc-de-vehicules-au-niveau-communal.2025-09.csv  (données brutes)
└── raw/
    └── communes.json  (géométries des communes)
```

**Bonnes pratiques :**
- Les fichiers dans `data/raw/` ne doivent **jamais** être modifiés directement
- Tous les fichiers transformés ou nettoyés doivent être créés en mémoire ou exportés de manière contrôlée
- Utilisez les fonctions de traitement de données pour toute manipulation

### Limitations et Considérations

1. **Complétude** : Certaines communes peut présenter des données manquantes ou nulles
2. **Classification** : La classification par Crit'Air et carburant dépend des informations déclarées
3. **Mise à jour** : Les données ont une fréquence de mise à jour trimestrielle
4. **Confidentialité** : Les données sont publiques et libres d'accès sous licence CC0

---

## Developer Guide

### Architecture Générale

Le projet suit une architecture **séparation des responsabilités** avec une structure client-serveur utilisant Dash/Flask :

```
ing1-s1-pm1/
├── src/
│   ├── main.py                          # Point d'entrée principal
│   ├── front_end.py                     # Interface utilisateur (layouts)
│   ├── Fonctions.py                     # Fonctions utilitaires (legacy)
│   ├── projet_multi_disciplinaire.py    # Module alternatif
│   │
│   ├── components/                      # Composants réutilisables
│   │   └── sidebar.py                   # Navigation latérale
│   │
│   ├── pages/                           # Layouts des pages
│   │   ├── fonctions.py                 # Page des outils/fonctions
│   │   ├── map.py                       # Page des cartes
│   │   ├── graphique.py                 # Page des graphiques
│   │   └── back_end_pages/              # Logique métier (callbacks)
│   │       ├── back_end_fonctions.py    # Traitement des fonctions
│   │       ├── back_end_graphique.py    # Logique des graphiques
│   │       └── back_end_map.py          # Logique des cartes
│   │
│   └── utils/                           # Utilitaires
│       ├── Fonctions.py                 # Fonctions de traitement
│       └── data_traitment.py            # Module de traitement (variables globales)
│
├── data/
│   ├── Donnees-sur-le-parc-de-vehicules-au-niveau-communal.2025-09.csv
│   └── raw/
│       └── communes.json
│
├── requirements.txt                     # Dépendances Python
├── LICENSE                              # Licence MIT
└── README.md                            # Ce fichier
```

### Stack Technologique

| Composant | Technologie | Version | Rôle |
|-----------|-------------|---------|------|
| Framework Web | Dash | 2.x | Interface interactive |
| Composants UI | Dash Bootstrap Components | 1.x | Thème et layout |
| Visualisation | Plotly | 5.x | Graphiques et cartes |
| Data Science | Pandas | 1.x | Manipulation de données |
| Calcul Scientifique | NumPy | 1.x | Opérations numériques |
| Optimisation | SciPy | 1.x | Curve fitting et statistiques |
| Sérialisation | PyArrow | 10.x | Format de stockage |
| Serveur Web | Flask (Dash) | intégré | Serveur applicatif |

### Flux de Données et Callbacks

#### 1. Initialisation (main.py)

```
- Crée l'application Dash
- Configure les meta-tags et thèmes
- Définit les chemins de base
- Initialise les stores (dcc.Store) pour la persistence des données
- Charge les layouts des pages
- Importe les callbacks back-end
```

#### 2. État Global (data_traitment.py)

Utilise des **variables globales** pour maintenir l'état du DataFrame :

```python
global_df_brut              # DataFrame brut chargé
global_df_mean              # DataFrame avec moyennes calculées
global_df_fusionnées        # DataFrames fusionnés
global_meandf_fusionnées    # Moyennes des fusionnés
global_df_1 à global_df_5   # 5 DataFrames utilisateur chargés
global_meandf_1 à global_meandf_5  # Leurs moyennes respectives
```

#### 3. Callbacks Principaux

**Structure d'un callback Dash :**
```python
@callback(
    Output('component_id', 'property'),  # Composant de sortie
    Input('trigger_id', 'property'),     # Déclencheur
    State('state_id', 'property'),       # État non-réactif
    prevent_initial_call=True
)
def ma_fonction(input_value, state_value):
    # Traitement
    return resultat
```

### Ajouter une Nouvelle Page

#### 1. Créer le layout (pages/ma_page.py)

```python
from dash import html, dcc

layout_ma_page = html.Div(
    id='table-ma-page',
    style={'display': 'none'},  # Caché par défaut
    children=[
        html.H2("Titre de ma page"),
        dcc.Graph(id='mon-graphique'),
        dcc.Dropdown(id='mon-filtre'),
        # ... autres composants
    ]
)
```

#### 2. Importer dans main.py

```python
from pages.ma_page import layout_ma_page

# Dans app.layout, ajouter:
layout_ma_page,
```

#### 3. Ajouter l'onglet à la barre latérale (components/sidebar.py)

```python
generate_sidebar_item('bi-icon-name', 'Ma Page', 'tab-ma-page'),
```

#### 4. Créer les callbacks (pages/back_end_pages/back_end_ma_page.py)

```python
from dash import Input, Output, callback
import dash

@callback(
    Output('table-ma-page', 'style'),
    Input('active-tab', 'data'),
    prevent_initial_call=True
)
def afficher_page(tab):
    if tab == 'ma-page':
        return {'display': 'block', ...styles...}
    return {'display': 'none'}

@callback(
    Output('mon-graphique', 'figure'),
    Input('mon-filtre', 'value'),
    prevent_initial_call=True
)
def update_mon_graphique(filtre_value):
    # Logique de mise à jour
    return figure
```

#### 5. Importer dans main.py

```python
from pages.back_end_pages.back_end_ma_page import *
```

### Ajouter un Nouveau Graphique

#### Approche 1 : Ajouter un type dans back_end_graphique.py

\\\python
# Dans la fonction update_graph()
if type_graph == 'mon-nouveau-type':
    fig = go.Figure()
    # Configuration spécifique
    fig.add_trace(go.Scatter(...))
    return fig
\\\

#### Approche 2 : Créer une fonction réutilisable

```python
# Dans utils/Fonctions.py
def creer_graphique_personnalise(df, x, y, **kwargs):
    """
    Crée un graphique personnalisé.
    
    Args:
        df (pd.DataFrame): DataFrame source
        x (str): Colonne X
        y (str ou list): Colonne(s) Y
        **kwargs: Options additionnelles
    
    Returns:
        go.Figure: Graphique Plotly
    """
    fig = go.Figure()
    
    # Logique
    
    return fig

# Utiliser dans back_end_graphique.py
fig = creer_graphique_personnalise(df, x, y)
```

### Fonctions de Traitement de Données

#### Chargement de fichier

```python
# Dans utils/Fonctions.py
def parse_contents(contents, filename):
    """Charge et traite un fichier CSV ou Excel."""
    # Détecte le format, l'encodage, le délimiteur
    # Retourne un DataFrame
    return df
```

#### Filtrage

```python
# Application de filtres avec conditions multiples
df_filtered = df[
    (df['colonne1'] > seuil) & 
    (df['colonne2'].isin(valeurs))
]
```

#### Calcul de moyenne

```python
df_mean = df.groupby('colonne_groupe')[['col1', 'col2']].mean()
```

---

## Rapport d'Analyse

### Objectifs de l'Analyse

Ce projet analyse le parc automobile français pour extraire des insights clés sur :
1. La répartition des véhicules par carburant et région
2. L'adoption des véhicules électriques et hybrides
3. Les tendances de conformité environnementale (Crit'Air)
4. Les disparités géographiques dans la motorisation

### Principales Conclusions

#### 1. **Transition Énergétique en Cours**

- La majorité du parc reste dominée par les carburants traditionnels (essence/diesel)
- Croissance progressive des véhicules électriques et hybrides
- Disparités régionales importantes dans l'adoption des énergies propres

#### 2. **Distribution Géographique**

- Concentration des véhicules dans les zones urbaines et périurbaines
- Les Île-de-France, Auvergne-Rhône-Alpes et Région PACA sont des pôles majeurs
- Opportunités d'analyse par clusters géographiques

#### 3. **Conformité Environnementale**

- Classification Crit'Air reflète l'âge moyen du parc par région
- Corrélation entre densité urbaine et possession de véhicules propres
- Opportunités d'amélioration dans les zones où Crit'Air > 3

#### 4. **Catégories de Véhicules**

- Véhicules particuliers (VP) dominent le parc
- VUL (Véhicules utilitaires légers) importants pour l'activité économique
- Faible proportion de poids lourds

### Utilisation du Dashboard pour l'Analyse

1. **Filtrer par région** via la carte choroplèthe
2. **Comparer les tendances** avec les graphiques multi-axes
3. **Exporter les données** filtrées pour analyse externe
4. **Calculer des statistiques** avec les outils de moyenne et profondeur

### Limitations de l'Analyse

- Données statiques au 30/09/2025 (mise à jour requise pour tendances)
- Pas de données sur l'utilisation réelle des véhicules
- Considérations socio-économiques non intégrées

---

## Architecture et Flux de Données

### Cycle de Vie d'une Donnée

```
Chargement → Validation → Stockage Global → Affichage → Export
    ↓           ↓             ↓              ↓        
  Parse      Transform    Store Dash     Callback
  CSV/XLSX   Encoding      (Memory)      Plotly
```

### Gestion des DataFrames Multiples

Le système supporte jusqu'à 5 DataFrames utilisateur simultanément :

```
global_df_1/global_df_2/global_df_3/global_df_4/global_df_5  ← DataFrames bruts
         ↓
global_meandf_1/.../_5                                        ← DataFrames moyennés
         ↓
Fusion optionnelle (global_df_fusionnées / global_meandf_fusionnées)
         ↓
global_df_brut (DataFrame actif sélectionné)
         ↓
Affichage et Traitement
```

---

## Copyright et Déclaration d'Originalité

### Déclaration Formelle

Je/nous déclare(s) sur l'honneur que le code fourni a été produit par moi/nous même, à l'exception des lignes ci-dessous :

### Code Emprunté et Références

#### 1. **Framework Dash et Callbacks**
- **Lignes** : Structure générale des callbacks (`@callback`)
- **Source** : Dash by Plotly - Documentation officielle (https://dash.plotly.com/)
- **Explication** : Syntaxe standard de Dash pour réactifs et callbacks
- **Fichiers affectés** : `main.py`, tous les fichiers `back_end_pages/*.py`

#### 2. **Génération de Composants Bootstrap**
- **Lignes** : Utilisation de `dbc.themes.BOOTSTRAP` et composants Bootstrap
- **Source** : Dash Bootstrap Components (https://dash-bootstrap-components.opensource.faculty.ai/)
- **Explication** : Syntaxe standard pour thèmes et composants UI
- **Fichiers affectés** : `main.py`, `components/sidebar.py`

#### 3. **Visualisation Plotly**
- **Lignes** : `go.Figure()`, `make_subplots()`, `px.choropleth_mapbox()`
- **Source** : Plotly Python Library (https://plotly.com/python/)
- **Explication** : API standard de Plotly pour création de graphiques
- **Fichiers affectés** : `pages/back_end_pages/back_end_graphique.py`, `back_end_map.py`

#### 4. **Optimisation Curve Fitting avec SciPy**
- **Lignes** : `curve_fit()` de `scipy.optimize`, modèles mathématiques standards
- **Source** : SciPy Documentation (https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)
- **Explication** : Utilisation de l'algorithme Levenberg-Marquardt standard
- **Fichiers affectés** : `pages/back_end_pages/back_end_graphique.py`

#### 5. **Détection d'Encodage et Délimiteur**
- **Lignes** : `chardet.detect()` et `csv.Sniffer().sniff()`
- **Source** : Bibliothèques Python standard (`csv`, `chardet`)
- **Explication** : Fonctions standard pour détection d'encodage et délimiteur CSV
- **Fichiers affectés** : `utils/Fonctions.py`

#### 6. **Manipulation Base64 et Fichiers**
- **Lignes** : `base64.b64decode()`, utilisation de `io.StringIO()` et `io.BytesIO()`
- **Source** : Python Standard Library
- **Explication** : Méthodes standard pour encodage/décodage et gestion d'entrées/sorties
- **Fichiers affectés** : `utils/Fonctions.py`

#### 7. **Icônes Bootstrap**
- **Source** : Bootstrap Icons CDN (https://cdn.jsdelivr.net/npm/bootstrap-icons/)
- **Utilisation** : Icônes pour la barre de navigation
- **Fichiers affectés** : `main.py` (meta-tags)

#### 8. **GeoJSON pour Cartes**
- **Lignes** : Chargement et parsing de GeoJSON
- **Source** : RFC 7946 GeoJSON Standard (https://tools.ietf.org/html/rfc7946)
- **Explication** : Format standard pour données géospatiales
- **Fichiers affectés** : `pages/back_end_pages/back_end_map.py`

### Code Original

Tout le code non déclaré ci-dessus est réputé être produit par l'auteur (ou les auteurs) du projet, notamment :

**Code original produit :**
- Architecture générale du projet et organisation modulaire
- Tous les callbacks personnalisés pour la logique métier
- Fonctions de traitement de données spécifiques (filtrage, scission, solveur, fusion)
- Interface utilisateur personnalisée et thème visuel
- Logique de gestion des DataFrames multiples
- Système de persistence d'état via stores Dash
- Intégration de 20+ modèles de curve fitting
- Logique des cartes choroplèthes avec filtres multiples
- Tous les fichiers dans `utils/`, `components/`, `pages/` sauf déclarations ci-dessus

### Licence

Ce projet est fourni sous licence **MIT**.

**MIT License**

Copyright © 2025 Félix MIELCAREK, Micael FEBRAS FRAGOSO CARMONA

Permission est accordée, gratuitement, à toute personne obtenant une copie de ce logiciel et des fichiers de documentation associés (le « Logiciel »), de traiter le Logiciel sans restriction, y compris, sans limitation, les droits d'utilisation, de copie, de modification, de fusion, de publication, de distribution, de concession de sous-licences et/ou de vente de copies du Logiciel, sous réserve que l'avis de copyright et la permission ci-dessus soient inclus dans toutes les copies ou portions substantielles du Logiciel.

Le Logiciel est fourni « TEL QUEL », sans garantie d'aucune sorte, expresse ou implicite, y compris, sans limitation, les garanties de commerciabilité, de conformité à un usage particulier et de non-contrefaçon.

### Contact et Support

Pour toute question sur l'originalité du code, les sources utilisées, ou l'architecture du projet :
- Consultez les commentaires dans le code source
- Référez-vous aux liens des sources externes inclus ci-dessus
- Contactez les auteurs du projet

---

## Annexe : Commandes Utiles

### Développement et Débogage

```bash
# Lancer avec rechargement automatique
python src/main.py --debug

# Installer des packages additionnels
pip install <package_name>

# Générer un requirements.txt à jour
pip freeze > requirements.txt

# Nettoyer les fichiers cache
rm -r src/__pycache__ src/*/__pycache__ src/*/*/__pycache__
```

### Tests

```bash
# Tester le chargement de données
python -c "import pandas as pd; df = pd.read_csv('data/Donnees-sur-le-parc-de-vehicules-au-niveau-communal.2025-09.csv', delimiter=';'); print(df.shape)"

# Vérifier l'installation des dépendances
pip list
```

---

**Document généré le** : 1 février 2026  
**Version** : 1.0  
**Statut** : Production
