#5. (Gerador de Tabuada) Receba um número inteiro e exiba a tabuada dele (multiplicações de 1 a 10).
#validar so numeros inteiros -

result = 0
multiplicator = 0
conditional = 10
number_1 = int(input('Digite um numero: '))

holder = number_1

while conditional  >= 0:
    result = holder * multiplicator
    print(f'{holder} x {multiplicator} = {result}')
    conditional  -= 1
    multiplicator += 1
else:
    print('fim')