#region LIB IMPORTS
import dash
import dash_bootstrap_components as dbc
import pandas as pd
import pathlib
#endregion

#region FUNC IMPORTS
from components.sidebar import *
from utils.navigation import *
#endregion


#region APP CONFIG
app = dash.Dash(
    __name__, 
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=[dbc.themes.BOOTSTRAP,"https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css"]
) 
app.title="Parc automobile Francais"

server = app.server
app.config.suppress_callback_exceptions = True
#endregion

#region PATH
BASE_PATH = pathlib.Path(__file__).parent.parent.resolve()
RAW_DATA_PATH = BASE_PATH.joinpath("data").joinpath("raw").resolve()
#endregion

#region READ DATA
df = pd.read_csv(RAW_DATA_PATH.joinpath("rawdata.csv"),delimiter=';',encoding='utf-8')
#endregion

#region APP LAYOUT
app.layout = html.Div(
    [
        generate_sidebar(),
        html.Div(id='page-content')
    ])
#enregion

#region RUN
if __name__ == '__main__':
    app.run(debug=True)
#endregion