Projet : Parc automobile Français
=================================

Résumé
------
Ce projet est une application d'analyse et de visualisation des données du parc automobile français. Il propose des vues interactives (tableaux, graphiques, cartes) et des outils de traitement de données pour explorer, filtrer, agréger et exporter des jeux de données bruts et transformés.

Objectifs
---------
- Fournir une interface web interactive pour explorer les données du parc automobile.
- Offrir des outils de nettoyage, de moyennage, de fusion et d'export des données.
- Permettre la visualisation géographique (cartes) et graphique des indicateurs.

Principales technologies
------------------------
- Python 3.8+ (recommandé)
- Dash (framework web pour visualisations interactives)
- dash-bootstrap-components (composants UI)
- Plotly (visualisations)
- pandas, numpy, scipy (traitement et calculs)

Fichiers et organisation du projet
----------------------------------
Racine du projet
- README.md : description générale (existante)
- LICENSE : licence du projet
- requirements.txt : commande d'installation des dépendances de base

Répertoire `src/`
- `main.py` : point d'entrée de l'application Dash (lance le serveur web et ouvre le navigateur).
- `components/` : composants réutilisables de l'interface (ex. `sidebar.py`, `tableau.py`).
- `pages/` : définitions de pages et layouts (`graphique.py`, `map.py`, `fonctions.py`, `informations.py`) et logique back-end dans `back_end_pages/`.
- `utils/` : fonctions utilitaires et traitement des données (`data_traitment.py`, `Fonctions.py`, `globals.py`, `navigation.py`).
- `assets/` : fichiers CSS et ressources statiques (`common.css`, `sidebar.css`, `tableau-page.css`).

Répertoire `data/`
- `raw/` : données brutes (ex. `rawdata.csv`, `communes.json`).
- `cleaned/` : données nettoyées ou sorties du pipeline.

Installation (Windows)
---------------------
1) Créez et activez un environnement virtuel (PowerShell) :

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

2) Installez les dépendances :

   pip install -r requirements.txt

Remarques : `requirements.txt` inclut les paquets de base. Le projet utilise également `numpy` et `scipy` (utilisés dans `src/main.py`). Installez-les si nécessaire :

   pip install numpy scipy

Exécution
---------
Depuis la racine du projet, lancez :

   python src/main.py

L'application Dash s'ouvrira automatiquement dans le navigateur par défaut (http://127.0.0.1:8050/).

Structure et flux de l'application
---------------------------------
- `main.py` configure l'application Dash, charge les layouts (`pages/*`) et les composants (`components/*`) puis importe les callbacks back-end depuis `pages/back_end_pages/`.
- Les magasins (`dcc.Store`) conservent l'état des DataFrames, des fichiers ajoutés et des résultats intermédiaires (moyennages, filtres, fusions).
- Les boutons/onglets de la barre latérale déclenchent la génération des vues (tableau, graphique, cartes, export).
- L'export de données est géré via `dcc.Download` et prépare un CSV à télécharger.

Description des modules importants
---------------------------------
- `src/main.py` : configuration Dash, layout principal, routage des pages et exécution.
- `src/components/sidebar.py` : barre de navigation latérale et onglets.
- `src/components/tableau.py` : génération des tableaux interactifs.
- `src/pages/*` : layouts et définitions de pages (graphique, map, fonctions, informations).
- `src/pages/back_end_pages/*` : callbacks et logique métier (calculs, filtrage, transformation de DataFrame).
- `src/utils/Fonctions.py` et `src/utils/data_traitment.py` : fonctions utilitaires pour charger, nettoyer et transformer les données.

Données
-------
- Fichiers sources principaux : `data/raw/rawdata.csv` (jeu de données principal) et `data/raw/communes.json` (géodonnées ou correspondances).
- `data/cleaned/` : réservé aux fichiers produits par le pipeline (sauvegarde des sorties nettoyées/agrégées).

Bonnes pratiques pour les données
--------------------------------
- Conserver les fichiers bruts dans `data/raw/` et ne pas les modifier.
- Placer les sorties intermédiaires ou finales dans `data/cleaned/`.
- Pour ajouter un nouveau jeu de données, suivre la structure attendue par les fonctions de chargement dans `src/utils/`.

Personnalisation et configuration
---------------------------------
- Modifier les styles dans `src/assets/` (CSS).
- Ajouter ou adapter des layouts dans `src/pages/` pour de nouvelles vues.
- Étendre les callbacks et la logique métier dans `src/pages/back_end_pages/`.

Dépendances et versions recommandées
------------------------------------
- Python 3.8+
- dash
- dash-bootstrap-components
- pandas
- plotly
- numpy (recommandé)
- scipy (recommandé)
- requests (si utilisé pour fetch distants)

Tests
-----
Le projet ne contient pas de suite de tests automatisés fournie. Il est recommandé d'ajouter des tests unitaires pour :
- fonctions de traitement des données (`src/utils/`)
- logique de génération des tableaux et agrégations

Déploiement
-----------
Pour déployer sur un serveur (ex. VPS, service PaaS) :
- Créer un environnement virtuel sur le serveur.
- Installer les dépendances via `pip install -r requirements.txt`.
- Lancer l'application avec un serveur WSGI adapté (Gunicorn + un proxy Nginx) ou via `gunicorn "src.main:server"` si compatible.

Contribuer
----------
- Forkez le dépôt, créez une branche feature/bugfix, puis ouvrez une Pull Request décrivant les changements.
- Respectez l'architecture existante : composants réutilisables dans `components/`, pages dans `pages/`, et logique dans `pages/back_end_pages/`.

License
-------
Voir le fichier `LICENSE` à la racine du dépôt pour les détails de la licence.

Contacts et crédits
-------------------
Pour toute question, bug ou demande d'amélioration, ouvrez une issue sur le dépôt ou contactez l'auteur du projet directement.

Annexes
-------
- Fichiers clés à consulter pour démarrer :
  - src/main.py
  - src/components/sidebar.py
  - src/pages/graphique.py
  - src/pages/map.py
  - src/pages/back_end_pages/back_end_graphique.py
  - src/utils/Fonctions.py
