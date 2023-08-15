
from jogada import Jogada
class Jogador:
    def __init__(self, nome):
        self.nome = nome

    def fazer_jogada(self):
        escolha = input(f"{self.nome}, faça sua escolha (pedra, papel ou tesoura): ")

        while escolha.lower() not in ["pedra", "papel", "tesoura"]:
            print("Escolha inválida. Escolha entre pedra, papel ou tesoura.")
            escolha = input(f"{self.nome}, faça sua escolha (pedra, papel ou tesoura): ")
        return Jogada(escolha.lower())

