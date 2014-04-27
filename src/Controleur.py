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
        print("fking works")
        self.modele.commencerPartie()
        self.vue.AfficherPartie()

    def testerTemps(self):
        for i in self.modele.humain.flottes:
            print("Flotte humaine", i)
        test = True
        while test:
            print (self.modele.temps)
            for e in self.modele.etoiles:
                for f in self.modele.humain.flottes:
                    if f.arrive == e and f.momentArrivee - self.modele.temps <= 0: # La flotte est arrivee
                        print("Flotte", f, "est arrivee a", e)
                        f.momentArrivee = None
                        self.modele.deplacement(f, f.arrive)
            self.modele.ajouterTemps()
            test = not self.modele.verifierTourFini()
        self.vue.AfficherPartie()
       # while not verifierPartieFinie():
          #  tourHumain()
            #tourGubru() -appelle Gubru.joueSonTour
            #tourCzin()  -appelle Czin.joueSonTour            
           # while not verifierTourFini():
              # ajouterTemps()
                #verifierFlotteArrivee()
              #  verifierCombat()
              #  combat()
            #updateVue()
         #   incrementerVaisseau()
       # partieFinie()
       # recommencerNouvellePartie()


        #GAME OVER merci d'avoir joué à Galax
        #note pour drago : mettre des tags les icone etoile pour que ca retourne le tag : "etoile+nbEtoile"
        #note tester tout le transtypage de l'operation tag
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
