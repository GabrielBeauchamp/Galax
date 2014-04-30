#TP - Galax - Par Gabriel Beauchamp, Antoine Delbast et Dragomir Dobrev
#remis à Jean-Marc Deschamps le 30 avril 2014 dans le cadre du cours 420-B41-VM
import traceback
import modele
import VueGraphique

class Controleur():
    def __init__(self):
      self.nbShipToSave = 0
      self.race = modele.Race()
      self.modele = modele.Modele(self, 30, 20, 40)
      self.vue = VueGraphique.VueGraphique(self)
      self.vue.mainloop()
            
    def boucleDeJeu(self):
        self.modele.commencerPartie()
        self.vue.AfficherPartie()


    def boucleTour(self):
        if self.modele.verifierPartieFinie():
            self.finPartie()
            
        self.modele.updateEtoile()
        # self.vue.InitialiserPanelInfo()

        # Emule un do..while en python
        test = True
        while test:
            self.vue.InitialiserPanelInfo()
            for e in self.modele.etoiles:
                for f in self.modele.humain.flottes:
                    if f.arrive == e and f.momentArrivee - self.modele.temps <= 0: # La flotte est arrivee
                        print("Flotte", f, "est arrivee a", e)
                        f.momentArrivee = None
                        self.modele.deplacement(f, f.arrive)
            self.modele.ajouterTemps()
            test = not self.modele.verifierTourFini()

        self.modele.gubru.joueSonTour()
        #self.modele.czin.joueSonTour()
        
        self.vue.AfficherPartie()

    def finPartie(self):
        print("La partie est terminée. Merci d'avoir joué.")
        exit(0)
        
    def savePlaneteDepart(self,etoile):
        self.modele.departTemp=etoile
        self.vue.texteLabelFlotte = "Port: " + str(self.modele.departTemp.nbShip)

        self.vue.InitialiserPanelInfo()

    def savePlaneteArrivee(self,etoile):
        self.modele.arriveeTemp=etoile
        self.vue.texteLabelDistance = "Distance: " + str(self.modele.calculerDistance(self.modele.departTemp, self.modele.arriveeTemp))[0:4]
        self.vue.texteLabelTemps = "Temp: " + str(self.modele.calculTempsVoyage(self.modele.departTemp, self.modele.arriveeTemp)/10)[0:4]

        self.vue.InitialiserPanelInfo()

    def launchFlotte(self):
        print("Depart:", self.modele.departTemp, " Arrivee:", self.modele.arriveeTemp)#, "NbShip:", self.nbShipToSave)
        if self.modele.departTemp == None:
            return
        if self.modele.arriveeTemp == None:
            return
        if self.nbShipToSave <= 0:
            return
        if self.nbShipToSave >= self.modele.departTemp.nbShip:
            self.nbShipToSave = self.modele.departTemp.nbShip

        self.modele.humain.formeFlotte(self.nbShipToSave, self.race.humain, self.modele.departTemp)
        self.modele.humain.envoitFlotte(self.modele.humain.flottes[-1], self.modele.arriveeTemp)
        print("Flotte a la -1", self.modele.humain.flottes[-1])

        for f in self.modele.humain.flottes:
            print("Temps voyage:", f.momentArrivee)

                               
if __name__ == "__main__":
    
    controleur = Controleur()
