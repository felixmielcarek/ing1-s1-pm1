#region IMPORTS
import dash
import dash_bootstrap_components as dbc
import pandas as pd
#endregion


#region APP CONFIG
app = dash.Dash(
    __name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP,"https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css"]
) 
app.title="Parc automobile Francais"

server = app.server
app.config.suppress_callback_exceptions = True
#endregion

#region READ DATA
df = pd.read_csv("../data/raw/rawdata.csv",delimiter=';',encoding='utf-8')
#endregion


app.layout = app_layout

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


if __name__ == '__main__':
    app.run(debug=True)