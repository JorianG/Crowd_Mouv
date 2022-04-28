from operator import le
from tkinter import *
import time
global root

root = Tk()
class jeu:
    '''
    La classe jeu permet de creer la fenetre dans laquelle on affichera les balles du jeu.
    Les balles presentes dans le jeu sont listees dans la liste self.balles.
    '''
    def __init__(self):
        self.Largeur = 900
        self.Hauteur = 700

    def cree_fenetre(self):
        '''
        Cree la fenetre dans laquelle on veut afficher les balles
        In: self
        Out: cree un fenetre
        '''
        self.canvas=Canvas(root,width=self.Largeur,height=self.Hauteur,background="white")
        self.canvas.pack(side=LEFT, padx=5, pady=5)

    
    '''
    def nextRound(self,salle):

            #print(f'rendeding  {individu.nom } at {newX, newY}')
            #self.canvas.move(individu.rond, newX, newY)
            """for individu in salle.individus:
                #print(f' for {individu.nom} : {self.canvas.find_overlapping(self.canvas.coords(individu.rond)[0], self.canvas.coords(individu.rond)[1], self.canvas.coords(individu.rond)[2], self.canvas.coords(individu.rond)[3])}')
                print(f'corrd for {individu.nom} : {self.canvas.coords(individu.rond)[0],self.canvas.coords(individu.rond)[1], self.canvas.coords(individu.rond)[2], self.canvas.coords(individu.rond)[3]}')"""
            for i in range (100):
                for individu in salle.individus:
                    
                    x1 = individu.positionPrecedenteX - individu.r + individu.coefDeplacementX
                    y1 = individu.positionPrecedenteY - individu.r + individu.coefDeplacementY
                    x2 = individu.positionPrecedenteY + individu.r + individu.coefDeplacementX
                    y2 = individu.positionPrecedenteY + individu.r + individu.coefDeplacementY
                    overlap = self.canvas.find_overlapping(x1, y1, x2, y2)
                    if len(overlap) == 1 or (1 in overlap and len(overlap) == 2):
                    #if overlap[0] == individu.valeur_canvas or overlap[0] == 1:
                        self.canvas.move(individu.rond, individu.coefDeplacementX/100, individu.coefDeplacementY/100)
                    self.canvas.update()
                    time.sleep(1/50)
    '''

    def nextRound(self,salle):

            #print(f'rendeding  {individu.nom } at {newX, newY}')
            #self.canvas.move(individu.rond, newX, newY)
            """for individu in salle.individus:
                #print(f' for {individu.nom} : {self.canvas.find_overlapping(self.canvas.coords(individu.rond)[0], self.canvas.coords(individu.rond)[1], self.canvas.coords(individu.rond)[2], self.canvas.coords(individu.rond)[3])}')
                print(f'corrd for {individu.nom} : {self.canvas.coords(individu.rond)[0],self.canvas.coords(individu.rond)[1], self.canvas.coords(individu.rond)[2], self.canvas.coords(individu.rond)[3]}')"""
            for i in range (100):
                for individu in salle.individus:
                    
                    x1 = self.canvas.coords(individu.rond)[0] + individu.coefDeplacementX/100
                    y1 = self.canvas.coords(individu.rond)[1] + individu.coefDeplacementY/100
                    x2 = self.canvas.coords(individu.rond)[2] + individu.coefDeplacementX/100
                    y2 = self.canvas.coords(individu.rond)[3] + individu.coefDeplacementY/100
                    overlap = self.canvas.find_overlapping(x1, y1, x2, y2)
                    #if len(overlap) == 1 or (1 in overlap and len(overlap) == 2):
                    if overlap[0] == individu.valeur_canvas or overlap[0] == 1:
                        self.canvas.move(individu.rond, individu.coefDeplacementX/100, individu.coefDeplacementY/100)
                    self.canvas.update()
                    time.sleep(1/50)



jeu = jeu()
jeu.cree_fenetre()


