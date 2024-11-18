# 20. (Gerador de Números da Sequência de Sequência) Peça ao usuário um número n e
# gere uma lista com os n primeiros números da sequência de Fibonacci.

def sequencia():
    numero = int(input('Digite um numero: '))
    sequencia = [0, 1] 
    while len(sequencia) < numero: 

        sequencia.append(sequencia[-1] + sequencia[-2]) 
    return sequencia[:numero]

resultado = sequencia()
print(resultado)
