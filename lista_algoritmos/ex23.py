# 23. (Calculadora Básica com Estruturas Condicionais) Peça ao usuário dois números e
# uma operação (adição, subtração, multiplicação ou divisão) e execute a operação escolhida.
def calculadora():
    numero_1 = float(input('Digite seu primeiro numero:'))
    operador = input('Escolha seu operador: +, -, *, /  ')
    numero_2 = float(input('Digite seu segundo numero :'))

    if operador == '+':
        resultado = numero_1 + numero_2
        print(f"O resultado de {numero_1} + {numero_2} = {resultado}")

    elif operador == "-":
        resultado = numero_1 - numero_2
        print(f"O resultado de {numero_1} - {numero_2} = {resultado}")
    
    elif operador == "*":
        resultado = numero_1 * numero_2
        print(f"O resultado de {numero_1} * {numero_2} = {resultado}")
    
    elif operador == "/":
        if numero_2 != 0:
            resultado = numero_1 / numero_2
            print(f"O resultado de {numero_1} / {numero_2} = {resultado}")
        else:
            print("Erro: Não é possível dividir por zero!")
    else:
        print("Operação inválida! Escolha +, -, * ou /.")



    

calculadora()