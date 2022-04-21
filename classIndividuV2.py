# coding: utf-8

import affichage as aff


#__________________________________________________________________________________________#
class Individu:

    def __init__(self, x, y, vitesse, salle, nom,color):
        self.nom = nom
        self.positionX = x
        self.positionY = y
        self.position = (self.positionX, self.positionY)
        self.vitesse = vitesse
        self.droiteVerticale = False
        self.coefDirect = None
        self.ordOrigine = None
        self.sens = None
        self.distance = None
        self.distanceArrivee(salle)
        self.arriveeX= salle.arrivee[0]
        self.arriveeY= salle.arrivee[1]
        self.r = 10
        salle.individus.append(self)
        self.rond = aff.jeu.canvas.create_oval(self.positionX-self.r,self.positionY-self.r,self.positionX+self.r,self.positionY+self.r,width=1, outline="black",fill=color)

    def __repr__(self):
        return repr((self. nom, self.position, int(self.distance)))

    def estArrive(self, salle):
        if self.positionX == self.arriveeX and self.positionY == self.arriveeY:
            salle.individus.remove(self)
            print("Depassé arrivee")
                
    def isStrait(self):
        if self.positionX == self.arriveeX:
            self.droiteVerticale = True
        if self.positionY == self.arriveeY:
            self.droiteVerticale = True
        
    def deplacement(self):
        self.isStrait()
        if self.droiteVerticale == False:
            print (f' Indiv {self.nom} x:{self.positionX} for {(self.arriveeX - self.positionX)} y:{self.positionY} for {(self.arriveeY - self.positionY)}')

            self.positionX = (self.positionX + (self.arriveeX - self.positionX))
            self.positionX = (self.positionY + (self.arriveeY - self.positionY))

            self.position=(self.positionX,self.positionY)
            aff.jeu.nextRound(self)

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

    
    def collision(self, salle):
        return len(aff.jeu.canvas.find_overlapping(aff.jeu.canvas.coords(self.rond)[0], aff.jeu.canvas.coords(self.rond)[1], aff.jeu.canvas.coords(self.rond)[2], aff.jeu.canvas.coords(self.rond)[3])) > 1


#__________________________________________________________________________________________#

class Salle:
    def __init__(self):
        self.x = 800
        self.y = 400
        self.individus = []
        self.arrivee = (750, 0)
        self.r = 20
        self.aff = aff.jeu.canvas.create_oval(self.arrivee[0]-self.r,self.arrivee[1]-self.r,self.arrivee[0]+self.r,self.arrivee[1]+self.r,width=1, outline="red",fill="blue")
#__________________________________________________________________________________________#    
class Obstacles:
    def __init__(self, x, y):
        self.position = (x,y)

#__________________________________________________________________________________________#


def tour(salle):
    salle.individus = sorted(salle.individus, key = lambda individu: individu.distance, reverse = False)
    for individu in salle.individus:
        individu.deplacement()
        individu.distanceArrivee(salle)
        individu.estArrive(salle)
        

    '''
        anciennePosition = individu.rond
        aff.jeu.nextRound(individu, individu.position[0], individu.position[1])
        if individu.collision(salle):
            individu.rond = anciennePosition
        '''


def jeu(salle):
    while len(salle.individus) > 0:
        tour(salle)
        print(salle.individus)

#______________________TESTS_________________________#

salle = Salle()
cobaye = Individu(800, 400, 5, salle, "cobaye","red")
stagiaire = Individu(800, 0, 5, salle, "stagiaire","green")



jeu(salle)
#salle.printNbIndividu()

