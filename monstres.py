class Monstre:
    def __init__(self, nom, pv, force):
        self.nom = nom
        self.pv = pv
        self.force = force

    def attaquer(self, cible):
        degats = self.force
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégâts.")
        cible.subir_degats(degats)

    def subir_degats(self, degats):
        self.pv -= degats
        print(f"{self.nom} subit {degats} dégâts et a maintenant {self.pv} PV.")
        if self.pv <= 0:
            print(f"{self.nom} est vaincu !")

gobelin = Monstre("Gobelin", 50, 10)
ogre = Monstre("Ogre", 100, 20)
dragon = Monstre("Dragon", 200, 30)
