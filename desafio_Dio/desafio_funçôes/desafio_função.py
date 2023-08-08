def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado! ")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def extrato_geral(extrato, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def depositar():
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        extrato = f"Depósito: R$ {valor:.2f}\n"
        print('deposito realizado com sucesso')
        return valor, extrato

    else:
        print("Operação falhou! O valor informado é inválido.")


def sacar(saldo, numero_saques):
        LIMITE_SAQUES = 3
        limite = 500

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
                extrato = f"Saque: R$ {valor:.2f}\n"
                print("Saque realizado com sucesso !!!")
                return(valor, extrato)

        else:
            print("Operação falhou! O valor informado é inválido.")


def menu():
    menu = """

        [ d ] Depositar
        [ s ] Sacar
        [ e ] Extrato
        [ nc ] Nova conta
        [ lc ] Listar contas
        [ nu ] Novo usuário
        [ q ] Sair

    => """
        
    print(menu)


def main():
    
    AGENCIA = "0001"
    usuarios = []
    contas = []
    saldo = 0
    extrato = ""
    numero_saques = 0
    menu()

    while True:

        opcao = input()

        if opcao == 'q':
            print('saindo')
            break

        elif opcao == "d":
            print("Deposito")
            try:
                valor, ed = depositar()
                extrato += ed
                saldo += valor
            except:
                pass

        elif opcao == "s":
            print("Saque")
            try:
                valor, ex = sacar(saldo, numero_saques)
                extrato += ex
                saldo -= valor
                numero_saques += 1
            except:
                pass

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "e":
            extrato_geral(extrato, saldo)
           
main()