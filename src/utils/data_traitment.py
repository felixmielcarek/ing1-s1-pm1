

#Fonction permettant de sauvegarder les données  
def save_data(data, filename):
    with open(filename + '_settings.json', 'w') as f:#Nous pouvons choisir le nom du fichier de sauvegarde
        json.dump(data, f)#fonction de json pour sauvegarder


#Fonction afin de charger la sauvegarde selon le nom du fichier upload
def load_data(filename):
    with open(filename + '_settings.json', 'r') as f:
        return json.load(f)