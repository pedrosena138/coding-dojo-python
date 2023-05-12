import unittest

from main import Pokedex, Pokemon


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


class TestPokedex(unittest.TestCase):
    def test_adicionar_pokemon(self):
        # TODO: procurar fução beforeEach
        pokedex = Pokedex()
        pokemon = Pokemon(
            id=1,
            nome='Evaristo/INSS',
            altura=3.00,
            peso=50,
            habilidades=['Tomar Monster',
                         'Cuspir fogo', 'Investida', 'Teleport']
        )

        pokemon2 = Pokemon(
            id=1,
            nome='Eva',
            altura=3.60,
            peso=500,
            habilidades=['Tomar red bull',
                         'Cuspir fogo', 'Investida', 'Teleport']
        )

        pokedex.adiciona_pokemon(pokemon)
        pokedex.adiciona_pokemon(pokemon2)
        self.assertIn(pokemon, pokedex.pokemons)

        self.assertEqual(len(pokedex.pokemons), 1)

    def test_procurar_pokemon(self):
        pokedex = Pokedex()
        pokemon = Pokemon(
            id=1,
            nome='Evaristo/INSS',
            altura=3.00,
            peso=50,
            habilidades=['Tomar Monster',
                         'Cuspir fogo', 'Investida', 'Teleport']
        )

        pokedex.adiciona_pokemon(pokemon)

        self.assertIn(pokemon, pokedex.pokemons)
