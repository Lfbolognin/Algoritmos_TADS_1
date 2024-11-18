# 15. (Jogo de Adivinhação)
# Implemente um jogo onde o programa escolhe um número aleatório entre 1 e 100, e o
# usuário deve adivinhar. Após cada tentativa, diga se o número é maior ou menor que o
# número secreto, e conte o número de tentativas até acertar.
from random import randint

tentativas = 0
sort = randint(1, 100)

while True:
    print(sort)
    kick = int(input('Digite seu numero: '))
    tentativas +=1
    if kick > sort:
        print(f'O numero que voce digitou {kick} e maior que o numero sorteado')
    elif kick < sort:  
        print(f'O numero que voce digitou {kick} é menor que o numero sorteado')
    else:
        print(f'Voce ganhou o numero era {sort}')
        break
print(f'parabens, vc usou {tentativas} tentativas e o numero sorteado era {sort}')





