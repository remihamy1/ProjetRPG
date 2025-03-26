class Inventaire:
    def __init__(self):
        self.contenu = []

    def ajouter(self, objet):
        self.contenu.append(objet)

    def retirer(self, index):
        return self.contenu.pop(index)

    def afficher(self):
        for index, objet in enumerate(self.contenu):
            print(f"{index + 1}: {objet.nom}")
