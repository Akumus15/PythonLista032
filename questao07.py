'''
A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações.
'''
print("A nossa loja Mamão com Açúcar vende os os produtos em até 10 prestações sem juros.")
v = float(input("Qual é o valor da sua compra? "))
p = float(input("Você deseja pagar em quantas prestações? "))

f = v / p

print("O resultado do valor da sua compra foi de R$", f)
