'''
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês.
'''
nome = input("Qual é o seu nome ? ")
salfx = float(input("Qual é o seu salário fixo ? "))
vendas = float(input("Qual e o total de vendas efetuadas por você no mês (em dinheiro) ? "))

comi = vendas * 0.15
salcom = salfx + comi

print(nome, f" o seu salário é { salfx } sua comissão foi de R$ { comi } e o seu salário completo é R$", salcom)