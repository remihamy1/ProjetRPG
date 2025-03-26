import random
from objet import Objet, Potion, Arme, Armure

class GenerateurDonjon:
    def __init__(self, taille):
        self.taille = taille

    def generer_grille(self):
        return [[self.generer_contenu() for _ in range(self.taille)] for _ in range(self.taille)]

    def generer_contenu(self):
        contenu = random.choice(['vide', 'monstre', 'trésor'])
        if contenu == 'trésor':
            return random.choice([
                Potion("Potion de soin", 20),
                Arme("Épée tranchante", 10),
                Arme("Hache de guerre", 15),
                Arme("Arc long", 8),
                Armure("Bouclier en fer", 5)
            ])
        return contenu

class GestionnaireDeplacement:
    def __init__(self, grille):
        self.grille = grille

    def deplacer_personnage(self, personnage, direction):
        personnage.position.deplacer(direction)
        x, y = personnage.position.x, personnage.position.y
        if 0 <= x < len(self.grille) and 0 <= y < len(self.grille):
            contenu = self.grille[y][x]
            if isinstance(contenu, Objet):
                print(f"Vous avez trouvé un {contenu.nom}!")
                if isinstance(contenu, (Arme, Armure, Potion)):
                    choix = input("Voulez-vous stocker l'objet dans l'inventaire ? (1 pour Oui, 2 pour Non) : ")
                    if choix == "1":
                        personnage.inventaire.ajouter(contenu)
                self.grille[y][x] = 'vide'
            elif contenu == "monstre":
                print("Un monstre bloque votre chemin ! Vous devez le vaincre pour avancer.")
        else:
            print("Déplacement invalide. Vous ne pouvez pas sortir de la grille.")

class Donjon:
    def __init__(self, taille):
        self.taille = taille
        self.generateur = GenerateurDonjon(taille)
        self.grille = self.generateur.generer_grille()
        self.gestionnaire_deplacement = GestionnaireDeplacement(self.grille)

    def deplacer_personnage(self, personnage, direction):
        self.gestionnaire_deplacement.deplacer_personnage(personnage, direction)
