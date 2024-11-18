# 12. (Números Primos em um Intervalo) Receba um intervalo de números do usuário (por
# exemplo, entre 10 e 50) e retorne uma lista com todos os números primos dentro desse
# intervalo.




y = 0
span_1 = int(input('Digite o 1 intervalor: '))
span_2 = int(input('Digite o 2 intervalo: '))


for x in range (span_1, span_2 + 1 ):
    if x / x != 0:
        print
else:
    print('fim')
    