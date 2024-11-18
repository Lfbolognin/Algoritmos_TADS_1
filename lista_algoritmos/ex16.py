# 16. (Calculadora de Fatorial Recursiva) Crie uma função recursiva que calcula o fatorial
# de um número dado pelo usuário



def fatorial(fact):
    var_1 = 1 # USADA PARA ARMAZENAR O VALOR DO FATORIAL FINAL
    for x in range(fact, 0, -1): # ENQUANTO X ESTIVER NO RANGE DE FACT IR ATE O NUMERO 1 E SEMPRE DIMINUIR O STEP DE 1 EM 1
        var_1 *= x # MULTIPLICA O VALOR DE VAR_1 PELO VALOR DE X 
    return var_1 

print(fatorial(4)) # ATRIBUI A N O NUMERO FATORIAL QUE EU QUERO NO CASO FATORIAL DE 4


