class NPC():
    def __init__(self, parent):
        self.parent = parent     # Ca va etre Modele
        self.etoilePossedee = [] # Liste d'etoile
        self.nbVaisseau = 100   # Le nombre total
        self.nbManifacture = 10 # Le nombre total

    def joueSonTour(self):
        pass

    def nbTotalVaisseaux(self):
	total = 0
        for etoile in self.etoilePossedee:
            total += etoile.nbVaisseau

class Gubru():
    def __init__(self, modele):
        self.modele = modele
        # Parce que la premiere est de facto l'etoile mere.
        self.etoileMere = self.etoilePossedee[0]

        # On en fait des variables?
        # En fait je crois que j'ai pas compris cette partie.
	self.nbVaisseauParAttaque = 5        
        self.forceAttaqueBasique = 10
        self.puissanceAttaque
        
    def joueSonTour(self):
        # En premier, on change (ou pas) l'etoile mere.
        # Le test est dans la fonction.
        changerEtoileMere()

        # On calcules les forces d'attaque.
        self.puissaceAttaque = calculPuissanceAttaque()
        # On trouve une planete a attaquer

        # On l'attaque

    
    def doitChangerEtoileMere(self):
        for etoile in self.etoilePossedee:
            # Si etoileMere est dans la liste d'etoile.
            # On veut pas changer.
            if etoile == self.etoileMere: 
                return False
        return True # Faut changer d'etoile mere.

    def changerEtoileMere(self):
        if doitChangerEtoileMere():
            # J'ai envie de chercher celle qui est le plus securise
            # Mais pour l'instant, je fais juste prendre la premiere de la liste
		# En fait la doc dit de prendre la premiere de la liste.
            self.etoileMere = self.etoilePossedee[0]

    def calculPuissanceAttaque(self):
        pSelonTemps = self.modele.temps * self.nbVaisseauParAttaque + self.forceAttaqueBasique
        pBasique =  self.forceAttaqueBasique * 2
        
        if pSelonTemps > pBasique:
            return pSelonTemps
        else:
            return pBasique

class Czin(NPC):
    def __init__(self, modele):
        self.modele = modele

    def joueSonTour(self):
        pass
        
