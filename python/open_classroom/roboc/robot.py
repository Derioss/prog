# -*-coding:Utf-8 -*

class Robot:
    def __init__(self, avance):
        self.action = "Q"
        self.nord = "N"
        self.est = "E"
        self.sud = "S"
        self.ouest = "O"
        #nombre de case ou j'avance, forcément un int
        self.avance = avance

