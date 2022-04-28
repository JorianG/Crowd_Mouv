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
        
        if (self.positionPrecedenteX - self.arriveeX) * (self.positionX - self.arriveeX)  < 0 and (self.positionPrecedenteY - self.arriveeY) * (self.positionY - self.arriveeY) < 0:
            
            salle.individus.remove(self)
            aff.jeu.canvas.delete(self.rond)
            print("Arrivée dépassée" + self.nom)
                
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
        return overlap
        #return (len(overlap) > 1) or (1 in overlap and len(overlap) == 2)


#__________________________________________________________________________________________#

class Salle:
    def __init__(self):
        self.x = 600
        self.y = 800
        self.individus = []
        self.arrivee = (80, 0)
        self.r = 20
        self.aff = aff.jeu.canvas.create_oval(self.arrivee[0]-self.r,self.arrivee[1]-self.r,self.arrivee[0]+self.r,self.arrivee[1]+self.r,width=1, outline="red",fill="blue")
#__________________________________________________________________________________________#    
class Obstacles:
    def __init__(self, x, y):
        self.position = (x,y)

#__________________________________________________________________________________________#


"""
def tour(salle):
    salle.individus = sorted(salle.individus, key = lambda individu: individu.distance, reverse = False)
    #time.sleep(5)
    for individu in salle.individus:
        overlap = aff.jeu.canvas.find_overlapping(aff.jeu.canvas.coords(individu.rond)[0], aff.jeu.canvas.coords(individu.rond)[1], aff.jeu.canvas.coords(individu.rond)[2], aff.jeu.canvas.coords(individu.rond)[3])
        if not(1 in overlap and len(overlap) > 2):
        
            if overlap[0] != individu.valeur_canvas and overlap[0] != 1:
            #if individu.collisions()[0] != individu.valeur_canvas and not(int(1) in individu.collisions() and len(individu.collisions()) <v= 2):
                print(overlap)
                i = 0
                while i < len(salle.individus) and salle.individus[i].valeur_canvas != individu.collisions()[0]:
                    i += 1
                individu.vitesse = salle.individus[i].vitesse
                individu.calculDeplacement()
            
            individu.positionPrecedenteX = individu.positionX
            individu.positionPrecedenteY = individu.positionY
            individu.positionX += individu.coefDeplacementX
            individu.positionY += individu.coefDeplacementY
            individu.estArrive(salle)
    aff.jeu.nextRound(salle)
"""




def tour(salle):
    salle.individus = sorted(salle.individus, key = lambda individu: individu.distance, reverse = False)
    #time.sleep(5)
    aff.jeu.nextRound(salle)
    for individu in salle.individus:
        overlap = aff.jeu.canvas.find_overlapping(aff.jeu.canvas.coords(individu.rond)[0], aff.jeu.canvas.coords(individu.rond)[1], aff.jeu.canvas.coords(individu.rond)[2], aff.jeu.canvas.coords(individu.rond)[3])
        if not(1 in overlap and len(overlap) > 2):
        
            if overlap[0] != individu.valeur_canvas and overlap[0] != 1:
            #if individu.collisions()[0] != individu.valeur_canvas and not(int(1) in individu.collisions() and len(individu.collisions()) <v= 2):
                print(overlap)
                i = 0
                while i < len(salle.individus) and salle.individus[i].valeur_canvas != individu.collisions()[0]:
                    i += 1
                individu.vitesse = salle.individus[i].vitesse
                individu.calculDeplacement()
            
            individu.positionPrecedenteX = individu.positionX
            individu.positionPrecedenteY = individu.positionY
            individu.positionX += individu.coefDeplacementX
            individu.positionY += individu.coefDeplacementY
            individu.estArrive(salle)
        



def initialisation(salle):
    for individu in salle.individus:
        individu.calculDeplacement()

def jeu(salle):
    initialisation(salle)
    while len(salle.individus) > 0:
        tour(salle)
        print(salle.individus)




#______________________TESTS_________________________#

salle = Salle()
cobaye = Individu(0, 300, 200, salle, "cobaye","red")
stagiaire = Individu(800, 600, 270, salle, "stagiaire","green")
Usain = Individu(440, 550, 1500, salle, "Usain","black")
Bob = Individu(300, 20, 110, salle, "Bob","black")
Dylan = Individu(500, 320, 175, salle, "Dylan","black")
Ana = Individu(320, 721, 175, salle, "Ana","black")
Polina = Individu(420, 420, 210, salle, "Polina","black")
Remi_Pages = Individu(333, 666, 751, salle, "Remi Pages","purple")
Usain = Individu(500, 560, 1500, salle, "Usain","black")
Jacob = Individu(100, 400, 300, salle, "Jacob","black")
Paul = Individu(200, 200, 110, salle, "Paul","black")
Tim = Individu(500, 400, 300, salle, "Tim","black")


jeu(salle)
#salle.printNbIndividu()

