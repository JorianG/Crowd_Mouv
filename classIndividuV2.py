# coding: utf-8
from math import atan, cos, sin
import affichageV2 as aff
import time

nombre_element = 1
#__________________________________________________________________________________________#
class Individu:

    def __init__(self, x, y, vitesse, salle, nom,color):
        global nombre_element
        nombre_element += 1
        self.nom = nom
        self.positionX = x
        self.positionY = y
        self.positionPrecedenteX = x
        self.positionPrecedenteY = y
        self.vecteurArriveeX= 0
        self.vecteurArriveeY = 0
        self.positionDepart = (x, y)
        self.vitesse = vitesse
        self.droiteVerticale = False
        self.distance = None
        self.distanceArrivee(salle)
        self.arriveeX= salle.arrivee[0]
        self.arriveeY= salle.arrivee[1]
        self.coefDeplacementX = 0
        self.coefDeplacementY = 0
        self.r = 20
        salle.individus.append(self)
        self.valeur_canvas = nombre_element
        self.rond = aff.jeu.canvas.create_oval(self.positionX-self.r,self.positionY-self.r,self.positionX+self.r,self.positionY+self.r,width=1, outline="black",fill=color)

    def __repr__(self):
        return repr((self.nom, self.positionX, self.positionY, int(self.distance)))

    def estArrive(self, salle):
        
        if (self.positionPrecedenteX - self.arriveeX) * (self.positionX - self.arriveeX)  < 0 and (self.positionPrecedenteY - self.arriveeX) * (self.positionY - self.arriveeX):
            
            salle.individus.remove(self)
            print("Arrivée dépassée")
                
    def isStrait(self):
        if self.positionX == self.arriveeX:
            self.droiteVerticale = True
        if self.positionY == self.arriveeY:
            self.droiteVerticale = True

    def calculDeplacement(self):
        print (f' calculated {self.nom} at : x:{self.positionX} for vector {(self.arriveeX - self.positionX)} y:{self.positionY} for vector {(self.arriveeY - self.positionY)}')
        self.vecteurArriveeX = (self.arriveeX - self.positionX)
        self.vecteurArriveeY = (self.arriveeY - self.positionY)
        hypotenuse = (((self.vecteurArriveeX**2)+(self.vecteurArriveeY**2))**0.5)
        self.coefDeplacementX = (self.vecteurArriveeX * self.vitesse)/ hypotenuse
        self.coefDeplacementY = (self.vecteurArriveeY * self.vitesse) / hypotenuse
        print(f'delacement de {self.nom} : x:{self.coefDeplacementX} y:{self.coefDeplacementY}')
     

    def distanceArrivee(self, salle):
        """
        calcule la distance entre l'arrivee et l'individu
        In: salle
        Out: None
        """
        if self.droiteVerticale:
            self.distance = abs(salle.arrivee[1] - self.positionY)
        else:
            self.distance = ((salle.arrivee[0] - self.positionX) ** 2 + (salle.arrivee[1] - self.positionY) ** 2) ** 0.5

    
    #def collision(self, salle):
    #    return len(aff.jeu.canvas.find_overlapping(aff.jeu.canvas.coords(self.rond)[0], aff.jeu.canvas.coords(self.rond)[1], aff.jeu.canvas.coords(self.rond)[2], aff.jeu.canvas.coords(self.rond)[3])) > 1

    def collisions(self):
        overlap = aff.jeu.canvas.find_overlapping(aff.jeu.canvas.coords(self.rond)[0] + self.coefDeplacementX/100, aff.jeu.canvas.coords(self.rond)[1] + self.coefDeplacementY/100, aff.jeu.canvas.coords(self.rond)[2] + self.coefDeplacementX/100, aff.jeu.canvas.coords(self.rond)[3] + self.coefDeplacementY/100)
        return overlap[0]
        #return (len(overlap) > 1) or (1 in overlap and len(overlap) == 2)


#__________________________________________________________________________________________#

class Salle:
    def __init__(self):
        self.x = 800
        self.y = 400
        self.individus = []
        self.arrivee = (80, 0)
        self.r = 20
        self.aff = aff.jeu.canvas.create_oval(self.arrivee[0]-self.r,self.arrivee[1]-self.r,self.arrivee[0]+self.r,self.arrivee[1]+self.r,width=1, outline="red",fill="blue")
#__________________________________________________________________________________________#    
class Obstacles:
    def __init__(self, x, y):
        self.position = (x,y)

#__________________________________________________________________________________________#


def tour(salle):
    salle.individus = sorted(salle.individus, key = lambda individu: individu.distance, reverse = False)
    aff.jeu.nextRound(salle)
    #time.sleep(5)
    for individu in salle.individus:
        #overlap = aff.jeu.canvas.find_overlapping(aff.jeu.canvas.coords(individu.rond)[0] + individu.coefDeplacementX/100, aff.jeu.canvas.coords(individu.rond)[1] + individu.coefDeplacementY/100, aff.jeu.canvas.coords(individu.rond)[2] + individu.coefDeplacementX/100, aff.jeu.canvas.coords(individu.rond)[3] + individu.coefDeplacementY/100)
        if individu.collisions() != individu.valeur_canvas and individu.collisions() != 1:
            i = 0
            while salle.individus[i].valeur_canvas != individu.collisions():
                i += 1
            individu.vitesse = salle.individus[i].vitesse
            individu.calculDeplacement()
        
        individu.positionX += individu.coefDeplacementX
        individu.positionY += individu.coefDeplacementY
        individu.estArrive(salle)

        

'''
anciennePosition = individu.rond
aff.jeu.nextRound(individu, individu.position[0], individu.position[1])
if individu.collision(salle):
individu.rond = anciennePosition
'''


def initialisation(salle):
    for individu in salle.individus:
        individu.calculDeplacement()

def jeu(salle):
    initialisation(salle)
    while len(salle.individus) > 0:
        tour(salle)
        print(salle.individus)

"""
def ajouter_individus(x, y, vitesse, salle, nom,color):
    individu_nouveau = Individu(x, y, vitesse, salle, nom,color)
    nombre_element += 1
    salle.individus[individu_nouveau] = nombre_element
"""


#______________________TESTS_________________________#

salle = Salle()
cobaye = Individu(0, 300, 200, salle, "cobaye","red")
stagiaire = Individu(800, 600, 270, salle, "stagiaire","green")
Usain = Individu(440, 550, 1500, salle, "Usain","black")
Bob = Individu(300, 20, 110, salle, "Bob","black")
Dylan = Individu(721, 320, 175, salle, "Dylan","black")
Ana = Individu(320, 721, 175, salle, "Ana","black")
Polina = Individu(420, 420, 210, salle, "Polina","black")
Remi_Pages = Individu(333, 666, 751, salle, "Remi Pages","purple")
une_croute = Individu(30, 20, 11, salle, "une_croute","brown")
Jamel = Individu(10, 10, 10, salle, "Jamel","brown")
Usain = Individu(500, 560, 1500, salle, "Usain","black")



jeu(salle)
#salle.printNbIndividu()

