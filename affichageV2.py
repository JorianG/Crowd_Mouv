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

    
    def nextRound(self,individu):
            newX = individu.vecteurArriveeX
            newY = individu.vecteurArriveeY

            print(f'rendeding  {individu.nom } at {newX, newY}')
            #self.canvas.move(individu.rond, newX, newY)
            for i in range (100):
                self.canvas.move(individu.rond, (newX/100), newY/100)
                self.canvas.update()
                time.sleep(1/50)

    def nouvelle_pos(self, individu):
        self.canvas.move(individu.rond, individu.positionX, individu.positionY)
        self.canvas.update()


jeu = jeu()
jeu.cree_fenetre()


