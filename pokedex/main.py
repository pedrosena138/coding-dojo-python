
class Pokemon:
    def __init__(self, id, nome, altura, peso, habilidades):
        self.id = id
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.habilidades = habilidades


class Pokedex:
    def __init__(self, pokemon: Pokemon = None):
        self.pokemon = None
        self.pokemons = []

    def adiciona_pokemon(self, pokemon):
        ...