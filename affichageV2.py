from tkinter import *
import time

global root
root = Tk()


#__________________________________________________________________________________________#
class Simulation:
    def __init__(self):
        self.Largeur = 1000
        self.Hauteur = 1000


    def cree_fenetre(self):
        '''
        Cree la fenetre dans laquelle on veut afficher les individus
        In: None
        Out: None
        '''
        
        self.canvas=Canvas(root,width=self.Largeur,height=self.Hauteur,background="white")
        self.canvas.pack(side=LEFT, padx=5, pady=5)


    def nextRound(self,salle):
        '''
        Met a jour l'affichage des individus
        In: salle
        Out: None
        '''

        for i in range (200):
            salle.individus = sorted(salle.individus, key = lambda individu: individu.distance, reverse = False)
            for individu in salle.individus:
                x1 = self.canvas.coords(individu.rond)[0] + individu.coefDeplacementX/200
                y1 = self.canvas.coords(individu.rond)[1] + individu.coefDeplacementY/200
                x2 = self.canvas.coords(individu.rond)[2] + individu.coefDeplacementX/200
                y2 = self.canvas.coords(individu.rond)[3] + individu.coefDeplacementY/200
                overlap = self.canvas.find_overlapping(x1, y1, x2, y2)
                if (overlap[0] == individu.valeur_canvas or overlap[0] == 1):
                    self.canvas.move(individu.rond, individu.coefDeplacementX/200, individu.coefDeplacementY/200)
                self.canvas.update()
                time.sleep(1/100)
#__________________________________________________________________________________________#

simulation = Simulation()
simulation.cree_fenetre()