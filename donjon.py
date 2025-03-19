import random
from objet import Objet, Potion, Arme, Armure

class Donjon:
    def __init__(self, taille):
        self.taille = taille
        self.grille = self.generer_grille()

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

    def deplacer_personnage(self, personnage, direction):
        x, y = personnage.position
        if direction == "N":
            y -= 1
        elif direction == "S":
            y += 1
        elif direction == "E":
            x += 1
        elif direction == "O":
            x -= 1

        if 0 <= x < self.taille and 0 <= y < self.taille:
            contenu = self.grille[y][x]
            if isinstance(contenu, Objet):
                print(f"Vous avez trouvé un {contenu.nom}!")
                personnage.inventaire.append(contenu)
                self.grille[y][x] = 'vide' 
            elif contenu == "monstre":
                print("Un monstre bloque votre chemin ! Vous devez le vaincre pour avancer.")
            personnage.position = (x, y)
        else:
            print("Déplacement invalide. Vous ne pouvez pas sortir de la grille.")
