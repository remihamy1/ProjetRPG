from jeu import Jeu

def main():
    jeu = Jeu()

    nom = input("Entrez le nom de votre personnage : ")

    print("Choisissez votre classe :")
    print("1. Guerrier")
    print("2. Mage")
    print("3. Voleur")

    choix_classe = input("Entrez le numéro de votre classe (1-3) : ")

    if choix_classe == "1":
        classe = "guerrier"
    elif choix_classe == "2":
        classe = "mage"
    elif choix_classe == "3":
        classe = "voleur"
    else:
        print("Choix invalide. Le jeu va se terminer.")
        return

    jeu.initialiser(nom, classe)

    print(f"Bienvenue, {nom} le {classe}! Votre aventure commence...")

    jeu.jouer()

if __name__ == '__main__':
    main()
