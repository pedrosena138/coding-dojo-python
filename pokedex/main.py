from typing import List


class Pokemon:
    def __init__(self, id, nome, altura, peso, habilidades):
        self.id = id
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.habilidades = habilidades


class Pokedex:
    def __init__(self):
        self.pokemons: List[Pokemon] = list()

    def adiciona_pokemon(self, pokemon: Pokemon):
        # TODO: Mudar verificação do pokemon na lista
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
