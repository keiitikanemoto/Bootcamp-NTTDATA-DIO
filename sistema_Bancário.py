menu = """


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif (opcao == "s"):
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente")

        elif excedeu_limite:
            print("Você excedeu o limite de valor para saque. O limite é de R$500,00")

        elif excedeu_saques:
            print("Você excedeu o limite de saques. ")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: -R$ { valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("O valor informado é inválido. Repita a operação")


    elif (opcao == "e"):
        print("=" * 10, " EXTRATO ", "=" * 10)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo R$ {saldo:.2f}")
        print("=" * 30)
        
    elif (opcao == "q"):
        print("Encerrando a operação")
        break

    else:
        print("Opcão inválida, por favor tente novamente")
