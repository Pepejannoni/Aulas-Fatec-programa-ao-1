# Exercício 1
# Verificador Lógico de Maioridade
# Desenvolva um programa que verifique se a pessoa está com idade para dirigir ou não.
# Solicite ao usuário que digite o seu ano de nascimento utilizando input().
# Converta essa entrada para inteiro (int) e calcule a idade atual da pessoa
# (considere o ano atual como 2026).
# Crie uma variável lógica chamada pode_dirigir. Essa variável deve receber o resultado
# da comparação se a idade calculada é maior ou igual a 18 (idade >= 18).
# Sem usar if, exiba na tela a mensagem utilizando f-strings:
# "Tem permissão para dirigir?"

anonasc = int(input('Para saber se pode dirigir digite seu ano de nascimento: '))
pode_dirigir = 2026 - anonasc >= 18
print("Você pode dirigir? ", pode_dirigir)


# Exercício 1 - Versão alternativa
# Solicite ao usuário que digite seu ano de nascimento e calcule sua idade,
# considerando o ano atual como 2026.
# Exiba diretamente se a pessoa pode dirigir, verificando se possui 18 anos ou mais.

anonasc = int(input('Para saber se pode dirigir digite seu ano de nascimento: '))
print(f'Pode dirigir? {2026 - anonasc >= 18}')


# Exercício 2
# Sensor de Temperatura de Servidor
# Em salas de servidores, a temperatura não pode passar de 40°C.
# Solicite ao usuário que digite a temperatura atual medida pelo sensor.
# Converta essa entrada para número decimal (float).
# Crie uma variável booleana chamada alerta_ativo. Ela deve receber True se a temperatura
# lida for maior que 40.0, e False caso contrário.
# Exiba o status do alerta no terminal usando uma f-string.

tempatual = float(input('Digite a temperatura atual: '))
print(f'Status do alerta: {tempatual >= 40}')


# Exercício 3
# Validador de Meta de Vendas
# Uma loja de eletrônicos estabeleceu uma meta de vendas diária de R$ 1.500,00.
# Peça ao vendedor para digitar o valor total que ele vendeu hoje.
# Converta a entrada para float.
# Crie uma variável do tipo bool chamada meta_atingida que armazene se o valor vendido
# foi maior ou igual à meta de 1500.00.
# Exiba o resultado formatando a saída com f-strings.

vendahj = float(input('Digite o valor em vendas de hoje: '))
print(f'Meta atingida? {vendahj >= 1500}')


# Exercício 4
# Calculadora de Combustível de Viagem
# Três amigos vão fazer uma viagem de carro e querem dividir igualmente o custo
# do combustível.
# Solicite a distância total planejada para a viagem em quilômetros,
# o consumo médio de combustível do carro e o preço atual do litro do combustível.
# Calcule:
# 1. A quantidade de litros necessários para a viagem (distância / consumo).
# 2. O custo total do combustível (litros necessários * preço).
# 3. Quanto cada um dos 3 amigos deverá pagar (custo total / 3).
# Ao final, exiba os valores utilizando f-strings, com os custos em R$
# e duas casas decimais.

kmtotal = float(input('Digite a distância total planejada para a viagem: '))
consumo = float(input('Digite o consumo do veículo: '))
preco = float(input('Digite o valor do combustível: '))

litronecessario = kmtotal / consumo
custototal = litronecessario * preco
cadaumpaga = custototal / 3

print(f'A quantidade de litros necessário é de: {litronecessario}')
print(f'O custo total de combustível será: R${custototal: .2f}')
print(f'Quanto cada um deverá pagar é: R${cadaumpaga: .2f}')


# Exercício 5
# Sistema de Segurança de Parque de Diversões
# Para poder andar na montanha-russa, o visitante precisa cumprir dois requisitos:
# 1. Ter idade igual ou maior que 12 anos.
# 2. Ter altura igual ou maior que 1.50 metros.
# Peça ao usuário o seu ano de nascimento e calcule sua idade, considerando o ano
# atual como 2026.
# Peça sua altura em metros.
# Crie uma variável booleana chamada pode_entrar. Ela deve receber o resultado lógico
# que valide se a idade é suficiente E (and) se a altura é suficiente.
# Exiba o resultado final na tela utilizando f-strings.

anonasc = float(input('Informe o seu ano de nascimento: '))
altura = float(input('Informe sua altura: '))
idade = 2026 - anonasc
podeentrar = idade >= 12 and altura >= 1.50

print(f'Pode entrar no parque? {podeentrar}')


# Exercício 6
# Validador de Desconto no Cinema
# Um cinema local concede o benefício da meia-entrada para clientes que cumprem
# pelo menos um dos seguintes critérios:
# 1. Ter 60 anos ou mais.
# 2. Ser estudante, identificado se o usuário digitar exatamente a letra "S".
# Peça para o usuário digitar sua idade e converta para int.
# Pergunte se ele é estudante com a mensagem "Você é estudante? S/N".
# Crie uma variável booleana chamada e_estudante que armazena o resultado de verificar
# se o que ele digitou é igual a "S".
# Crie uma variável booleana chamada tem_direito_desconto. Ela deve receber True se
# a idade for maior ou igual a 60 OU (or) se ele for estudante.
# Exiba na tela a resposta final utilizando f-strings.

idade = int(input('Digite sua idade: '))
resposta = input('Você é estudante? S/N ').upper()
estudante = resposta == 'S'
temdesconto = idade >= 60 or estudante
print(f'Tem direito a desconto? {temdesconto}')
