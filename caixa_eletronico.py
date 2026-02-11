saldo = 1000
historico = []
opcao = ""

while opcao != "4":
    print("=== CAIXA ELETRÔNICO ===")
    print("1 - Ver Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    print("5 - Ver Histórico")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Saldo atual: R$", saldo)

    elif opcao == "2":
        valor = int(input("Valor do depósito: "))
        if valor > 0:
            saldo = saldo + valor
            historico.append("Depósito de R$ " + str(valor))
            print("Depósito realizado")
        else:
            print("Valor inválido")

    elif opcao == "3":
        valor = int(input("Valor do saque: "))
        if valor > 0 and valor <= saldo:
            saldo = saldo - valor
            historico.append("Saque de R$ " + str(valor))
            print("Saque realizado!")
        else:
            print("Saldo insuficiente ou valor inválido")

    elif opcao == "5":
        print("=== HISTÓRICO ===")
        if len(historico) == 0:
            print("Nenhuma movimentação ainda")
        else:
            for item in historico:
                print(item)

    elif opcao == "4":
        print("Saindo do sistema...")

    else:
        print("Opção inválida")
