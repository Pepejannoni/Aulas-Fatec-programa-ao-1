nome = input('Qual o seu nome: ')
idade = int(input('Digite a sua idade: '))
estudante = input('Você é estudante? SIM/NAO ').upper() .strip().lower()
# Uma dica é aplicar strip().lower() no final do input de sim ou não para remover os espaços em branco de deixar o texto em minúsculo. O .uper(), serve para aceitar so o S/N

if idade >= 60 or estudante == 'sim':
    print(f'{nome} o seu ingresso é meia entrada! ')
else:
    print(f'{nome} o seu ingresso é inteiro!')


nome = input('Qual o seu nome? ')
nota = float(input('Qual a sua nota: '))

if nota < 5:
    print(f'{nome} você está reprovado! sua nota é: {nota}')
elif nota >= 5 and nota <= 6.9:
    print(f'{nome} você está em recuperação! sua nota é: {nota} ')
else:
    print(f'{nome} vocÊ está Aprovado com sucesso! sua nota é: {nota}')


num = int(input('Digite um número inteiro: '))

if num % 5 == 0:
    print('O número é multiplo de 5!')
else:
    print('O número não é multiplo de 5!')



ano = int(input('Digite um ano inteiro: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')
