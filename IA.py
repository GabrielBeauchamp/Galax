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
        # Parce que la premiere est de facto l'etoile mere.
        self.etoileMere = self.etoilePossedee[0]

        # On en fait des variables?
        # En fait je crois que j'ai pas compris cette partie.
        
	self.forceAttaque
        self.forceAttaqueBasique
        self.puissanceAttaque
        
    def joueSonTour():
        # En premier, on change (ou pas) l'etoile mere.
        # Le test est dans la fonction.
        changerEtoileMere()

        # On calcules les forces d'attaque.

        # On trouve une planete a attaquer

        # On l'attaque

    
    def doitChangerEtoileMere():
        for etoile in self.etoilePossedee:
            # Si etoileMere est dans la liste d'etoile.
            # On veut pas changer.
            if etoile == self.etoileMere: 
                return False
        return True # Faut changer d'etoile mere.

    def changerEtoileMere():
        if doitChangerEtoileMere():
            # J'ai envie de chercher celle qui est le plus securise
            # Mais pour l'instant, je fais juste prendre la premiere de la liste
		# En fait la doc dit de prendre la premiere de la liste.
            self.etoileMere = self.etoilePossedee[0]


class Czin(NPC):
    def __init__(modele):
        self.modele = modele

    def joueSonTour():
        pass
        
