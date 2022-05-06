import affichageV2 as aff

nombre_element = 1
#__________________________________________________________________________________________#
class Individu:
    def __init__(self, x, y, vitesse, salle, nom, color):
        global nombre_element
        nombre_element += 1
        self.nom = nom
        self.positionX = x
        self.positionY = y
        self.positionDepartX = x
        self.positionDepartY = y
        self.vitesse = vitesse
        self.distance = None
        self.distanceArrivee(salle)
        self.coefDeplacementX = 0
        self.coefDeplacementY = 0
        self.r = 20
        self.valeur_canvas = nombre_element
        self.rond = aff.simulation.canvas.create_oval(self.positionX-self.r, self.positionY-self.r, self.positionX+self.r, self.positionY+self.r, width=1, outline="black", fill=color)
        
        for individu in salle.individus:
            assert ((self.positionX - individu.positionX) ** 2 + (self.positionY - individu.positionY) ** 2) ** 0.5 > 2 * self.r, f"L'individu {self} est en collision avec l'individu {individu}"
        assert(0 < self.positionX - self.r and self.positionX + self.r < salle.x and 0 < self.positionY - self.r and self.positionY + self.r < salle.y), f"l'individu {self} n'est pas dans la salle."
        salle.individus.append(self)

    def __repr__(self):
        '''
        In: None
        Out: Renvoie une represation de l'objet, que l'on peut afficher.
        '''
        
        return repr((self.nom, self.positionX, self.positionY, int(self.distance)))


    def estArrive(self, salle):
        '''
        Supprime l'individu de la liste des individus et du canvas s'il a depasse la sortie.
        In: objet salle
        Out: None
        '''

        if (self.positionDepartX - salle.arriveeX) * (self.positionX - salle.arriveeX)  < 0 and (self.positionDepartY - salle.arriveeY) * (self.positionY - salle.arriveeY) < 0:
            salle.individus.remove(self)
            aff.simulation.canvas.delete(self.rond)


    def calculDeplacement(self, salle):
        '''
        Modifie les attributs coefDeplacementX, coefDeplacementY de l'individu.
        In: objet salle
        Out: None
        '''
        
        vecteurArriveeX = (salle.arriveeX - self.positionX)
        vecteurArriveeY = (salle.arriveeY - self.positionY)
        hypotenuse = (((vecteurArriveeX ** 2) + (vecteurArriveeY ** 2)) ** 0.5)
        self.coefDeplacementX = (vecteurArriveeX * self.vitesse) / hypotenuse
        self.coefDeplacementY = (vecteurArriveeY * self.vitesse) / hypotenuse
        
    
    def distanceArrivee(self, salle):
        '''
        calcule la distance entre l'arrivee et l'individu
        In: objet salle
        Out: None
        '''
        
        self.distance = ((salle.arriveeX - self.positionX) ** 2 + (salle.arriveeY - self.positionY) ** 2) ** 0.5

#__________________________________________________________________________________________#

class Salle:
    def __init__(self, arriveeX, arriveeY):
        self.x = aff.simulation.Largeur - 100
        self.y = aff.simulation.Hauteur - 100
        self.individus = []
        self.arriveeX = arriveeX
        self.arriveeY = arriveeY
        self.r = 20
        self.aff = aff.simulation.canvas.create_oval(self.arriveeX - self.r, self.arriveeY - self.r, self.arriveeX + self.r, self.arriveeY + self.r, width=1 , outline="red" , fill="blue")


#__________________________________________________________________________________________#


def tour(salle):
    '''
    deplace chaque individu de la salle d'une distance correspondant a sa vitesse
    appel de la fonction nextRound() , de la classe Simulation du fichier affichage
    In: objet salle
    Out: None
    '''
    
    salle.individus = sorted(salle.individus, key = lambda individu: individu.distance, reverse = False)
    aff.simulation.nextRound(salle)
    for individu in salle.individus:
        individu.positionX = aff.simulation.canvas.coords(individu.rond)[0] - individu.r
        individu.positionY = aff.simulation.canvas.coords(individu.rond)[1] - individu.r
        individu.estArrive(salle)
        

def jeu(salle):
    '''
    Fonction principale, permettant d'executer le programme.
    In: objet salle
    Out: None
    '''
    
    for individu in salle.individus:
        individu.calculDeplacement(salle)
    while len(salle.individus) > 0:
        tour(salle)

#______________________TESTS_________________________#

salle = Salle(80, 0)
cobaye = Individu(30, 300, 200, salle, "cobaye","black")
Usain = Individu(440, 550, 1500, salle, "Usain","black")
Bob = Individu(300, 30, 110, salle, "Bob","black")
Dylan = Individu(500, 320, 175, salle, "Dylan","black")
Ana = Individu(320, 721, 300, salle, "Ana","black")
Claude = Individu(420, 420, 210, salle, "Claude","black")
Usain = Individu(500, 560, 1500, salle, "Usain","black")
Jacob = Individu(100, 400, 300, salle, "Jacob","black")
Paul = Individu(200, 200, 110, salle, "Paul","black")
a1 = Individu(40, 50, 500, salle, "a1","black")
a3 = Individu(90, 175, 800, salle, "a3","black")
a4 = Individu(130, 200, 520, salle, "a4","black")
a5 = Individu(160, 235, 500, salle, "a5","black")
a6 = Individu(160, 110, 880, salle, "a6","black")
a7 = Individu(245, 400, 760, salle, "a7","black")
a8 = Individu(500, 480, 900, salle, "a8","black")
a9 = Individu(250, 30, 610, salle, "a9","black")
a10 = Individu(800, 30, 1050, salle, "a10","black")
a11 = Individu(490, 30, 2275, salle, "a11","black")
a12 = Individu(50, 400, 999, salle, "a12","black")
a13 = Individu(70, 600, 1084, salle, "a13","black")
a14 = Individu(800, 85, 950, salle, "a14","black")
a15 = Individu(90, 440, 667, salle, "a15","black")
a16 = Individu(790, 169, 785, salle, "a16","black")
a17 = Individu(320, 490, 1000, salle, "a17","black")
a18 = Individu(390, 600, 811, salle, "a18","black")
a19 = Individu(500, 200, 666, salle, "a19","black")
a20 = Individu(800, 380, 751, salle, "a20","black")
a21 = Individu(550, 470, 799, salle, "a21","black")
a22 = Individu(512, 600, 367, salle, "a22","black")
a23 = Individu(600, 500, 2129, salle, "a23","black")
a24 = Individu(600, 600, 932, salle, "a24","black")
a25 = Individu(700, 600, 842, salle, "a25","black")
a26 = Individu(800, 600, 1205, salle, "a26","black")

a27_SupprimezMoi = Individu(800, 600, 1205, salle, "a27_SupprimezMoi","red")


jeu(salle)