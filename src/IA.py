class Humain():
    def __init__(self, parent):
        self.parent = parent     # Ca va etre Modele
        self.etoilePossedee = [] # Liste d'etoile
        self.nbVaisseau = 100   # Le nombre total
        self.nbManifacture = 10 # Le nombre total
        self.flottes = []

    def joueSonTour(self):
        pass

    def nbTotalVaisseaux(self):
        total = 0
        for etoile in self.etoilePossedee:
            total += etoile.nbVaisseau
        self.nbVaisseau = total

    def formeFlotte(self, nbShip, race, etoile):
        etoile.flottes.append(Flotte(nbShip, race, etoile))
        etoile.nbShip -= nbShip
        
    def envoitFlotte(self, flotte, arrivee):
        flotte.arrive = arrivee
        flotte.momentDepart = modele.temps
        
class Gubru():
    def __init__(self, modele):
        self.etoilePossedee = [] # Liste d'etoile
        self.nbVaisseau = 100   # Le nombre total
        self.nbManifacture = 10 # Le nombre total
        self.flottes = []

        self.modele = modele
        # Parce que la premiere est de facto l'etoile mere.
        self.etoileMere = self.etoilePossedee[0]

        self.nbVaisseauParAttaque = 5
        self.forceAttaqueBasique = 10
        self.puissanceAttaque   # ou force_attaque

        
    def joueSonTour(self):
        # En premier, on change (ou pas) l'etoile mere.
        # Le test est dans la fonction.
        changerEtoileMere()

        # On calcules les forces d'attaque.
        self.puissaceAttaque = calculPuissanceAttaque()
        # On prepare les flottes
        self.formationFlottes()
        # On l'attaque
        self.attaqueEtoiles()
        self.rapatriement()


    def formeFlotte(self, etoile, nbShip):
        etoile.flottes.append(Flotte(nbShip, Race.gubru, etoile))
        etoile.nbShip -= nbShip
    
    def doitChangerEtoileMere(self):
        for etoile in self.etoilePossedee:
            # Si etoileMere est dans la liste d'etoile.
            # On veut pas changer.
            if etoile == self.etoileMere: 
                return False
        return True # Faut changer d'etoile mere.

    def changerEtoileMere(self):
        if doitChangerEtoileMere():
            # J'ai envie de chercher celle qui est le plus securisee
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

    def formationFlottes(self):
        while self.etoileMere.nbShip > self.puissaceAttaque + self.forceAttaqueBasique:
            self.formeFlotte(self.etoileMere, self.puissaceAttaque)


    def sortDistanceEtoile(self):    # Cherche une etoile a attaquer. Retourne l'etoile.
        distance = []
        for etoile in modele.etoiles: 
            if etoile.prorio == Race.gubru:
                pass            # Si c'est une des miennes, je fais rien.
            else:
                a = modele.distance(self.etoileMere, etoile)
                distance.append((a, etoile)) # Un tuple
        distance.sort()                
        return distance             

    def envoitFlotte(self, flotte, arrivee):
        flotte.arrive = arrivee
        flotte.momentDepart = modele.temps

    def attaqueEtoiles(self):
        etoileSort = sortDistanceEtoile()
        i = 0
        for flotte in self.flottes:
            if i > len(etoileSort)
            envoitFlotte(flotte, etoileSort[i][1]) # C'est un tuple.
            i += 1

    def rapatriement(self):
        flotte = []
        for f in self.flottes:
            # Si la flotte est pas en mouvement. Et qu'elle est pas sur l'etoileMere
            if f.arrive == None and f.depart != self.etoileMere: 
                flotte.append(f)

        for f in flotte:
            if f.nbShip > 25:   # Si le nombre de vaisseau est plus que 25
                newF = Flotte(15, Race.gubru, f.depart) # On en laisse 15
                f.nbShip -= 15
                self.envoitFlotte(f, self.etoileMere) # On envoit le reste a etoileMere
                self.flottes.append(newF)             # On ajoute la nouvelle flotte

class Czin():
    def __init__(self, modele):
        self.etoilePossedee = [] # Liste d'etoile
        self.nbVaisseau = 100   # Le nombre total
        self.nbManifacture = 10 # Le nombre total
        self.flottes = []

        self.modele = modele

    def joueSonTour(self):
        pass
        
if __name__ == "__main__":
    
    print("works")
