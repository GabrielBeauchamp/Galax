class NPC():
    def __init__(parent):
        self.parent = parent     # Ca va etre Modele
        self.etoilePossedee = [] # Liste d'etoile
        self.nbVaisseau = 100   # Le nombre total
        self.nbManifacture = 10 # Le nombre total

    def joueSonTour():
        pass

    def nbTotalVaisseaux():
	total = 0
        for etoile in self.etoilePossedee:
            total += etoile.nbVaisseau

class Gubru():
    def __init__(modele):
        self.modele = modele
        self.etoileMere = self.etoilePossedee[0] # Parce que la premiere est de facto l'etoile mere.

    def joueSonTour():
        pass

    def doitChangerEtoileMere():
        for etoile in self.etoilePossedee:
            if etoile == self.etoileMere: # Donc qu'on possede toujours la meme etoile mere
                return False
        return True # Faut changer d'etoile mere.


class Czin(NPC):
    def __init__(modele):
        self.modele = modele

    def joueSonTour():
        pass
        
