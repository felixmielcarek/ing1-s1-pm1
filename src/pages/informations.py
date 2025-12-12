import dash.html as html

def generate_informations_page():
    return html.Div([html.H1("Page Informations")])

layout_informations = html.Div([
    html.H1("Page Informations"),
    html.P("Contenu de la page informations")
])