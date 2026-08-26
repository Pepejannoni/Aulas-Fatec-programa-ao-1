# Exercício 1
# Crie um programa de monitoramento de segurança. O sistema possui um limite padrão
# de 5 tentativas de login. Solicite ao usuário que informe quantas tentativas ele já
# realizou sem sucesso. O programa deve calcular quantas chances ainda restam e
# exibir o resultado usando f-strings.

TOTALTENTATIVAS = 5
print('Para entrar é necessário inserir Usuário e Senha')
tentativasUsuarios = input('Digite quantas tentativas você teve sem sucesso: ')
print(f'Você ainda tem: {TOTALTENTATIVAS - int(tentativasUsuarios)} restantes')


# Exercício 2
# Leia a idade como texto usando input(), converta para inteiro e imprima a idade
# da pessoa daqui a 5 anos.

idade = input('Digite sua Idade: ')
print(f'Sua Idade daqui a 5 anos será: {int(idade) + 5}')


# Exercício 3
# Desenvolva um programa que solicite ao usuário o nome de um produto, seu preço
# unitário e a quantidade em estoque. O programa deve calcular o valor total em
# estoque e exibir uma frase informativa utilizando f-strings.

produto = input('Digite o nome do produto: ')
preco = float(input('Digite o preço unitário do produto: '))
estoque = int(input('Digite a quantidade de estoque do produto: '))
print(f'O valor em estoque total é de: {estoque * preco}')


# Exercício 4
# Desenvolva um programa que solicite ao usuário o preço de um produto. O programa
# deve calcular um desconto de 15% sobre esse valor e exibir:
# 1. O valor exato do desconto;
# 2. O preço final após a subtração.
# Utilize f-strings para a saída dos dados.

desconto = 0.15
preco = float(input('Digite o preço do produto: '))
print(f'O valor do Desconto é de: ', desconto * 100, '%')
print(f'O preço final após o desconto é de: {preco * desconto}')


# Exercício 5
# Média de Notas: Peça 3 notas. Calcule a média garantindo que a soma seja
# priorizada pelos parênteses: (n1 + n2 + n3) / 3.

print('Escreva as notas para obter a média: ')
nota1 = float(input('Digite a nota número 1: '))
nota2 = float(input('Digite a nota número 2: '))
nota3 = float(input('Digite a nota número 3: '))

medianota = (nota1 + nota2 + nota3) / 3

print('A média das notas é: ', medianota)


# Exercício 6
# Crie um programa que peça ao usuário dois valores distintos (Valor A e Valor B).
# O programa deve primeiro exibir os valores na ordem em que foram digitados.
# Em seguida, utilize a sintaxe simplificada do Python para trocar os valores entre
# as variáveis e exiba o resultado final, mostrando que agora A possui o valor de B
# e vice-versa.

val1 = float(input('Digite o valor 1: '))
val2 = float(input('Digite o valor 2: '))

print('O valor 1 digitado em ordem é: ', val1)
print('O valor 2 digitado em ordem é: ', val2)

val1, val2 = val2, val1

print('Agora o valor 1 é: ', val1)
print('Agora o valor 2 é: ', val2)


# Exercício 7
# Crie um programa para auxiliar uma professora na divisão de guloseimas. O sistema
# deve solicitar a quantidade total de doces disponíveis e o número de alunos na turma.
# O programa deve calcular e exibir:
# 1. Quantos doces cada aluno receberá (divisão inteira);
# 2. Quantos doces restarão para a professora (resto da divisão).
# Utilize f-strings para uma exibição clara dos resultados.

doces = int(input('Digite o total de doces disponíveis: '))
alunos = int(input('Digite a quantidade total de alunos: '))
print(f'A quantidade de doces para cada aluno é de: {doces // alunos}')
print(f'A quantidade de doces que restou para a professora é de: {doces % alunos}')
