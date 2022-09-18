# Projeto 3 - Chute o núMemoryError
# Objetivo: Criar um algoritmo que gera u mvalor aleatório e eu tenho que ficar tentando o número até acertar.

import random


class ChuteONumero:
  def __init__(self):
    self.valor_aleatorio = 0
    self.valor_minimo = 1
    self.valor_maximo = 100
    self.tentar_novamente = True

  
  def Iniciar(self):
      self.GerarNumeroAleatorio()
      self.PedirValorAleatorio()
      try:
        while self.tentar_novamente == True:
          if int(self.valor_do_chute) > self.valor_aleatorio:
            print('Chute um valor mais baixo! ')
            self.PedirValorAleatorio()
          elif int(self.valor_do_chute) < self.valor_aleatorio:
            print('Chute um valor mais alto! ')
            self.PedirValorAleatorio()
          if int(self.valor_do_chute) == self.valor_aleatorio:
            self.tentar_novamente = False
            print('PARABÉNS! VOCÊ ACERTOU!')
      except:
        print('Favor Digitar apenas números!  ')
        self.Iniciar()

  def PedirValorAleatorio(self):
    self.valor_do_chute = input('Chute um número: ')   

    
  def GerarNumeroAleatorio(self):
    self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.Iniciar()