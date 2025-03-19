import random
from personnage import Personnage
from donjon import Donjon
from monstres import gobelin, ogre, dragon
from joueur import Joueur

class Jeu:
    def __init__(self):
        self.personnage = None
        self.donjon = None
        self.joueur = None

    def initialiser(self, nom, classe):
        self.personnage = Personnage(nom, classe)
        self.personnage.position = (0, 0)  
        self.donjon = Donjon(10)
        self.joueur = Joueur(self.personnage)

    def jouer(self):
        while True:
            commande = input("Entrez une commande (N, S, E, O) : ")
            if commande in ["N", "S", "E", "O"]:
                self.deplacer_personnage(commande)
            else:
                print("Commande invalide.")

    def deplacer_personnage(self, direction):
        x, y = self.personnage.position
        if direction == "N":
            y -= 1
        elif direction == "S":
            y += 1
        elif direction == "E":
            x += 1
        elif direction == "O":
            x -= 1

        if 0 <= x < self.donjon.taille and 0 <= y < self.donjon.taille:
            contenu = self.donjon.grille[y][x]
            print(f"Le personnage se déplace vers ({x}, {y}) et trouve : {contenu}")
            if contenu == "monstre":
                monstre = random.choice([gobelin, ogre, dragon])
                print(f"Un {monstre.nom} bloque votre chemin ! Vous devez le vaincre pour avancer.")
                self.combattre(monstre)
            self.personnage.position = (x, y)
        else:
            print("Déplacement invalide. Vous ne pouvez pas sortir de la grille.")

    def combattre(self, monstre):
        while self.personnage.statistiques["PV"] > 0 and monstre.pv > 0:
            self.joueur.choisir_action(cible=monstre)

            if monstre.pv > 0:
                monstre.attaquer(self.personnage)

        if self.personnage.statistiques["PV"] > 0:
            print("Vous avez vaincu le monstre !")
        else:
            print("Vous avez été vaincu par le monstre...")
