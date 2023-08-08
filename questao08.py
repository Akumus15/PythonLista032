'''
Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabese que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
'''

p = float(input("Qual é o preço do seu produto ? "))
por = float(input("Qual é o percenual que será acresentado a sua compra? "))

percentual = 100 / (p * por)
total = p + percentual

print("O da sua venda é R$", total)