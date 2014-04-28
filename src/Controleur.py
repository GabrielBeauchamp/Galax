import modele
import VueGraphique

class Controleur():
    def __init__(self):
      self.race = modele.Race()
      self.modele = modele.Modele(self, 30, 20, 40)
      self.vue = VueGraphique.VueGraphique(self)
      self.vue.mainloop()
      self.nbShipToSave = 0
        
    
    def boucleDeJeu(self):
        #print("fking works")
        self.modele.commencerPartie()
        self.vue.AfficherPartie()

    def boucleTour(self):
        if self.modele.verifierPartieFinie():
            self.finPartie()
            
        self.modele.updateEtoile()
        self.vue.InitialiserPanelInfo()
        test = True
        while test:
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

    def savePlaneteArrivee(self,etoile):
        self.modele.arriveeTemp=etoile

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
