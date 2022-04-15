# coding: utf-8
from msilib.schema import SelfReg
from pickle import NEWOBJ_EX
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
        self.r = 10
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
            self.coefDirect = (Salle.arrivee[1] - self.position[1]) / (Salle.arrivee[0] - self.position[0])
            self.ordOrigine = self.position[1] - (self.coefDirect*self.position[0])

            if self.position[0] > Salle.arrivee[0]:
                self.sens = -1
            else:
                self.sens = 1
            
    '''
    def deplacement(self, salle):
        
        In: None
        Out: None
        
        if not(self.droiteVerticale):
            x = self.position[0] + self.sens * self.vitesse
            y = self.coefDirect * x + self.ordOrigine
            self.position = (x,y)
            
        else:
            y = self.position[1] + self.sens * self.vitesse
            self.position = (self.position[0], y)
        self.distanceArrivee(salle)
    '''
    def deplacement(self, salle):
        self.droiteCheminNaif(salle)
        print(self.coefDirect)
        v = self.vitesse
        deltaM = v/10
        distMin = self.distanceMinimale(salle)
        i = 0
        newX = 0
        newY = 0
        while distMin > self.r*2 and  i < 10 :
            newX = ((deltaM**2)/self.coefDirect**2+1)**1/2
            newY = self.coefDirect*newX
            i+=1
        self.position= (self.position[0] + newX, self.position[1] + newY)

    def distanceMinimale(self, salle):
        mini = 100000
        for individu in salle.individus[:salle.individus.index(self)]:
            dist = ((self.position[0] - individu.position[0])**2 + (self.position[1] - individu.position[1])**2) ** 1/2
            if dist < mini:
                mini = dist
        #print(mini)
        return mini

    def estArrive(self, salle):
        if self.droiteVerticale:
            if self.sens == 1:
                if self.position[1] >= salle.arrivee[1]:
                    salle.individus.remove(self)
                    print("1")
            else:
                if self.position[1] <= salle.arrivee[1]:
                    salle.individus.remove(self)
                    print("2")
        else:   
            if self.sens == 1:
                if self.position[0] >= salle.arrivee[0]:
                    salle.individus.remove(self)
                    print("3")
                    print()
            else:
                if self.position[0] <= salle.arrivee[0]:
                    salle.individus.remove(self)
                    print("Depassé arrivee")


    def distanceArrivee(self, salle):
        """
        calcule la distance entre l'arrivee et l'individu
        In: salle
        Out: None
        """
        if self.droiteVerticale:
            self.distance = abs(salle.arrivee[1] - self.position[1])
        else:
            self.distance = ((salle.arrivee[0] - self.position[0]) ** 2 + (salle.arrivee[1] - self.position[1]) ** 2) ** 0.5

    
    def collision(self, salle):
        return len(aff.jeu.canvas.find_overlapping(aff.jeu.canvas.coords(self.rond)[0], aff.jeu.canvas.coords(self.rond)[1], aff.jeu.canvas.coords(self.rond)[2], aff.jeu.canvas.coords(self.rond)[3])) > 1


#__________________________________________________________________________________________#

class Salle:
    def __init__(self):
        self.x = 800
        self.y = 600
        self.individus = []
        self.arrivee = (400, 100)
        self.r = 20
        self.aff = aff.jeu.canvas.create_oval(self.arrivee[0]-self.r,self.arrivee[1]-self.r,self.arrivee[0]+self.r,self.arrivee[1]+self.r,width=1, outline="red",fill="blue")
#__________________________________________________________________________________________#    
class Obstacles:
    def __init__(self, x, y):
        self.position = (x,y)

#__________________________________________________________________________________________#


def tour(salle):
    print(salle.individus)
    salle.individus = sorted(salle.individus, key = lambda individu: individu.distance, reverse = False)
    for individu in salle.individus:
        individu.deplacement(salle)
        individu.distanceArrivee(salle)
        individu.estArrive(salle)
    aff.jeu.nextRound(salle)
    '''
        anciennePosition = individu.rond
        aff.jeu.nextRound(individu, individu.position[0], individu.position[1])
        if individu.collision(salle):
            individu.rond = anciennePosition
        '''


def jeu(salle):
    while len(salle.individus) > 0:
        tour(salle)

#______________________TESTS_________________________#

salle = Salle()
cobaye = Individu(800, 400, 1, salle, "cobaye")
stagiaire = Individu(800, 0, 1, salle, "stagiaire")


for individu in salle.individus:    
    individu.droiteCheminNaif(salle)


jeu(salle)
#salle.printNbIndividu()

