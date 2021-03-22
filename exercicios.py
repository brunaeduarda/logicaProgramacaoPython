#Escreva um codigo que leia dois valores numericos digitados pelo usuario e informe se estes dois valores sao iguais.

#Escreva um codigo que leia dois valores numericos digitados pelo usuario e informe se os valores sao iguais ou diferentes.

valor_1 = input(" Digite o valor 1: ")
valor_2 = input(" Digite o valor 2: ")

valor_1 = int(valor_1)
valor_2 = int(valor_2)

if ( valor_1 == valor_2 ):
    print(" Os dois valores sao iguais ")
else:
    print(" Sao diferentes ")
    
if ( (valor_1 + valor_2) > 50):
    print(" Soma maior que 50 ")
else:
    print(" Soma menor que 50 ")