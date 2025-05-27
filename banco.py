saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("\n=== MENU ===")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido para depósito!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if valor > saldo:
            print("Saldo insuficiente.")
        elif valor > limite:
            print("Limite máximo por saque é R$ 500.00")
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido para saque!")

    elif opcao == "e":
        print("\n=== EXTRATO ===")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Opção inválida, tente novamente.")
