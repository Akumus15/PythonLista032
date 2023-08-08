'''
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros
'''
print("Me informe o seu peso em quilograms e a sua altura em metros, depois eu lhe mostrei esses valores em gramas e centímetros ")
peso = int(input("Informe aqui o seu peso: "))
altura = float(input("Informe aqui a sua altura: "))

g = peso * 1000
cm = altura * 100

print("O seu peso ficou em ", g, "gramas e a sua altura ficou em ", cm, "cm")
