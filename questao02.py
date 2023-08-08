'''
Desenvolver um programa que faça duas perguntas: o valor referente às horas atuais e o valor referente aos
minutos atuais. Exemplo, se agora são 09:35h o usuário deverá informar como resposta às horas atuais o valor
09 e como resposta aos minutos atuais o valor 35. Em seguida o programa deverá apresentar como resposta
quantos minutos já se passaram desde às 00:00h deste dia
'''

print("Me informe o atual horário, que lhe mostarei quantas minutos se passaram desde ás 00:00h deste dia")
h = int(input("Qual é a hora: "))
min = int(input("Quais são os atuais minutos: "))

hemmin = h * 60

total = min + hemmin

print(" Já se passaram", total, "min")