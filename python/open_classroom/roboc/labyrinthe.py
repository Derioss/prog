# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles, sortie, porte):
        self.robot = robot
        self.grille = {}
        self.obstables = obstacles
        self.sortie = sortie
        self.porte = porte
        # ...
