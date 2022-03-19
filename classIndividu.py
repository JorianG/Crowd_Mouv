# coding: utf-8

class Individu:

    def __init__(self, x, y):
        self.position= (x, y)
        self.coefDirect = None
        self.ordOrigine = None
        self.sens= None
        Salle.individu.append(self)
    
    
    def droiteCheminNaif(self, Individu, Salle.arrivee):
        #Salle.arrivee est un tuple avec les coords
        if Individu.position[0] == Salle.arrivee[0]:
            if Individu.position[1] == Salle.arrivee[1]:
                Individu.isDrawn == False
            else:
                #droite horizontale
                #TODO
                pass

        else:
            self.coefDirect = (Individu.position[1] - Salle.arrivee[1]) / (Individu.position[0] - Salle.arrivee[0])
            self.ordOrigine = Individu.position[1]-(self.coefDirect*Individu.position[0])
            if Individu.position[0] > Salle.arrivee[0]:
                self.sens = -1
            else:
                self.sens = 1
    
    def supprimer_balle(self,Salle):
        '''
        Supprime la balle de la liste des balles en jeu
        In: jeu
        Out: None
        '''
        if len(Salle.individu) != 0:    
            for i in range (len(Salle.individu)):
                if Salle.individu[i]==self:
                    Salle.individu.pop(i)
                    break
            

    def deplacement(self, vitesse):
        x = self.position[0] + self.sens * vitesse
        y = self.coefDirect * x + self.ordOrigine
        self.position = (x,y)

    def deplacementVertical(self, vitesse):
        y = self.position[1] + self.sens * vitesse
        self.position = (self.position[0], y)


class Salle:
    def __init__(self):
        self.x = 800
        self.y = 600
        self.individu = []
        self.arrivee = (0,300)
    
class Obstacles:
    def __init__(self, x, y):
        self.position = (x,y)
        self.mouvement = False