opcao = 0

while opcao != 5:
    print("\nEscolha uma opção:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao >= 1 and opcao <= 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            resultado = num1 + num2
            print("Resultado:", resultado)

        elif opcao == 2:
            resultado = num1 - num2
            print("Resultado:", resultado)

        elif opcao == 3:
            resultado = num1 * num2
            print("Resultado:", resultado)

        elif opcao == 4:
            if num2 != 0:
                resultado = num1 / num2
                print("Resultado:", resultado)
            else:
                print("Não é possível dividir por zero!")

    elif opcao == 5:
        print("Encerrando a calculadora...")

    else:
        print("Opção inválida!")
