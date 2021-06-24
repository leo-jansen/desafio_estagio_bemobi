"""
Script de partida do programa
"""
from Usuario import Usuario

# metodo main
def main():
  usuarios = []
  caminho_arquivo = input("Digite o caminho completo do txt(caminho_do_arquivo/arquivo.txt):")
  arquivo = open(caminho_arquivo, "r")

  # percorre o arquivo de linha em linha, separando o contudo da linha e adcinando um 
  # novo usuario com os dados da linha da linha capturada
  for linha in arquivo:
    linha = linha.replace("\n", "")
    linha_separda = linha.split(" ")
    primeiro_elemento = True
    for elemento in linha_separda:
      if primeiro_elemento:
        usuario_completo = elemento
        primeiro_elemento = False
      else:
        status = elemento
    codigo = int(usuario_completo[0:2])
    user = int(usuario_completo[2:])
    usuarios.append(Usuario(codigo, user, status))
  
  # as 3 lista teram o mesmo tamanho, pois vou relacionar o dados deles pelo indice
  codigos = [] #lista de codigo
  usuarios_pais = [] #lista do usuarios daquele pais
  usuarios_ativos = [] #lista dos usuarios ativos de um pais
  
  # percorre a lista de usuarios, verifica se o codigo do usuario já está na 
  # lista de codigos e adiciona se não estiver na lista, tbm adiciona um 0 na
  # lista de usuarios_pais e usarios_ativos para ter o mesmo tamanho
  for usuario in usuarios:
    if codigos.count(usuario.codigo) == 0:
      codigos.append(usuario.codigo)
      usuarios_pais.append(0)
      usuarios_ativos.append(0)

  # percorre a lista de codigo e depois a de usuarios verifica se o codigo do usuario é igual
  # ao codigo do momento, se for soma 1 na lista de usuarios_pais no mesmo indice do codigo na
  # lista dele, verifica se o status é assinado e soma um na mesma logica 
  saidas = []
  for codigo in codigos:
    indice = codigos.index(codigo)
    for usuario in usuarios:
      if usuario.codigo == codigo:
        usuarios_pais[indice] += 1
        if usuario.status == "assinado":
          usuarios_ativos[indice] += 1
    # adiciona a linha de saida no vetor de saidas 
    saidas.append("{}, {}, {}\n".format(Usuario.estado(codigo), usuarios_pais[indice], usuarios_ativos[indice]))
    
  # escreve no arquivo as saidas que foram adicionadas na lista de saida
  with open("saida.txt", "w") as arquivo:
    for saida in saidas:
      arquivo.write(saida)

if __name__ == "__main__":
  main()
