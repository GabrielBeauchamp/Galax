from tkinter import *

class VueGraphique(Frame):
	def __init__(self):
		self.fenetreMenu = Tk()
		Frame.__init__(self, self.fenetreMenu)
		#self.controleur = Controleur
		self.AfficherMenuUI()
	
	def mainloop(self):
		self.fenetreMenu.mainloop()

	def centerWindow(self, width, height, window):
		w= width
		h= height

		sw= window.winfo_screenwidth()
		sh= window.winfo_screenheight()

		x= (sw - w)/2
		y= (sh - h)/2

		window.geometry('%dx%d+%d+%d' % (w, h, x, y)) 

	# Définition de fonctionnement des boutons pour le menu
	# Bouton nouvelle partie
	def Bouton_Nouvelle_Partie(self):
		self.fenetreMenu.destroy()
		self.AfficherJeuUI()
		print("*** Nouvelle partie ***")
	

	def AfficherMenuUI(self):
		self.fenetreMenu.title("Galax - Menu")
		width= 960      # LOOK: Magic numbers?
		height= 640

		self.canevas = Canvas(self.fenetreMenu, width=width, height=height, bd=-2)
		self.canevas.pack() # LOOK: Got a pack there.

		self.imgMenu = PhotoImage(file= "imageSource/menuScene.gif")
		self.canevas.create_image(0,0, image= self.imgMenu, anchor= NW)

		bouton_nouvelle_partie = Button(self.fenetreMenu, text= "NOUVELLE PARTIE", bg="black", fg= "white", width= 30, height= 2,command= self.Bouton_Nouvelle_Partie)
		self.canevas.create_window(380, 500, anchor='nw', window= bouton_nouvelle_partie)

		bouton_quitter = Button(self.fenetreMenu, text= "QUITTER", bg="black", fg= "white", width= 30, height= 2,command= self.fenetreMenu.destroy)
		self.canevas.create_window(380, 550, anchor='nw', window= bouton_quitter)

		self.centerWindow(width, height, self.fenetreMenu)

	# Définition de fonctionnement des boutons pour le jeu
	def BoutonLaunch(self):
		print("The button Launch was pressed!")

	def BoutonGo(self):
		print("The buttonm Go was pressed!")

	def BoutonMoin(self):
		print("-1 Ship")

	def BoutonPlus(self):
		print("+1 Ship")

	# Gestion de la sourir
	def MouseManeger(self, event): # LOOK: Dude.. fait un peu attention au francais ><
		X= int(event.x/32)
		Y= int(event.y/32)
		print("Position du Clic ->", X,',', Y) # LOOK: Oh et la fonction sert a rien.
                # LOOK: Devrait retourner un tuple.


	def AfficherJeuUI(self):
		self.fenetreJeu = Tk()
		self.fenetreJeu.title("Galax - Jeu")
		width= 1200     # LOOK: Magic numbers \o/
		height= 720

		########################################Panel Canevas#############################################
		panelCanevas = Frame(self.fenetreJeu, width= 1000, height= 650, bg= "lightgray")
		panelCanevas.grid(row= 0, sticky= N)

		self.canevas = Canvas(panelCanevas, width= 960, height=640, bd=-2, bg= "black")
		self.canevas.grid(padx= 5 ,pady= 5)

		self.imgJeu = PhotoImage(file= "imageSource/playScene.gif")
		self.canevas.create_image(0,0, image= self.imgJeu, anchor= NW)
		##################################################################################################


		##########################################Panel Info##############################################
		panelInfo = Frame(self.fenetreJeu, width= 230, height= 650, background= "darkgray")
		panelInfo.grid(row= 0, column= 1, sticky= N, rowspan= 2)

		panelNbPlanetPlayer = Frame(panelInfo, width= 220, height= 200, bg= "gray", relief= "sunken", bd= 3)
		panelNbPlanetPlayer.grid(row= 0, padx = 5, pady= 15)

		labelNbPlanetPlayer = Label(panelNbPlanetPlayer, text= "--- Nomber of planets ---", width= 29, bg= "black", fg= "white", relief= "raised", bd= 3)
		labelNbPlanetPlayer.grid(row= 0, column= 0, columnspan= 2)

		imgPlanetHumain = PhotoImage(file="imageSource/planetHumain.gif")
		labelImageHumain = Label(panelNbPlanetPlayer, image= imgPlanetHumain, bg= "gray")
		labelImageHumain.image = imgPlanetHumain
		labelImageHumain.grid(row= 1, column= 0, sticky= E, pady= 5)

		labelHumain = Label(panelNbPlanetPlayer, text= "Humain : ", bg="gray")
		labelHumain.grid(row= 1, column= 1, sticky= W, padx=5, pady= 8)

		imgPlanetGubru = PhotoImage(file="imageSource/planetGubru.gif")
		labelImageGubru = Label(panelNbPlanetPlayer, image= imgPlanetGubru, bg= "gray")
		labelImageGubru.image= imgPlanetGubru
		labelImageGubru.grid(row= 2, column= 0, sticky= E, pady= 5)

		labelGubru = Label(panelNbPlanetPlayer, text= "Gubru    : ", bg="gray")
		labelGubru.grid(row= 2, column= 1, sticky= W, padx=5, pady= 8)

		imgPlanetCzin = PhotoImage(file="imageSource/planetCzin.gif")
		labelImageCzin = Label(panelNbPlanetPlayer, image= imgPlanetCzin, bg="gray")
		labelImageCzin.image = imgPlanetCzin
		labelImageCzin.grid(row= 3, column= 0, sticky= E, pady= 5)

		labelCzin = Label(panelNbPlanetPlayer, text= "Czin       : ", bg="gray")
		labelCzin.grid(row= 3, column= 1, sticky= W, padx=5, pady= 8)

		panelAttaque = Frame(panelInfo, width= 220, height= 170, bg= "gray", relief= "sunken", bd= 3)
		panelAttaque.grid(row= 1, padx = 5, pady= 15)

		labelAttaque = Label(panelAttaque, text= "--- Attack ---", width= 29, bg= "black", fg= "white", relief= "raised", bd= 3)
		labelAttaque.grid(row= 0, column= 0, columnspan= 2)

		labelFrom = Label(panelAttaque, text= "From : ", bg= "gray")
		labelFrom.grid(row= 1, column= 0, sticky= W, padx= 10, pady= 10)

		labelTo = Label(panelAttaque, text= "To : ", bg= "gray")
		labelTo.grid(row= 1, column= 1, sticky= W, padx= 10, pady= 10)

		labelDistance = Label(panelAttaque, text= "Distance : ", bg= "gray")
		labelDistance.grid(row= 2, column= 0, sticky= W, padx= 10, pady= 10)

		labelTemps = Label(panelAttaque, text= "Temps : ", bg= "gray")
		labelTemps.grid(row= 2, column= 1, sticky= W, padx= 10, pady= 10)

		panelFlotte = Frame(panelInfo, width= 220, height= 200, bg= "gray", relief= "sunken", bd= 3)
		panelFlotte.grid(row= 2, padx = 5, pady= 15)

		labelFlotte = Label(panelFlotte, text= "--- Flect ---", width= 29, bg= "black", fg= "white", relief= "raised", bd= 3)
		labelFlotte.grid(row= 0)

		labelPort = Label(panelFlotte, text= "Port : ", bg= "gray")
		labelPort.grid(row= 1, sticky= W, padx= 10, pady= 8)

		labelTransit = Label(panelFlotte, text= "Transit : ", bg= "gray")
		labelTransit.grid(row= 2, sticky= W, padx= 10, pady= 8)

		labelAnnee = Label(panelInfo, text= "Year X", width= 23, height= 2, font=(14),bg= "black", fg= "white", relief= "raised", bd= 3)
		labelAnnee.grid(row= 3, padx = 5, pady= 15)

		panelStatus = Frame(panelInfo, width= 220, height= 134, bg= "black", relief= "sunken", bd= 3)
		panelStatus.grid(row= 4, padx = 5, pady= 31)
		##################################################################################################


		######################################Panel Boutons###############################################
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

		boutonGo = Button(panelBoutons, text= "Go", bg="black", fg= "white", width= 26, height= 3, command= self.BoutonGo)
		boutonGo.grid(row= 0, column= 3, padx= 5, pady= 7)
		##################################################################################################

		self.canevas.bind('<ButtonRelease-1>', self.MouseManeger)

		self.centerWindow(width, height, self.fenetreJeu)

                # LOOK:  OK COME THE FUCK ON seriously avec la fonction qui finit pas?

#Main
if __name__ == '__main__':
	v = VueGraphique()
	v.mainloop() 




