import random
import math


class Etoile():
    def __init__(self,parent,x,y,nbManu,nbShip,NbNivInt,numeroEtoile,proprio):
        self.parent=parent
        self.x=x
        self.y=y
        self.nbManu=nbManu
        self.nbShip=nbShip
        self.NbInt=nbNivInt
        self.numeroEtoile=numeroEtoile
        self.proprio = proprio;
        self.vaisseaux=[]

    def incrementerVaisseau(self):
        if self.parent.tourFini == true:
            for i in self.parent.etoiles:
                for j in self.parent.etoiles.nbManu:
                    self.parent.etoiles.nbShip+1
        

class Vaisseau():
    def __init__(self,parent,depart):
        self.parent=parent
        self.depart=depart
        self.arrive=null
        self.momentDepart=null
        self.momentArrivee=null

class AireJeu():
    def __init__(self,xMax,yMax):
        self.xMax=xMax
        self.yMax=yMax

class Modele():
     def __init__(self,parent,xMax,yMax,nbEtoile):
        self.nbEtoiles=nbEtoiles
        self.etoiles=[]
        self.tourFini=False
        self.partieFinie=False
        self.posX=0
        self.poxY=0
        self.parent=parent
        self.aireDeJeu=AireJeu(xMax,yMax)
        self.temps=0

    def verifierTourFini(self,temps):
        if self.temps % 10 == 0:
            return true
        else:
            return false

    def calculTemps (self,xDepart,yDepart,xArrivee,yArrivee,tempsVoyage):
        self.xDepart=xDepart
        self.yDepart=yDepart
        self.xArrivee=xArrivee
        self.yArrivee=yArrivee
        self.tempsVoyage=tempsVoyage

        if xDepart == xArrivee:
            if ((abs(yArrivee -yDepart <= 2)):
                tempsVoyage = (abs(yArrivee -yDepart) / 2
                               
            elif ((abs(yArrivee -yDepart > 2)):
                tempsVoyage = 1+ ( (abs(yArrivee -yDepart) -2) / 3)
                            
        if yDepart == yArrivee:
            if (abs(xArrivee - xDepart) <= 2)):
                tempsVoyage = (abs(xArrivee -xDepart) / 2

            elif:
                tempsVoyage = 1+ ( (abs(xArrivee - xDepart) -2) / 3)

        if ((yDepart != yArrivee) and (xDepart != xArrivee)):
            if (math.trunc ( ( math.pow (abs(xArrivee-xDepart,2)) + math.pow(abs(yArrivee-yDepart,2))))) <= 2
                  tempsVoyage = (math.trunc ( ( math.pow (abs(xArrivee-xDepart,2)) + math.pow(abs(yArrivee-yDepart,2))))) /2
            elif:
                  tempsVoyage = 1+ (math.trunc ( ( math.pow (abs(xArrivee-xDepart,2)) + math.pow(abs(yArrivee-yDepart,2))) -2) / 3)
                  
              
            
        
    def commencerPartie(self):
        self.planeteMaxAtteint=0                   #pas sur syntaxe
        self.xMax=self.parent.AireJeu.xMax          #pas sur syntaxe
        self.yMax=self.parent.AireJeu.yMax          #pas sur syntaxe 
        self.PosX=0;
        self.posY=0
        self.planeteMaxAtteint=0
        self.positionDansListe=0
        
        while (planeteMaxAtteint<=self.modele.nbEtoile):
        
            self.posX=random.randint(0,self.xMax)
            self.posY=random.randint(0,self.yMax)
          
            if etoileNonPresente (self.posX,self.posy):     
                x = Etoile(self.poxX,self.posY,0,0,0,planeteMaxAtteint,null)
                self.etoiles.append(x)
                self.planeteMaxAtteint+1
                self.positionDansListe+1

    def etoileNonPrésente (x,y):                  #à verifier la source de posY
        for Etoile in self.etoile:
            if self.posX==x and self.posY==y:
            return false
        else:
            return true
        
            
                                           
        
        

    def verifierPartieFinie(self):                      #Ici je présuppose qu'il y a 3 valeurs  pour les propriétaires des planète 0-humains 1-Gubru 2-Czin
        self.memePriorio=memeProprio;
        for i in range (self.nbEtoiles):
            for self.etoiles[i]:
                if proprio !=0:
                    memeProprio=false
                else:
                    memeProprio=true

        for i in range (self.nbEtoiles):
            for self.etoiles[i]:
                if proprio != 1:
                    memeProprio=false
                else:
                    self.memeProprio=true
                    
        for i in range (self.nbEtoiles):
            for self.etoiles[i]:
                if proprio != 2
                    memeProprio=false
                else:
                    memeProprio=true

        return memeProprio

class Controleur():
    def __init__(self):
        self.modele=Modele(self,10,10,40)
   
if __name__=="__main__":       
    controleur=Controleur()


















    
