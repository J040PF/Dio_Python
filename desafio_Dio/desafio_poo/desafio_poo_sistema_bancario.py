
from abc import ABC, abstractclassmethod, abstractproperty


class Cliente:
    def __init__(self, endereço):
        self.endereço = endereço
        self.contas = []


    def realizar_transaçao(self, conta, Transaçao):
        # registra uma transação na classe transação
        Transaçao.registrar(conta)



    def adicionar_conta(self, conta):
        # realiza a adiçao de uma conta para o cliente
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self,nome, cpf, data_nascimento, endereço):
        # atraves do super recuperar o atributo endereço da classe pai
        super().__init__(endereço)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    
    def __init__(self, numero, Cliente):
        # suficxo _ indica que o metodo e privado e nao pode ser acessado diretamento
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = Cliente
        self._historico = Historico()

    @ classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    # atraves do property, criar metodos getters
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Deposito realizado !")
            input("Aperte qualquer tecla para retornar... ")
            return True
        
        else:
            print("Operação falhou! O valor informado é inválido.")
            input("Aperte qualquer tecla para retornar... ")
            return False
            

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            input("Aperte qualquer tecla para retornar... ")

        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado !")
            input("Aperte qualquer tecla para retornar... ")
            return True
        
        else:
            print("Operação falhou! O valor informado é inválido.")
            input("Aperte qualquer tecla para retornar... ")
            
        return False

        
class ContaCorrente(Conta):

    def __init__(self, numero, Cliente, limite = 500, limite_saque = 3):
        super().__init__(numero, Cliente)
        self._limite = limite
        self._limite_saques = limite_saque

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transaçoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            input("Aperte qualquer tecla para retornar... ")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido. ")
            input("Aperte qualquer tecla para retornar... ")

        else:
            return super().sacar(valor)
        return False
    

    def __str__(self):
        return f"""\
            Agência: {self.agencia}
            C/C: {self.numero}
            Titular:  {self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transaçoes = []

    @property
    def transaçoes(self):
        return self._transaçoes
    
    def adicionar_transaçao(self, transaçao):
        self._transaçoes.append({"tipo": transaçao.__class__.__name__,
                                 "valor": transaçao.valor})


class Transaçao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self,conta):
        pass


class Deposito(Transaçao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        sucesso_transaçao = conta.depositar(self.valor)
        if sucesso_transaçao:
            conta.historico.adicionar_transaçao(self)


class Saque(Transaçao):
    def __init__(self, valor):
        self._valor = valor


    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transaçao(self)

# ------------------- usuario - criar e filtrar
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    cliente= filtrar_usuario(cpf, usuarios)

    if cliente:
        print("Já existe usuário com esse CPF!")
        input("Aperte qualquer tecla para retornar... ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome = nome, data_nascimento = data_nascimento, cpf = cpf, endereço = endereco)
    usuarios.append(cliente)
    print("=== Usuário criado com sucesso! ===")
    input("Aperte qualquer tecla para retornar... ")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


# ------------- conta - criar, listar, recuperar

def criar_conta(numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_usuario(cpf, usuarios)

    if not cliente:
        print("\nCliente não encontrado, fluxo de criação de conta encerrado!")
        input("Aperte qualquer tecla para retornar... ")
        return

    conta = ContaCorrente.nova_conta(cliente = cliente, numero = numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")
    input("Aperte qualquer tecla para retornar... ")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(str(conta))
    input("Aperte qualquer tecla para retornar... ")


def recuperar_conta_usuario(usuario):
    if not usuario.contas:
        print("\nCliente não possui conta!")
        input("Aperte qualquer tecla para retornar... ")
        return
    return usuario.contas[0]

# ------------ Funçoes da conta - Depositar, Estrato Sacar

def extrato_geral(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_usuario(cpf, usuarios)

    if not cliente:
        print("Cliente não encontrado! ")
        input("Aperte qualquer tecla para retornar... ")
        return

    conta = recuperar_conta_usuario(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transaçoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")
    input("Aperte qualquer tecla para retornar... ")


def depositar(usuarios):
    # realiza a filtragem do cpf do cliente, se tiver conta joga para classe deposito
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_usuario(cpf, usuarios)

    if not cliente:
        print("Cliente não encontrado!")
        input("Aperte qualquer tecla para retornar... ")
        return

    valor = float(input("Informe o valor do Deposito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_usuario(cliente)
    if not conta:
        return

    cliente.realizar_transaçao(conta, transacao)


def sacar(usuarios):
    # realiza a filtragem do cpf do cliente, se tiver conta joga para classe saque
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_usuario(cpf, usuarios)

    if not cliente:
        print("Cliente não encontrado ! ")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_usuario(cliente)
    if not conta:
        return

    cliente.realizar_transaçao(conta, transacao)

# --------------- menu conta
def menu():
    menu = """

        [ 1 ] Depositar
        [ 2 ] Sacar
        [ 3 ] Extrato
        [ 4 ] Novo usuário
        [ 5 ] Novo Conta
        [ 6 ] Listar Contas
        [ 7 ] Sair

    => """
        
    print(menu)


def main():
    
    usuarios = []
    contas = []

    while True:
        menu()
        opcao = input()

        if opcao == "1":
            depositar(usuarios)

        elif opcao == "2":
            sacar(usuarios)

        elif opcao == "3":
            extrato_geral(usuarios)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, usuarios, contas)

        elif opcao == "6":
            listar_contas(contas)
        
        elif opcao == '7':
            print('saindo')
            break
        else:
            input("Operação invalida, tente novamente... aperter qualquer tecla")


main()
