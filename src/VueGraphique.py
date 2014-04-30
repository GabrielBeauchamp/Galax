#TP - Galax - Par Gabriel Beauchamp, Antoine Delbast et Dragomir Dobrev
#remis à Jean-Marc Deschamps le 30 avril 2014 dans le cadre du cours 420-B41-VM

from tkinter import *
from Controleur import *

class VueGraphique():
        def __init__(self, Controleur):
                self.fenetre = Tk()
                self.controleur = Controleur
                self.AfficherMenuUI()
                self.cliqueDepart=True
                self.nbShipToSave = 0
                self.texteLabelDistance = "Distance: "
                self.texteLabelTemps = "Temps: "
                self.texteLabelFlotte = "Port: "

        def mainloop(self):
                self.fenetre.mainloop()

        def centerWindow(self, width, height, window):
                w= width
                h= height

                sw= window.winfo_screenwidth()
                sh= window.winfo_screenheight()

                x= (sw - w)/2
                y= (sh - h)/2

                window.geometry('%dx%d+%d+%d' % (w, h, x, y)) 


        ##################################################################################################
        #                                         Fenêtre Menu                                          #
        ##################################################################################################

        ##################### Définition de fonctionnement des boutons pour le menu #####################
        def Bouton_Nouvelle_Partie(self):
                self.fenetreMenu.pack_forget()
                self.AfficherFenetreJeuUI()
                print("*** Nouvelle partie ***")
                self.controleur.boucleDeJeu()
        #################################################################################################


        ######################################### Afficher Menu #########################################
        def AfficherMenuUI(self):
                self.fenetre.title("Galax - Menu")
                width= 960      
                height= 640

                self.fenetreMenu = Frame(self.fenetre)
                self.fenetreMenu.pack()

                self.canevas = Canvas(self.fenetreMenu, width=width, height=height, bd=-2)
                self.canevas.pack() 

                self.imgMenu = PhotoImage(file= "imageSource/menuScene.gif")
                self.canevas.create_image(0,0, image= self.imgMenu, anchor= NW)

                bouton_nouvelle_partie = Button(self.fenetreMenu, text= "NOUVELLE PARTIE", bg="black", fg= "white", width= 30, height= 2,command= self.Bouton_Nouvelle_Partie)
                self.canevas.create_window(380, 500, anchor='nw', window= bouton_nouvelle_partie)

                bouton_quitter = Button(self.fenetreMenu, text= "QUITTER", bg="black", fg= "white", width= 30, height= 2,command= self.fenetre.destroy)
                self.canevas.create_window(380, 550, anchor='nw', window= bouton_quitter)

                self.centerWindow(width, height, self.fenetre)
        #################################################################################################



        ##################################################################################################
        #                                         Fenêtre Jeu                                           #
        ##################################################################################################

        ################### Définition de fonctionnement des boutons pour le jeu ########################
        def BoutonLaunch(self):
                print("The button Launch was pressed!")
                self.controleur.launchFlotte()

        def BoutonGo(self):
                print("The button End Turn was pressed!")
                self.controleur.boucleTour()

        def BoutonMoin(self):
                self.nbShipToSave = self.nbShipToSave-1
                self.controleur.nbShipToSave = self.nbShipToSave
                print(self.nbShipToSave)
                

        def BoutonPlus(self):
                self.nbShipToSave = self.nbShipToSave+1
                self.controleur.nbShipToSave = self.nbShipToSave
                print(self.nbShipToSave)
                
        ##################################################################################################


        ################################ Initialiser la Fenêtre du Jeu ################################## 
        def InitialiserJeuUI(self):
                self.fenetre.title("Galax - Jeu")
                width= 1200     
                height= 720

                self.fenetreJeu = Frame(self.fenetre)
                self.fenetreJeu.pack()

                self.centerWindow(width, height, self.fenetre)
        ##################################################################################################


        ############################# Initialiser les images du jeu ######################################
        def InitialsierImageJeu(self):
                self.imgPlanetHumain = PhotoImage(file="imageSource/planetHumain.gif")
                self.imgPlanetGubru = PhotoImage(file="imageSource/planetGubru.gif")
                self.imgPlanetCzin = PhotoImage(file="imageSource/planetCzin.gif")
                self.imgPlanetNoName = PhotoImage(file="imageSource/noName.gif")
        ##################################################################################################


        ####################################### Panel Canevas ############################################
        def InitialiserCanevas(self):
                panelCanevas = Frame(self.fenetreJeu, width= 1000, height= 650, bg= "lightgray")
                panelCanevas.grid(row= 0, sticky= N)

                self.canevas = Canvas(panelCanevas, width= 960, height=640, bd=-2, bg= "black")
                self.canevas.grid(padx= 5 ,pady= 5)

                self.imgJeu = PhotoImage(file= "imageSource/playScene.gif")
                self.canevas.create_image(0,0, image= self.imgJeu, anchor= NW)
        ##################################################################################################


        ######################################### Panel Info #############################################
        def InitialiserPanelInfo(self):
                # Probleme dans l'affichage des nombres. Peut-etre un probleme dans le modele.
                texteLabelHumain = "Humain : " + str(len(self.controleur.modele.humain.etoilePossedee) )
                texteLabelGubru = "Gubru : " + str(len(self.controleur.modele.gubru.etoilePossedee) )
                texteLabelCzin = "Czin : " + str(len(self.controleur.modele.czin.etoilePossedee) )

                texteLabelAnnee = "Annee : " + str(int(self.controleur.modele.temps / 10))


                if self.controleur.modele.departTemp != None:
                        texteLabelEtoileDep = "Depart : " + str(self.controleur.modele.departTemp).split("at ")[1].split(">")[0]
                else:
                        texteLabelEtoileDep = "Depart : None"

                if self.controleur.modele.arriveeTemp != None:
                        texteLabelEtoileArr = "Arrivee : " + str(self.controleur.modele.arriveeTemp).split("at ")[1].split(">")[0]
                else:
                        texteLabelEtoileArr = "Arrivee : None"       
                
                panelInfo = Frame(self.fenetreJeu, width= 230, height= 650, background= "darkgray")
                panelInfo.grid(row= 0, column= 1, sticky= N, rowspan= 2)

                panelNbPlanetPlayer = Frame(panelInfo, width= 220, height= 200, bg= "gray", relief= "sunken", bd= 3)
                panelNbPlanetPlayer.grid(row= 0, padx = 5, pady= 15)

                labelNbPlanetPlayer = Label(panelNbPlanetPlayer, text= "--- Nombres de systèmes ---", width= 29, bg= "black", fg= "white", relief= "raised", bd= 3)
                labelNbPlanetPlayer.grid(row= 0, column= 0, columnspan= 2)

                labelImageHumain = Label(panelNbPlanetPlayer, image= self.imgPlanetHumain, bg= "gray")
                labelImageHumain.image = self.imgPlanetHumain
                labelImageHumain.grid(row= 1, column= 0, sticky= E, pady= 5)

                labelHumain = Label(panelNbPlanetPlayer, text= texteLabelHumain, bg="gray")
                labelHumain.grid(row= 1, column= 1, sticky= W, padx=5, pady= 8)

                labelImageGubru = Label(panelNbPlanetPlayer, image= self.imgPlanetGubru, bg= "gray")
                labelImageGubru.image= self.imgPlanetGubru
                labelImageGubru.grid(row= 2, column= 0, sticky= E, pady= 5)

                labelGubru = Label(panelNbPlanetPlayer, text= texteLabelGubru, bg="gray")
                labelGubru.grid(row= 2, column= 1, sticky= W, padx=5, pady= 8)

                labelImageCzin = Label(panelNbPlanetPlayer, image= self.imgPlanetCzin, bg="gray")
                labelImageCzin.image = self.imgPlanetCzin
                labelImageCzin.grid(row= 3, column= 0, sticky= E, pady= 5)

                labelCzin = Label(panelNbPlanetPlayer, text= texteLabelCzin, bg="gray")
                labelCzin.grid(row= 3, column= 1, sticky= W, padx=5, pady= 8)

                panelAttaque = Frame(panelInfo, width= 220, height= 170, bg= "gray", relief= "sunken", bd= 3)
                panelAttaque.grid(row= 1, padx = 5, pady= 15)

                labelAttaque = Label(panelAttaque, text= "--- Attaque ---", width= 29, bg= "black", fg= "white", relief= "raised", bd= 3)
                labelAttaque.grid(row= 0, column= 0, columnspan= 2)

                labelFrom = Label(panelAttaque, text= texteLabelEtoileDep, bg= "gray")
                labelFrom.grid(row= 1, column= 0, sticky= W, padx= 10, pady= 10)

                labelTo = Label(panelAttaque, text= texteLabelEtoileArr, bg= "gray")
                labelTo.grid(row= 1, column= 1, sticky= W, padx= 10, pady= 10)

                labelDistance = Label(panelAttaque, text= self.texteLabelDistance, bg= "gray")
                labelDistance.grid(row= 2, column= 0, sticky= W, padx= 10, pady= 10)

                labelTemps = Label(panelAttaque, text= self.texteLabelTemps, bg= "gray")

                labelTemps.grid(row= 2, column= 1, sticky= W, padx= 10, pady= 10)

                panelFlotte = Frame(panelInfo, width= 220, height= 200, bg= "gray", relief= "sunken", bd= 3)
                panelFlotte.grid(row= 2, padx = 5, pady= 15)

                labelFlotte = Label(panelFlotte, text= "--- Flotte ---", width= 29, bg= "black", fg= "white", relief= "raised", bd= 3)
                labelFlotte.grid(row= 0)

                labelPort = Label(panelFlotte, text= self.texteLabelFlotte, bg= "gray")
                labelPort.grid(row= 1, sticky= W, padx= 10, pady= 8)

                labelTransit = Label(panelFlotte, text= "Transit : ", bg= "gray")
                labelTransit.grid(row= 2, sticky= W, padx= 10, pady= 8)

                labelAnnee = Label(panelInfo, text= texteLabelAnnee, width= 23, height= 2, font=(14),bg= "black", fg= "white", relief= "raised", bd= 3)
                labelAnnee.grid(row= 3, padx = 5, pady= 15)

                panelStatus = Frame(panelInfo, width= 220, height= 134, bg= "black", relief= "sunken", bd= 3)
                panelStatus.grid(row= 4, padx = 5, pady= 31)
        ##################################################################################################


        ##################################### Panel Boutons ##############################################
        def InitialiserPanelBouton(self):
                panelBoutons = Frame(self.fenetreJeu, width= 970, height= 70, background= "darkgray")
                panelBoutons.grid(row= 1, columnspan= 1, sticky= N)

                boutonLaunch = Button(panelBoutons, text= "Launch", bg="black", fg= "white", width= 26, height= 3, command= self.BoutonLaunch)
                boutonLaunch.grid(row= 0, column= 0, padx= 5, pady= 7)

                panelBoutonSpiner = Frame(panelBoutons, height= 56)
                panelBoutonSpiner.grid(row= 0, column= 1, padx= 172, pady= 7)

                boutonMoin = Button(panelBoutonSpiner, text= "-", bg="black", fg= "white", width= 8, height= 3, command= self.BoutonMoin)
                boutonMoin.grid(row= 0, column= 0)

                labelNbVesseaux = Label(panelBoutonSpiner, text="X", width= 12)
                labelNbVesseaux.grid(row=0, column=1)

                boutonPlus = Button(panelBoutonSpiner, text= "+", bg="black", fg= "white", width= 8, height= 3, command= self.BoutonPlus)
                boutonPlus.grid(row= 0, column= 2)

                boutonGo = Button(panelBoutons, text= "End Turn", bg="black", fg= "white", width= 26, height= 3, command= self.BoutonGo)
                boutonGo.grid(row= 0, column= 3, padx= 5, pady= 7)

                self.canevas.bind('<ButtonRelease-1>', self.GestionSouris)
        ######################################################################################################

        ################################## Afficher la fenêtre du jeu ########################################
        def AfficherFenetreJeuUI(self):
                self.InitialiserJeuUI()
                self.InitialsierImageJeu()
                self.InitialiserCanevas()
                self.InitialiserPanelInfo()
                self.InitialiserPanelBouton()
        ######################################################################################################

                 
        ####################################### Gestion de la souris #########################################
        def GestionSouris(self, event): 
                X= int(event.x/32)
                Y= int(event.y/32)
                print("Position du Clic ->", X,',', Y)
                for etoile in self.controleur.modele.etoiles:
                        if etoile.x==X and etoile.y==Y:# and etoile.proprio == self.controleur.race.humain:
                                if self.cliqueDepart==True and etoile.proprio == self.controleur.race.humain:
                                        self.controleur.savePlaneteDepart(etoile)
                                        self.InitialiserPanelInfo()
                                        print(etoile)
                                if self.cliqueDepart==False:
                                        self.controleur.savePlaneteArrivee(etoile)
                                        print(etoile)
                                self.cliqueDepart = not self.cliqueDepart
                                print (etoile.nbShip)
                                print (self.cliqueDepart)
                                
                        if etoile.x==X and etoile.y==Y and etoile.proprio is not self.controleur.race.humain:
                                print (etoile.nivInt)
                                                
                

                #if self.controleur.getVerifierEtoilePresent(X, Y):
                        #self.cotroleur.get

        ######################################################################################################
                


        ################ Affichage des images sur le canevas du jeu et les info du jeu ########################
        def AfficherPartie(self):
                for y in range(self.controleur.modele.aireDeJeu.yMax):
                        for x in range(self.controleur.modele.aireDeJeu.xMax):
                                for Etoile in self.controleur.modele.etoiles:
                                        if Etoile.x==x and Etoile.y==y:
                                                if Etoile.proprio == self.controleur.race.humain:
                                                        self.canevas.create_image(x*32,y*32, image= self.imgPlanetHumain,tag = "etoile"+str(Etoile.numeroEtoile), anchor= NW)
                                                elif Etoile.proprio == self.controleur.race.gubru:
                                                        self.canevas.create_image(x*32,y*32, image= self.imgPlanetGubru, tag = "etoile"+str(Etoile.numeroEtoile),anchor= NW)
                                                elif Etoile.proprio == self.controleur.race.czin:
                                                        self.canevas.create_image(x*32,y*32, image= self.imgPlanetCzin,tag = "etoile"+str(Etoile.numeroEtoile), anchor= NW)
                                                else:
                                                        self.canevas.create_image(x*32,y*32, image= self.imgPlanetNoName,tag = "etoile"+str(Etoile.numeroEtoile), anchor= NW)







        ######################################################################################################

#Main
#if __name__ == '__main__':
        #v = VueGraphique()
        #v.fenetre.mainloop() 




