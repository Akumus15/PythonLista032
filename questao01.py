'''
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom.
'''
cont = float(input("Qual é o valor da sua conta, que eu te mostrarie o mesmo com um acrecimo de 10%"))
total = cont + ( cont * 0.10)

print("O valor da sua conta ficou em R$ ", total)