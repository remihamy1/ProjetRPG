from statistique_factory import StatistiquesFactory
from inventaire import Inventaire
from position import Position

class Personnage:
    def __init__(self, nom, classe):
        self.nom = nom
        self.classe = classe
        self.statistiques = StatistiquesFactory.creer_statistiques(classe)
        self.inventaire = Inventaire()
        self.position = Position()

    def attaquer(self, cible):
        degats = self.statistiques.force
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégâts.")
        cible.subir_degats(degats)

    def defendre(self):
        print(f"{self.nom} se défend et réduit les dégâts subis.")
        return self.statistiques.defense

    def subir_degats(self, degats):
        self.statistiques.pv -= max(degats - self.defendre(), 0)
        print(f"{self.nom} subit {degats} dégâts et a maintenant {self.statistiques.pv} PV.")
