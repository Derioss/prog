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
        self._lieu_residence = "Paris"

    def __repr__(self):
        """QUand on entre notre objet dans l'interpreateur"""
        return "Personne: nom({}), prénom({}), âges ({})".format(self.nom, self.prenom, self.age)

    def _get_lieu_residence(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture à l'attribut 'lieu de résidence'"""
        print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence

    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode qui sera appelée quand on souhaitera modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format( \
            self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)


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


class Exemple:
    """Un petit exemple de classe"""
    def __init__(self, nom):
        self.nom = nom

        self.autre_attribut = "une valeur"
    def __del__(self):
        """méthode appelée quand l'objet est supprimé"""
        print("C'est la fin! On me supprime")

class Protege:
    """Classe possédant une méthode particluière d'accès à ses attributs :
    Si l'attribut n'est pas trouvé, on affiche une alerte et renvoie None"""

    def __init__(self):
        """On crée quelques attributs par défault"""
        self.a = 1
        self.b = 2
        self.c = 3
    def __getattr__(self, item):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle cette méthode.
        On affiche une alerte"""

        print("Alerte! Il n'y a pas d'attribut {} ici!".format(item))
    def __setattr__(self, key, value):
        """Méthode appelée quand on fait objet.nom_attr = val_attr."""

        object.__setattr__(self, key, value)
        self.enregistrer()
    def __delattr__(self, item):
        """On ne peut supprimer d'attribut, on lève l'exception AttributeError"""
        raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")

class Zdict:
    """CLasse enveloppe d'un dictionnaire"""
    def __init__(self):
        """Notre classe n'accept aucun paramètre"""
        self.dictionnaire = {}
    def __getitem__(self, item):
        """Cette méthode spéciale est appelée quand on fait object[item]
        Elle redirige vers self._dictionnaire[item]"""
        return self._dictionnaire[item]
    def __setitem__(self, key, value):
        """Cette méthode est appelée quand on écrit object[item] = valeur
        On redirige vers self._dictionnaire[index] = valeur"""

        self._dictionnaire[key] = value
    def __contains__(self, item):
        """Cette méthode spéciale est appelée quand on fait item in list
        elle redirige vers list.__contains__(item)"""
        self.__contains__(self, item)

class Duree:
    """CLasse contenant des durées sous la forme d'un nombre de minutes et de secondes"""

    def __init__(self, min=0, sec=0):
        """Constructeur de la classe"""
        self.min = min
        self.sec = sec
    def __str__(self):
        """Affichage un peu plus joli des objets"""
        return "{0:02}:{1:02}".format(self.min, self.sec)
    def __add__(self, objet_a_ajouter):
        """L'objet à ajouter est un entier, le nombre de secondes"""
        nouvelle_duree = Duree()
        nouvelle_duree.min = self.min
        nouvelle_duree.sec = self.sec
        nouvelle_duree.sec += objet_a_ajouter
        if nouvelle_duree.sec >= 60:
            nouvelle_duree.min += nouvelle_duree.sec // 60
            nouvelle_duree.sec = nouvelle_duree.sec % 60
        return nouvelle_duree
