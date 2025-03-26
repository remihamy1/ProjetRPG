# Infractions aux Principes SOLID

## Single Responsibility Principle (SRP)

1. **Classe Personnage** (`personnage.py`)
   - Gère à la fois les caractéristiques, le mouvement et les actions
   - Mélange la logique de combat et la gestion des états
   - Responsable de sa propre création et de sa propre destruction
   ```python
   class Personnage:
       def __init__(self, nom, classe):
           self.nom = nom
           self.classe = classe
           self.statistiques = self.initialiser_statistiques()  # Responsabilité de création
           self.inventaire = []
           self.position = (0, 0)  

       def initialiser_statistiques(self):  # Responsabilité de configuration
           if self.classe == "guerrier":
               return {"PV": 150, "PM": 50, ...}
           elif self.classe == "mage":
               return {"PV": 90, "PM": 150, ...}
           # ...

       def attaquer(self, cible):  # Responsabilité de combat
           degats = self.statistiques["Force"]
           print(f"{self.nom} attaque {cible.nom}...")
           cible.subir_degats(degats)

       def valider_nom(self):  # Responsabilité de validation
           if len(self.nom) < 3 or len(self.nom) > 20:
               raise ValueError("Nom invalide")
   ```

2. **Classe Joueur** (`joueur.py`)
   - Gère à la fois la création et la configuration du joueur
   - Mélange la logique de gestion et la définition des caractéristiques
   - Responsable de la validation et de la création
   ```python
   class Joueur:
       def __init__(self, personnage):
           self.personnage = personnage

       def choisir_action(self, cible=None):  # Responsabilité d'interface utilisateur
           print("Choisissez une action :")
           print("1. Attaquer")
           # ...

       def utiliser_objet(self):  # Responsabilité de gestion d'inventaire
           if not self.personnage.inventaire:
               print("Votre inventaire est vide.")
               return
           # ...

       def afficher_inventaire(self):  # Responsabilité d'affichage
           if not self.personnage.inventaire:
               print("Votre inventaire est vide.")
           else:
               print("Objets dans votre inventaire :")
               # ...
   ```

## Open/Closed Principle (OCP)

1. **Système de Classes** (`classes.py`)
   - Modification nécessaire pour ajouter de nouvelles classes
   - Changement du code existant pour étendre les fonctionnalités
   - Couplage fort avec les implémentations concrètes

2. **Système de Combat** (`jeu.py`)
   - Modification nécessaire pour ajouter de nouveaux types d'attaques
   - Changement du code existant pour ajouter des effets
   - Couplage fort avec les mécaniques de combat

## Liskov Substitution Principle (LSP)

1. **Héritage des Personnages** (`personnage.py`, `joueur.py`)
   - Les sous-classes ne peuvent pas remplacer leur classe parente sans effets de bord
   - Violation des contrats de base dans les méthodes héritées
   - Comportements incohérents entre les classes parentes et enfants
   ```python
   class Personnage:
       def attaquer(self, cible):
           degats = self.statistiques["Force"]  # Précondition non respectée pour les mages
           cible.subir_degats(degats)

   class Joueur:
       def __init__(self, personnage):  # Couplage fort avec Personnage
           self.personnage = personnage
   ```

2. **Polymorphisme** (`monstres.py`, `objet.py`)
   - Les objets ne sont pas interchangeables sans modification du code
   - Les préconditions et postconditions ne sont pas respectées
   ```python
   def subir_degats(self, degats):
       self.statistiques["PV"] -= max(degats - self.defendre(), 0)  # Comportement non substituable
       print(f"{self.nom} subit {degats} dégâts...")
   ```

## Interface Segregation Principle (ISP)

1. **Interfaces Monolithiques** (`stats.py`)
   - Les interfaces forcent l'implémentation de méthodes non utilisées
   ```python
   class Stats:
       def __init__(self, pv, pm, force, intelligence, defense, resistance_magique, agilite, chance, endurance, esprit):
           self.pv = pv
           self.pm = pm
           self.force = force
           # Toutes les stats sont forcées même si non utilisées
   ```

2. **Dépendances Forcées** (`personnage.py`, `joueur.py`)
   - Les classes sont forcées de dépendre de méthodes qu'elles n'utilisent pas
   - Les interfaces ne sont pas spécifiques aux besoins des clients
   - Pas de granularité dans les contrats
   ```python
   def choisir_action(self, cible=None):
       # Forcé d'implémenter toutes les actions même si non utilisées
       print("1. Attaquer")
       print("2. Défendre")
       print("3. Utiliser un objet")
       print("4. Afficher l'inventaire")
   ```

## Dependency Inversion Principle (DIP)

1. **Dépendances Concrètes** (`donjon.py`, `grille.py`)
   - Dépendance directe vers des implémentations concrètes
   - Couplage fort avec les classes de base
   - Pas d'abstraction pour les dépendances

2. **Injection de Dépendances** (`main.py`)
   - Pas d'injection de dépendances
   - Création directe des objets
   - Couplage fort avec les constructeurs
   ```python
   def attaquer(self, cible):
       degats = self.statistiques["Force"]  # Dépendance directe vers l'implémentation
       cible.subir_degats(degats)
   ```
   ```python
   def __init__(self, personnage):  # Dépendance directe vers Personnage
       self.personnage = personnage
   ``` 
