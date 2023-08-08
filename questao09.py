'''
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias.
'''
i = int(input("Quantos anos você tem ?"))
m = int(input("Quantos meses você tem ?"))
d = int(input("Quantos dias você tem ?"))

im = i * 365
mm = m * 30
dd = im + mm + d
print("A sua idade em dias é ", dd)