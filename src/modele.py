import random
import math

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

    def setNombreManifacture(self):
        self.nbManu = random.randint(0, 6)

class Flotte():
    def __init__(self, nbShip, prorio):
        self.parent = parent
        self.noIdent = noIdent
        self.nbShip = nbShip
        self.prorio = prorio
        self.depart = None
        self.arrive = None
        self.momentDepart = None
        self.momentArrivee = None


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
        
    def verifierTourFini(self, temps):
        if self.temps % 10 == 0:
            return True
        else:
            return False
        
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
                self.planeteMaxAtteint += 1
    
      
        

        
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
        
        
        print (self.planeteMaxAtteint)
        self.verifierTableau()

    def etoileNonPresente (self, x, y): 
        for Etoile in self.etoiles:
            if Etoile.x == x and Etoile.y == y :
                return False
        return True

    def verifierTableau (self):  #fonction de test
        self.numero=0
        for i in range(self.aireDeJeu.yMax):
            for j in range(self.aireDeJeu.xMax):
                self.isEtoile =False
                for k in self.etoiles:
                    if k.y==i and k.x==j:
                        self.isEtoile = True
                        if k.proprio == Race.humain:
                            print ("H",end='')
                        elif k.proprio == Race.gubru:
                            print ("G",end='')
                        elif k.proprio == Race.czin:
                            print ("C",end='')
                        else:
                            print ("X",end='')
                        k.numeroEtoile=self.numero+1
                        
                if not self.isEtoile:
                    print("-",end='')
            print ('\n')
        print (self.etoiles[0].x)
        print (self.etoiles[0].y)
        print(self.etoiles[0].nbManu)
        
         
    
    def verifierPartieFinie(self):
        proprio0=True
        proprio1=True
        proprio2=True
    
        for i in self.etoiles[i]:
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
                

    
    def verifierCombat(self):
        for Etoile in self.etoiles:
            if len(racePresentes) > 1:
                self.etoileEnConflit.append(noEtoile)

    def combat(self,defenseurs,attaquants,Etoile, propAttaquant,propDefenseur):    
        while attaquants > 0 or defenseurs > 0:
            if  randint(0,100) >=70:
                attaquants-1
            if randint(0,100) >=70:
                 defenseurs-1

            if defenseurs >0:
                Etoile.nbShip = defenseurs
                
            elif attaquants > 0:
                Etoile.nbShip = attaquants

        if defenseurs == 0:
            Etoile.proprio = propAttaquant
        elif attaquants == 0:
            Etoile.proprio == propDefenseur
        
    def ajouterTemps (self):
        self.temps=self.Temps+0.1
        
    def calculTempsVoyage (self, xDepart, yDepart, xArrivee, yArrivee):
        tempsVoyage=0

        if xDepart == xArrivee:
            if  abs(yArrivee - yDepart) <= 2:
                tempsVoyage = (abs(yArrivee - yDepart) / 2)
                               
            elif abs(yArrivee - yDepart) > 2:
                tempsVoyage = 1+ ( (abs(yArrivee - yDepart) -2) / 3)
                            
        if yDepart == yArrivee:
            if (abs(xArrivee - xDepart) <= 2):
                tempsVoyage = (abs(xArrivee - xDepart) / 2)

            else:
                tempsVoyage = 1+ ( (abs(xArrivee - xDepart) -2) / 3)

        if ((yDepart != yArrivee) and (xDepart != xArrivee)):
            if (math.trunc ( ( math.pow (abs(xArrivee - xDepart, 2)) + math.pow(abs(yArrivee - yDepart, 2))))) <= 2:
                  tempsVoyage = (math.trunc ( ( math.pow (abs(xArrivee - xDepart, 2)) + math.pow(abs(yArrivee - yDepart, 2))))) /2
            elif (math.trunc ( ( math.pow (abs(xArrivee - xDepart, 2)) + math.pow(abs(yArrivee - yDepart, 2))))) > 2: 
                  tempsVoyage = 1+ (math.trunc ( ( math.pow (abs(xArrivee - xDepart, 2)) + math.pow(abs(yArrivee - yDepart, 2))) -2) / 3)

    def joueurProprio (self, tag):
        tag[6:]

        if self.etoiles[tab].proprio == Race.humain:
            return True
        else:
            return False

    def niveauIntel (self, tag):
        tag[6:]
        return self.etoiles[tag].nivInt

    def IncrementerIntel (self, tag):
        tag[6:]
        if self.etoiles[tag].nivInt == 0:
            self.etoiles[tag].nivInt =1
        if self.etoiles[tag].nivInt == 1:
            self.etoiles[tag].nivInt =2
        if self.etoiles[tag].nivInt == 2:
            self.etoiles[tag].nivInt =3

    def creerFlotte (self,tag,nbShip,proprio):                ##les AI utilisent cette fonction pour creer leur flottes
        tag[6:]
        if self.etoiles[tag].nbShip >= nbShip:
            self.flotte.append(Flotte(nbShip,proprio))
            self.etoiles[tag].nbShip = self.etoiles[tag].nbShip - nbShip
                
            return len(self.flotte)-1
        else:
           return False
        
    def donnerDestFlotte (tagFlotte,tagEtoile):
        tagFlotte[6:]
        tagEtoile[6:]
        self.flotte[tagFlotte].arrivee = self.etoiles[tagEtoile]

            

class Controleur():
    def __init__(self):
        self.modele = Modele(self, 30, 20, 40)
        self.modele.commencerPartie()
        #note ajouterTemps et VerifierTourFini et #verifier partiefini est ici
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
        #note pour drago : mettre des tags les icone etoile pour que ca retourne le tag : "etoile+nbEtoile"
        #note tester tout le transtypage de l'operation tag
                               
if __name__ == "__main__":
    
    controleur = Controleur()
