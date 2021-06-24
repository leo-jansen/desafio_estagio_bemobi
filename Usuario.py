"""
Classe criada para representar um usuario
"""
import csv 

class Usuario:
  # construtor da classe
  def __init__(self, codigo, user, status):
    self.codigo = codigo
    self.user = user
    self.status = status
  
  # metodo que retorna o nome do pais do codigo passado no parametro, abrindo um 
  # csv com a lista dos paises e seus codigos (dados de paises e codigos pegados da wikipedia) 
  @staticmethod
  def estado(codigo):
    with open('dados/codigo_pais.csv', 'r', encoding='UTF-8') as arquivo_csv:
      leitor = csv.DictReader(arquivo_csv, delimiter=',')
      for linha in leitor:
        if codigo == int(linha['codigo']):
          return linha['pais']