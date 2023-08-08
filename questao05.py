'''
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número.
'''

print("Me informe dois números e lhe mostarei alguns cáculos")
a = float(input("o primeiro número:"))
b = float(input("o segundo número:"))

cont1 = a + b
cont2 = a - b
cont3 = b - a
cont4 = a * b
cont5 = a // b
cont6 = cont5 % b
print("Aqui estão os seus valores dos cáculos ", cont1, cont2, cont3, cont4, cont5, cont6)
