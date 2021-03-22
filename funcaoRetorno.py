#Funcao - Com retorno

'''def nome_da_funcao('parametros'):
    'codigo'
    return 'variavel'''

#Exemplo 1 - Calculo do dobro do valor

def dobroDoValor(numero):
    resultado = 2 * numero
    return resultado

valor = 10

tv = dobroDoValor(valor)

print( tv )

#Exemplo 2 - Soma de dois valores

def somaValores(valor_1, valor_2):
    soma = valor_1 + valor_2
    return soma

valor_1 = 10
valor_2 = 10

soma = somaValores(valor_1, valor_2)

print( soma )