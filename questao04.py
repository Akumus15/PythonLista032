'''
 Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metros.
'''

print("Me informe o seu peso e a sua altura e o seu peso que lhe direi o seu índice de massa corporal (IMC)")
p = int(input("Seu peso: "))
a = float(input("Sua altura: "))

imc = p / ( a * a )

print("O seu IMC é ", imc)