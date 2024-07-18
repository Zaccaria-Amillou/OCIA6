"""
Script pour interagir avec l'API Edamam Food and Grocery Database.
Il effectue une requête pour obtenir des informations sur des aliments,
structure les données pertinentes, les sauvegarde dans un fichier CSV,
charge les données dans un dataframe pandas, sélectionne certaines colonnes,
et exporte le résultat dans un nouveau fichier CSV.

Auteur: Zaccaria Amillou
"""

import json
import requests
import pandas as pd
import csv

# URL de l'API
url = "https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser"

# Paramètres pour l'API
querystring = {"ingr":"champagne"}

# En-têtes de la requête pour l'API
headers = {
    "X-RapidAPI-Key": "279d3e1367msh23732bcf30a5598p1ec127jsn4ba6087d5aed",
    "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
}

# requête pour l'API et réponse
response = requests.request("GET", url, headers=headers, params=querystring)


# Charger la réponse en format JSON
json_data = json.loads(response.text)


# Extraire les données pertinentes et les structurer en une liste de dict
csv_data = []
for item in json_data['hints']:
    row = {
        'foodId': item['food']['foodId'],
        'label': item['food']['label'],
        'category': item['food']['category'],
        'foodContentsLabel': item['food'].get('foodContentsLabel'),
        'image': item['food'].get('image')
    }
    csv_data.append(row)

# sauvegarde des données CSV dans un fichier
with open('output.csv', 'w', newline='') as csv_file:
    fieldnames = ['foodId', 'label', 'category', 'foodContentsLabel', 'image']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in csv_data:
        writer.writerow(row)

# Charger les données dans un dataframe et sélectionner colonnes souhaitées
df = pd.read_csv('output.csv', nrows=10, usecols=['foodId', 'label', 'category', 'foodContentsLabel', 'image'])

# Exporter le dataframe en fichier CSV
df.to_csv('output_2.csv', index=False)

# Constat du fichier
df

#%%
