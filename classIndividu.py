# coding: utf-8
import affichage as aff

class Individu:

    def __init__(self, x, y, vitesse, salle):
        self.position = (x, y)
        self.vitesse = vitesse
        self.droiteVerticale = False
        self.coefDirect = None
        self.ordOrigine = None
        self.sens = None
        salle.individus.append(self)
    
    
    def droiteCheminNaif(self, Salle):
        '''
        In: salle
        Out: None
        '''
        #Salle.arrivee est un tuple avec les coords

        if self.position[0] == Salle.arrivee[0]:
            if self.position[1] == Salle.arrivee[1]:
                self.supprimer_individu()
            else:
                self.droiteVerticale = True
                if self.position[1] > Salle.arrivee[1]:
                    self.sens = -1
                else:
                    self.sens = 1
        else:
            #l'individu n'est pas sur l'arrivée
            self.coefDirect = (self.position[1] - Salle.arrivee[1]) / (self.position[0] - Salle.arrivee[0])
            self.ordOrigine = self.position[1] - (self.coefDirect*self.position[0])

            if self.position[0] > Salle.arrivee[0]:
                self.sens = -1
            else:
                self.sens = 1
            

    def deplacement(self):
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


class Salle:
    def __init__(self):
        self.x = 800
        self.y = 600
        self.individus = []
        self.arrivee = (0,0)
    
    def printNbIndividu(self):
        print(len(self.individus))
    
class Obstacles:
    def __init__(self, x, y):
        self.position = (x,y)
        self.mouvement = False



def tour(salle):
    for individu in salle.individus:
        individu.deplacement()
        individu.estArrive(salle)
        print(individu.position)

def jeu(salle):
    while len(salle.individus) > 0:
        tour(salle)
        print(salle.individus)

#______________________TESTS_________________________#

salle = Salle()
cobaye = Individu(400, 300, 100, salle)
stagiere = Individu(200, 400, 100, salle)


for individu in salle.individus:
    individu.droiteCheminNaif(salle)


jeu(salle)
#salle.printNbIndividu()


