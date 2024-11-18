#9. (Verificador de Maioridade) Peça a idade do usuário e informe se ele é maior de idade (18 anos ou mais) ou menor de idade.
#aceitar somente inteiros - e elaborar um pouco


number_Age = int(input('Digite sua idade: '))


if number_Age >= 18:
    print('Parabens, vc ja é idoso')
else:
    print('Parabens, vc não é idoso')