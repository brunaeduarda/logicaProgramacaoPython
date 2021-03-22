#Atencao! Resolva o exercicio utilizando a estrutura de repeticao 'for'
#Imprima todos os numeros impares do vetor numeros.

numeros = [ 1, 2, 33, 44, 51, 6, 73, 82, 9, 10]

for i in range(0, 10):
    
    if (numeros[i] % 2 == 0):
        continue
    
    print(numeros[i])