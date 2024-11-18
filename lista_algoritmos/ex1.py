#1. (Calculadora de Soma Simples) Receba dois números do usuário e exiba a soma deles

# #add validação para numeros somente

def receber_numeros():
    # Captura os dois números via input
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))
    return numero_1, numero_2  # Retorna os números como uma tupla

def calcular_soma(numero_1, numero_2):
    # Calcula a soma
    return numero_1 + numero_2

# Chamando as funções
num1, num2 = receber_numeros()  # Captura os números retornados
soma = calcular_soma(num1, num2)  # Calcula a soma usando os números capturados

# Exibindo o resultado
print(f"A soma de {num1} e {num2} é: {soma}")


