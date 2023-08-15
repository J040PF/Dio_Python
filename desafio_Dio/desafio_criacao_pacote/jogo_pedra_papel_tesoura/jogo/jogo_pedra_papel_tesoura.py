from jogador import Jogador

class JogoPedraPapelTesoura:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def jogar(self):
        jogada1 = self.jogador1.fazer_jogada()
        jogada2 = self.jogador2.fazer_jogada()

        print(f"{self.jogador1.nome} jogou: {jogada1.escolha}")
        print(f"{self.jogador2.nome} jogou: {jogada2.escolha}")

        if jogada1.vence(jogada2):
            vencedor = self.jogador1
        elif jogada2.vence(jogada1):
            vencedor = self.jogador2
        else:
            vencedor = None

        if vencedor:
            print(f"{vencedor.nome} venceu!")
        else:
            print("Empate!")

# Exemplo de uso
jogador1 = Jogador("Alice")
jogador2 = Jogador("Bob")
jogo = JogoPedraPapelTesoura(jogador1, jogador2)
jogo.jogar()

