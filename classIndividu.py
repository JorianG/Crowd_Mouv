
class Individu:
    def __init__(self, x, y):
        self.position= (x, y)
        self.chemin = None 


class Salle:
    def __init__(self,longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

class Droites:
    def __init__(self):
        self.coefDirect = None
        self.ordOrigine = None
        
    def droiteCheminNaif(Individu, arrivee):
        #arrivee est un tuple avec les coords
        if Individu.position[0]== arrivee[0]:
            print("lol")
            #droite horizontale
        else:
            self.coefDirect = (Individu.position[1] - arrivee[1]) / (Individu.position[0] - arrivee[0])
            self.ordOrigine = Individu.position[1]-(coefDirect*Individu.position[0])
            if Individu.position[0] > arrivee[0]:
                self.sens= -1
            else:
                self.sens= 1

class Obstacles:
    def __init__(self, x, y):
        self.position = (x,y)
        self.mouvement = False