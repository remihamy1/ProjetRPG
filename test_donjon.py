import unittest
from donjon import Salle, Donjon, creer_donjon, Monstre

class TestDonjon(unittest.TestCase):

    def test_creation_donjon(self):
        donjon = creer_donjon(3, 3)
        self.assertEqual(donjon.largeur, 3)
        self.assertEqual(donjon.hauteur, 3)
        self.assertEqual(len(donjon.salles), 3)
        self.assertEqual(len(donjon.salles[0]), 3)

    def test_connexions_salles(self):
        donjon = creer_donjon(2, 2)
        self.assertIn("est", donjon.salles[0][0].connexions)
        self.assertIn("sud", donjon.salles[0][0].connexions)
        self.assertNotIn("ouest", donjon.salles[0][0].connexions)
        self.assertNotIn("nord", donjon.salles[0][0].connexions)

        self.assertIn("ouest", donjon.salles[1][1].connexions)
        self.assertIn("nord", donjon.salles[1][1].connexions)
        self.assertNotIn("est", donjon.salles[1][1].connexions)
        self.assertNotIn("sud", donjon.salles[1][1].connexions)

    def test_deplacement_joueur(self):
        donjon = creer_donjon(3, 3)
        initial_position = donjon.position_joueur

        donjon.deplacer_joueur("sud")
        nouvelle_position = donjon.position_joueur
        self.assertNotEqual(initial_position, nouvelle_position)
        self.assertEqual(nouvelle_position, (0, 1))

        donjon.deplacer_joueur("est")
        nouvelle_position = donjon.position_joueur
        self.assertEqual(nouvelle_position, (1, 1))

    def test_afficher_salle_actuelle(self):
        donjon = creer_donjon(2, 2)
        description = donjon.afficher_salle_actuelle()
        self.assertIn("La salle est vide.", description)

        x, y = donjon.position_joueur
        donjon.salles[x][y].tresor = "Or"
        description = donjon.afficher_salle_actuelle()
        self.assertIn("Trésor: Or", description)

    def test_monstre_dans_salle(self):
        donjon = creer_donjon(2, 2)
        x, y = donjon.position_joueur
        donjon.salles[x][y].monstre = Monstre("Gobelin", 20, 5)
        description = donjon.afficher_salle_actuelle()
        self.assertIn("Monstre: Gobelin", description)

    def test_deplacement_vers_monstre(self):
        donjon = creer_donjon(3, 3)
        donjon.salles[1][1].monstre = Monstre("Gobelin", 20, 5)

        donjon.deplacer_joueur("est")
        donjon.deplacer_joueur("est")
        description = donjon.afficher_salle_actuelle()
        self.assertIn("Monstre: Gobelin", description)

if __name__ == '__main__':
    unittest.main()
