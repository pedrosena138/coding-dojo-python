import unittest

from main import Pokemon


class TestCase(unittest.TestCase):
    def test_example(self):
        """Should be a test case"""
        self.assertEqual(1, 1)


class TestPokemon(unittest.TestCase):
    def test_criar_pokemon(self):
        pokemon = Pokemon(
            id=1,
            nome='Evaristo/INSS',
            altura=3.00,
            peso=50,
            habilidades=['Tomar Monster',
                         'Cuspir fogo', 'Investida', 'Teleport']
        )
        self.assertEqual(1, pokemon.id)
        self.assertTrue(pokemon)
        self.assertEqual('Evaristo/INSS', pokemon.nome)
        self.assertEqual(3.00, pokemon.altura)
        self.assertEqual(50, pokemon.peso)
