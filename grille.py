class Grille:
    def __init__(self, taille):
        self.taille = taille
        self.cases = [[None for _ in range(taille)] for _ in range(taille)]

    def obtenir_case(self, x, y):
        if 0 <= x < self.taille and 0 <= y < self.taille:
            return self.cases[x][y]
        return None
