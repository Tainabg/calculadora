def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if x != 0:
        return x / y
    else:
        return "Erro: Divisão por zero!"

def calculadora():
    print("Calculadora Digital")
    print("Escolha a operação:")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. encerrar calculadora")
    
    while True:
        operacao = input("Digite a operação desejada: ")
        
        if operacao == '5':
            print("Encerrando a calculadora. Até logo!")
            break
        
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")
            continue
        
        if operacao not in {'1', '2', '3', '4'}:
            print("Opção inválida! Por favor, escolha uma opção válida.")
            continue
        
        if operacao == '1':
            resultado = soma(num1, num2)
        elif operacao == '2':
            resultado = subtracao(num1, num2)
        elif operacao == '3':
            resultado = multiplicacao(num1, num2)
        elif operacao == '4':
            resultado = divisao(num1, num2)
        
        print("O resultado da operação é:", resultado)
calculadora()
