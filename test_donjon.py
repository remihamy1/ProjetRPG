import unittest
from donjon import Donjon

class TestDonjon(unittest.TestCase):
    def test_generation_donjon(self):
        donjon = Donjon(5)
        self.assertEqual(len(donjon.grille), 5)
        self.assertEqual(len(donjon.grille[0]), 5)

if __name__ == '__main__':
    unittest.main()
