class OrderedDict(key,value):

    def __init__(self,base={}, **donnees):
        self.key = []
        self.value = []

        for key in donnees:
            self[key] = base[key]

        for value in base:
            self[value] = base[value]

    def __repr__(self):

