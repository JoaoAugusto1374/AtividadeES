def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero!"


def menu():
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")


opcao = 0

while opcao != 5:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if 1 <= opcao <= 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            print("Resultado:", soma(num1, num2))

        elif opcao == 2:
            print("Resultado:", subtracao(num1, num2))

        elif opcao == 3:
            print("Resultado:", multiplicacao(num1, num2))

        elif opcao == 4:
            print("Resultado:", divisao(num1, num2))

    elif opcao == 5:
        print("Encerrando...")

    else:
        print("Opção inválida!")
