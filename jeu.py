import random
from personnage import Personnage
from donjon import Donjon
from monstres import gobelin, ogre, dragon
from joueur import Joueur, InterfaceUtilisateur

class Jeu:
    def __init__(self):
        self.personnage = None
        self.donjon = None
        self.joueur = None

    def initialiser(self, nom, classe):
        self.personnage = Personnage(nom, classe)
        self.donjon = Donjon(10)
        interface_utilisateur = InterfaceUtilisateur()
        self.joueur = Joueur(self.personnage, interface_utilisateur)

    def jouer(self):
        while True:
            commande = input("Entrez une commande (N, S, E, O) : ")
            if commande in ["N", "S", "E", "O"]:
                self.deplacer_personnage(commande)
            else:
                print("Commande invalide.")

    def deplacer_personnage(self, direction):
        x, y = self.personnage.position.x, self.personnage.position.y
        self.personnage.position.deplacer(direction)
        new_x, new_y = self.personnage.position.x, self.personnage.position.y

        if 0 <= new_x < self.donjon.taille and 0 <= new_y < self.donjon.taille:
            contenu = self.donjon.grille[new_y][new_x]
            print(f"Le personnage se déplace vers ({new_x}, {new_y}) et trouve : {contenu}")
            if contenu == "monstre":
                monstre = random.choice([gobelin, ogre, dragon])
                print(f"Un {monstre.nom} bloque votre chemin ! Vous devez le vaincre pour avancer.")
                self.combattre(monstre)
        else:
            print("Déplacement invalide. Vous ne pouvez pas sortir de la grille.")
            self.personnage.position.x, self.personnage.position.y = x, y  # Restaurer la position précédente

    def combattre(self, monstre):
        while self.personnage.statistiques.pv > 0 and monstre.pv > 0:
            self.joueur.jouer_tour(cible=monstre)

            if monstre.pv > 0:
                monstre.attaquer(self.personnage)

        if self.personnage.statistiques.pv > 0:
            print("Vous avez vaincu le monstre !")
        else:
            print("Vous avez été vaincu par le monstre...")
