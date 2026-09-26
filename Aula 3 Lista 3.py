# Exercício 1: Crie um programa que simule a tela de login de um sistema.
# Solicite o nome de usuário e a senha. Se o usuário for "admin" E a senha
# for "python123", exiba "Acesso liberado! Bem-vindo ao painel.".
# Caso contrário, exiba "Usuário ou senha incorretos."

usuario = input('Digite o usuário: ')
senha = input('Digite a senha: ')

if usuario == 'admin' and senha == 'python123':
    print('Acesso liberado! Bem-vindo ao painel')
else:
    print('Usuário ou senha incorretos')


# Exercício 2: Monte o menu de um robô de atendimento. Mostre na tela as opções:
# 1 - Suporte Técnico
# 2 - Financeiro
# 3 - Falar com Atendente
# Solicite que o usuário digite a opção desejada. Exiba para qual setor a chamada
# está sendo transferida ou diga "Opção inválida" se for digitado algo fora do menu.

print('Escolha uma das opções abaixo:')
print('Opção 1 - Suporte técnico.')
print('Opção 2 - Financeiro.')
print('Opção 3 - Falar com atendente.')

opcao = int(input('O que deseja fazer? '))

if opcao == 1:
    print('Você está sendo redirecionado para o suporte técnico!')
elif opcao == 2:
    print('Você está sendo redirecionado para o Financeiro!')
elif opcao == 3:
    print('Você está sendo redirecionado para falar com o atendente!')
else:
    print('Selecione uma opção válida!')


# Exercício 3: Crie um verificador de cupons para um e-commerce. O usuário deve
# digitar o código do cupom.
# Se digitar "DEV10", exiba "Cupom aceito! Você ganhou 10% de desconto."
# Se digitar "DEV20", exiba "Cupom aceito! Você ganhou 20% de desconto."
# Caso contrário, exiba "Cupom inválido ou expirado."

cupom = input('Digite o cupom que deseja utilizar: ').upper().strip()

if cupom == 'DEV10':
    print('Cupom Aceito! Você ganhou 10% de desconto!')
elif cupom == 'DEV20':
    print('Cupom Aceito! Você ganhou 20% de desconto!')
else:
    print('Cupom Inválido ou expirado!')


# Exercício 4: Peça a largura e o comprimento de um terreno em metros.
# Calcule a área com a fórmula: area = largura * comprimento.
# Se a área for maior ou igual a 300 m², exiba "Terreno de Grande Porte";
# caso contrário, exiba "Terreno de Porte Médio". Use f-string.

comprimento = int(input('Digite o comprimento do terreno: '))
largura = int(input('Digite a largura do terreno: '))

area = largura * comprimento

if area >= 300:
    print(f'Terreno de Grande Porte! {area}')
else:
    print(f'Terreno de Porte Médio! {area}')


# Exercício 5: Crie um programa que solicite a temperatura corporal do usuário
# (em °C). Se a temperatura for maior ou igual a 37.8 °C, exiba a mensagem
# "Atenção: Estado de febre!". Caso contrário, exiba "Temperatura normal".
# Use f-string para exibir o resultado.

temp = float(input('Digite a temperatura em °C: '))

if temp >= 37.8:
    print(f'Atenção! Estado de Febre!! {temp}°C')
else:
    print(f'Temperatura Normal!! {temp}°C')


# Exercício 6: Crie um programa que ajude um motorista a saber qual atitude
# tomar ao se aproximar de um cruzamento. O sistema deve solicitar a cor atual
# do semáforo (verde, amarelo ou vermelho).
# Se a cor for "verde", exiba "Ação: Siga em frente!".
# Se a cor for "amarelo", exiba "Ação: Atenção! Reduza a velocidade.".
# Se a cor for "vermelho", exiba "Ação: Pare! Aguarde a liberação.".
# Se for digitada qualquer outra cor, exiba "Sinal inválido!".

print('Escolha uma das opções abaixo:')
print('Opção 1 - Verde')
print('Opção 2 - Amarelo.')
print('Opção 3 - Vermelho.')

opcao = int(input('Qual a cor do Sinal?? '))

if opcao == 1:
    print('Ação: Siga em frente!')
elif opcao == 2:
    print('Ação: Atenção! Reduza a velocidade!')
elif opcao == 3:
    print('Ação: Pare! Aguarde a liberação!')
else:
    print('Selecione uma opção válida!')


# Exercício 7: Para alugar um carro, uma locadora exige que o cliente tenha
# pelo menos 21 anos E possua carteira de habilitação (CNH) ('s' para sim ou
# 'n' para não). Crie um programa que solicite a idade (inteiro) e a confirmação
# da CNH e exiba se o aluguel foi liberado ou negado usando f-string.

idade = int(input('Digite a idade do motorista: '))
carta = input('O motorista possui CNH? sim/nao ').upper()

if idade >= 21 and carta == 'SIM':
    print(f'Aluguel liberado! idade {idade} anos e CNH {carta}')
else:
    print(f'Aluguel Negado! idade {idade} anos e CNH {carta}')


# Exercício 8: Um e-commerce oferece frete grátis se o cliente for assinante
# do clube VIP ('s') OU se o valor total da compra for maior ou igual a
# R$ 150.00. Crie um programa que peça o valor da compra (float) e se o cliente
# é assinante ('s'/'n') e exiba o resultado com f-string.

valor = float(input('Digite o valor da compra: '))
vip = input('Você é membro VIP: sim/nao ').upper()

if valor >= 150 or vip == 'SIM':
    print(f'Você ganhou frete grátis! Sua compra deu R${valor} e você {vip} participa do grupo VIP!')
else:
    print(f'Você não ganhou frete grátis! Sua compra deu R${valor} e você {vip} participa do grupo VIP!')
