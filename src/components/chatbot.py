# Icône du chatbot
    html.Div(id='chat-icon', children='🤖', style=styles_chatbot['chat-icon']),
    # Fenêtre de chat
    html.Div(id='chat-window', style=styles_chatbot['chat-window'], children=[
        html.Div("Chatbot", style=styles_chatbot['chat-header']),
        html.Div(id='chat-messages1'),
        html.Div([
            dcc.Markdown(id='chat-messages'),
        ], style=styles_chatbot['chat-messages']),

        html.Div(style=styles_chatbot['chat-input-container'], children=[
            dcc.Input(id='chat-input', type='text', placeholder='Écrivez un message...', style=styles_chatbot['chat-input']),
            html.Button('Envoyer', id='chat-send-button',n_clicks=0, style=styles_chatbot['chat-send-button']),
        ]),
    ])