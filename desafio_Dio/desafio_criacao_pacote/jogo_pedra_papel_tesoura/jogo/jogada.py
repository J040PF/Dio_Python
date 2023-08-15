class Jogada:
    def __init__(self, escolha):
        self.escolha = escolha

    def vence(self, outra_jogada):
        if self.escolha == "pedra" and outra_jogada.escolha == "tesoura":
            return True
        elif self.escolha == "papel" and outra_jogada.escolha == "pedra":
            return True
        elif self.escolha == "tesoura" and outra_jogada.escolha == "papel":
            return True
        return False

