from personnage import creation_personnage, Monstre

def simuler_combat(personnage, monstre):
    print(f"Un combat commence entre {personnage.nom} et {monstre.nom}!")
    while personnage.est_vivant() and monstre.est_vivant():
        personnage.attaquer(monstre)
        if not monstre.est_vivant():
            print(f"{monstre.nom} a été vaincu!")
            break
        monstre.attaquer(personnage)
        if not personnage.est_vivant():
            print(f"{personnage.nom} a été vaincu!")
            break

def main():
    nom = input("Nommez votre personnage : ")
    while len(nom) < 1 or len(nom) > 20:
        nom = input("Le nom doit avoir entre 1 et 20 caractères. Réessayez : ")

    choix_classe = input("Choisissez votre classe (1. Guerrier, 2. Mage, 3. Voleur) : ")
    while choix_classe not in ["1", "2", "3"]:
        choix_classe = input("Veuillez entrer un chiffre entre 1 et 3 : ")

    classes = {
        "1": "guerrier",
        "2": "mage",
        "3": "voleur"
    }

    classe = classes[choix_classe]
    personnage = creation_personnage(nom, classe)
    print(personnage)

    monstre = Monstre("Gobelin", 20, 5, 2)  

    simuler_combat(personnage, monstre)

if __name__ == "__main__":
    main()
