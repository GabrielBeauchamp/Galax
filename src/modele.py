#TP - Galax - Par Gabriel Beauchamp, Antoine Delbast et Dragomir Dobrev
#remis à Jean-Marc Deschamps le 30 avril 2014 dans le cadre du cours 420-B41-VM
import random
import math

from IA import *

class Race():
    humain = 0
    gubru = 1
    czin = 2

class Etoile():
    def __init__(self, parent, x, y, numeroEtoile, proprio):
        self.parent = parent
        self.x = x
        self.y = y
        self.nbShip = 0
        self.nivInt = 0
        self.numeroEtoile = numeroEtoile
        self.proprio =  proprio
        self.racePresentes = []
        self.setNombreManifacture()
        self.czinValeurGrappe = 0      # Pour les Czin
        self.czinValeurBase = 0
        
    def setNombreManifacture(self):
        self.nbManu = random.randint(0, 6)

class Flotte():
    def __init__(self, nbShip, proprio, depart):
        self.noIdent = 0
        self.nbShip = nbShip
        self.proprio = proprio
        self.depart = depart
        self.arrive = None
        self.momentDepart = None
        self.momentArrivee = None

    def estArrivee(self):
        if self.momentArrivee - self.modele.temps == 0:
            return True
        else:
            return False

class AireJeu():
    def __init__(self, xMax, yMax):
        self.xMax=xMax
        self.yMax=yMax

class Modele():
    def __init__(self, parent, xMax, yMax, nbEtoile): 
        self.nbEtoiles = nbEtoile
        self.etoiles = []
        self.tourFini = False
        self.partieFinie = False
        self.posX = 0
        self.posY = 0
        self.parent = parent
        self.aireDeJeu = AireJeu(xMax, yMax)
        self.temps = 0
        self.etoilesEnConflit = []
        self.vaisseauxDeplacement = []
        self.flotte = []
        self.departTemp=None
        self.arriveeTemp=None

        self.humain = Humain(self)
        self.gubru = Gubru(self)
        self.czin = Czin(self)
        
    def verifierTourFini(self):
        if self.temps % 10 == 0:
            return True
        else:
            return False

    def updateEtoile(self):
        for e in self.etoiles:
            if e.proprio == Race.humain and not e in self.humain.etoilePossedee:
                self.humain.etoilePossedee.append(e)
            elif e.proprio == Race.gubru and not e in self.gubru.etoilePossedee:
                self.gubru.etoilePossedee.append(e)
            elif e.proprio == Race.czin and not e in self.czin.etoilePossedee:
                self.czin.etoilePossedee.append(e)
        
    def commencerPartie(self):
        self.planeteMaxAtteint = 0 
        self.xMax = self.aireDeJeu.xMax 
        self.yMax = self.aireDeJeu.yMax 
        self.PosX = 0;
        self.posY = 0
        self.planeteMaxAtteint = 0
    
        while self.planeteMaxAtteint < self.nbEtoiles:
            self.posX=random.randint(0, self.xMax-1)
            self.posY=random.randint(0, self.yMax-1)
          
            if self.etoileNonPresente (self.posX, self.posY):
                x = Etoile(self,self.posX, self.posY, self.planeteMaxAtteint, None)
                for i in range (x.nbManu):
                     x.nbShip += 1
                    
                self.etoiles.append(x)
                self.planeteMaxAtteint = self.planeteMaxAtteint+1
    
        x = random.randint(0, 39)
        
        self.etoiles[x].proprio = Race.humain
        self.etoiles[x].nbManu = 10
        self.etoiles[x].nbShip = 100
                    
        i=0
        
        while i<1:
            x = random.randint(0, 39)
            if self.etoiles[x].proprio == None:
                self.etoiles[x].proprio = Race.gubru
                self.etoiles[x].nbManu = 10
                self.etoiles[x].nbShip = 100
                i=+1
        i=0
        
        while i<1:
            x = random.randint(0, 39)
            if self.etoiles[x].proprio == None:
                self.etoiles[x].proprio = Race.czin
                self.etoiles[x].nbManu = 10
                self.etoiles[x].nbShip = 100
                i=+1

    def etoileNonPresente (self, x, y): 
        for Etoile in self.etoiles:
            if Etoile.x == x and Etoile.y == y :
                return False
        return True        
    
    def verifierPartieFinie(self):
        proprio0=True
        proprio1=True
        proprio2=True
    
        for i in self.etoiles:
            if i.proprio != Race.humain :
                proprio0 = False
                
            if i.proprio != Race.gubru :
                proprio1 = False
                
       
            if i.proprio != Race.czin:
                proprio2 = False
                
        if proprio0 or proprio1 or proprio2:
            return True
        else:
            return False

    def incrementerVaisseau(self):
        for i in self.etoiles:
            i.nbShip+=i.nbManu
            for j in range (i.nbManu):
                i.vaisseaux.append(Vaisseaux ())

    def deleteFlotte(self, flotte):
        flotte.depart = None
        flotte.arrive = None
        flotte.propio = None
        flotte.nbShip = 0
        flotte.momentArrivee = -4

    def deplacement(self, flotte, etoileArrivee):
        if flotte.proprio != etoileArrivee.proprio:
            self.combat(flotte, etoileArrivee)
        else:
            etoileArrivee.nbShip += flotte.nbShip
            self.deleteFlotte(flotte)        
    
    def verifierCombat(self):
        for Etoile in self.etoiles:
            if len(racePresentes) > 1:
                self.etoileEnConflit.append(noEtoile)


    def combat(self, flotteAttaquant, etoile):
        while etoile.nbShip > 0 and flotteAttaquant.nbShip > 0:
            if etoile.nbShip / flotteAttaquant.nbShip <= 0.05:
                if random.randint(0,100) >= 70:
                    flotteAttaquant.nbShip -= 1
                if random.randint(0,100) >= 70:
                    etoile.nbShip -= 1
            else:
                if random.randint(0,100) >= 70:
                    etoile.nbShip -= 1
                if random.randint(0,100) >= 70:
                    flotteAttaquant.nbShip -= 1

        if etoile.nbShip == 0:
            etoile.proprio = flotteAttaquant.proprio
        elif flotteAttaquant.nbShip == 0:
            pass # Sont deja proprio de leur etoile
        
        if etoile.nbShip > 0:
            pass # Sont deja sur leur etoile   
        elif flotteAttaquant.nbShip > 0:
            etoile.nbShip = flotteAttaquant.nbShip

        self.deleteFlotte(flotteAttaquant)
        
    def ajouterTemps (self):
        self.temps=self.temps+1
        
    def calculTempsVoyage(self, depart, arrivee):
        temps = 0
        distance = self.calculerDistance(depart, arrivee)

        if distance <= 2:
            temps = distance/2
        else:
            temps = 1 + ((distance-2)/3)
        return temps * 10

    def calculerDistance (self, etoileDepart,etoileArrivee):
        return ((etoileDepart.x - etoileArrivee.x)**2 + (etoileDepart.y - etoileArrivee.y)**2)**0.5
