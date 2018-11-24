class Personne:
    """CLasse définissant une personne caractérisé par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    def __init__(self, nom, prenom):
        """Pour l'instannt, on ne va définir qu'un seul attribut"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self.lieu_residence = "Paris"

class Compteur:
    '''Cette classe possède un attribut de classe qui s'incrémente à chaque fois que l'on crée un objet de ce type'''
    objets_crees = 0
    def __init__(self):
        """A chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur.objets_crees += 1
    def combien(cls):
        """Méthode de classe affichant combien d'objet on était crée"""
        print("on a créé {} d'objet".format(cls.objets_crees))
    combien = classmethod(combien)
class TableauNoir:
    '''Classe définnissant une surface sur laquelle on peut écrire,
    que l'ont peut lire et effacer, par jeu de méthodes. L'attribut modifié est surface
    '''

    def __init__(self):
        """ Par défaults notre surface est vide"""
        self.surface = ""
    def ecrire(self, message_a_ecrire):
        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire
    def lire(self):
        """Cette méthode se charge d'afficher, grâce à print la surface du tableau"""
        print(self.surface)
    def effacer(self):
        """Cette méthode permet d'effacer la surface du tableau"""
        self.surface = ""

    class Test:
        '''Une classe de test tous simplement'''
        def afficher():
            """Fonction chargés d'afficher quelquechose"""
            print("On affiche la même chose")
            print("peu importe les données de l'objet ou de la classe")
        afficher = staticmethod(afficher)

