saldo = 0
Extrato = ""
SAQUES_DIARIOS = 3
numero_de_saques = 0
limite = 500

mensagem = """ 
               (1) Extrato
               (2) Deposito
               (3) Saque
               (4) Sair
"""
print(mensagem)


while True:
    operação = float(input())
    if operação == 1:
        print("#########################")
        print("========= Extrato ========")
        print("#########################")
        if Extrato == "":
            print("Não foram realizadas movimentações")
        else:
            print(f"{Extrato}\nSaldo: R${saldo:.2f}")


    elif operação == 2:
        print("Deposito")
        valor = float(input("Digite o valor do deposito\n"))
        if valor > 0:
            saldo += valor
            Extrato += f"Deposito:R$ {valor:.2f}\n"
            print("Deposito Realizado com Sucesso.")
        else:
            print('Desposito Invalido, Tente novamente')


    elif operação == 3:
        print("Saque")
        valor = float(input("Digite o valor do saque\n"))
        if saldo >= valor and numero_de_saques < SAQUES_DIARIOS and valor <= 500:
            saldo -= valor
            numero_de_saques += 1
            Extrato += f"Saque:R$ {valor:.2f}\n"

            print(f"Saque Realizado com Sucesso. \nNumero de saques : {numero_de_saques}/{SAQUES_DIARIOS}")

        elif numero_de_saques == SAQUES_DIARIOS:
            print('Operação Falhou, limite de saques excedidos')
        
        elif valor > 500:
            print("Operação Falhou, valor excedeu limite de saque")

        else:
            print('Saque nao Realizado, Devido a Falta de saldo')



    elif operação == 4:
        print("Sair")
        break

    else:
        print("Opção Invalida tente novamente")
