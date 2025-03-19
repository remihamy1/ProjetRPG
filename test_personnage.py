import unittest
from personnage import Personnage

class TestPersonnage(unittest.TestCase):
    def test_creation_personnage_valide(self):
        personnage = Personnage("Aragorn", "guerrier")
        self.assertEqual(personnage.nom, "Aragorn")
        self.assertEqual(personnage.statistiques["PV"], 150)

    def test_validation_nom_trop_court(self):
        with self.assertRaises(ValueError):
            Personnage("A", "guerrier")

    def test_validation_nom_trop_long(self):
        with self.assertRaises(ValueError):
            Personnage("A" * 21, "guerrier")

if __name__ == '__main__':
    unittest.main()
