import unittest

from main import Pokedex, Pokemon


class TestPokemon(unittest.TestCase):
    def test_criar_pokemon(self):
        """Deve criar um pokemon com seus atributos"""
        pokemon = Pokemon(
            id=1,
            nome='Evaristo/INSS',
            altura=3.00,
            peso=50,
            habilidades=['Tomar Monster',
                         'Cuspir fogo', 'Investida', 'Teleport']
        )

        self.assertEqual(1, pokemon.id)
        self.assertIsInstance(pokemon, Pokemon)
        self.assertEqual('Evaristo/INSS', pokemon.nome)
        self.assertEqual(3.00, pokemon.altura)
        self.assertEqual(50, pokemon.peso)


class TestPokedex(unittest.TestCase):
    def setUp(self):
        self.pokedex = Pokedex()

    def test_instancia_pokedex(self):
        """Deve verificar se a pokedex é uma classe Pokedex"""
        self.assertIsInstance(self.pokedex, Pokedex)

    def test_adicionar_pokemon(self):
        pokemon1 = Pokemon(
            id=1,
            nome='Evaristo/INSS',
            altura=3.00,
            peso=50,
            habilidades=['Tomar Monster',
                         'Cuspir fogo', 'Investida', 'Teleport']
        )

        pokemon2 = Pokemon(
            id=2,
            nome='Eva',
            altura=3.60,
            peso=500,
            habilidades=['Tomar red bull',
                         'Cuspir fogo', 'Investida', 'Teleport']
        )

        self.pokedex.adicionar_pokemon(pokemon1)
        self.pokedex.adicionar_pokemon(pokemon2)

        self.assertIn(pokemon1, self.pokedex.pokemons)
        self.assertIn(pokemon2, self.pokedex.pokemons)
        self.assertEqual(len(self.pokedex.pokemons), 2)

    def test_procurar_pokemon(self):
        pokemon = Pokemon(
            id=1,
            nome='Evaristo/INSS',
            altura=3.00,
            peso=50,
            habilidades=['Tomar Monster',
                         'Cuspir fogo', 'Investida', 'Teleport']
        )

        self.pokedex.adiciona_pokemon(pokemon)

        self.assertIn(pokemon, self.pokedex.pokemons)
