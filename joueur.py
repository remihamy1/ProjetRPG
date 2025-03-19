class Joueur:
    def __init__(self, personnage):
        self.personnage = personnage

    def choisir_action(self, cible=None):
        print("Choisissez une action :")
        print("1. Attaquer")
        print("2. Défendre")
        print("3. Utiliser un objet")
        print("4. Afficher l'inventaire")  # Ajout de cette option

        choix_action = input("Entrez le numéro de l'action (1-4) : ")

        if choix_action == "1":
            if cible is None:
                print("Aucune cible à attaquer.")
            else:
                self.personnage.attaquer(cible)
        elif choix_action == "2":
            self.personnage.defendre()
        elif choix_action == "3":
            self.utiliser_objet()
        elif choix_action == "4":
            self.afficher_inventaire()  # Appel de la méthode pour afficher l'inventaire
        else:
            print("Choix invalide.")

    def utiliser_objet(self):
        if not self.personnage.inventaire:
            print("Votre inventaire est vide.")
            return

        print("Objets dans votre inventaire :")
        for index, objet in enumerate(self.personnage.inventaire):
            print(f"{index + 1}: {objet.nom}")

        choix = int(input("Choisissez l'objet à utiliser (numéro) : ")) - 1
        if 0 <= choix < len(self.personnage.inventaire):
            objet = self.personnage.inventaire.pop(choix)
            print(f"Vous utilisez {objet.nom}.")
            objet.utiliser(self.personnage)
        else:
            print("Choix invalide.")

    def afficher_inventaire(self):
        if not self.personnage.inventaire:
            print("Votre inventaire est vide.")
        else:
            print("Objets dans votre inventaire :")
            for index, objet in enumerate(self.personnage.inventaire):
                print(f"{index + 1}: {objet.nom}")
