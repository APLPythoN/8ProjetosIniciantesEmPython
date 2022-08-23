'''Escreva um programa que, ao iniciar gere um valor aleatório de 1 a 10 e permita que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.

# Método 5Q's para montar um algorítmo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
R - Um randomizador que gere ou devemos entregar uma lista que dê um valor de 0 a 10.
R - Chute do usuário
2. O que devo fazer com estes dados?
R - Compara o valor gerado e com isto, caso necessário nosso programa deve informar se o valor informado pelo usuário foi maior ou menor ao valor que o nosso programa foi entregue ou randomizado.

3. Quais são as restrições deste problema?
R - Está restrito a ter apenas 10 números e sendo eles de 1 a 10.

4. Qual é o resultado esperado? 
R - Gerar o número e receber uma comparação entre os valores informados, caso esteja certo encerrar, caso errado informar se foi a mais ou a menos e re-solicitar outro valor.

5. Qual é a sequencia de passos a ser feitas para chegar o resultado esperado ?
R -
valor_aleatorio = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
jogador = 'chute do usuario'
if jogador == computador:
  print acertou e encerre.
else
  if jogador > valor_aleatorio
    print número foi maior, digite um menor para tentar acertar.
  elif jogador < valor_aleatorio
    print número foi menor, digite um maior para tentar acertar.
print encerrar.
'''

from random import randint
#
valor_aleatorio = randint(1, 10)
acertou = False
palpites = 0
#

while not acertou:
  jogador = int(input('Chute um número entre 1 e 10: '))
  if jogador == valor_aleatorio:
    palpites += 1
    acertou = True
  else:
    if jogador > valor_aleatorio:
      palpites += 1
      print('valor aleatório é menor, tente novamente...')
    elif jogador < valor_aleatorio:
      palpites += 1
      print('valor aleatório é maior, tente novamente...')
      
print(f'Programa finalizado com {palpites} tentativas.')