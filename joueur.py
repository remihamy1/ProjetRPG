class InterfaceUtilisateur:
    def choisir_action(self):
        print("Choisissez une action :")
        print("1. Attaquer")
        print("2. Défendre")
        print("3. Utiliser un objet")
        print("4. Afficher l'inventaire")
        return input("Entrez le numéro de l'action (1-3) : ")

class Joueur:
    def __init__(self, personnage, interface_utilisateur):
        self.personnage = personnage
        self.interface_utilisateur = interface_utilisateur

    def jouer_tour(self, cible=None):
        while True:
            choix_action = self.interface_utilisateur.choisir_action()
            if choix_action == "1":
                if cible is None:
                    print("Aucune cible à attaquer.")
                else:
                    self.personnage.attaquer(cible)
                break
            elif choix_action == "2":
                self.personnage.defendre()
                break
            elif choix_action == "3":
                self.utiliser_objet()
                break
            elif choix_action == "4":
                if not self.personnage.inventaire.contenu:
                    print("Votre inventaire est vide ! Bonne chance hehe.")
                else:
                    self.personnage.inventaire.afficher()
            else:
                print("Choix invalide.")

    def utiliser_objet(self):
        if not self.personnage.inventaire.contenu:
            print("Votre inventaire est vide.")
            return

        self.personnage.inventaire.afficher()
        choix = int(input("Choisissez l'objet à utiliser (numéro) : ")) - 1
        if 0 <= choix < len(self.personnage.inventaire.contenu):
            objet = self.personnage.inventaire.retirer(choix)
            print(f"Vous utilisez {objet.nom}.")
            objet.utiliser(self.personnage)
        else:
            print("Choix invalide.")
