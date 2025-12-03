#Message pour le bouton Aide 
modal = dbc.Modal(
    [
        dbc.ModalHeader("Aide",style={'backgroundColor':couleur_background, 'color':couleur_text}),
        dbc.ModalBody(
            [dcc.Markdown('''
                ## Utilité

                Cet outil de visualisation et d’analyse de données permet de représenter les données issues des essais PAC (ou autre type de données) sous forme de graphique ou de tableaux, et de les traiter à l’aide de diverses fonctions. 
                ### Fonctionnement

            '''),
                  
                       
                        html.Br(),
                        
                        html.Br(),
                        html.A("Calcul de moyenne",id="text_moyenneglissante",className="mb-3"),
                        dbc.Collapse(
                            dcc.Markdown('''
                                L’utilisateur peut choisir une ou plusieurs colonnes dans « Sélection ». 
                                Dans Option/validation, il peut choisir 3 types de moyenne, moyenne glissante, moyenne cumulée ou moyenne horaire. 
                                Les colonnes moyennées sont ajoutées à un nouveau jeu de données avec un suffixe "moyennées" . 
                                En fonction du type de moyenne sélectionner les colonnes seront intitulées « nom de la colonne "_mean_glissante", " nom de la colonne _mean_cum" et " nom de la colonne _mean_horaire ". 
                                
                                Calcule d'une moyenne glissante : 
                                Préciser la plage de temps glissante. 
                                
                                Calcule d'une moyenne horaire : 
                                Le calcule se fait au termes de la periode. 



                             '''
                                ),
                            
                            id="text_moyenneg",
                            ),
                            
                            html.Br(),
                            html.A("Profondeur",id="text_profondeur",className="mb-3"),
                            dbc.Collapse(
                                dcc.Markdown('''
                                     
                                   Associe une palette de couleurs aux données d'une colonne choisie. 
                                    Le menu déroulant permet de choisir la colonne de référence. 
                                    Pour ajouter une couleur à la palette, cliquer sur la couleur et sur « Valider ». 
                                    Il est possible de supprimer la derniere couleur sélectionnée en cliquant sur " Clear". 
                                    Par défaut, 3 palettes sont déjà créées : 
                                    -	Température ( bleu et rouge) 
                                    -	Heure de la journée (minuit à minuit)  ( noir , bleu , orange, rouge et noir ) 
                                    -	Autres données ( gris , noir) 
                                    
                                    L’utilisateur peut ensuite retourner dans l’onglet "Graphique". 
                                    Dans la partie gauche un nouvel élément permet d’activer ou non la profondeur sur la 1er colonne sélectionner en axe y primaire. 
                                    
                                                 '''                                  
                               ),
                                
                                id="text_prof",
                                ),
                            html.Br(),
                           
                            html.A(" Régression Linéaire ", id="reg_lin_button", className="mb-3"),
                            dbc.Collapse(
                                dcc.Markdown('''
                                                                            
                                      Il est possible de l'activer ou non en choisissant "Avec régression" dans l'onglet Graphique, la régression se fait sur la 1re colonne y primaire. 
                                      Lorsque cette fonction est activée les seules colonnes temporelles utilisables en axe des x sont "temps_heure_24" ou "temps_heure_cumulée". 
                            
                     '''),
                                id="text_regression_lineaire",
                            ),
                            html.Br(),
                            html.A("Exclusion de(s) colonne(s)",id="text_exclusion",className="mb-3"),
                            dbc.Collapse(
                                dcc.Markdown('''
                                             En sélectionnant "Filtrage", un menu déroulant permet de sélectionner les colonnes à supprimer.                                          
                                        '''                                  
                               ),
                                
                                id="text_exclu",
                                ),

                            html.Br(),
                            html.A("Filtrage des données",id="text_filtrage",className="mb-3"),
                            dbc.Collapse(
                                dcc.Markdown('''
                                      Sélectionnez jusqu'à 3 colonnes de références dans la section 'Sélection'. Pour chaque colonne sélectionnée, vous devez indiquer leur valeur seuil et le type de filtre. 
                                      Pour valider le (s) filtrage (s), cliquer sur « Valider ». Pour activer ou désactiver ce filtrage, il faut se rendre dans l’onglet "Graphique"... 
                                       
                                           '''                                  
                               ),
                                
                                id="text_filtre",
                                ),
                            html.Br(),

                               
                          
            ],style={'backgroundColor':couleur_background, 'color': couleur_text}
        ),
        dbc.ModalFooter(
            dbc.Button("Fermer", id="close", className="ml-auto"),style={'backgroundColor':couleur_background, 'color': couleur_text}
        ),
    ],
    id="modal",
    size="fullscreen",#“sm”, “lg”, “xl” et “fullscreen”.
    style={
        'backgroundColor':couleur_background, # Couleur de fond du bouton
        'color': couleur_text, # Couleur du texte du bouton
        'border': '2px solid #4b5160' # Supprime la bordure par défaut du bouton
    }
)