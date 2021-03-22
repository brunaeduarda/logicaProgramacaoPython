#Funcao - Sem retorno

'''def nome_da_funcao('parametros'):
    'codigo'''

#Exemplo 1 - Exibicao da mensagem 'Ola Mundo!'
# Definicao da funcao
def olaMundo():
    mensagem = "Ola Mundo!"
    print(mensagem)

#Chamada da funcao
olaMundo()

#Exemplo 2 - Exibicao da soma de dois valores
def somaValores(valor_1, valor_2):
  soma = valor_1 + valor_2
  print(soma)
    

a = 10
b = 5 

somaValores(a, b)

#Exemplo 3 - Exibicao de um vetor
def printVetor(vetor):
    print(vetor)


A = [20,30,40,50]

printVetor(A)