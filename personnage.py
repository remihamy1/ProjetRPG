class Personnage:
    def __init__(self, nom, classe):
        self.nom = nom
        self.classe = classe
        self.statistiques = self.initialiser_statistiques()
        self.inventaire = []
        self.position = (0, 0)  

    def initialiser_statistiques(self):
        if self.classe == "guerrier":
            return {"PV": 150, "PM": 50, "Force": 15, "Intelligence": 5, "Défense": 12, "Résistance Magique": 6, "Agilité": 8, "Chance": 5, "Endurance": 10, "Esprit": 4}
        elif self.classe == "mage":
            return {"PV": 90, "PM": 150, "Force": 4, "Intelligence": 15, "Défense": 5, "Résistance Magique": 12, "Agilité": 7, "Chance": 6, "Endurance": 5, "Esprit": 10}
        elif self.classe == "voleur":
            return {"PV": 110, "PM": 70, "Force": 10, "Intelligence": 7, "Défense": 8, "Résistance Magique": 7, "Agilité": 15, "Chance": 12, "Endurance": 7, "Esprit": 6}
        else:
            raise ValueError("Classe invalide")

    def valider_nom(self):
        if len(self.nom) < 3 or len(self.nom) > 20:
            raise ValueError("Nom invalide")

    def attaquer(self, cible):
        degats = self.statistiques["Force"]
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégâts.")
        cible.subir_degats(degats)

    def defendre(self):
        print(f"{self.nom} se défend et réduit les dégâts subis.")
        return self.statistiques["Défense"]

    def subir_degats(self, degats):
        self.statistiques["PV"] -= max(degats - self.defendre(), 0)
        print(f"{self.nom} subit {degats} dégâts et a maintenant {self.statistiques['PV']} PV.")
