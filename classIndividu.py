# coding: utf-8

class Individu:

    def __init__(self, x, y, vitesse):
        self.position= (x, y)
        self.vitesse = vitesse
        self.droiteVerticale= False
        self.coefDirect = None
        self.ordOrigine = None
        self.sens= None
        salle.individus.append(self)
    
    
    def droiteCheminNaif(self, Salle):
        '''
        
        In: 
        Out: 
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
    
    def supprimer_individu(self, Salle):
        '''
        OK
        Supprime l'individu de la liste des individu de la classe Salle
        In: jeu
        Out: None
        '''
        if len(Salle.individus) != 0:   

            for i in range (len(Salle.individus)):
                if Salle.individus[i]==self:
                    Salle.individus.pop(i)
                    break
            

    def deplacement(self):
        '''

        In: None
        Out: None
        '''
        if not(self.droiteVerticale):
            x = self.position[0] + self.sens * self.vitesse
            y = self.coefDirect * x + self.ordOrigine
            self.position = (x,y)
            
        else:
            y = self.position[1] + self.sens * self.vitesse
            self.position = (self.position[0], y)


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



#______________________TESTS_________________________#

salle = Salle()
cobaye = Individu(10, 10, 1)

cobaye.droiteCheminNaif(salle)

def jeu():
    if cobaye.droiteVerticale == True:
        if cobaye.sens == 1:
            while cobaye.position[1] < salle.arrivee[1]:
                cobaye.deplacement()
                print(cobaye.position)
        else:
            while cobaye.position[1] > salle.arrivee[1]:
                cobaye.deplacement()
                print(cobaye.position)
    else:   
        if cobaye.sens == 1:
            while cobaye.position[0] < salle.arrivee[0]:
                cobaye.deplacement()
                print(cobaye.position)
        else:
            while cobaye.position[0] > salle.arrivee[0]:
                cobaye.deplacement()
                print(cobaye.position)

jeu()
salle.printNbIndividu()