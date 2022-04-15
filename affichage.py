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

    
    def nextRound(self,salle):

        for individu in salle.individus:
            newX,newY=individu.position
            #self.canvas.move(individu.rond, newX, newY)
            for i in range (50):
                self.canvas.move(individu.rond, -newX/50, -newY/50)
                self.canvas.update()
                time.sleep(1/70)


jeu = jeu()
jeu.cree_fenetre()

