# Exercício 1: Um cinema concede o benefício da meia-entrada para pessoas que tenham
# 60 anos ou mais, ou que sejam estudantes. Escreva um programa em Python que receba
# o nome do espectador, a sua idade (int) e se ele é estudante ("sim" ou "não").
# O sistema deve fazer o teste lógico e informar se o acesso foi registrado como
# "Meia-Entrada Liberada" ou "Ingresso Inteiro".

nome = input('Qual o seu nome: ')
idade = int(input('Digite a sua idade: '))
estudante = input('Você é estudante? SIM/NAO ').strip().lower()

if idade >= 60 or estudante == 'sim':
    print(f'{nome} o seu ingresso é meia entrada!')
else:
    print(f'{nome} o seu ingresso é inteiro!')


# Exercício 2: Escreva um programa que solicite a nota final de um aluno
# (número real entre 0.0 e 10.0) e exiba a sua situação acadêmica de acordo
# com as seguintes regras:
# Nota menor que 5.0: "Reprovado"
# Nota entre 5.0 e 6.9 (inclusive): "Em Recuperação"
# Nota igual ou maior que 7.0: "Aprovado com Sucesso"

nome = input('Qual o seu nome? ')
nota = float(input('Qual a sua nota: '))

if nota < 5:
    print(f'{nome} você está reprovado! Sua nota é: {nota}')
elif nota >= 5 and nota <= 6.9:
    print(f'{nome} você está em recuperação! Sua nota é: {nota}')
else:
    print(f'{nome} você está aprovado com sucesso! Sua nota é: {nota}')


# Exercício 3: Crie um programa que solicite um número inteiro qualquer ao usuário.
# Utilizando o operador de resto (%) e a estrutura condicional if/else, verifique
# e exiba se o número digitado é ou não MÚLTIPLO de 5.

num = int(input('Digite um número inteiro: '))

if num % 5 == 0:
    print('O número é múltiplo de 5!')
else:
    print('O número não é múltiplo de 5!')


# Exercício 4: Escreva um programa que solicite um ano em formato inteiro
# (Ex: 2024) e determine se ele é um Ano Bissexto ou não, utilizando combinação
# dos operadores de resto (%), relacionais (==, !=) e lógicos (and, or).

ano = int(input('Digite um ano inteiro: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')
