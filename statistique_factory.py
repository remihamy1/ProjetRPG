from statistiques import Statistiques

class StatistiquesFactory:
    @staticmethod
    def creer_statistiques(classe):
        if classe == "guerrier":
            return Statistiques(150, 50, 15, 5, 12, 6, 8, 5, 10, 4)
        elif classe == "mage":
            return Statistiques(90, 150, 4, 15, 5, 12, 7, 6, 5, 10)
        elif classe == "voleur":
            return Statistiques(110, 70, 10, 7, 8, 7, 15, 12, 7, 6)
        else:
            raise ValueError("Classe invalide")
