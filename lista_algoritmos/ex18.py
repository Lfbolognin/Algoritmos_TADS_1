# 18. (Soma de Diagonais de uma Matriz Quadrada) Receba uma matriz quadrada de
# inteiros e calcule a soma dos elementos das diagonais principal e secundária.


matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0]] # defino os 9 (3x3) elementos da minha matriz
for linha in range (0, 3): # faça um for para atribuir com o input um valor para o indice linha de 0 a 2, for exclui o 3 no caso.
    for coluna in range (0, 3): # faça um for para atribuir com o input um valor para o indice coluna de 0 a 2, for exclui o 3 no caso.
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: ')) # DOU UM INPUT PARA MOSTAR AO USUARIO OS ELEMENTOS DA COLUNA E LINHA
        #  faça um input que ira pegar os dados e atribuir na lista matriz, objetos linha e coluna

print('-='* 30) # enfeite
#MONTAGEM DA MATRIZ 3X3
for linha in range (0, 3): # PERCORRE O ELEMENTO DA LINHA PARA FORMAÇÃO 0, 1, 2
    for coluna in range (0,3): # PERCORRE O ELEMENTO DA COLUNA PARA FORMAÇÃO 0, 1, 2
        print(f'[{matriz[linha][coluna]:^7}]', end='') 
        # PRINT COM O FORMATO DA DA MINHA MATRIZ NO CASO [X] [Y] [Z]... 
        #:^7 PARA ARRUMAR A VISUALIZAÇÃO DO DO PRINT, END PARA MANTER NA MSM LINHA

    print()# SEMPRE QUE TERMINAR O 2 FOR O PRINT JOGA PARA A LINHA DE BAIXO

print('-='* 30)# enfeite
soma_principal = matriz[0][0] + matriz[1][1] + matriz[2][2]
soma_secundaria = matriz[0][2] + matriz[1][1] + matriz[2][0]
print(f'A soma da diagonais principal é {matriz[0][0]} + {matriz[1][1]} + {matriz[2][2]} = {soma_principal}')
print(f'A soma da diagonais secundaria é {matriz[0][2]} + {matriz[1][1]} + {matriz[2][0]} = {soma_secundaria}')
print('-='* 30)# enfeite