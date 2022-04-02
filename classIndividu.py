# coding: utf-8
from msilib.schema import SelfReg
import affichage as aff


#__________________________________________________________________________________________#
class Individu:

    def __init__(self, x, y, vitesse, salle, nom):
        self.nom = nom
        self.position = (x, y)
        self.vitesse = vitesse
        self.droiteVerticale = False
        self.coefDirect = None
        self.ordOrigine = None
        self.sens = None
        self.distance = None
        self.distanceArrivee(salle)
        self.r=15
        salle.individus.append(self)
        self.rond = aff.jeu.canvas.create_oval(self.position[0]-self.r,self.position[1]-self.r,self.position[0]+self.r,self.position[1]+self.r,width=1, outline="red",fill="red")
    

    def __repr__(self):
        return repr((self. nom, self.position, int(self.distance)))
    
    def droiteCheminNaif(self, Salle):
        '''
        In: salle
        Out: None
        '''
        #Salle.arrivee est un tuple avec les coords

        if self.position[0] == Salle.arrivee[0]:
            self.droiteVerticale = True
            if self.position[1] > Salle.arrivee[1]:
                self.sens = -1
            else:
                self.sens = 1
        else:
            self.coefDirect = (self.position[1] - Salle.arrivee[1]) / (self.position[0] - Salle.arrivee[0])
            self.ordOrigine = self.position[1] - (self.coefDirect*self.position[0])

            if self.position[0] > Salle.arrivee[0]:
                self.sens = -1
            else:
                self.sens = 1
            

    def deplacement(self, salle):
        '''

        In: None
        Out: None
        '''
        if not(self.droiteVerticale):
            x = self.position[0] + self.sens * self.vitesse
            y = self.coefDirect * x + self.ordOrigine
            #aff.jeu.nextRound(self,x,y)
            self.position = (x,y)
            
        else:
            y = self.position[1] + self.sens * self.vitesse
            #aff.jeu.nextRound(self,self.position[0], y)
            self.position = (self.position[0], y)
        #aff.jeu.nextRound(self, x, y)
        self.distanceArrivee(salle)

    def estArrive(self, salle):
        if self.droiteVerticale:
            if self.sens == 1:
                if self.position[1] >= salle.arrivee[1]:
                    salle.individus.remove(self)
            else:
                if self.position[1] <= salle.arrivee[1]:
                    salle.individus.remove(self)
        else:   
            if self.sens == 1:
                if self.position[0] >= salle.arrivee[0]:
                    salle.individus.remove(self)
            else:
                if self.position[0] <= salle.arrivee[0]:
                    salle.individus.remove(self)


    def distanceArrivee(self, salle):
        if self.droiteVerticale:
            self.distance = abs(salle.arrivee[1] - self.position[1])
        else:
            self.distance = ((salle.arrivee[0] - self.position[0]) ** 2 + (salle.arrivee[1] - self.position[1]) ** 2) ** 0.5


#__________________________________________________________________________________________#

class Salle:
    def __init__(self):
        self.x = 800
        self.y = 600
        self.individus = []
        self.arrivee = (0, 0)
#__________________________________________________________________________________________#    
class Obstacles:
    def __init__(self, x, y):
        self.position = (x,y)
        self.mouvement = False

#__________________________________________________________________________________________#


def tour(salle):
    salle.individus = sorted(salle.individus, key = lambda individu: individu.distance, reverse = False)
    print(salle.individus)
    for individu in salle.individus:
        individu.deplacement(salle)
        individu.distanceArrivee(salle)
        individu.estArrive(salle)
        


def jeu(salle):
    while len(salle.individus) > 0:
        tour(salle)

#______________________TESTS_________________________#

salle = Salle()
cobaye = Individu(800, 600, 100, salle, "cobaye")
stagiaire = Individu(400, 0, 25, salle, "stagiaire")


for individu in salle.individus:
    individu.droiteCheminNaif(salle)


jeu(salle)
#salle.printNbIndividu()

