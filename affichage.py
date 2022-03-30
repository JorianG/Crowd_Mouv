from tkinter import *
import time
global root
global indice

root = Tk()
class jeu:
    '''
    La classe jeu permet de creer la fenetre dans laquelle on affichera les balles du jeu.
    Les balles presentes dans le jeu sont listees dans la liste self.balles.
    '''
    def __init__(self):
        self.Largeur = 800
        self.Hauteur = 600

    def cree_fenetre(self):
        '''
        Cree la fenetre dans laquelle on veut afficher les balles
        In: self
        Out: cree un fenetre
        '''
        self.canvas=Canvas(root,width=self.Largeur,height=self.Hauteur,background="white")
        self.canvas.pack(side=LEFT, padx=5, pady=5)
    
    def nextRound(self,Individu,newX, newY):
        r=15
        x,y=Individu.position
        nbOfSteps = 30
        #rond = self.canvas.create_oval(x-r,y-r,x+r,y+r,width=1, outline="red",fill="red")
        for i in range (nbOfSteps):
            self.canvas.move(Individu.rond, -newX/nbOfSteps, -newY/nbOfSteps)
            self.canvas.update()
            time.sleep(1/nbOfSteps)


    
    def __str__(self) -> str:
        x = ""
        for i in range (len(self.balles)):
            x+= " "
            x+= str(self.balles[i].taille)
        return x

jeu = jeu()
jeu.cree_fenetre()
