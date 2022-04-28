# coding: utf-8
from math import atan, cos, sin
from re import A
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
    
    aff.jeu.nextRound(salle)
    for individu in salle.individus:
        overlap = aff.jeu.canvas.find_overlapping(aff.jeu.canvas.coords(individu.rond)[0], aff.jeu.canvas.coords(individu.rond)[1], aff.jeu.canvas.coords(individu.rond)[2], aff.jeu.canvas.coords(individu.rond)[3])
        individu.positionPrecedenteX = individu.positionX
        individu.positionPrecedenteY = individu.positionY
        individu.positionX = aff.jeu.canvas.coords(individu.rond)[0] - individu.r
        individu.positionY = aff.jeu.canvas.coords(individu.rond)[1] - individu.r
        '''
        if not(1 in overlap and len(overlap) > 2):
        
            if len(overlap) == 1 or (1 in overlap and len(overlap) == 2):
                individu.positionPrecedenteX = individu.positionX
                individu.positionPrecedenteY = individu.positionY
                individu.positionX += individu.coefDeplacementX
                individu.positionY += individu.coefDeplacementY
                individu.estArrive(salle)
            
            #if overlap[0] != individu.valeur_canvas and overlap[0] != 1:
            #if individu.collisions()[0] != individu.valeur_canvas and not(int(1) in individu.collisions() and len(individu.collisions()) <v= 2):
            
            else:
                print('Trop rapide')
                i = 0
                while i < len(salle.individus) and salle.individus[i].valeur_canvas != individu.collisions()[0]:
                    i += 1
                individu.vitesse = salle.individus[i].vitesse
                individu.calculDeplacement()
        '''
                
        



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
Claude = Individu(420, 420, 210, salle, "Claude","black")
Remi_Pages = Individu(333, 666, 751, salle, "Remi Pages","purple")
Usain = Individu(500, 560, 1500, salle, "Usain","black")
Jacob = Individu(100, 400, 300, salle, "Jacob","black")
Paul = Individu(200, 200, 110, salle, "Paul","black")
a1 = Individu(30, 50, 500, salle, "1","black")
#a2 = Individu(75, 150, 650, salle, "2","black")
a3 = Individu(90, 175, 800, salle, "3","black")
a4 = Individu(130, 200, 520, salle, "4","pink")
a5 = Individu(160, 235, 500, salle, "5","black")
a6 = Individu(160, 110, 880, salle, "6","black")
a7 = Individu(245, 400, 760, salle, "7","black")
a8 = Individu(500, 480, 900, salle, "8","black")
a9 = Individu(300, 0, 610, salle, "9","black")
a10 = Individu(800, 0, 1050, salle, "10","black")
a11 = Individu(490, 10, 2275, salle, "11","black")
a12 = Individu(50, 400, 999, salle, "12","black")
a13 = Individu(70, 600, 1084, salle, "13","black")
a14 = Individu(800, 0, 950, salle, "14","black")
a15 = Individu(120, 420, 667, salle, "15","black")
lelu = Individu(790, 169, 785, salle, "lélu","yellow")
a17 = Individu(320, 490, 1000, salle, "17","black")
a18 = Individu(390, 600, 811, salle, "18","black")
a19 = Individu(500, 300, 666, salle, "19","black")
a20 = Individu(800, 380, 751, salle, "20","black")
a21 = Individu(550, 470, 799, salle, "21","black")
a22 = Individu(500, 600, 367, salle, "22","black")
a23 = Individu(600, 500, 2129, salle, "23","black")
a24 = Individu(600, 600, 932, salle, "24","black")
a25 = Individu(700, 600, 842, salle, "25","black")
a26 = Individu(800, 600, 1205, salle, "26","black")




jeu(salle)
#salle.printNbIndividu()

