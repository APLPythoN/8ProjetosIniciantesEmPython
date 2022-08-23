# #Coleções(listas)
# preço_1 = 20
# preço_2 = 50
# preço_3 = 200
# #Lista
# preços = [20, 50, 200]
# #         0,   1,   2
# print(preços[0])
# print(preços.index(200)) 
# #Lista
# diversidades = [15, 'Jhonatan', True]
# print(diversidades[1])
# print(diversidades[0])
# print(diversidades[2])
# #Laços Itaráveis
# for preço in preços:
#   print(preço

#EX 5-

'''
Some os valores(exemploi com coleções) dados uma coleção de dados 
'idades'[15, 46, 75, 34, 23] imprima na sua tela a soma destes valores.

idades = [ 15, 46, 75, 34, 23] 
total = 0 
loop idade em idades
  total = total + idade
  print total
''' 

idades = [15, 46, 75, 34, 23]
total = 0
for idade in idades:
  total += idade  
print(total)