# début code branch Maps

url =r"..\Data\Donnees-sur-le-parc-de-vehicules-au-niveau-communal.2025-09.csv" #"https://data.statistiques.developpement-durable.gouv.fr/dido/api/v1/datafiles/1582861b-e042-4490-9161-6429d8229703/csv?COMMUNE_CODE=startsWith%3A77"

df = pd.read_csv(url,delimiter=';',encoding='utf-8')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP,"https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css"])#Création du site en precisant qu'on ne veut pas de message d'erreur avec " suppress_callback_exceptions=True"
app.title="Parc automobile Francais"
app.index_string=f"""
    <!DOCTYPE html>
        <html>
            <head>
                {{%metas%}}
                <title>Parc automobile Francais</title>
                {{%favicon%}}
                {{%css%}}
                {css_code}
            </head>
            <body>
                {{%app_entry%}}
                <footer>
                    {{%config%}}
                    {{%scripts%}}
                    {{%renderer%}}
                </footer>
            </body>
        </html>
"""
app.layout = app_layout


if __name__ == '__main__':
    app.run(debug=True)