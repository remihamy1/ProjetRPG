
## Violations du Single Responsibility Principle (SRP)
- Classe `Personnage` :
  - Gestion des données du personnage
  - Gestion de l'interaction utilisateur (saisie du nom)
  - Gestion de l'affichage (récapitulatif)
- Classe `Jeu` :
  - Mélange de la logique de jeu
  - Gestion de l'interface utilisateur
  - Gestion des commandes

## Violations du Open/Closed Principle (OCP)
- Modification nécessaire du code existant pour ajouter de nouvelles commandes dans la classe `Jeu` -> Pas bien
- Système de combat non extensible pour de nouveaux types d'attaques
- Logique de déplacement difficilement extensible

## Violations du Interface Segregation Principle (ISP)
- Interfaces trop larges des classes
- Exposition excessive des statistiques dans la classe `Personnage`
- Méthodes publiques non nécessaires

## Violations du Dependency Inversion Principle (DIP)
- Dépendances directes aux implémentations concrètes
- Absence d'interfaces abstraites
- Couplage fort entre les classes

## Autres Infractions au Clean Code

### Couplage Fort
- Classes fortement interdépendantes
- Logique de jeu liée à l'interface utilisateur
- Absence de séparation entre la logique métier et l'interface utilisateur

### Problèmes d'Encapsulation
- Attributs directement accessibles
- Stats du personnage exposées
- Collections exposées directement (liste_monstres)

### Testabilité
- Code difficilement testable
- Interaction utilisateur intégrée dans les classes métier
- Absence d'injection de dépendances

### Violations des Object Calisthenics
- Utilisation de getters primitifs
- Classes avec trop de responsabilités
- Non-respect de la loi de Déméter (je peux t'expliquer si il faut)
- Mauvaise encapsulation des collections
