#3. (Conversor de Temperatura) Receba uma temperatura em graus Celsius e converta
#para Fahrenheit usando a fórmula: F = C ∗ 1.8 + 32

#validação para inteiro 
#validação se a temperatura esta dentro do padrão maximo e minimo de fahrenheit

def temp_Celcius():
    number_1 = input('Digite a temperatura em celcius: ')
    teste = number_1
    return number_1, teste

def calc_Temp(number_1):
    temp_Fahrenheit = (temp_Celcius * 1.8) + 32
    print(f'A temperatura atual em fahrenheit é {calc_Temp} °F')


number_1 = temp_Celcius()
calc = calc_Temp(number_1)




