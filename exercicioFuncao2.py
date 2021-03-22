'''Escreva uma funcao que calcule a soma dos elementos do vetor A.

A = [ 11, 20, 25, 35, 42, 55 ]

'''

A = [ 11, 20, 25, 35, 42, 55 ]

def somaVetor(vetor, tamanho):
    soma = 0
    for i in range(tamanho):
        soma = soma + vetor[i]
    return soma

print(somaVetor(A, 6))
        
        
    