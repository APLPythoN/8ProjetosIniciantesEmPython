#EXEMPLO 5 - Fatorial de um número:
'''
Crei um programa que recebe um número e imprime o fatorial daquele número.

Método 5Q's para montar um algorítmo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
R - Número

2. O que devo fazer com estes dados?
R - Devemos calcular o fatorial do número que for passdo ao nosso programa e o exibir na tela.

3. Quais são as restrições deste problema?
R - O número Deve ser um valor positivo e inteiro.

4. Qual é o resultado esperado? 
R - O resultado esperado é que o fatorial do número providenciado seja exibido.

5. Qual é a sequencia de passos a ser feitas para chegar o resultado esperado ?
input numero
if numero > 10
if numero = inteiro
fatorial = 1
loop 1 ate numero
  fatorial *= numero
print(fatorial)
'''

numero = int(input('Digite um número: '))
if numero > 0:
  fatorial = 1
  for item in range(1, numero + 1):
    fatorial *= item
print(fatorial)