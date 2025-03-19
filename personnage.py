class Monstre:
    def __init__(self, nom, pv, force, defense):
        self.nom = nom
        self.pv = pv
        self.force = force
        self.defense = defense

    def est_vivant(self):
        return self.pv > 0

    def attaquer(self, cible):
        degats = max(self.force - cible.defense, 1)
        cible.pv -= degats
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégâts.")

class Personnage:
    def __init__(self, nom, classe):
        self.nom = nom
        self.classe = classe
        self.pv = 0
        self.pm = 0
        self.force = 0
        self.intelligence = 0
        self.defense = 0
        self.resistance_magique = 0
        self.agilite = 0
        self.chance = 0
        self.endurance = 0
        self.esprit = 0
        self.inventaire = []
        self.initialiser_statistiques()

    def initialiser_statistiques(self):
        if self.classe == "guerrier":
            self.pv = 150
            self.pm = 50
            self.force = 15
            self.intelligence = 5
            self.defense = 12
            self.resistance_magique = 6
            self.agilite = 8
            self.chance = 5
            self.endurance = 10
            self.esprit = 4
        elif self.classe == "mage":
            self.pv = 90
            self.pm = 150
            self.force = 4
            self.intelligence = 15
            self.defense = 5
            self.resistance_magique = 12
            self.agilite = 7
            self.chance = 6
            self.endurance = 5
            self.esprit = 10
        elif self.classe == "voleur":
            self.pv = 110
            self.pm = 70
            self.force = 10
            self.intelligence = 7
            self.defense = 8
            self.resistance_magique = 7
            self.agilite = 15
            self.chance = 12
            self.endurance = 7
            self.esprit = 6

    def est_vivant(self):
        return self.pv > 0

    def attaquer(self, cible):
        degats = max(self.force - cible.defense, 1)
        cible.pv -= degats
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégâts.")

    def __str__(self):
        return (f"Personnage: {self.nom}\n"
                f"Classe: {self.classe}\n"
                f"Points de Vie (PV): {self.pv}\n"
                f"Points de Mana (PM): {self.pm}\n"
                f"Force: {self.force}\n"
                f"Intelligence: {self.intelligence}\n"
                f"Défense: {self.defense}\n"
                f"Résistance Magique: {self.resistance_magique}\n"
                f"Agilité: {self.agilite}\n"
                f"Chance: {self.chance}\n"
                f"Endurance: {self.endurance}\n"
                f"Esprit: {self.esprit}\n"
                f"Inventaire: {self.inventaire}")

def creation_personnage(nom, classe):
    if len(nom) < 1 or len(nom) > 20:
        raise ValueError("Le nom doit avoir entre 1 et 20 caractères.")
    return Personnage(nom, classe)
