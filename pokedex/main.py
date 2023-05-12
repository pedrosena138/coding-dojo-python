from typing import List, Union


class Pokemon:
    def __init__(self, id: int, nome: str, altura: float, peso: float, habilidades: List[str]):
        self.id = id
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.habilidades = habilidades


class Pokedex:
    def __init__(self):
        # TODO: Talvez mudar para dict?
        self.pokemons: List[Pokemon] = list()

    def adicionar_pokemon(self, pokemon: Pokemon) -> Union[None, Exception]:
        # TODO: Mudar verificação do pokemon na lista
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
