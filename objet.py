class Objet:
    def __init__(self, nom, type_objet):
        self.nom = nom
        self.type_objet = type_objet

    def utiliser(self, personnage):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes.")

    def __str__(self):
        return f"{self.nom} ({self.type_objet})"

    def __repr__(self):
        return self.__str__()

class Potion(Objet):
    def __init__(self, nom, valeur):
        super().__init__(nom, "potion")
        self.valeur = valeur

    def utiliser(self, personnage):
        personnage.statistiques["PV"] += self.valeur
        print(f"{personnage.nom} utilise {self.nom} et récupère {self.valeur} PV.")

class Arme(Objet):
    def __init__(self, nom, degats):
        super().__init__(nom, "arme")
        self.degats = degats

    def utiliser(self, personnage):
        personnage.statistiques["Force"] += self.degats
        print(f"{personnage.nom} équipe {self.nom} et augmente sa force de {self.degats}.")

class Armure(Objet):
    def __init__(self, nom, defense):
        super().__init__(nom, "armure")
        self.defense = defense

    def utiliser(self, personnage):
        personnage.statistiques["Défense"] += self.defense
        print(f"{personnage.nom} équipe {self.nom} et augmente sa défense de {self.defense}.")

potion_soin = Potion("Potion de soin", 20)
epee = Arme("Épée tranchante", 10)
hache = Arme("Hache de guerre", 15)
arc = Arme("Arc long", 8)
bouclier = Armure("Bouclier en fer", 5)
