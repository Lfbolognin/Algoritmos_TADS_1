#2. (Verificador de Número Par ou Ímpar) Peça ao usuário um número inteiro e informe se ele é par ou ímpar.


#Validação para aceitar somente inteiro

def number_Receives():
    number_1 = int(input('Digite seu numero: '))
    return number_1
#_______________________________________________________________# 
#_______________________________________________________________#    
#_______________________________________________________________#    
#_______________________________________________________________#
def calc(number_1):
    """
    CALC FUNCTION TO VERIFY IF NUMBER_1 = O OR ≠ 0 
    """
    if number_1 % 2 == 0:
        print(f'O numero {number_1} é par')
    else:
        print(f'O numero {number_1} é impar')

number_1 = number_Receives()
result = calc(number_1)