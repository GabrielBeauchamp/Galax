import modele
import VueGraphique

class Controleur():
    def __init__(self):
      self.race = modele.Race()
      self.modele = modele.Modele(self, 30, 20, 40)
      self.vue = VueGraphique.VueGraphique(self)
      self.vue.mainloop()
        
    
    def boucleDeJeu(self):
      print("fking works")
      self.modele.commencerPartie()
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
    

                               
if __name__ == "__main__":
    
    controleur = Controleur()
