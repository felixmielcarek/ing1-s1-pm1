from dash import html
import dash.html as html

def generate_tableau(df):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(min(len(df), 10))
        ])
    ])

def generate_tableau_page(df):
    return html.Div(
        [ html.H1("Page Tableau"), generate_tableau(df)],
        id='tableau-page'
    )