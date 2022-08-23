'''Levando em consideração a velocidade máxima permitida de 80KM e uma determinada rua. Crie um programa que recebe do usuário um valor que represente a velocidade e com base nessa velocidade diga se ela tomou uma multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deverá exibir "não houve multa", caso esteja até 10km acima, deverá exibir: "Levou uma multa leve", caso esteja entre 11 a 20km acima da velocidade máxima permitida, deverá exibir: "Levou uma multa grave" e caso esteja acima de 20km acima da velocidade máxima permitida, exiba: "Levou uma multa gravíssima."

# Método 5Q's para montar um algorítmo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
R - Velocidade atual do motorista.

2. O que devo fazer com estes dados?
R - "Levando em consideração a velocidade máxima permitida de 80KM e uma determinada rua. Crie um programa que recebe do usuário um valor que represente a velocidade e com base nessa velocidade diga se ela tomou uma multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deverá exibir "não houve multa", caso esteja até 10km acima, deverá exibir: "Levou uma multa leve", caso esteja entre 11 a 20km acima da velocidade máxima permitida, deverá exibir: "Levou uma multa grave" e caso esteja acima de 20km acima da velocidade máxima permitida, exiba: "Levou uma multa gravíssima."

3. Quais são as restrições deste problema?
R - Buscar a velocidade atual do motorista.

4. Qual é o resultado esperado? 
R - deverá exibir: "Levou uma multa leve", caso esteja entre 11 a 20km acima da velocidade máxima permitida, deverá exibir: "Levou uma multa grave" e caso esteja acima de 20km acima da velocidade máxima permitida, exiba: "Levou uma multa gravíssima."


5. Qual é a sequencia de passos a ser feitas para chegar o resultado esperado ?

input velocidade
if velocidade < max_permitida
  msg
elif velocidade == max_permitida
  msg
elif velocidade >= 10
  msg
elif velocidade > 10 <= 20
  msg
'''
#
velocidade = int(input('Velocidade atual: '))
max_permitida = 80
#
if velocidade <= max_permitida:
  print('Tenha um ótimo dia, não houve multa. ')
else:
  if velocidade > max_permitida and velocidade <= max_permitida + 10:
    print('MULTADO!! Terá uma multa leve em sua CNH.' )
  elif velocidade >= max_permitida + 11 and velocidade <= max_permitida + 20:
    print('MULTADO!! Terá uma multa grave em sua CNH. ')
  elif velocidade > max_permitida + 20:
    print('MULTADO!! Terá uma multa gravíssima em sua CNH. ')