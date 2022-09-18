# Projeto 3 - Chute o núMemoryError
# Objetivo: Criar um algoritmo que gera um valor aleatório e nós usuários temos que ficar enviando números até acertar e no final informará quantas tentativas foram.

import random


class ChuteONumero:
  def __init__(self):
    self.valor_aleatorio = 0
    self.valor_minimo = 1
    self.valor_maximo = 100
    self.tentar_novamente = True
    self.palpites = 0

  
  def Iniciar(self):
      self.GerarNumeroAleatorio()
      self.PedirValorAleatorio()
      try:
        while self.tentar_novamente == True:
          if int(self.valor_do_chute) > self.valor_aleatorio:
            print('Chute um valor mais baixo! ')
            self.PedirValorAleatorio()
            self.palpites += 1
          elif int(self.valor_do_chute) < self.valor_aleatorio:
            print('Chute um valor mais alto! ')
            self.PedirValorAleatorio()
            self.palpites += 1
          if int(self.valor_do_chute) == self.valor_aleatorio:
            self.tentar_novamente = False
            print(f'PARABÉNS! VOCÊ ACERTOU COM {self.palpites} TENTATIVAS !')
      except:
        print('Favor Digitar apenas números!  ')
        self.Iniciar()

  def PedirValorAleatorio(self):
    self.valor_do_chute = input('Chute um número: ')   

    
  def GerarNumeroAleatorio(self):
    self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.Iniciar()