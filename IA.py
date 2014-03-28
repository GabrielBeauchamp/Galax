class NPC():
    def __init__(parent):
        self.parent = parent     # Ca va etre Modele
        self.etoilePossedee = [] # Liste d'etoile
        self.nbVaisseau = 100   # Le nombre total
        self.nbManifacture = 10 # Le nombre total

    def joueSonTour():
        # On incremente ici?
        # incrementeVaisseau se fait dans le modele ou dans la classe ici?
        parent.incrementeVaisseau() # Ou whatever.
        pass

class Czin(NPC):
    def __init__(modele):
        self.modele = modele

    def joueSonTour():
        pass    
