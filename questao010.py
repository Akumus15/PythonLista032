'''
Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos
e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores.
'''

e = int(input("Quantos eleitores tem em seu munícipio ?"))
b = int(input("Quantos foram brancos ?"))
n = int(input("Quantos foram nulos ?"))
v = int(input("Quantos forma válidos ?"))

bp = (b * 100) / e
np = (n * 100) / e
vp = (v * 100) / e

print(f"Os valores em precentuais são: "
      f"Eleitores no seu município é 100%. "
      f"Votos brnacos { bp }%. "
      f"Votos nulos { np }%. "
      f"Votos válodos { vp }%.")