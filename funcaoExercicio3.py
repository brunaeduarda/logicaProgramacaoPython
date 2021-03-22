#Escreva uma funcao que calcule a media dos valores de um vetor de tamanho N.

def media(vetor, tamanho):
    soma = 0
    for i in range(tamanho):
        soma = soma + vetor[i]
    media_obtida = soma/tamanho
    
    return media_obtida

vetor_1 = [5,5,10]
tam_1 = 3

print(media(vetor_1, tam_1))