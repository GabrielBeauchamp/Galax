import random
import math

class Etoile():
    def __init__(self, parent, x, y, nbManu, nbShip, NbNivInt, numeroEtoile, proprio): # TO LOOK On doit vraiment faire comme ca?
        self.parent=parent
        self.x=x
        self.y=y
        self.nbManu=nbManu
        self.nbShip=nbShip
        self.NbInt=nbNivInt
        self.numeroEtoile=numeroEtoile
        self.proprio = proprio;
        self.vaisseaux=[]
        self.racePresentes=[]

class Vaisseau():
    def __init__(self, parent, depart):
        self.parent=parent
        self.depart=depart
        self.arrive=null
        self.momentDepart=null
        self.momentArrivee=null
        self.noFlotte

class Flotte():
    def __init__(self, parent, noIdent,nbShip,prorio):
        self.parent=parent
        self.noIdent=noIdent
        self.nbShip=NbShip
        self.prorio=prorio

class AireJeu():
    def __init__(self, xMax, yMax):
        self.xMax=xMax
        self.yMax=yMax

class Modele():
    def __init__(self, parent, xMax, yMax, nbEtoile): # TO LOOK xMax, yMax, et nbEtoile ont besoin d'etre en parametre?
        self.nbEtoiles=nbEtoile
        self.etoiles=[]
        self.tourFini=False
        self.partieFinie=False
        self.posX=0
        self.poxY=0
        self.parent=parent
        self.aireDeJeu=AireJeu(xMax, yMax)
        self.temps=0
        self.etoilesEnConflit=[]
        
    def verifierTourFini(self, temps):
        if self.temps % 10 == 0:
            return true
        else:
            return false
        
    def commencerPartie(self):
        self.planeteMaxAtteint = 0 #pas sur syntaxe
        self.xMax = self.parent.AireJeu.xMax #pas sur syntaxe
        self.yMax = self.parent.AireJeu.yMax #pas sur syntaxe
        self.PosX = 0;
        self.posY = 0
        self.planeteMaxAtteint = 0
        self.positionDansListe = 0
        
        while planeteMaxAtteint <= self.modele.nbEtoile:
        
            self.posX=random.randint(0, self.xMax)
            self.posY=random.randint(0, self.yMax)
          
            if etoileNonPresente (self.posX, self.posy):
                x = Etoile(self.poxX, self.posY, 0, 0, 0, planeteMaxAtteint, null)
                self.etoiles.append(x)
                self.planeteMaxAtteint += 1
                self.positionDansListe += 1

    def etoileNonPresente (self, x, y): 
        for Etoile in self.etoiles:
            if Etoile.posX == x and Etoile.posY == y :
                return False
            else:
                return True
    
    def verifierPartieFinie(self): #Ici je presuppose qu'il y a 3 valeurs pour les proprietaires des planete 0-humains 1-Gubru 2-Czin 4-NPC mais on les utilise pas ici
        self.memePriorio = memeProprio; # TO LOOK Si tu fais ca, faut que ce soit clairement ecrit quelque part. Pas juste en commentaire.
        for i in range (self.nbEtoiles): # TO LOOK Oh et le code me semble.. etrange.
            for i in self.etoiles[i]:
                if proprio != 0 :
                    memeProprio = False
                else:
                    memeProprio = True
        for i in self.etoiles[i]:
                if proprio != 1 :
                    memeProprio = False
                else :
                    self.memeProprio = True
        for i in self.etoiles[i]:
                if proprio != 2:
                    memeProprio = False
                else :
                    memeProprio = True
        return memeProprio

    def incrementerVaisseau(self):
        if self.tourFini == True:
            for i in self.etoiles:
                for j in self.etoiles.nbManu:
                    self.etoiles.nbShip += 1
    
    def verifierCombat(self):
        for Etoile in self.etoiles:
            if len(racePresentes) > 1:
                self.etoileEnConflit.append(noEtoile)

    def combat(self,defenseurs,attaquants,Etoile):    ##trouver moyen de changer le proprio de l'étoile suite au combat
        while attaquants > 0 or defenseurs > 0:
            if randint(0,100) >=70:
                attaquants-1
            if randint(0,100) >=70:
                defenseurs-1

        if defenseurs >0:
            Etoile.nbShip = defenseurs
        elif attaquants > 0:
            Etoile.nbShip = attaquants

    
        
    def ajouterTemps (self):
        self.temps=self.Temps+0.1
        
    def calculTempsVoyage (self, xDepart, yDepart, xArrivee, yArrivee):
        tempsVoyage=0

        if xDepart == xArrivee:
            if  abs(yArrivee - yDepart) <= 2:
                tempsVoyage = (abs(yArrivee - yDepart) / 2
                               
            elif abs(yArrivee - yDepart) > 2:
                tempsVoyage = 1+ ( (abs(yArrivee - yDepart) -2) / 3)
                            
        if yDepart == yArrivee:
            if (abs(xArrivee - xDepart) <= 2)):
                tempsVoyage = (abs(xArrivee - xDepart) / 2

            else:
                tempsVoyage = 1+ ( (abs(xArrivee - xDepart) -2) / 3)

        if ((yDepart != yArrivee) and (xDepart != xArrivee)):
            if (math.trunc ( ( math.pow (abs(xArrivee - xDepart, 2)) + math.pow(abs(yArrivee - yDepart, 2))))) <= 2:
                  tempsVoyage = (math.trunc ( ( math.pow (abs(xArrivee - xDepart, 2)) + math.pow(abs(yArrivee - yDepart, 2))))) /2
            elif (math.trunc ( ( math.pow (abs(xArrivee - xDepart, 2)) + math.pow(abs(yArrivee - yDepart, 2))))) > 2: # TO LOOK Parce que elif demande un autre test, non?
                  tempsVoyage = 1+ (math.trunc ( ( math.pow (abs(xArrivee - xDepart, 2)) + math.pow(abs(yArrivee - yDepart, 2))) -2) / 3)


class Controleur():
    def __init__(self):
        self.modele = Modele(self, 10, 10, 40)
        #cree le modele
        #tour du joueur
        #tour des Gubru
        #tour des Czin
        #incrementation de temps 0.1
        #verification batailles
        #batailles
        #incrementation 0.1 encore
        #incrementation -batailles etc
        #verification si un tour est passé
        #verification si la partie est finie                       
        #si tour passé,si partie non finie incrémentation des vaisseaus sur chaque étoile conquise
        #Re-tour du joueur
        #on recommence jusqu'à la fin de la partie
        #GAME OVER merci d'avoir joué à Galax
                               
if __name__ == "__main__":
    controleur = Controleur()
