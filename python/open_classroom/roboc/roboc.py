# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
from carte import *
import pickle
from robot import *


# On charge les cartes existantes
cartes = []

def main():

    for nom_fichier in os.listdir("cartes"):
        if nom_fichier.endswith(".txt"):
            chemin = os.path.join("cartes", nom_fichier)
            nom_carte = nom_fichier[:-3].lower()
            with open(chemin, "r") as fichier:
                contenu = fichier.read()
                # Création d'une carte, à compléter
                cartes.append(Carte(nom_carte, contenu))


    # On affiche les cartes existantes
    print("Labyrinthes existants :")

    for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte.nom))


# Si il y a une partie sauvegardée, on l'affiche, à compléter

# j'enregistre les cartes existantes:
    with open('sauvegarde', wb) as sauvegarde:
        mon_picker = pickle.Pickler(sauvegarde)
        mon_picker.dump()


# ... Complétez le programme ...


main()